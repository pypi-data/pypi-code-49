import base64
import quopri
from copy import copy
from datetime import datetime
from email.header import decode_header

from bs4 import BeautifulSoup


class DecodeException(Exception):
    pass


def get_decode_content(encode_str):
    """
    获取邮件解码后的内容
    :param encode_str:
    :return:
    """
    decode_str, encoding = decode_header(encode_str)[0]
    if encoding == 'unknown-8bit' or encoding == 'gb2312':
        # 解码失败默认用 gbk
        encoding = 'gbk'

    if encoding is not None:
        decode_str = decode_str.decode(encoding)

    if '�' in decode_str:
        raise DecodeException('Decode_content_error.')
    return decode_str


def get_subject(msg):
    """
    获取邮件主题
    :param msg: Message 对象
    :return:
    """
    return get_decode_content(msg.get('Subject'))


def get_mail_date(msg):
    """
    获取邮件日期
    :param msg: Message 对象
    :return:
    """
    # https://www.simplifiedpython.net/python-convert-string-to-datetime/
    # 'Wed, 25 Sep 2019 20:59:23 +0800' ==> '25 Sep 2019 20:59:23'
    date_str = msg.get('Date').split(',')[-1].split('+')[0].strip()
    try:
        # 国内邮件时间解析
        return datetime.strptime(date_str, '%d %b %Y %H:%M:%S')
    except ValueError:
        # 英文系统邮件时间解析
        # 'Tue Jan 21 18:00:09 2020'
        return datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y')


def get_sender(msg):
    """
    获取邮件发件人名称，不是发件人邮件。
    '"eservice@nbcb.cn" <eservice@nbcb.cn>' => eservice@nbcb.cn
    '<yywbfa@cmschina.com.cn>' => yywbfa
    '=?GB2312?B?uqPNqNakyK8=?= <ppos@htsec.com>' => 海通证券
    :param msg: Message 对象
    :return:
    """
    raw_sender = msg.get('From')
    if '?' in raw_sender:
        sender = get_decode_content(raw_sender)
    else:
        if '"' in raw_sender:
            start = raw_sender.find('"') + 1
            end = raw_sender.find('"', start)
            sender = raw_sender[start:end]
        else:
            sender = raw_sender.split('@')[0]
            sender = sender.strip('<>')
    return sender


def has_attachment(msg):
    """
    check whether has attachments
    :param msg:
    :return:
    """
    attachment_num = msg.get('X-ATTACHMENT-NUM')
    # plain text 也算 attachment
    if attachment_num < 2:
        return False
    else:
        return True


def get_attachment_name(part):
    """
    get chinese attachment name if part.get_filename() fails.
    :param part: Message object
    :return:
    """
    file_name = part.get_filename()
    try:
        file_name = get_decode_content(file_name)
        return file_name
    except (AttributeError, DecodeException) as e:
        # Use shallow copy avoid string huge payload
        part_shallow = copy(part)
        part_shallow._payload = None
        part_str = part_shallow.as_string()
        part_str_elements = part_str.split('unknown-8bit')
        for item in part_str_elements:
            if '?b?' in item:
                file_name_b64 = item.split('?=')[0].strip().replace('?b?', '')
                file_name = base64.b64decode(file_name_b64).decode('gb2312')
                file_name = file_name.split('=')[-1].replace('"', '')
                return file_name


def get_attachment(msg, file_filter=('xls', 'xlsx', 'pdf', 'doc', 'docx')):
    """
    获取邮件里的附件
    :param msg:
    :param file_filter:
    :return:
    """
    attachments = []
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart': continue
        if part.get_content_maintype() == 'text': continue
        if part.get('Content-Disposition') is None: continue
        file_name = get_attachment_name(part)
        file_extension = file_name.split('.')[-1]
        file = part.get_payload(decode=True)
        if file_extension not in file_filter:
            continue
        attachments.append({'name': file_name, 'file': file})
    return attachments


def get_body_content(msg):
    """
    获取邮件 body 信息
    :param msg:
    :return:
    """
    content = None
    for part in msg.walk():
        if part.get_content_type() in ("text/html", "text/plain"):
            content_encode = part.get_payload()
            content_transfer_encoding = part.get('Content-Transfer-Encoding')
            if part.get('Content-Type'):
                charset = part.get('Content-Type').split('=')[1].lower()
                if content_transfer_encoding == 'quoted-printable':
                    content = quopri.decodestring(content_encode).decode(charset)
                elif content_transfer_encoding == 'base64':
                    try:
                        content = base64.b64decode(content_encode).decode(charset)
                    except UnicodeDecodeError as e:
                        # 可能是这种 '"gb2312"'，所以用 in
                        if 'gb2312' in charset:
                            content = base64.b64decode(content_encode).decode('gbk')
                        else:
                            raise e
                elif content_transfer_encoding == '7bit' or content_transfer_encoding == '8bit':
                    content = content_encode
                else:
                    raise Exception('Content 无法处理。')

                if part.get_content_type() == 'text/html':
                    content = {'text': BeautifulSoup(content, features='lxml').text, 'html': content}
                else:
                    content = {'text': content}

    return content
