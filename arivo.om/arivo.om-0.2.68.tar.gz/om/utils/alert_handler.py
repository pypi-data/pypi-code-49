# coding=utf-8
from __future__ import unicode_literals

import zmq

from om.message import Topic, Message


class Status:
    OK = "ok"
    ERROR = "error"
    OFFLINE = "offline"


class AlertHandler(object):
    def __init__(self, config=None):
        self.pub_socket = None
        self.version = "unknown"
        self.name = "unknown"
        self.package = "unknown"
        self.alerts = []

        if config:
            self._connect(config.BROKER_HOST, config.BROKER_SUB_PORT)
            self.version = config.VERSION
            self.name = config.NAME

    def _connect(self, broker_host, broker_sub_port):
        context = zmq.Context()
        self.pub_socket = context.socket(zmq.PUB)
        self.pub_socket.connect("tcp://{}:{}".format(broker_host, broker_sub_port))

    def _status_dict(self, status, _message=None, **meta):
        _status_dict = ({
            "status": status,
            "meta": meta,
        })
        if _message:
            _status_dict["message"] = _message
        return _status_dict

    def _send_message(self, alert_id, _status_dict):
        alert = self.alerts[alert_id]
        old_status = alert["alert_dict"].get("status")
        alert["alert_dict"].update(_status_dict)
        if alert["always_send_alert"] or alert["alert_dict"]["status"] != old_status:
            message = Message(
                name=self.name,
                type="alert",
            )
            message.update(alert["alert_dict"])
            message.to_socket(self.pub_socket, Topic.ALERT)
            return True
        return False

    def get_or_add_alert_id(self, source, alert_type, handle_type, package_name=None, version="",
                            always_send_alert=False):
        """Define an alert with its name parameters

        Args:
            source (str): The source of the error (i.e. which pin, camera)
            alert_type (str): Name of the alert all lower_case with '_' (i.e. high_time_check)
            handle_type (str): How the error should be handled on the server (state, state_change, count)
            package (str) (default=config.NAME): You send the error for this package
            version (str) (default=config.VERSION): Current version of the package
            always_send_alert (bool): Flag to declare if you want to send every alert or only every change in the status

        Returns:
            alert_id of the saved alert
        """

        alert_dict = dict(source=source, alert_type=alert_type, handle_type=handle_type)
        alert_dict["package"] = package_name or self.name

        for alert in self.alerts:
            if alert_dict.items() <= alert["alert_dict"].items():
                alert["always_send_alert"] = always_send_alert
                return alert["id"]

        alert_dict["version"] = version or self.version
        alert = {"alert_dict": alert_dict, "id": len(self.alerts), "always_send_alert": always_send_alert}
        self.alerts.append(alert)
        return alert["id"]

    def send(self, status, alert_id, meta, kwargs):
        """ Send a status message on the given alert with the corresponding meta/kwarg arguments
            Returns True if alert was send else False"""

        if (isinstance(status, str) and status == Status.OK) or (isinstance(status, bool) and status):
            self.send_ok(alert_id, meta, kwargs)
        else:
            self.send_error(alert_id, meta, kwargs)

    def send_ok(self, alert_id, meta, kwargs={}):
        """ Send an ok message on the given alert with the corresponding meta/kwarg arguments
            Returns True if alert was send else False"""

        _status_dict = self._status_dict(Status.OK, **meta)
        _status_dict.update(kwargs)
        return self._send_message(alert_id, _status_dict)

    def send_error(self, alert_id, meta={}, kwargs={}):
        """ Send an error message on the given alert with the corresponding meta/kwarg arguments
            Returns True if alert was send else False"""

        _status_dict = self._status_dict(Status.OK, **meta)
        _status_dict.update(kwargs)
        return self._send_message(alert_id, _status_dict)

    def send_offline(self, alert_id, **meta):
        """ Send an offline message on the given alert with the corresponding meta/kwarg arguments
            Also checks if the parameters are chosen correctly
            Returns True if alert was send else False"""

        _status_dict = self._status_dict(Status.OFFLINE, meta)
        alert = self.alerts[alert_id]
        if alert["alert_dict"]["package"] == self.name:
            return False

        alert_type = "health_" + "_".join(alert["package"].split("_")[:-1])

        if alert["source"] != "health" or alert_type != alert["alert_type"] or alert["handle_type"] != "state_change":
            alert_id = self.get_or_add_alert("health", alert_type, "state_change", name=alert["package"],
                                             version="unknown", always_send_alert=True)

        return self._send_message(alert_id, _status_dict)

    def send(self, source, alert_type, handle_type, status=Status.ERROR, package=None, meta={}, kwargs={}):
        """Sends an alert to the device server

        Args:
            source (str): The source of the error (i.e. which pin, camera)
            alert_type (str): Name of the alert all lower_case with '_' (i.e. high_time_check)
            handle_type (str): How the error should be handled on the server (state, state_change, count)
            status (Status/bool): The status you want to send(Status.OK, Status.ERROR, Status.OFFLINE)
            package (str) optional: You can send errors for other packages
            meta (dict): Meta information
            kwargs (dict): Additional parameters you want to add to the message (i.e. value of error metric)

        Returns:
            True
        """

        name = package or self.name
        alert_dict = dict(source=source, alert_type=alert_type, handle_type=handle_type, package=name)

        if status == Status.OK or (isinstance(status, bool) and status):
            _status_dict = self._status_dict(Status.OK, **meta)
        elif package and status == Status.OFFLINE:
            _status_dict = self._status_dict(Status.OFFLINE, **meta)
        else:
            _status_dict = self._status_dict(Status.ERROR, **meta)

        message = Message(
            name=self.name,
            type="alert",
        )
        message.update(_status_dict)
        message.update(kwargs)
        message.update(alert_dict)
        message.to_socket(self.pub_socket, Topic.ALERT)
        return True
