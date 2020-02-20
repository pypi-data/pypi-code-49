from keyrings.lastpass.cli import lpass, AccountNotFound
import json


def load_notes(service):
    try:
        output = lpass("show", "keyring/" + service, "--notes")
        # print(output)
        return json.loads(output)
    except AccountNotFound:
        return {}


def save_notes(service, notes):
    rendered_notes = json.dumps(notes)
    try:
        output = lpass(
            "edit",
            "keyring/" + service,
            "--notes",
            "--non-interactive",
            input=rendered_notes.encode("utf-8"),
        )
        return output
    except AccountNotFound:
        return {}
