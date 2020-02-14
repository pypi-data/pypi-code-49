# coding: utf-8
import json
import requests

from django import forms
from sentry.plugins.bases import notify

AFONE_WECHAT_WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={key}"

class AfoneWechatWebhookOptionsForm(notify.NotificationConfigurationForm):
    key = forms.CharField(
        max_length=255,
        help_text='Wechat webhook key'
    )

class AfoneWechatWebhookPlugin(notify.NotificationPlugin):
    author = 'RayLau'
    author_url = 'https://github.com/raylua2566/sentry-afone-integrations'
    version = '0.0.6'
    description = u'Sentry 企业微信 Webhook 插件'
    resource_links = [
        ('Source', 'https://github.com/raylua2566/sentry-afone-integrations'),
        ('Bug Tracker', 'https://github.com/raylua2566/sentry-afone-integrations/issues'),
        ('README', 'https://github.com/raylua2566/sentry-afone-integrations/blob/master/README.md'),
    ]

    slug = 'afone_wechat_webhook'
    title = 'Afone Wechat Webhook'
    conf_key = slug
    conf_title = title
    project_conf_form = AfoneWechatWebhookOptionsForm

    def is_configured(self, project, **kwargs):
        return bool(self.get_option('key', project))

    def notify_users(self, group, event, fail_silently=False, **kwargs):
        key = self.get_option('key', group.project)
        url = AFONE_WECHAT_WEBHOOK_URL.format(key=key)
        title = u"有新的通知来自 {} 项目".format(event.project.slug)
        event_id = event.event_id
        data = {
            "msgtype": "markdown",
            "markdown": {
                "content": u"#### {title} \n > {message} [查看]({url})".format(
                    title=title,
                    message=event.message,
                    url=u"{}events/{}/".format(group.get_absolute_url(), event_id),
                )
            }
        }
        requests.post(
            url=url,
            headers={"Content-Type": "application/json"},
            data=json.dumps(data).encode("utf-8")
        )