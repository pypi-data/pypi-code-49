import sys
import re
from pypinyin import pinyin, Style, load_phrases_dict


consonant_list = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k',
                  'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z',
                  'c', 's'] # 'y', 'w'


TRANSFORM_DICT = {'ju':'jv', 'qu':'qv', 'xu':'xv', 'zi':'zii',
                    'ci':'cii', 'si':'sii', 'zhi':'zhiii', 
                    'chi':'chii', 'shi':'shii', 'ri':'ri',
                    
                    'quan':'qvan','xuan':'xvan','juan':'jvan',
                    'qun':'qvn','xun':'xvn', 'jun':'jvn',
                  
                    'yuan':'van', 'yue':'ve', 'yun':'vn',
                    'ya':'ia', 'ye':'ie', 'yao':'iao',
                    'yi':'i','yu':'v',
                    'you':'iou', 'yan':'ian', 'yin':'in',
                    'yang':'iang', 'ying':'ing', 'yong':'iong',
                    'yvan':'van', 'yve':'ve', 'yvn':'vn',
                    'wu':'u',
                    'wa':'ua', 'wo':'uo', 'wai':'uai','wei':'uei',
                    'wan':'uan', 'wen':'uen',
                    'weng':'ueng', 'wang':'uang'}

trans_dict = {'uan':'van','iu':'iou','ui':'uei', 'un':'uen', }


def _pre_pinyin_setting():
    ''' fix pinyin error'''
    load_phrases_dict({'嗯':[['ēn']]})

_pre_pinyin_setting()




def _pinyinformat(syllable):
    '''format pinyin to mtts's format''' 
    if not syllable[-1].isdigit():
        syllable = syllable + '5'
    assert syllable[-1].isdigit()
    syl_no_tone = syllable[:-1]
    if syl_no_tone in TRANSFORM_DICT:
        syllable = syllable.replace(syl_no_tone, TRANSFORM_DICT[syl_no_tone])
    return syllable
 
symbol_dict = {',':'sp1', '，':'sp1'}
def _seprate_syllable(syllable):
    '''seprate syllable to consonant + ' ' + vowel '''
    assert syllable[-1].isdigit()

    if syllable[0:2] in consonant_list:
        if syllable[2:-1] in trans_dict.keys():
            syllable = syllable.replace(syllable[2:-1], trans_dict[syllable[2:-1]])
        return syllable[0:2], syllable[2:]

    elif syllable[0] in consonant_list:
        if syllable[1:-1] in trans_dict.keys():
            syllable = syllable.replace(syllable[1:-1], trans_dict[syllable[1:-1]])
        return syllable[0], syllable[1:]
    # guang
    elif syllable[:-1] in symbol_dict.keys():
        return (symbol_dict[syllable[:-1]],)
    else:
        return (syllable,)


def txt2ph(txt):
    phone_list = []

    pinyin_list = pinyin(txt, style = Style.TONE3)
    for item in pinyin_list:
        phone_list.append(_seprate_syllable(_pinyinformat(item[0])))
    return phone_list