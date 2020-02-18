#!/usr/bin/python3

import sys
import time
import re
import random
import asyncio
import glob
import json
import logging as log

from dataclasses import dataclass
from urllib.parse import urlparse

import yaml
import aiopg
import psycopg2
import pysnmp.hlapi.asyncio as snmp
from pysnmp.proto.rfc1905 import NoSuchObject, NoSuchInstance
from pyonf import pyonf


config = """
metrics_dir: /etc/kwollect/metrics.d/
db_host: localhost
db_name: kwdb
db_user: kwuser
db_password: changeme
log_level: warning
"""
config = pyonf(config)

log.basicConfig(
    level=str.upper(config.get("log_level", "warning")),
    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
)


def main():
    # asyncio.run(main(), debug=config.get("log_level") == "debug")
    asyncio.run(async_main())


async def async_main():

    init_snmp()
    await init_psql()

    metrics = load_metric_descriptions(config["metrics_dir"])
    metrics_per_device = merge_metrics_per_device_and_protocol(metrics)
    metrics_per_device = await parse_snmp_iface_metrics(metrics_per_device)

    for device, metrics in metrics_per_device.items():
        if device.protocol == "snmp":
            process_method = process_snmp_host
        elif device.protocol == "ipmisensor":
            process_method = process_ipmisensor_host
        else:
            log.warn(f"Unsupported protocol for device {device}")
            continue

        req_interval_ms = min(metric.update_every for metric in metrics)

        log.info(f"Scheduling {device} requests every {req_interval_ms} milli-seconds")
        task = asyncio.create_task(
            schedule_every(req_interval_ms / 1000, process_method, (device, metrics))
        )

    # Waiting for infinity, but catching failing tasks
    ended_task, _ = await asyncio.wait(
        asyncio.all_tasks(), return_when=asyncio.FIRST_COMPLETED
    )
    log.error("Scheduling task %s as ended, that should not happen", ended_task)
    sys.exit(1)


@dataclass(frozen=True)
class MetricDevice:
    """A device to be queried by some protocol"""
    hostname: str
    protocol: str
    port: int = None
    username: str = None
    password: str = None


@dataclass
class MetricDescription:
    """A metrics to fetch"""
    name: str
    device_id: str
    url: str
    device_alias: str = None
    update_every: int = 10000
    optional: bool = False

    def __post_init__(self):
        _url = urlparse(self.url)
        self.device = MetricDevice(
            hostname=_url.hostname,
            protocol=_url.scheme,
            port=_url.port,
            username=_url.username,
            password=_url.password,
        )
        self.path = re.sub(r"^/", "", _url.path)


def load_metric_descriptions(metrics_dir):
    """Load metric descriptions from directory"""
    log.debug(f"Loading metric descriptions from {metrics_dir}")
    metrics = []
    for description_file in glob.glob(metrics_dir + "/*.conf"):
        with open(description_file) as f:
            try:
                ydata = yaml.safe_load(f.read())
                if isinstance(ydata, list):
                    metrics += [MetricDescription(**d) for d in ydata]
                elif isinstance(ydata, dict):
                    metrics.append(MetricDescription(**ydata))
                elif ydata is None:
                    pass
                else:
                    raise Exception("Unparsable metric description")
            except Exception as ex:
                log.error(f"Error when reading {description_file} content")
                log.error(f"{repr(ex)}: {str(ex)}")
                sys.exit(1)

    log.debug(metrics)
    return metrics


def merge_metrics_per_device_and_protocol(metrics):
    """Merge list of metrics per involved device and returns a Dict[MetricDevice, MetricDescription]"""
    metrics_per_device = {}
    for metric in metrics:
        if metric.device not in metrics_per_device:
            metrics_per_device[metric.device] = []
        metrics_per_device[metric.device].append(metric)
    return metrics_per_device


async def schedule_every(period, func_name, args=[], kwargs={}, delayed_start=True):
    """Schedule func_name to run every period"""

    TIMEOUT_MAX_COUNT = 5

    if delayed_start and period > 1:
        await asyncio.sleep(random.randint(0, int(period)))

    log.debug(f"Start task scheduler for {func_name} {args} {kwargs}")

    while True:

        task = asyncio.create_task(func_name(*args, **kwargs))
        timeout_count = 0

        while True:
            await asyncio.sleep(period)
            if not task.done():
                timeout_count += 1
                if timeout_count >= TIMEOUT_MAX_COUNT:
                    log.warning(
                        f"Cancelling task that did not finished after {TIMEOUT_MAX_COUNT} periods of {period} sec: {func_name} {args} {kwargs}"
                    )
                    task.cancel()
                    break
                else:
                    log.warning(
                        f"Waiting for task that did not finish under its period of {period} sec: {func_name} {args} {kwargs}"
                    )
            elif task.exception():
                log.warning(
                    f"Task had an exception %s, scheduling new one ({func_name} {args} {kwargs})",
                    task.exception(),
                )
                break
            else:
                log.debug(
                    f"Task correctly finished, scheduling new one ({func_name} {args} {kwargs})"
                )
                break


async def process_snmp_host(device, metrics):
    """Process one query for metrics on a device using SNMP"""

    metrics = await filter_optional_metrics(device, metrics)
    if not metrics:
        log.info(
            f"Nothing to process after filtering optional metrics for SNMP host {device.hostname}"
        )
        return

    # "oids" maps SNMP OID with the associated metric position in "metrics" list
    # (the OID must be stored as string, without heading "." as in PySNMP)
    oids = {metric.path: metric_idx for metric_idx, metric in enumerate(metrics)}

    # "results" stores SNMP request result and has same length and ordering than metrics
    # (None value is used if result is not available for a metric)
    results = [None] * len(metrics)

    timestamp = time.time()
    _results = await make_snmp_request(
        device.hostname, "get", oids.keys(), device.username
    )
    for oid, value in _results.items():
        results[oids[oid]] = value

    if not any(results):
        log.warning(f"Nothing to process for SNMP host {device.hostname}")
        return

    values = [(timestamp, result) for result in results]
    await insert_metrics_values(metrics, values)


async def process_ipmisensor_host(device, metrics):
    """Process one query for metrics on a device using IPMI"""

    metrics = await filter_optional_metrics(device, metrics)
    if not metrics:
        log.info(
            f"Nothing to process after filtering optional metrics for IPMI host {device.hostname}"
        )
        return

    timestamp = time.time()

    command = f"/usr/sbin/ipmi-sensors -D LAN_2_0 -h {device.hostname}"
    if device.username:
        command += f" -u {device.username}"
    if device.password:
        command += f" -p {device.password}"
    process = await asyncio.create_subprocess_shell(
        command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )

    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        log.warning(f"Error on ipmi-sensor command for {device.hostname}")
        log.warning(stderr)
        return

    # parse ipmi-sensor stdout and store values by sensor name and sensor ID.
    # (both ipmi-sensor's ID and name fields may be used in the MetricDescription
    # URL path but some devices use identical names for different sensor, so ID is safer)
    ipmisensor_values = {}
    for ipmisensor_output in stdout.decode().strip().split("\n")[1:]:
        values = [value.strip() for value in ipmisensor_output.split("|")]
        sensor_id, sensor_name, sensor_value = values[0], values[1], values[3]
        ipmisensor_values[sensor_id] = sensor_value
        ipmisensor_values[sensor_name] = sensor_value

    # "results" stores IPMI result and has same length and ordering than metrics
    # (None value is used if result is not available for a metric)
    results = [None] * len(metrics)

    for metric_idx, sensor_name in enumerate(metric.path for metric in metrics):
        if sensor_name not in ipmisensor_values:
            log.warning(
                f"Could not find IPMI sensor with name or ID {sensor_name} on device {device.hostname}"
            )
        elif ipmisensor_values[sensor_name] != "N/A":
            results[metric_idx] = ipmisensor_values[sensor_name]

    if not any(results):
        log.warning(f"Nothing to process for IPMI sensor host {device.hostname}")
        return

    values = [(timestamp, result) for result in results]
    await insert_metrics_values(metrics, values)


async def filter_optional_metrics(device, metrics):
    """Query DB to filter out optional metrics from metrics argument for a device"""
    promoted_device = [
        line[0]
        for line in await sql("SELECT device_id FROM promoted_metrics", fetch=True)
    ]
    return [
        metric
        for metric in metrics
        if not metric.optional
        or metric.device_id in promoted_device
        or (metric.device_alias and metric.device_alias in promoted_device)
    ]


async def insert_metrics_values(metrics, values):
    """Insert metrics and associated values into DB"""

    sql_insert = (
        "INSERT INTO metrics(timestamp, device_id, metric_id, value, labels) VALUES\n  "
    )
    sql_labels = {}

    for i, metric in enumerate(metrics):
        timestamp, value = values[i]
        if value:
            sql_insert += f"(to_timestamp({timestamp}), "
            sql_insert += f"'{metric.device_id}', "
            sql_insert += f"'{metric.name}', "
            try:
                sql_insert += f"{float(value)}, "
            except ValueError:
                sql_insert += "'NaN', "
                sql_labels.update({"str_value": value})
            if metric.device_alias:
                sql_labels.update({"_device_alias": metric.device_alias})

            if sql_labels:
                sql_insert += f"'{json.dumps(sql_labels)}'"
            else:
                sql_insert += "NULL"

            sql_insert += "),\n  "

    # Remove trailing '),\n  '
    sql_insert = sql_insert[:-4]

    log.debug(sql_insert)
    await sql(sql_insert)


async def parse_snmp_iface_metrics(metrics_per_device):
    """Find real OID of SNMP metrics that use {{ iface }} alias in their URLs"""

    parsed_metrics_per_device = {}

    # Parse metrics with SNMP {{iface}} URL
    for device, metrics in metrics_per_device.items():
        if device.protocol != "snmp":
            parsed_metrics_per_device[device] = metrics
        elif not any(
            metric for metric in metrics if re.findall(r"{{(.*)}}", metric.path)
        ):
            parsed_metrics_per_device[device] = metrics
        else:
            parsed_metrics_per_device[device] = await parse_device_snmp_iface_metrics(
                device, metrics
            )

    # Purge devices that don't have anymore metrics after iface parsing
    parsed_metrics_per_device = {
        device: metrics
        for device, metrics in parsed_metrics_per_device.items()
        if metrics
    }
    return parsed_metrics_per_device


async def parse_device_snmp_iface_metrics(device, metrics):
    """Send SNMP request to retrieve OID suffixes corresponding to metrics' {{ iface }}"""

    log.debug(f"Getting SNMP IF-MIB::ifDescr values on host {device.hostname}...")
    results = await make_snmp_request(
        device.hostname, "walk", "1.3.6.1.2.1.2.2.1.2", device.username
    )

    for oid, snmp_iface_descr in results.items():
        for metric in metrics:
            metric_iface = re.findall(r"{{(.*)}}", metric.path)
            if metric_iface:
                metric_iface = metric_iface[0].strip()

                if snmp_iface_descr == metric_iface:
                    iface_oid_suffix = oid.replace("1.3.6.1.2.1.2.2.1.2.", "")
                    metric.path = re.sub(r"{{.*}}", iface_oid_suffix, metric.path)
                    log.debug(f"  {metric_iface} is {iface_oid_suffix}")

    new_metrics = []
    for metric in metrics:
        if re.findall(r"{{(.*)}}", metric.path):
            log.warning(
                f"SNMP iface {metric.path} for {device.hostname} not converted, deleting metrics"
            )
        else:
            new_metrics.append(metric)
    log.debug(new_metrics)
    return new_metrics


snmp_engine = None


def init_snmp():
    global snmp_engine
    snmp_engine = snmp.SnmpEngine()


psql_pool = None


async def init_psql():
    global psql_pool
    psql_pool = await aiopg.create_pool(
        database=config["db_name"],
        user=config["db_user"],
        password=config["db_password"],
        host=config["db_host"],
    )


async def sql(cmd, fetch=False):
    with (await psql_pool.cursor()) as cur:
        try:
            await cur.execute(cmd)
            ret = []
            if fetch:
                async for row in cur:
                    ret.append(row)
            return ret
        except psycopg2.ProgrammingError as ex:
            log.warning(f"Error when performing SQL request {cmd}")
            log.warning(f"{repr(ex)}: {str(ex)}")


async def make_snmp_request(host, snmp_command, oids, community="public"):
    """PySNMP glue"""
    try:
        if snmp_command not in ("get", "walk"):
            raise Exception(f"Unsupported snmp_command (must be get or walk)")

        cmd_args = [
            snmp_engine,
            snmp.CommunityData(community),
            snmp.UdpTransportTarget((host, 161), timeout=10),
            snmp.ContextData(),
        ]
        cmd_opts = {"lookupMib": False}

        if snmp_command == "get":
            if isinstance(oids, str):
                oids = [oids]
            cmd_oids = [snmp.ObjectType(snmp.ObjectIdentity(oid)) for oid in oids]

            var_binds = []
            # Slicing OIDs to perform SNMP GET with a maximum of 50 objects and avoid fragmentation
            for cmd_oids_slice in (
                cmd_oids[i : min(i + 50, len(cmd_oids))]
                for i in (range(0, len(cmd_oids), 50))
            ):
                error_indication, error_status, error_index, _var_binds = await snmp.getCmd(
                    *cmd_args, *cmd_oids_slice, **cmd_opts
                )
                if error_indication:
                    raise Exception(f"error_indication: {error_indication}")
                elif error_status:
                    raise (
                        Exception(
                            "{} at {}".format(
                                error_status.prettyPrint(),
                                error_index
                                and var_binds[int(error_index) - 1][0]
                                or "?",
                            )
                        )
                    )
                else:
                    var_binds += _var_binds

        if snmp_command == "walk":
            if not isinstance(oids, str):
                raise Exception(
                    f"Unsupported OID list for snmp_command walk (must be unique string)"
                )

            cmd_oids = [snmp.ObjectType(snmp.ObjectIdentity(oids))]

            var_binds = []
            end_of_walk = False
            while not end_of_walk:
                # error_indication, error_status, error_index, var_binds_table = await snmp.bulkCmd(
                #     *cmd_args, 0, 50, *cmd_oids, **cmd_opts
                # )
                error_indication, error_status, error_index, var_binds_table = await snmp.nextCmd(
                    *cmd_args, *cmd_oids, **cmd_opts
                )
                if error_indication:
                    raise Exception(f"error_indication: {error_indication}")
                elif error_status:
                    raise (
                        Exception(
                            "{} at {}".format(
                                error_status.prettyPrint(),
                                error_index
                                and var_binds[int(error_index) - 1][0]
                                or "?",
                            )
                        )
                    )

                for _var_binds in var_binds_table:
                    if snmp.isEndOfMib(_var_binds):
                        break
                    for oid, value in _var_binds:
                        # log.debug("%s %s", oid, value)
                        if oids not in str(oid):
                            end_of_walk = True
                            break
                        var_binds.append((oid, value))
                cmd_oids = _var_binds

        results = {}
        for oid, value in var_binds:
            if isinstance(value, NoSuchInstance) or isinstance(value, NoSuchObject):
                log.warning(f"Object {oid} does not exist on {host}")
                results[str(oid)] = None
            else:
                results[str(oid)] = value.prettyPrint()
        return results

    except Exception as ex:
        log.warning(
            f"Error when performing SNMP request {snmp_command} on {host} with {oids}"
        )
        log.warning(f"{repr(ex)}: {str(ex)}")
        log.warning(f"{oids}")
        raise ex
        return {}


if __name__ == "__main__":
    main()
