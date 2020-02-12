#  encoding=utf-8

# A collection of regular expressions for parsing Tweet text. The regular expression
# list is frozen at load time to ensure immutability. These reular expressions are
# used throughout the Twitter classes. Special care has been taken to make
# sure these reular expressions work with Tweets in all languages.
import re, string

REGEXEN = {} # :nodoc:

def regex_range(start, end = None):
    if end:
        return u'%s-%s' % (unichr(start), unichr(end))
    else:
        return u'%s' % unichr(start)

# Space is more than %20, U+3000 for example is the full-width space used with Kanji. Provide a short-hand
# to access both the list of characters and a pattern suitible for use with String#split
#  Taken from: ActiveSupport::Multibyte::Handlers::UTF8Handler::UNICODE_WHITESPACE
UNICODE_SPACES = []
for space in reduce(lambda x,y: x + y if type(y) == list else x + [y], [
        range(0x0009, 0x000D),  # White_Space # Cc   [5] <control-0009>..<control-000D>
        0x0020,                 # White_Space # Zs       SPACE
        0x0085,                 # White_Space # Cc       <control-0085>
        0x00A0,                 # White_Space # Zs       NO-BREAK SPACE
        0x1680,                 # White_Space # Zs       OGHAM SPACE MARK
        0x180E,                 # White_Space # Zs       MONGOLIAN VOWEL SEPARATOR
        range(0x2000, 0x200A),  # White_Space # Zs  [11] EN QUAD..HAIR SPACE
        0x2028,                 # White_Space # Zl       LINE SEPARATOR
        0x2029,                 # White_Space # Zp       PARAGRAPH SEPARATOR
        0x202F,                 # White_Space # Zs       NARROW NO-BREAK SPACE
        0x205F,                 # White_Space # Zs       MEDIUM MATHEMATICAL SPACE
        0x3000,                 # White_Space # Zs       IDEOGRAPHIC SPACE
    ]):
    UNICODE_SPACES.append(unichr(space))
REGEXEN['spaces'] = re.compile(ur''.join(UNICODE_SPACES))

# Characters not allowed in Tweets
INVALID_CHARACTERS  =   [
    0xFFFE, 0xFEFF,                         # BOM
    0xFFFF,                                 # Special
    0x202A, 0x202B, 0x202C, 0x202D, 0x202E, # Directional change
]
REGEXEN['invalid_control_characters']   =   [unichr(x) for x in INVALID_CHARACTERS]

REGEXEN['list_name'] = re.compile(ur'^[a-zA-Z][a-zA-Z0-9_\-\u0080-\u00ff]{0,24}$')

# Latin accented characters
# Excludes 0xd7 from the range (the multiplication sign, confusable with "x").
# Also excludes 0xf7, the division sign
LATIN_ACCENTS = [
    regex_range(0x00c0, 0x00d6),
    regex_range(0x00d8, 0x00f6),
    regex_range(0x00f8, 0x00ff),
    regex_range(0x0100, 0x024f),
    regex_range(0x0253, 0x0254),
    regex_range(0x0256, 0x0257),
    regex_range(0x0259),
    regex_range(0x025b),
    regex_range(0x0263),
    regex_range(0x0268),
    regex_range(0x026f),
    regex_range(0x0272),
    regex_range(0x0289),
    regex_range(0x028b),
    regex_range(0x02bb),
    regex_range(0x0300, 0x036f),
    regex_range(0x1e00, 0x1eff),
]
REGEXEN['latin_accents'] = re.compile(ur''.join(LATIN_ACCENTS), re.IGNORECASE | re.UNICODE)
LATIN_ACCENTS = u''.join(LATIN_ACCENTS)

RTL_CHARACTERS = ''.join([
    regex_range(0x0600,0x06FF),
    regex_range(0x0750,0x077F),
    regex_range(0x0590,0x05FF),
    regex_range(0xFE70,0xFEFF)
])

NON_LATIN_HASHTAG_CHARS = ''.join([
    # Cyrillic (Russian, Ukrainian, etc.)
    regex_range(0x0400, 0x04ff), # Cyrillic
    regex_range(0x0500, 0x0527), # Cyrillic Supplement
    regex_range(0x2de0, 0x2dff), # Cyrillic Extended A
    regex_range(0xa640, 0xa69f), # Cyrillic Extended B
    regex_range(0x0591, 0x05bf), # Hebrew
    regex_range(0x05c1, 0x05c2),
    regex_range(0x05c4, 0x05c5),
    regex_range(0x05c7),
    regex_range(0x05d0, 0x05ea),
    regex_range(0x05f0, 0x05f4),
    regex_range(0xfb12, 0xfb28), # Hebrew Presentation Forms
    regex_range(0xfb2a, 0xfb36),
    regex_range(0xfb38, 0xfb3c),
    regex_range(0xfb3e),
    regex_range(0xfb40, 0xfb41),
    regex_range(0xfb43, 0xfb44),
    regex_range(0xfb46, 0xfb4f),
    regex_range(0x0610, 0x061a), # Arabic
    regex_range(0x0620, 0x065f),
    regex_range(0x066e, 0x06d3),
    regex_range(0x06d5, 0x06dc),
    regex_range(0x06de, 0x06e8),
    regex_range(0x06ea, 0x06ef),
    regex_range(0x06fa, 0x06fc),
    regex_range(0x06ff),
    regex_range(0x0750, 0x077f), # Arabic Supplement
    regex_range(0x08a0),         # Arabic Extended A
    regex_range(0x08a2, 0x08ac),
    regex_range(0x08e4, 0x08fe),
    regex_range(0xfb50, 0xfbb1), # Arabic Pres. Forms A
    regex_range(0xfbd3, 0xfd3d),
    regex_range(0xfd50, 0xfd8f),
    regex_range(0xfd92, 0xfdc7),
    regex_range(0xfdf0, 0xfdfb),
    regex_range(0xfe70, 0xfe74), # Arabic Pres. Forms B
    regex_range(0xfe76, 0xfefc),
    regex_range(0x200c, 0x200c), # Zero-Width Non-Joiner
    regex_range(0x0e01, 0x0e3a), # Thai
    regex_range(0x0e40, 0x0e4e), # Hangul (Korean)
    regex_range(0x1100, 0x11ff), # Hangul Jamo
    regex_range(0x3130, 0x3185), # Hangul Compatibility Jamo
    regex_range(0xA960, 0xA97F), # Hangul Jamo Extended-A
    regex_range(0xAC00, 0xD7AF), # Hangul Syllables
    regex_range(0xD7B0, 0xD7FF), # Hangul Jamo Extended-B
    regex_range(0xFFA1, 0xFFDC)  # Half-width Hangul
])

CJ_HASHTAG_CHARACTERS = ''.join([
    regex_range(0x30A1, 0x30FA), regex_range(0x30FC, 0x30FE), # Katakana (full-width)
    regex_range(0xFF66, 0xFF9F), # Katakana (half-width)
    regex_range(0xFF10, 0xFF19), regex_range(0xFF21, 0xFF3A), regex_range(0xFF41, 0xFF5A), # Latin (full-width)
    regex_range(0x3041, 0x3096), regex_range(0x3099, 0x309E), # Hiragana
    regex_range(0x3400, 0x4DBF), # Kanji (CJK Extension A)
    regex_range(0x4E00, 0x9FFF), # Kanji (Unified)
])

try:
    CJ_HASHTAG_CHARACTERS = ''.join([
        CJ_HASHTAG_CHARACTERS,
        regex_range(0x20000, 0x2A6DF), # Kanji (CJK Extension B)
        regex_range(0x2A700, 0x2B73F), # Kanji (CJK Extension C)
        regex_range(0x2B740, 0x2B81F), # Kanji (CJK Extension D)
        regex_range(0x2F800, 0x2FA1F), regex_range(0x3003), regex_range(0x3005), regex_range(0x303B) # Kanji (CJK supplement)
    ])
except ValueError:
    # this is a narrow python build so these extended Kanji characters won't work
    pass

PUNCTUATION_CHARS = ur'!"#$%&\'()*+,-./:;<=>?@\[\]^_\`{|}~'
SPACE_CHARS = ur" \t\n\x0B\f\r"
CTRL_CHARS = ur"\x00-\x1F\x7F"

# A hashtag must contain latin characters, numbers and underscores, but not all numbers.
HASHTAG_ALPHA = ur'[a-z_%s]' % (LATIN_ACCENTS + NON_LATIN_HASHTAG_CHARS + CJ_HASHTAG_CHARACTERS)
HASHTAG_ALPHANUMERIC = ur'[a-z0-9_%s]' % (LATIN_ACCENTS + NON_LATIN_HASHTAG_CHARS + CJ_HASHTAG_CHARACTERS)
HASHTAG_BOUNDARY = ur'\A|\z|\[|[^&a-z0-9_%s]' % (LATIN_ACCENTS + NON_LATIN_HASHTAG_CHARS + CJ_HASHTAG_CHARACTERS)

HASHTAG = re.compile(ur'(%s)(#|＃)(%s*%s%s*)' % (HASHTAG_BOUNDARY, HASHTAG_ALPHANUMERIC, HASHTAG_ALPHA, HASHTAG_ALPHANUMERIC), re.IGNORECASE)

REGEXEN['valid_hashtag'] = HASHTAG
REGEXEN['end_hashtag_match'] = re.compile(ur'\A(?:[#＃]|:\/\/)', re.IGNORECASE | re.UNICODE)
REGEXEN['numeric_only'] = re.compile(ur'^[\d]+$')

REGEXEN['valid_mention_preceding_chars'] = re.compile(r'(?:[^a-zA-Z0-9_!#\$%&*@＠]|^|RT:?)')
REGEXEN['at_signs'] = re.compile(ur'[@＠]')
REGEXEN['valid_mention_or_list'] = re.compile(
    ur'(%s)' % REGEXEN['valid_mention_preceding_chars'].pattern.decode('utf-8') +   # preceding character
    ur'(%s)' % REGEXEN['at_signs'].pattern +                                        # at mark
    ur'([a-zA-Z0-9_]{1,20})' +                                                      # screen name
    ur'(\/[a-zA-Z][a-zA-Z0-9_\-]{0,24})?'                                           # list (optional)
)
REGEXEN['valid_reply'] = re.compile(ur'^(?:[%s])*%s([a-zA-Z0-9_]{1,20})' % (REGEXEN['spaces'].pattern, REGEXEN['at_signs'].pattern), re.IGNORECASE | re.UNICODE)
 # Used in Extractor for final filtering
REGEXEN['end_mention_match'] = re.compile(ur'\A(?:%s|[%s]|:\/\/)' % (REGEXEN['at_signs'].pattern, REGEXEN['latin_accents'].pattern), re.IGNORECASE | re.UNICODE)

# URL related hash regex collection
REGEXEN['valid_url_preceding_chars'] = re.compile(ur'(?:[^A-Z0-9@＠$#＃%s]|^)' % ur''.join(REGEXEN['invalid_control_characters']), re.IGNORECASE | re.UNICODE)
REGEXEN['invalid_url_without_protocol_preceding_chars'] = re.compile(ur'[-_.\/]$')
DOMAIN_VALID_CHARS = ur'[^%s%s%s%s%s]' % (PUNCTUATION_CHARS, SPACE_CHARS, CTRL_CHARS, ur''.join(REGEXEN['invalid_control_characters']), ur''.join(UNICODE_SPACES))
REGEXEN['valid_subdomain'] = re.compile(ur'(?:(?:%s(?:[_-]|%s)*)?%s\.)' % (DOMAIN_VALID_CHARS, DOMAIN_VALID_CHARS, DOMAIN_VALID_CHARS), re.IGNORECASE | re.UNICODE)
REGEXEN['valid_domain_name'] = re.compile(ur'(?:(?:%s(?:[-]|%s)*)?%s\.)' % (DOMAIN_VALID_CHARS, DOMAIN_VALID_CHARS, DOMAIN_VALID_CHARS), re.IGNORECASE | re.UNICODE)
REGEXEN['valid_gTLD'] = re.compile(ur'(?:(?:삼성|닷컴|닷넷|香格里拉|餐厅|食品|飞利浦|電訊盈科|集团|通販|购物|谷歌|诺基亚|联通|网络|网站|网店|网址|组织机构|移动|珠宝|点看|游戏|淡马锡|机构|書籍|时尚|新闻|政府|政务|招聘|手表|手机|我爱你|慈善|微博|广东|工行|家電|娱乐|天主教|大拿|大众汽车|在线|嘉里大酒店|嘉里|商标|商店|商城|公益|公司|八卦|健康|信息|佛山|企业|中文网|中信|世界|ポイント|ファッション|セール|ストア|コム|グーグル|クラウド|みんな|คอม|संगठन|नेट|कॉम|همراه|موقع|موبايلي|كوم|كاثوليك|عرب|شبكة|بيتك|بازار|العليان|ارامكو|اتصالات|ابوظبي|קום|сайт|рус|орг|онлайн|москва|ком|католик|дети|zuerich|zone|zippo|zip|zero|zara|zappos|yun|youtube|you|yokohama|yoga|yodobashi|yandex|yamaxun|yahoo|yachts|xyz|xxx|xperia|xin|xihuan|xfinity|xerox|xbox|wtf|wtc|wow|world|works|work|woodside|wolterskluwer|wme|winners|wine|windows|win|williamhill|wiki|wien|whoswho|weir|weibo|wedding|wed|website|weber|webcam|weatherchannel|weather|watches|watch|warman|wanggou|wang|walter|walmart|wales|vuelos|voyage|voto|voting|vote|volvo|volkswagen|vodka|vlaanderen|vivo|viva|vistaprint|vista|vision|visa|virgin|vip|vin|villas|viking|vig|video|viajes|vet|versicherung|vermögensberatung|vermögensberater|verisign|ventures|vegas|vanguard|vana|vacations|ups|uol|uno|university|unicom|uconnect|ubs|ubank|tvs|tushu|tunes|tui|tube|trv|trust|travelersinsurance|travelers|travelchannel|travel|training|trading|trade|toys|toyota|town|tours|total|toshiba|toray|top|tools|tokyo|today|tmall|tkmaxx|tjx|tjmaxx|tirol|tires|tips|tiffany|tienda|tickets|tiaa|theatre|theater|thd|teva|tennis|temasek|telefonica|telecity|tel|technology|tech|team|tdk|tci|taxi|tax|tattoo|tatar|tatamotors|target|taobao|talk|taipei|tab|systems|symantec|sydney|swiss|swiftcover|swatch|suzuki|surgery|surf|support|supply|supplies|sucks|style|study|studio|stream|store|storage|stockholm|stcgroup|stc|statoil|statefarm|statebank|starhub|star|staples|stada|srt|srl|spreadbetting|spot|sport|spiegel|space|soy|sony|song|solutions|solar|sohu|software|softbank|social|soccer|sncf|smile|smart|sling|skype|sky|skin|ski|site|singles|sina|silk|shriram|showtime|show|shouji|shopping|shop|shoes|shiksha|shia|shell|shaw|sharp|shangrila|sfr|sexy|sex|sew|seven|ses|services|sener|select|seek|security|secure|seat|search|scot|scor|scjohnson|science|schwarz|schule|school|scholarships|schmidt|schaeffler|scb|sca|sbs|sbi|saxo|save|sas|sarl|sapo|sap|sanofi|sandvikcoromant|sandvik|samsung|samsclub|salon|sale|sakura|safety|safe|saarland|ryukyu|rwe|run|ruhr|rugby|rsvp|room|rogers|rodeo|rocks|rocher|rmit|rip|rio|ril|rightathome|ricoh|richardli|rich|rexroth|reviews|review|restaurant|rest|republican|report|repair|rentals|rent|ren|reliance|reit|reisen|reise|rehab|redumbrella|redstone|red|recipes|realty|realtor|realestate|read|raid|radio|racing|qvc|quest|quebec|qpon|pwc|pub|prudential|pru|protection|property|properties|promo|progressive|prof|productions|prod|pro|prime|press|praxi|pramerica|post|porn|politie|poker|pohl|pnc|plus|plumbing|playstation|play|place|pizza|pioneer|pink|ping|pin|pid|pictures|pictet|pics|piaget|physio|photos|photography|photo|phone|philips|phd|pharmacy|pfizer|pet|pccw|pay|passagens|party|parts|partners|pars|paris|panerai|panasonic|pamperedchef|page|ovh|ott|otsuka|osaka|origins|orientexpress|organic|org|orange|oracle|open|ooo|onyourside|online|onl|ong|one|omega|ollo|oldnavy|olayangroup|olayan|okinawa|office|off|observer|obi|nyc|ntt|nrw|nra|nowtv|nowruz|now|norton|northwesternmutual|nokia|nissay|nissan|ninja|nikon|nike|nico|nhk|ngo|nfl|nexus|nextdirect|next|news|newholland|new|neustar|network|netflix|netbank|net|nec|nba|navy|natura|nationwide|name|nagoya|nadex|nab|mutuelle|mutual|museum|mtr|mtpc|mtn|msd|movistar|movie|mov|motorcycles|moto|moscow|mortgage|mormon|mopar|montblanc|monster|money|monash|mom|moi|moe|moda|mobily|mobile|mobi|mma|mls|mlb|mitsubishi|mit|mint|mini|mil|microsoft|miami|metlife|merckmsd|meo|menu|men|memorial|meme|melbourne|meet|media|med|mckinsey|mcdonalds|mcd|mba|mattel|maserati|marshalls|marriott|markets|marketing|market|map|mango|management|man|makeup|maison|maif|madrid|macys|luxury|luxe|lupin|lundbeck|ltda|ltd|lplfinancial|lpl|love|lotto|lotte|london|lol|loft|locus|locker|loans|loan|llc|lixil|living|live|lipsy|link|linde|lincoln|limo|limited|lilly|like|lighting|lifestyle|lifeinsurance|life|lidl|liaison|lgbt|lexus|lego|legal|lefrak|leclerc|lease|lds|lawyer|law|latrobe|latino|lat|lasalle|lanxess|landrover|land|lancome|lancia|lancaster|lamer|lamborghini|ladbrokes|lacaixa|kyoto|kuokgroup|kred|krd|kpn|kpmg|kosher|komatsu|koeln|kiwi|kitchen|kindle|kinder|kim|kia|kfh|kerryproperties|kerrylogistics|kerryhotels|kddi|kaufen|juniper|juegos|jprs|jpmorgan|joy|jot|joburg|jobs|jnj|jmp|jll|jlc|jio|jewelry|jetzt|jeep|jcp|jcb|java|jaguar|iwc|iveco|itv|itau|istanbul|ist|ismaili|iselect|irish|ipiranga|investments|intuit|international|intel|int|insure|insurance|institute|ink|ing|info|infiniti|industries|inc|immobilien|immo|imdb|imamat|ikano|iinet|ifm|ieee|icu|ice|icbc|ibm|hyundai|hyatt|hughes|htc|hsbc|how|house|hotmail|hotels|hoteles|hot|hosting|host|hospital|horse|honeywell|honda|homesense|homes|homegoods|homedepot|holiday|holdings|hockey|hkt|hiv|hitachi|hisamitsu|hiphop|hgtv|hermes|here|helsinki|help|healthcare|health|hdfcbank|hdfc|hbo|haus|hangout|hamburg|hair|guru|guitars|guide|guge|gucci|guardian|group|grocery|gripe|green|gratis|graphics|grainger|gov|got|gop|google|goog|goodyear|goodhands|goo|golf|goldpoint|gold|godaddy|gmx|gmo|gmbh|gmail|globo|global|gle|glass|glade|giving|gives|gifts|gift|ggee|george|genting|gent|gea|gdn|gbiz|garden|gap|games|game|gallup|gallo|gallery|gal|fyi|futbol|furniture|fund|fun|fujixerox|fujitsu|ftr|frontier|frontdoor|frogans|frl|fresenius|free|fox|foundation|forum|forsale|forex|ford|football|foodnetwork|food|foo|fly|flsmidth|flowers|florist|flir|flights|flickr|fitness|fit|fishing|fish|firmdale|firestone|fire|financial|finance|final|film|fido|fidelity|fiat|ferrero|ferrari|feedback|fedex|fast|fashion|farmers|farm|fans|fan|family|faith|fairwinds|fail|fage|extraspace|express|exposed|expert|exchange|everbank|events|eus|eurovision|etisalat|esurance|estate|esq|erni|ericsson|equipment|epson|epost|enterprises|engineering|engineer|energy|emerck|email|education|edu|edeka|eco|eat|earth|dvr|dvag|durban|dupont|duns|dunlop|duck|dubai|dtv|drive|download|dot|doosan|domains|doha|dog|dodge|doctor|docs|dnp|diy|dish|discover|discount|directory|direct|digital|diet|diamonds|dhl|dev|design|desi|dentist|dental|democrat|delta|deloitte|dell|delivery|degree|deals|dealer|deal|dds|dclk|day|datsun|dating|date|data|dance|dad|dabur|cyou|cymru|cuisinella|csc|cruises|cruise|crs|crown|cricket|creditunion|creditcard|credit|courses|coupons|coupon|country|corsica|coop|cool|cookingchannel|cooking|contractors|contact|consulting|construction|condos|comsec|computer|compare|company|community|commbank|comcast|com|cologne|college|coffee|codes|coach|clubmed|club|cloud|clothing|clinique|clinic|click|cleaning|claims|cityeats|city|citic|citi|citadel|cisco|circle|cipriani|church|chrysler|chrome|christmas|chloe|chintai|cheap|chat|chase|charity|channel|chanel|cfd|cfa|cern|ceo|center|ceb|cbs|cbre|cbn|cba|catholic|catering|cat|casino|cash|caseih|case|casa|cartier|cars|careers|career|care|cards|caravan|car|capitalone|capital|capetown|canon|cancerresearch|camp|camera|cam|calvinklein|call|cal|cafe|cab|bzh|buzz|buy|business|builders|build|bugatti|budapest|brussels|brother|broker|broadway|bridgestone|bradesco|box|boutique|bot|boston|bostik|bosch|boots|booking|book|boo|bond|bom|bofa|boehringer|boats|bnpparibas|bnl|bmw|bms|blue|bloomberg|blog|blockbuster|blanco|blackfriday|black|biz|bio|bingo|bing|bike|bid|bible|bharti|bet|bestbuy|best|berlin|bentley|beer|beauty|beats|bcn|bcg|bbva|bbt|bbc|bayern|bauhaus|basketball|baseball|bargains|barefoot|barclays|barclaycard|barcelona|bar|bank|band|bananarepublic|banamex|baidu|baby|azure|axa|aws|avianca|autos|auto|author|auspost|audio|audible|audi|auction|attorney|athleta|associates|asia|asda|arte|art|arpa|army|archi|aramco|arab|aquarelle|apple|app|apartments|aol|anz|anquan|android|analytics|amsterdam|amica|amfam|amex|americanfamily|americanexpress|alstom|alsace|ally|allstate|allfinanz|alipay|alibaba|alfaromeo|akdn|airtel|airforce|airbus|aigo|aig|agency|agakhan|africa|afl|afamilycompany|aetna|aero|aeg|adult|ads|adac|actor|active|aco|accountants|accountant|accenture|academy|abudhabi|abogado|able|abc|abbvie|abbott|abb|abarth|aarp|aaa|onion)(?=[^0-9a-z]|$))', re.IGNORECASE | re.UNICODE)
REGEXEN['valid_ccTLD'] = re.compile(ur'(?:(?:한국|香港|澳門|新加坡|台灣|台湾|中國|中国|გე|ไทย|ලංකා|ഭാരതം|ಭಾರತ|భారత్|சிங்கப்பூர்|இலங்கை|இந்தியா|ଭାରତ|ભારત|ਭਾਰਤ|ভাৰত|ভারত|বাংলা|भारोत|भारतम्|भारत|ڀارت|پاکستان|موريتانيا|مليسيا|مصر|قطر|فلسطين|عمان|عراق|سورية|سودان|تونس|بھارت|بارت|ایران|امارات|المغرب|السعودية|الجزائر|الاردن|հայ|қаз|укр|срб|рф|мон|мкд|ею|бел|бг|ελ|zw|zm|za|yt|ye|ws|wf|vu|vn|vi|vg|ve|vc|va|uz|uy|us|um|uk|ug|ua|tz|tw|tv|tt|tr|tp|to|tn|tm|tl|tk|tj|th|tg|tf|td|tc|sz|sy|sx|sv|su|st|ss|sr|so|sn|sm|sl|sk|sj|si|sh|sg|se|sd|sc|sb|sa|rw|ru|rs|ro|re|qa|py|pw|pt|ps|pr|pn|pm|pl|pk|ph|pg|pf|pe|pa|om|nz|nu|nr|np|no|nl|ni|ng|nf|ne|nc|na|mz|my|mx|mw|mv|mu|mt|ms|mr|mq|mp|mo|mn|mm|ml|mk|mh|mg|mf|me|md|mc|ma|ly|lv|lu|lt|ls|lr|lk|li|lc|lb|la|kz|ky|kw|kr|kp|kn|km|ki|kh|kg|ke|jp|jo|jm|je|it|is|ir|iq|io|in|im|il|ie|id|hu|ht|hr|hn|hm|hk|gy|gw|gu|gt|gs|gr|gq|gp|gn|gm|gl|gi|gh|gg|gf|ge|gd|gb|ga|fr|fo|fm|fk|fj|fi|eu|et|es|er|eh|eg|ee|ec|dz|do|dm|dk|dj|de|cz|cy|cx|cw|cv|cu|cr|co|cn|cm|cl|ck|ci|ch|cg|cf|cd|cc|ca|bz|by|bw|bv|bt|bs|br|bq|bo|bn|bm|bl|bj|bi|bh|bg|bf|be|bd|bb|ba|az|ax|aw|au|at|as|ar|aq|ao|an|am|al|ai|ag|af|ae|ad|ac)(?=[^0-9a-z]|$))', re.IGNORECASE | re.UNICODE)
REGEXEN['valid_punycode'] = re.compile(ur'(?:xn--[0-9a-z]+)', re.IGNORECASE | re.UNICODE)

REGEXEN['valid_domain'] = re.compile(ur'(?:%s*%s(?:%s|%s|%s))' % (REGEXEN['valid_subdomain'].pattern, REGEXEN['valid_domain_name'].pattern, REGEXEN['valid_gTLD'].pattern, REGEXEN['valid_ccTLD'].pattern, REGEXEN['valid_punycode'].pattern), re.IGNORECASE | re.UNICODE)

# This is used in Extractor
REGEXEN['valid_ascii_domain'] = re.compile(ur'(?:(?:[A-Za-z0-9\-_]|[%s])+\.)+(?:%s|%s|%s)' % (REGEXEN['latin_accents'].pattern, REGEXEN['valid_gTLD'].pattern, REGEXEN['valid_ccTLD'].pattern, REGEXEN['valid_punycode'].pattern), re.IGNORECASE | re.UNICODE)

# This is used in Extractor for stricter t.co URL extraction
REGEXEN['valid_tco_url'] = re.compile(ur'^https?:\/\/t\.co\/[a-z0-9]+', re.IGNORECASE | re.UNICODE)

# This is used in Extractor to filter out unwanted URLs.
REGEXEN['invalid_short_domain'] = re.compile(ur'\A%s%s\Z' % (REGEXEN['valid_domain_name'].pattern, REGEXEN['valid_ccTLD'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['valid_port_number'] = re.compile(ur'[0-9]+')

REGEXEN['valid_general_url_path_chars'] = re.compile(ur"[a-z0-9!\*';:=\+\,\.\$\/%%#\[\]\-_~&|@%s]" % LATIN_ACCENTS, re.IGNORECASE | re.UNICODE)
# Allow URL paths to contain balanced parens
#  1. Used in Wikipedia URLs like /Primer_(film)
#  2. Used in IIS sessions like /S(dfd346)/
REGEXEN['valid_url_balanced_parens'] = re.compile(ur'\(%s+\)' % REGEXEN['valid_general_url_path_chars'].pattern, re.IGNORECASE | re.UNICODE)
# Valid end-of-path chracters (so /foo. does not gobble the period).
#   1. Allow =&# for empty URL parameters and other URL-join artifacts
REGEXEN['valid_url_path_ending_chars'] = re.compile(ur'[a-z0-9=_#\/\+\-%s]|(?:%s)' % (LATIN_ACCENTS, REGEXEN['valid_url_balanced_parens'].pattern), re.IGNORECASE | re.UNICODE)
REGEXEN['valid_url_path'] = re.compile(ur'(?:(?:%s*(?:%s %s*)*%s)|(?:%s+\/))' % (REGEXEN['valid_general_url_path_chars'].pattern, REGEXEN['valid_url_balanced_parens'].pattern, REGEXEN['valid_general_url_path_chars'].pattern, REGEXEN['valid_url_path_ending_chars'].pattern, REGEXEN['valid_general_url_path_chars'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['valid_url_query_chars'] = re.compile(ur"[a-z0-9!?\*'\(\);:&=\+\$\/%#\[\]\-_\.,~|@]", re.IGNORECASE | re.UNICODE)
REGEXEN['valid_url_query_ending_chars'] = re.compile(ur'[a-z0-9_&=#\/]', re.IGNORECASE | re.UNICODE)
REGEXEN['valid_url'] = re.compile(ur'((%s)((https?:\/\/)?(%s)(?::(%s))?(/%s*)?(\?%s*%s)?))' % (
    REGEXEN['valid_url_preceding_chars'].pattern,
    REGEXEN['valid_domain'].pattern,
    REGEXEN['valid_port_number'].pattern,
    REGEXEN['valid_url_path'].pattern,
    REGEXEN['valid_url_query_chars'].pattern,
    REGEXEN['valid_url_query_ending_chars'].pattern
), re.IGNORECASE | re.UNICODE)
#   Matches
#   $1 total match
#   $2 Preceeding chracter
#   $3 URL
#   $4 Protocol (optional)
#   $5 Domain(s)
#   $6 Port number (optional)
#   $7 URL Path and anchor
#   $8 Query String

REGEXEN['cashtag'] = re.compile(ur'[a-z]{1,6}(?:[._][a-z]{1,2})?', re.IGNORECASE)
REGEXEN['valid_cashtag'] = re.compile(ur'(^|[%s])(\$|＄|﹩)(%s)(?=$|\s|[%s])' % (REGEXEN['spaces'].pattern, REGEXEN['cashtag'].pattern, PUNCTUATION_CHARS), re.IGNORECASE)

# These URL validation pattern strings are based on the ABNF from RFC 3986
REGEXEN['validate_url_unreserved'] = re.compile(ur'[a-z0-9\-._~]', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_pct_encoded'] = re.compile(ur'(?:%[0-9a-f]{2})', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_sub_delims'] = re.compile(ur"[!$&'()*+,;=]", re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_pchar'] = re.compile(ur'(?:%s|%s|%s|[:\|@])' % (REGEXEN['validate_url_unreserved'].pattern, REGEXEN['validate_url_pct_encoded'].pattern, REGEXEN['validate_url_sub_delims'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['validate_url_scheme'] = re.compile(ur'(?:[a-z][a-z0-9+\-.]*)', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_userinfo'] = re.compile(ur'(?:%s|%s|%s|:)*' % (REGEXEN['validate_url_unreserved'].pattern, REGEXEN['validate_url_pct_encoded'].pattern, REGEXEN['validate_url_sub_delims'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['validate_url_dec_octet'] = re.compile(ur'(?:[0-9]|(?:[1-9][0-9])|(?:1[0-9]{2})|(?:2[0-4][0-9])|(?:25[0-5]))', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_ipv4'] = re.compile(ur'(?:%s(?:\.%s){3})' % (REGEXEN['validate_url_dec_octet'].pattern, REGEXEN['validate_url_dec_octet'].pattern), re.IGNORECASE | re.UNICODE)

# Punting on real IPv6 validation for now
REGEXEN['validate_url_ipv6'] = re.compile(ur'(?:\[[a-f0-9:\.]+\])', re.IGNORECASE | re.UNICODE)

# Also punting on IPvFuture for now
REGEXEN['validate_url_ip'] = re.compile(ur'(?:%s|%s)' % (REGEXEN['validate_url_ipv4'].pattern, REGEXEN['validate_url_ipv6'].pattern), re.IGNORECASE | re.UNICODE)

# This is more strict than the rfc specifies
REGEXEN['validate_url_subdomain_segment'] = re.compile(ur'(?:[a-z0-9](?:[a-z0-9_\-]*[a-z0-9])?)', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_domain_segment'] = re.compile(ur'(?:[a-z0-9](?:[a-z0-9\-]*[a-z0-9])?)', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_domain_tld'] = re.compile(ur'(?:[a-z](?:[a-z0-9\-]*[a-z0-9])?)', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_domain'] = re.compile(ur'(?:(?:%s\.)*(?:%s\.)%s)' % (REGEXEN['validate_url_subdomain_segment'].pattern, REGEXEN['validate_url_domain_segment'].pattern, REGEXEN['validate_url_domain_tld'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['validate_url_host'] = re.compile(ur'(?:%s|%s)' % (REGEXEN['validate_url_ip'].pattern, REGEXEN['validate_url_domain'].pattern), re.IGNORECASE | re.UNICODE)

# Unencoded internationalized domains - this doesn't check for invalid UTF-8 sequences
REGEXEN['validate_url_unicode_subdomain_segment'] = re.compile(ur'(?:(?:[a-z0-9]|[^\x00-\x7f])(?:(?:[a-z0-9_\-]|[^\x00-\x7f])*(?:[a-z0-9]|[^\x00-\x7f]))?)', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_unicode_domain_segment'] = re.compile(ur'(?:(?:[a-z0-9]|[^\x00-\x7f])(?:(?:[a-z0-9\-]|[^\x00-\x7f])*(?:[a-z0-9]|[^\x00-\x7f]))?)', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_unicode_domain_tld'] = re.compile(ur'(?:(?:[a-z]|[^\x00-\x7f])(?:(?:[a-z0-9\-]|[^\x00-\x7f])*(?:[a-z0-9]|[^\x00-\x7f]))?)', re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_unicode_domain'] = re.compile(ur'(?:(?:%s\.)*(?:%s\.)%s)' % (REGEXEN['validate_url_unicode_subdomain_segment'].pattern, REGEXEN['validate_url_unicode_domain_segment'].pattern, REGEXEN['validate_url_unicode_domain_tld'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['validate_url_unicode_host'] = re.compile(ur'(?:%s|%s)' % (REGEXEN['validate_url_ip'].pattern, REGEXEN['validate_url_unicode_domain'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['validate_url_port'] = re.compile(ur'[0-9]{1,5}')

REGEXEN['validate_url_unicode_authority'] = re.compile(ur'(?:(%s)@)?(%s)(?::(%s))?' % (REGEXEN['validate_url_userinfo'].pattern, REGEXEN['validate_url_unicode_host'].pattern, REGEXEN['validate_url_port'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['validate_url_authority'] = re.compile(ur'(?:(%s)@)?(%s)(?::(%s))?' % (REGEXEN['validate_url_userinfo'].pattern, REGEXEN['validate_url_host'].pattern, REGEXEN['validate_url_port'].pattern), re.IGNORECASE | re.UNICODE)

REGEXEN['validate_url_path'] = re.compile(ur'(/%s*)*' % REGEXEN['validate_url_pchar'].pattern, re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_query'] = re.compile(ur'(%s|/|\?)*' % REGEXEN['validate_url_pchar'].pattern, re.IGNORECASE | re.UNICODE)
REGEXEN['validate_url_fragment'] = re.compile(ur'(%s|/|\?)*' % REGEXEN['validate_url_pchar'].pattern, re.IGNORECASE | re.UNICODE)

# Modified version of RFC 3986 Appendix B
REGEXEN['validate_url_unencoded'] = re.compile(ur'\A(?:([^:/?#]+)://)?([^/?#]*)([^?#]*)(?:\?([^#]*))?(?:\#(.*))?\Z', re.IGNORECASE | re.UNICODE)

REGEXEN['rtl_chars'] = re.compile(ur'[%s]' % RTL_CHARACTERS, re.IGNORECASE | re.UNICODE)
