#!/usr/bin/python3

from dataclasses import dataclass
from typing import Dict

import sys
import logging as log

from pyonf import pyonf

import yaml
import psycopg2


config = """
wattmetre_id: wattmetre
mapping_file_path: ''
db_name: kwdb
db_user: kwuser
db_password: changeme
db_host: localhost
log_level: debug
"""
config = pyonf(config)

log.basicConfig(
    level=str.upper(config.get("log_level", "warning")),
    format="%(asctime)s:%(levelname)s:%(name)s:%(message)s",
)


def main():

    init_wattmetre_node_mapping()
    init_sql()

    cur_entries = []
    cur_timestamp_sec = -1
    pred_timestamp_sec = None

    for line in sys.stdin:

        new_entry = read_entry_from_wattmetre(line)
        if not new_entry:
            continue

        cur_timestamp_sec = int(new_entry.timestamp)
        if not pred_timestamp_sec:
            pred_timestamp_sec = cur_timestamp_sec

        if cur_timestamp_sec == pred_timestamp_sec:
            cur_entries.append(new_entry)
        else:
            if cur_timestamp_sec != pred_timestamp_sec + 1:
                log.warning("Gap found in timestamps")
            insert_values(prepare_values_to_insert(cur_entries))
            cur_entries = [new_entry]

        pred_timestamp_sec = cur_timestamp_sec


def prepare_values_to_insert(new_entries):

    high_freq_node = get_highfreq_node()
    log.debug("High freq node to monitor: %s", high_freq_node)

    values_to_insert = {}

    for entry in new_entries:
        for port_num, measure in entry.measures.items():
            wattmetre_port = f"{entry.wattmetre_id}-port{port_num}"
            if wattmetre_port not in values_to_insert:
                values_to_insert[wattmetre_port] = []
            values_to_insert[wattmetre_port].append((entry.timestamp, measure))

    # If the corresponding node must not be highfreq monitored, we average values to insert
    for wattmetre_port, values in values_to_insert.items():
        if values and node_by_wattmetre_map.get(wattmetre_port) not in high_freq_node:
            avg_timestamp_sec = int(values[0][0])
            avg_value = sum([m[1] for m in values]) / len(values)

            values_to_insert[wattmetre_port] = [(avg_timestamp_sec, avg_value)]

    return values_to_insert


def insert_values(values_to_insert):
    sql_insert = (
        "INSERT INTO metrics(timestamp, device_id, metric_id, value, labels) VALUES\n  "
    )

    for wattmetre_port, values in values_to_insert.items():
        for timestamp, value in values:
            sql_insert += f"(to_timestamp({timestamp}), "
            sql_insert += f"'{wattmetre_port}', "
            sql_insert += f"'wattmetre_power_watt', "
            sql_insert += f"{value}, "
            mapped_node = node_by_wattmetre_map.get(wattmetre_port)
            if mapped_node:
                sql_insert += '\'{"_device_alias": "%s"}\'' % mapped_node
            else:
                sql_insert += "NULL"
            sql_insert += "),\n  "

    # Remove trailing '),\n  '
    sql_insert = sql_insert[:-4]

    log.debug(sql_insert)
    try:
        sql_cur.execute(sql_insert)
        sql_conn.commit()
    except psycopg2.ProgrammingError as ex:
        log.warning(f"Error when performing SQL request {sql_insert}")
        log.warning(f"{repr(ex)}: {str(ex)}")
        sql_conn.rollback()


def get_highfreq_node():
    try:
        sql_cur.execute(
            "SELECT device_id FROM promoted_metrics WHERE metric_id = 'wattmetre_power_watt'"
        )
        sql_conn.commit()
        return [row[0] for row in sql_cur.fetchall()]
    except psycopg2.ProgrammingError as ex:
        log.warning("Error when performing SQL request in get_highfreq_node")
        log.warning(f"{repr(ex)}: {str(ex)}")
        sql_conn.rollback()
        return []


@dataclass
class WattmetreEntry:
    wattmetre_id: str
    port_count: int
    timestamp: str
    measures: Dict[int, float]


def read_entry_from_wattmetre(line):
    log.debug(line)
    values = line.strip().split(",")
    if len(values) > 4 and values[3] == "OK":
        port_count = len(values[4:])
        try:
            entry = WattmetreEntry(
                wattmetre_id=config["wattmetre_id"],
                port_count=port_count,
                timestamp=float(values[2]),
                measures={
                    port_num + 1: float(values[port_num + 4])
                    for port_num in range(port_count)
                    if values[port_num + 4] != ""
                },
            )
            log.debug(entry)
            return entry
        except (ValueError, IndexError) as ex:
            log.warning("Error when decoding data, skipping frame")
            log.warning(values)
            log.warning(ex)


node_by_wattmetre_map = {}
wattmetre_by_node_map = {}


def init_wattmetre_node_mapping():
    global node_by_wattmetre_map
    global wattmetre_by_node_map
    if config.get("mapping_file_path"):
        try:
            with open(config["mapping_file_path"]) as mapping_file:
                wattmetre_by_node_map = yaml.safe_load(mapping_file.read())
                node_by_wattmetre_map = {
                    wattmetreid_port: node
                    for node in wattmetre_by_node_map.keys()
                    for wattmetreid_port in wattmetre_by_node_map[node]
                }
                log.debug("Wattmetre-Node mapping are:")
                log.debug(wattmetre_by_node_map)
                log.debug(node_by_wattmetre_map)
        except Exception as ex:
            log.error(f"Error when reading wattmetre/node mapping file %s", config["mapping_file_path"])
            log.error(f"{repr(ex)}: {str(ex)}")
            sys.exit(1)


sql_conn = None
sql_cur = None


def init_sql():
    global sql_conn
    global sql_cur
    sql_conn = psycopg2.connect(
        database=config["db_name"],
        user=config["db_user"],
        password=config["db_password"],
        host=config["db_host"],
    )
    sql_cur = sql_conn.cursor()


if __name__ == "__main__":
    main()

# SSH_AUTH_SOCK=/tmp/ssh-o9EVVaAfzQ/agent.17088 ssh sdelamar@crunch1.lip 'while true; do gotail -n 1 -p -f /local/wattmetre-log/*[^z]; done' | while read l; do echo $l; done | ./wattmetre.py mapping.yml
