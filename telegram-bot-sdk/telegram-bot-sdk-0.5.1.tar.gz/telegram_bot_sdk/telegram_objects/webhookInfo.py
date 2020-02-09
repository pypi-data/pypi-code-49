class WebhookInfo:
    """
    :param url: Webhook URL, may be empty if webhook is not set up
    :type url: str
    :param has_custom_certificate: True, if a custom certificate was provided for webhook certificate check
    :type has_custom_certificate: bool
    :param pending_update_count: Number of updates awaiting delivery
    :type pending_update_count: int
    :param last_error_date: Optional: Unix time for the most recent error that happened when trying do deliver an \
    update via webhook
    :type last_error_date: int
    :param last_error_message: Optional: Error message in human-readable format for the most recent error that \
    happened when trying to deliver an update via webhook
    :type last_error_message: str
    :param max_connections: Optional: Maximum allowed number of simultaneous HTTPS connections to the webhook for \
    update delivery
    :type max_connections: int
    :param allowed_updates: Optional: A list of update types the bot is subscribed to. Defaults to all update types
    :type allowed_updates: list of str
    """
    def __init__(self, *, url, has_custom_certificate=None, pending_update_count=None, last_error_date=None,
                 last_error_message=None, max_connections=None, allowed_updates=None):
        self.url = url
        self.has_custom_certificate = has_custom_certificate
        self.pending_update_count = pending_update_count
        self.last_error_date = last_error_date
        self.last_error_message = last_error_message
        self.max_connections = max_connections
        self.allowed_update = [x for x in allowed_updates] if allowed_updates else None
