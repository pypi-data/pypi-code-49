import smtplib

def connect_smtp(config):
    """Connect to an SMTP server
    Parameters:
    config  Root Config object
    """
    cfg = config.smtp

    def ssl_context():
        import ssl
        return ssl.create_default_context()

    kw = dict(host=cfg.host, port=cfg.port)
    if cfg.encryption == "ssl":
        s = smtplib.SMTP_SSL(context=ssl_context(), **kw)
    else:
        s = smtplib.SMTP(**kw)

    if cfg.encryption == "starttls":
        s.starttls(context=ssl_context())

    if cfg.username:
        s.login(cfg.username, cfg.password)

    return s
