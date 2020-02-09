import re

replace_list = {
    'òa': 'oà', 'óa': 'oá', 'ỏa': 'oả', 'õa': 'oã', 'ọa': 'oạ', 'òe': 'oè', 'óe': 'oé', 'ỏe': 'oẻ',
    'õe': 'oẽ', 'ọe': 'oẹ', 'ùy': 'uỳ', 'úy': 'uý', 'ủy': 'uỷ', 'ũy': 'uỹ', 'ụy': 'uỵ', 'uả': 'ủa',
    'ả': 'ả', 'ố': 'ố', 'u´': 'ố', 'ỗ': 'ỗ', 'ồ': 'ồ', 'ổ': 'ổ', 'ấ': 'ấ', 'ẫ': 'ẫ', 'ẩ': 'ẩ',
    'ầ': 'ầ', 'ỏ': 'ỏ', 'ề': 'ề', 'ễ': 'ễ', 'ắ': 'ắ', 'ủ': 'ủ', 'ế': 'ế', 'ở': 'ở', 'ỉ': 'ỉ',
    'ẻ': 'ẻ', 'àk': u'à ', 'aˋ': 'à', 'iˋ': 'ì', 'ă´': 'ắ', 'ử': 'ử', 'e˜': 'ẽ', 'y˜': 'ỹ', 'a´': 'á',
    # Remove emoji
    '👹': '', '👻': '', '💃': '', '🤙': '', '👍': '', '💄': '', '💎': '', '💩': '', '😕': '', '😱': '', '😸': '',
    '😾': '', '🚫': '', '🤬': '', '🧚': '', '🧡': '', '🐶': '', '👎': '', '😣': '', '✨': '', '❣': '', '♥': '',
    '🤩': '', 'like': '', '💌': '', '❌': '', '👎': '', '👹': '', '💀': '', '🔥': '', '🤔': '', '😏': '', '😐': '',
    '😑': '', '😒': '', '😓': '', '😔': '', '😕': '', '😖': '', '😞': '', '😟': '', '😠': '', '😡': '', '😢': '',
    '😣': '', '😤': '', '😥': '', '😧': '', '😨': '', '😩': '', '😪': '', '😫': '', '😭': '', '😰': '', '😱': '',
    '😳': '', '😵': '', '😶': '', '😾': '', '🙁': '', '🙏': '', '🚫': '', '♡': '', '✌': '', '✨': '', '❤': '', '☹': '',
    '🌝': '', '🌷': '', '🌼': '', '💌': '', '💎': '', '🤣': '', '🖤': '', '🤤': '', ':(': '', '😢': '', '❤': '',
    '😍': '', '🏻': '',
    '😘': '', '😪': '', '😊': '', '?': '?', '😁': '', '💖': '', '😟': '', '😭': '', '💯': '', '💗': '', '♡': '',
    '💜': '',
    '🤗': '', '^^': '', '😨': '', '☺': '', '💋': '', '👌': '', '😖': '', '😀': '', ':((': '', '😡': '', '😠': '',
    '😒': '',
    '🙂': '', '😏': '', '😝': '', '😄': '', '😙': '', '😤': '', '😎': '', '😆': '', '💚': '', '✌': '', '💕': '',
    '😞': '',
    '😓': '', '️🆗️': '', '😉': '', '😂': '', '=))': '', '😋': '', '💓': '', '😐': '', '😫': '', '😥': '', '💀': '',
    '😃': '', '😬': '😬', '😌': '😌', '💛': '', '🤝': '', '🎈': '', '😗': '', '🤔': '', '😑': '', '🔥': '', '😻': '',
    '💙': '', '💟': '', '😚': '', '❌': '', '👏': '', ';)': '', '<3': '', '🌝': '', '🌷': '', '🌸': '', '🌺': '',
    '🌼': '',
    '🍓': '', '🐅': '', '🐾': '', '👉': '', '💐': '', '💞': '', '💥': '', '💪': '', '💰': '', '😇': '', '😛': '',
    '😜': '',
    '🙃': '', '🤑': '', '🤪': '', '🎉': u'', ' :D': '', ' :v': '',
    # Chuẩn hóa 1 số sentiment words/English words
    ':))': ' ', ':)': ' ', 'ô kêi': ' ok ', 'okie': ' ok ', ' o kê ': ' ok ', 'okey': ' ok ', 'ôkê': ' ok ',
    'smp': 'điện thoại thông minh',
    'oki': ' ok ', ' oke ': ' ok ', ' okay': ' ok ', 'okê': ' ok ', ' tks ': u' cám ơn ', 'thks': u' cám ơn ',
    'haizz': '',
    'thanks': u' cám ơn ', 'ths': u' cám ơn ', 'thank': u' cám ơn ', 'kg ': u' không ', 'not': u' không ',
    'simili': 'giống', ' a ': ' anh ', ' e ': ' em ',
    u' kg ': u' không ', '"k ': u' không ', ' kh ': u' không ', 'kô': u' không ', 'hok': u' không ',
    ' kp ': u' không phải ', 'roleyes': '',
    u' kô ': u' không ', '"ko ': u' không ', u' ko ': u' không ', u' k ': u' không ', 'khong': u' không ',
    u' hok ': u' không ', 'dél': 'đéo',
    'he he': ' ', 'hehe': ' ', 'hihi': ' ', 'haha': ' ', 'hjhj': ' ', ' lol ': '', 'cute': u' dễ thương ',
    ' vs ': u' với ', 'zỵ': 'vậy', 'cmt': 'bình luận',
    'đc': u' được ', 'wa': ' quá ', 'wá': u' quá', '“': ' ', 'dk': u' được ', 'dc': u' được ', 'đk': u' được ',
    u' đx ': u' được ', 'link': 'đường dẫn',
    ' sz ': u' cỡ ', 'size': u' cỡ ', 'authentic': u' chuẩn chính hãng ', u' aut ': u' chuẩn chính hãng ',
    u' auth ': u' chuẩn chính hãng ', 'delete': 'xóa',
    'thick': u' ', 'store': u' cửa hàng ', 'shop': u' cửa hàng ', 'sp': u' sản phẩm ', 'gud': u' tốt ', 'god': u' tốt ',
    'wel done': ' tốt ', 'review': 'cảm nhận',
    'good': u' tốt ', 'gút': u' tốt ', 'sấu': u' xấu ', 'gut': u' tốt ', u' tot ': u' tốt ', u' nice ': u' tốt ',
    'perfect': 'rất tốt', 'comision': 'chiết khấu',
    'bt': u' bình thường ', 'time': u' thời gian ', 'qá': u' quá ', u' ship ': u' giao hàng ', u' m ': u' mình ',
    u' mik ': u' mình ', 'me too': 'tôi cũng vậy',
    'ể': 'ể', 'product': 'sản phẩm', 'quality': 'chất lượng', 'chat': ' chất ', 'excelent': 'hoàn hảo', 'bad': 'tệ',
    'fresh': ' tươi ', 'sad': ' tệ ',
    'date': u' hạn sử dụng ', 'hsd': u' hạn sử dụng ', 'quickly': u' nhanh ', 'quick': u' nhanh ', 'fast': u' nhanh ',
    'delivery': u' giao hàng ', 'zoom': 'phóng to',
    u' síp ': u' giao hàng ', 'beautiful': u' đẹp tuyệt vời ', u' tl ': u' trả lời ', u' r ': u' rồi ',
    u' shopE ': u' cửa hàng ', u' order ': u' đặt hàng ',
    'chất lg': u' chất lượng ', u' sd ': u' sử dụng ', u' dt ': u' điện thoại ', u' nt ': u' nhắn tin ',
    u' tl ': u' trả lời ', u' sài ': u' xài ', u'bjo': u' bao giờ ',
    'thik': u' thích ', u' sop ': u' cửa hàng ', ' fb ': ' facebook ', ' face ': ' facebook ', ' very ': u' rất ',
    u'quả ng ': u' quảng  ', 'dep': u' đẹp ',
    u' xau ': u' xấu ', 'delicious': u' ngon ', u'hàg': u' hàng ', u'qủa': u' quả ', 'iu': u' yêu ',
    'fake': u' giả mạo ', 'trl': 'trả lời', '><': u' ',
    ' por ': u' tệ ', ' poor ': u' tệ ', 'ib': u' nhắn tin ', 'rep': u' trả lời ', u'fback': ' feedback ',
    'fedback': ' feedback ', 'ji': 'gì', 'haizzz': '', 'grace': 'chú trọng'}


class Text:
    def __init__(self, text):
        self.text = text
        self.to_string()
        self.lowercase()

    def to_string(self):
        self.text = str(self.text)

    def lowercase(self):
        self.text = self.text.lower()

    def normalize(self):
        self.punctuate()
        self.regex_normalize()
        return self.text

    def punctuate(self):
        for k, v in replace_list.items():
            self.text = self.text.replace(k, v)

    def regex_normalize(self):
        patterns = ['\[([^\]=]+)(?:=[^\]]+)?\].*?\[\/\\1\\n]', r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*',
                    "[\(\[].*?[\)\]]"]
        for pattern in patterns:
            self.text = re.sub(pattern, '', self.text)

        self.text = re.sub(r'(\D)\1+', r'\1', self.text)
        self.text = self.text.replace('\r', '')
        # Remove numbers
        self.text = re.sub(r'\d+', ' ', self.text)
        # Removing multiple spaces
        self.text = re.sub(r'\s+', ' ', self.text)
