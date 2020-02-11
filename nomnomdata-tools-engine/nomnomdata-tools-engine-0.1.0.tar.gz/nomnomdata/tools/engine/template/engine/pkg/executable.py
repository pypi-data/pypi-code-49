from nomnomdata.engine.api import NominodeClient
from nomnomdata.engine.core import Executable

__author__ = "Nom Nom Data LLC"
__copyright__ = "Copyright 2018, Nom Nom Data LLC"


class TemplateExecutable(Executable):
    def __init__(self):
        super().__init__("nomigen.{{engine_name}}")
        self.creds = {}
        self.creds["aws_connection"] = self.params["config"][
            self.params["aws_connection"]["connection_uuid"]
        ]
        self.nominode = NominodeClient()

    def do_thing(self):
        self.logger.info("I did a thing!")
        self.nominode.update_progress(message="I did it!")
