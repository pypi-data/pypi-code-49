import salt.utils.files
from sh import su, diff, tail
from io import StringIO


def managed(name,
            source=None,
            hash=None,
            hash_name=None,
            saltenv='base',
            engine='jinja',
            skip_verify=False,
            context=None,
            defaults=None,
            commit=True,
            **vars):

    ret = {
        'changes': {},
        'comment': '',
        'name': name,
        'result': True
    }

    sfn, _, __ = __salt__['file.get_managed'](
        name=name,
        template=engine,
        source=source,
        source_hash=hash,
        source_hash_name=hash_name,
        user=None,
        group=None,
        mode=None,
        attrs=None,
        saltenv=saltenv,
        context=context,
        defaults=defaults,
        skip_verify=skip_verify,
        **vars)

    su('admin', _in="discard")  # Discard pending changes

    with open(sfn, 'rb') as commands:

        command_block = """
    start transaction
    configure terminal

    {}

    configure terminal

    show candidate-configuration | save /tmp/gestion_candidate
    show running-configuration | save /tmp/gestion_running
    """.format(commands.read())

    errors = StringIO()

    su('admin', _in=command_block, _out='/dev/null', _err=errors)

    errors = errors.getvalue()

    errors = errors.replace("WARNING: Cluster manager is using default credentials", "").strip()

    if errors:
        ret['result'] = False
        ret['comment'] = errors

        return ret

    with open("/tmp/gestion_candidate_tail", 'wb') as f:
        tail("/tmp/gestion_candidate", n="+6", _out=f)

    with open("/tmp/gestion_running_tail", 'wb') as f:
        tail("/tmp/gestion_running", n="+6", _out=f)

    changes = diff("/tmp/gestion_running_tail", "/tmp/gestion_candidate_tail", "--label", "Current configuration", "--label", "New configuration", u=True, _ok_code=[0, 1])

    if changes:
        ret['changes']['diff'] = str(changes)

    if __opts__['test']:

        if ret['result']:
            ret['result'] = None

        su('admin', _in="discard")

    elif not commit:

        su('admin', _in="discard")

        ret['comment'] = 'Changes have not been commited'

    else:
        su('admin', _in="commit")
        su('admin', _in="copy running-configuration startup-configuration")

    salt.utils.files.remove(sfn)

    return ret
