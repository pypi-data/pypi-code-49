# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: attenton
@Email: 18212010081@fudan.edu.cn
@Created: 2019/12/13
------------------------------------------
@Modify: 2019/12/24
------------------------------------------
@Description:
"""

import spacy
from spacy.lang.char_classes import ALPHA, HYPHENS, ALPHA_LOWER, ALPHA_UPPER, CONCAT_QUOTES

from sekg.text.spacy_pipeline.sentenceHandler import SentenceHandler


class CustomizeSpacy:
    """
    apcy中的tokenizer主要原理分为五个部分，例外rules（也可以被称为tokenizer_exceptions）， 前缀prefix，后缀suffix，中缀infix，以及例外的正则匹配token_match
    修改以上任意一个都可以修改spacy中的tokenizer，实现自定义的tokenizer
    可以使用nlp.tokenizer.explain()查看每一个token的成分，是suffix，inffix，prefix还是token_match
    """

    @staticmethod
    def customize_tokenizer_split_single_lowcase_letter_and_period(nlp):
        """
        自定义的tokenzier，修改spacy中的exception，
        spacy中的tokenizer exception添加了{a.|b.|c.}等单个字母与句号连接的例外，这个可能导致分句出现错误，比如 1 < n < r. 出现在句尾。
        :param nlp:
        :return:
        """
        # prefix_re = spacy.util.compile_prefix_regex(nlp.Defaults.prefixes)
        # suffix_re = spacy.util.compile_suffix_regex(nlp.Defaults.suffixes)
        # infix_re = spacy.util.compile_infix_regex(nlp.Defaults.infixes)
        #
        # # remove all exceptions where a single letter is followed by a period (e.g. 'h.')
        exceptions = {k: v for k, v in dict(nlp.Defaults.tokenizer_exceptions).items() if
                      not (len(k) == 2 and k[1] == '.')}
        # 添加特殊的tokenizer exception
        for orth in [
            "C#",
            "c#"
        ]:
            exceptions[orth] = [{"ORTH": orth}]
        # new_tokenizer = Tokenizer(nlp.vocab, exceptions,
        #                           prefix_search=prefix_re.search,
        #                           suffix_search=suffix_re.search,
        #                           infix_finditer=infix_re.finditer,
        #                           token_match=nlp.tokenizer.token_match)
        #
        # nlp.tokenizer = new_tokenizer
        nlp.tokenizer.rules = exceptions

    @staticmethod
    def customize_tokenizer_merge_hyphen(nlp):
        """
        将连字符相连的合并为一个token， 如原来的fail-fast在tokenize之后会分成fail - fast三个，修改之后会全部合并为fail-fast这一个token
        实现方法： 删除infix中分离连字符的正则表达式
        :param nlp:
        :return:
        """
        _infixes = list(nlp.Defaults.infixes)
        _infixes.remove(r"(?<=[{a}])(?:{h})(?=[{a}])".format(a=ALPHA, h=HYPHENS), )
        infix_regex = spacy.util.compile_infix_regex(_infixes)
        nlp.tokenizer.infix_finditer = infix_regex.finditer

    @staticmethod
    def customize_tokenizer_merge_dot_upper_letter(nlp):
        """
        将.{upper_letter}相连的合并为一个token， 如原来的java.String.format在tokenize之前会被拆分为`java.` `String.format`
        修改tokenizer之后会合并为`java.String.format`一个
        实现方法： 删除infix中.{upper_letter}的正则表达式
        :param nlp:
        :return:
        """
        _infixes = list(nlp.Defaults.infixes)
        _infixes.remove(r"(?<=[{al}{q}])\.(?=[{au}{q}])".format(
            al=ALPHA_LOWER, au=ALPHA_UPPER, q=CONCAT_QUOTES
        ), )
        infix_regex = spacy.util.compile_infix_regex(_infixes)
        nlp.tokenizer.infix_finditer = infix_regex.finditer

    @staticmethod
    def customize_tokenizer_api_name_recognition(nlp):
        """
        将句子中的api名字识别成一个token, 在生成tokenizer的函数后加上token.match
        将中括号的内容合并，之前会将]作为单独的token
        TODO: 目前只是将中括号的合并了，由于token_match是在suffix、prefix之后执行，所以复杂的正则会被suffix、prefixoverride，所以目前还是用doc.retoeknizer()方法实现api_name的识别
        :param nlp:
        :return:
        """
        # re_token_match = _get_regex_pattern(nlp.Defaults.token_match)
        _suffixes = list(nlp.Defaults.suffixes)
        _suffixes.remove("\]")
        suffixes_regex = spacy.util.compile_suffix_regex(_suffixes)
        nlp.tokenizer.suffix_search = suffixes_regex.search
        # api_name_match = re.compile("(\w+(\[[\w+-]+\])?\.)+\w+\(.*?\)", re.UNICODE).match
        # token_match = nlp.Defaults.token_match
        # print(token_match)
        # token_match.append(api_name_match)
        # nlp.tokenizer.token_match = api_name_match

    @staticmethod
    def customize_sentencizer_merge_colon(doc):
        """
        之前碰到冒号会分句，处理之后不再会分句
        :param doc:
        :return:
        """
        for token in doc[:-1]:
            if token.text == ":":
                doc[token.i+1].is_sent_start = False
        return doc

    @staticmethod
    def pipeline_merge_bracket(doc):
        """
        Java int to String - Integer.toString(i) vs new Integer(i).toString
        --> ['Java', 'int', 'to', 'String', '-', 'Integer.toString(i)', 'vs', 'new', 'Integer(i).toString']
        将括号合并： 如果'('的左边是空格，那么就括号内的内容自身合并， 如果左边不是空格，那么就和左边的内容一起合并，比如Integer.toString(i)
        :param doc:
        :return:
        """
        method_brace_pair_list = []
        method_left_brace_cache_index = -1
        left_angle_bracket = -1
        angle_brackets_list = []
        count = 0
        for i, token in enumerate(doc):
            # todo" complete this for sentence containing method name
            # 添加了对method name的处理
            if "<" == token.text:
                if i > 0 and doc[i-1].text != ">":
                    left_angle_bracket = i-1
                else:
                    left_angle_bracket = i
            elif "<" in token.text:
                left_angle_bracket = i

            if ">" == token.text and left_angle_bracket != -1:
                angle_brackets_list.append((left_angle_bracket, i))
                left_angle_bracket = -1
        # print(method_brace_pair_list)
        with doc.retokenize() as retokenizer:
            for star_index, end_index in angle_brackets_list:
                attrs = {"LEMMA": " ".join([token.text for token in doc[(star_index):(end_index+1)]]),
                         "POS": "NOUN",
                         "TAG": "NN",
                         }
                retokenizer.merge(doc[star_index:end_index+1], attrs=attrs)
        for i, token in enumerate(doc):
            # todo" complete this for sentence containing method name
            # 添加了对method name的处理
            if "(" == token.text:
                if count == 0:
                    # 判断'('在原句中和前一个token有没有空格，如果没有空格就与前一个token一起合并
                    if i > 0 and doc[i - 1].text != ")" and doc[i - 1].text != "." and doc.text.find(doc[i - 1].text+'(') != -1:
                        method_left_brace_cache_index = i-1
                    else:
                        method_left_brace_cache_index = i
                count += 1
            # 有些时候'('和其他一些单词一起组成一个token
            elif "(" in token.text:
                if count == 0:
                    method_left_brace_cache_index = i
                count += 1
            if ")" == token.text and method_left_brace_cache_index != -1:
                count -= 1
                if count == 0:
                    method_brace_pair_list.append((method_left_brace_cache_index, i))
                    method_left_brace_cache_index = -1
        # print(method_brace_pair_list)
        with doc.retokenize() as retokenizer:
            for star_index, end_index in method_brace_pair_list:
                span = doc[star_index:(end_index + 1)]
                if not SentenceHandler.is_complete_sentence(span):
                    attrs = {"LEMMA": " ".join([token.text for token in doc[(star_index):(end_index + 1)]]),
                             "POS": "NOUN",
                             "TAG": "NN",
                             }
                    retokenizer.merge(doc[star_index:end_index + 1], attrs=attrs)

        return doc


if __name__ == '__main__':
    nlp = spacy.load('en_core_web_sm')
    CustomizeSpacy.customize_tokenizer_split_single_lowcase_letter_and_period(nlp)
    CustomizeSpacy.customize_tokenizer_merge_hyphen(nlp)
    CustomizeSpacy.customize_tokenizer_merge_dot_upper_letter(nlp)
    CustomizeSpacy.customize_tokenizer_api_name_recognition(nlp)
    sentencizer = nlp.create_pipe("sentencizer")
    nlp.add_pipe(sentencizer, before="tagger")
    nlp.add_pipe(CustomizeSpacy.customize_sentencizer_merge_colon, before="tagger")
    # nlp.add_pipe(SentenceHandler.hyphen_handler, name='sh', after='tagger')
    nlp.add_pipe(CustomizeSpacy.pipeline_merge_bracket, name='pipeline_merge_bracket', after='tagger')
    # sentence = 'java.lang.StringBuffer create StringBuffer'
    # sentence = 'Suppose that a byte sequence of length n is written, where < n <= r. Up to the first srcs[offset].remaining() bytes of this sequence are written from buffer srcs[offset], up to the next srcs[offset+1].remaining() bytes are written from buffer srcs[offset+1], and so forth, until the entire byte sequence is written.'
    sentences = ['How to use java.String.format in Scala?',
                 'How to use java.string.format in Scala?',
                 'How to use (use) dfads.',
                 'However, I get a NoSuchElementException (since there is no invocation of hasNext) -CODE- .',
                 'Why is 2 * (i * i) faster than 2 * i * i in Java?',
                 'Why is 2 * i Java?',
                 'In C# it is DateTime.Now.',
                 "I was really surprised but I haven't been able to find anything that shows how to get the MD5 checksum of a file.",
                 "you get the className + @ + the hex of the hashCode of the array, as defined by Object.toString(): -CODE- .",
                 "I get this: -CODE- .",
                 "I'm trying to remove some elements from an ArrayList while iterating it like this: -CODE- .",
                 "There are some obvious ways of doing this (i.e. with a loop) but I would like something a bit neater, something like: -CODE- .",
                 "Equivalent of C#'s DateTime.Now in Java?",
                 "Java int to String - Integer.toString(i) vs new Integer(i).toString()",
                 "What is the fundamental difference between the Set<E> and List<E> interfaces?",
                 "What issues / pitfalls must be considered when overriding equals and hashCode?",
                 "In the following program you can see that each value slightly less than .5 is rounded down, except for 0.5.",
                 "I can accomplish this easily using Java 8 and Guava but I would like to know how to do this without Guava.",
                 "However, when I deploy in WebSphere I get a java.lang.NoClassDefFoundError: org.slf4j.impl.StaticLoggerBinder.",
                 "Method one: static initialiser Method two: instance initialiser (anonymous subclass) or some other method?",
                 "What I would like to know is whether I should use System.currentTimeMillis() or System.nanoTime() when updating my object's positions in my game?",
                 "I get this: -CODE- and I would like to find the enum value of a string, for example \"A\" which would be Blah.A.",
                 "Are System.out.printf and System.out.format totally the same or perhaps they differ in somehow? Are printf and format totally the same or perhaps they differ in somehow?",
                 "Are printf and format totally the same or perhaps they differ in somehow?"
                 ]
    # sentence = 'How do I get the current stacktrace in Java, like how in .NET you can do Environment.StackTrace'
    # sentence = "The elements in the array returned by the method executeBatch may be one of the following: A number greater than or equal to zero -- indicates that the command was processed successfully and is an update count giving the number of rows in the database that were affected by the command's execution"
    # sentence = "The maximum number of buffers-dke-dfs to be accessed 1 < n < r. So API must be non-negative and no larger than srcs.length - offset Returns long The number of bytes written, possibly zero"
    for sentence in sentences:
        doc = nlp(sentence)
        # debug tokenizer
        tok_exp = nlp.tokenizer.explain(sentence)
        for t in tok_exp:
            print(t[1], "\t", t[0])
        for i in doc.sents:
            print(i)
            print([token.text for token in i])
            print([token.dep_ for token in i])
            print([token.tag_ for token in i])
            print('\n')
        print('-------------------------')
        print('\n')
