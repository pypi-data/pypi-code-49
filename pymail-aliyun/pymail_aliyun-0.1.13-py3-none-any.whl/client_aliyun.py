import email
import ssl

import requests
from imapclient import IMAPClient, SEEN
from imapclient.exceptions import IMAPClientError
from tqdm import tqdm

from pymail_aliyun.mail_utils import get_subject, get_mail_date, get_body_content, get_sender, get_attachment

USR_AGENT = (
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/78.0.3904.108 Safari/537.36'
)

ssl_context = ssl.create_default_context()
# don't check if certificate hostname doesn't match target hostname
ssl_context.check_hostname = False
# don't check if the certificate is trusted by a certificate authority
ssl_context.verify_mode = ssl.CERT_NONE


class MailAliyun(object):
    """
    单封邮件对像
    """

    def __init__(self, uid, subject, mail_date, body, attachments, sender):
        self.subject = subject
        self.mail_date = mail_date
        self.body = body
        self.attachments = attachments
        self.uid = uid
        self.sender = sender


class MailAliyunClient(IMAPClient):
    """
    Extend IMAPClient with aliyun mail
    """

    def __init__(self, user_name, password, host='imap.aliyun.com', port=None, use_uid=True, ssl=True, stream=False,
                 ssl_context=ssl_context, timeout=None):
        super(MailAliyunClient, self).__init__(host, port=port, use_uid=use_uid, ssl=ssl, stream=stream,
                                               ssl_context=ssl_context, timeout=timeout)
        self._user_name = user_name
        self._password = password
        self.req_session = requests.Session()

    def __enter__(self):
        self.login(self._user_name, self._password)
        return self

    def mark_unread(self, uid):
        """
        标记邮件为未读
        :param uid: mail uid
        :return:
        """
        self.remove_flags(uid, [SEEN])

    def mark_read(self, uid):
        """
        标记邮件为已读
        :param uid:
        :return:
        """
        self.add_flags(uid, [SEEN])

    def create_aliyun_folder(self, folder_name):
        """
        创建目录，支持 nested 目录。
        :return: None or {folder_name: folder_id}
        """
        paths_element = folder_name.split('/')
        possible_path = ['/'.join(paths_element[:i]) for i in reversed(range(1, len(paths_element) + 1))]
        final_pointer = 0
        total_iter_counts = 0
        while True:
            if total_iter_counts > 10:
                raise Exception('Too many nested folder')
            try:
                msg = self.create_folder(possible_path[final_pointer])
                if msg.decode('utf-8') == 'CREATE completed':
                    if final_pointer == 0:
                        break
                    final_pointer = final_pointer - 1
            except IMAPClientError:
                # 失败后，尝试创建父目录。
                final_pointer = final_pointer + 1
            total_iter_counts = total_iter_counts + 1

    def move_mail(self, uid, dest_path):
        """
        :param uid:
        :param dest_path: 准备移动到的 '/parent_folder/sub_folder/sub_folder'
        :return:
        """
        dest_path = dest_path.strip('/')
        try:
            self.copy(uid, dest_path)
        except IMAPClientError:
            # 可能是没有目标文件夹，或者此邮件就在这个目标文件夹里。
            if self.folder_exists(dest_path):
                return
            else:
                self.create_aliyun_folder(dest_path)
                self.copy(uid, dest_path)

    def handle_mails(self, func, folder_name='Inbox', criteria='UNSEEN', mails_count=50,
                     attch_filter=('xls', 'xlsx', 'pdf', 'doc', 'docx'), **kwargs):
        """
        处理未读邮件
        :param func: 处理邮件的方法，input 为 Mail263 对象，output 为 'success' or 'fail'
        :param folder_name: 邮件所在文件夹
        :param criteria: 搜索条件
        :param mails_count: 设置一次处理多少邮件
        :param attch_filter: 附件过滤器，只保留哪些附件
        :param kwargs: nas_client nas 客户端等 func 需要用到的客户端
        :return:
        """
        self.select_folder(folder_name)
        messages = self.search(criteria)
        if messages:
            if mails_count != 'ALL':
                messages = messages[:mails_count]
            for uid, message_data in tqdm(self.fetch(messages, 'RFC822').items()):
                email_message = email.message_from_bytes(message_data[b'RFC822'])
                try:
                    subject = get_subject(email_message)
                except Exception:
                    self.move_mail(uid, 'Decode_failed/subject')
                    break

                try:
                    mail_date = get_mail_date(email_message)
                except Exception:
                    self.move_mail(uid, 'Decode_failed/mail_date')
                    break

                try:
                    body = get_body_content(email_message)
                except Exception:
                    self.move_mail(uid, 'Decode_failed/body')
                    break

                try:
                    attachments = get_attachment(email_message, file_filter=attch_filter) or None
                except Exception:
                    self.move_mail(uid, 'Decode_failed/attachments')
                    break

                try:
                    sender = get_sender(email_message)
                except Exception:
                    self.move_mail(uid, 'Decode_failed/sender')
                    break

                mail = MailAliyun(uid, subject, mail_date, body, attachments, sender)
                func(self, mail, **kwargs)
        self.close_folder()
