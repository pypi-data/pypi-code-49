#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
-----------------------------------------
@Author: isky
@Email: 19110240019@fudan.edu.cn
@Created: 2020/02/20
------------------------------------------
@Modify: 2020/02/20
------------------------------------------
@Description:
"""
from sekg.ir.doc.wrapper import MultiFieldDocumentCollection, MultiFieldDocument, PreprocessMultiFieldDocumentCollection


class FakeDocumentCollectionData:
    @staticmethod
    def fake_dc():
        texts = [
            "Difference between StringBuilder and StringBuffer",
            "What is the main difference between StringBuffer and StringBuilder? Is there any performance issues when deciding on any one of these?",
            "IDEA: javac: source release 1.7 requires target release 1.7",
            "When running a JUnit test, using IntelliJ IDEA, I get How can I correct this? Using SDK 1.7 Module language level is 1.7 Maven build works fine. (That's why I believe this in IDEA configuration issue)",
            "How do I split a string with any whitespace chars as delimiters?",
            "What regex pattern would need I to pass to the java.lang.String.split() method to split a String into an Array of substrings using all whitespace characters (' ', '\\t', '\\n', etc.) as delimiters?",
            "How to check if a String is numeric in Java",
            "It is supposed to be generally preferable to use a StringBuilder for string concatenation in Java. Is this always the case? What I mean is this: Is the overhead of creating a StringBuilder object, calling the append() method and finally toString() already smaller then concatenating existing strings with the + operator for two strings, or is it only advisable for more (than two) strings? If there is such a threshold, what does it depend on (perhaps the string length, but in which way)? And finally, would you trade the readability and conciseness of the + concatenation for the performance of the StringBuilder in smaller cases like two, three or four strings? Explicit use of StringBuilder for regular concatenations is being mentioned as obsolete at obsolete Java optimization tips as well as at Java urban myths.",
            "How to check if a String contains another String in a case insensitive manner in Java?",
            "Say I have two strings, -CODE- . I want to perform a check returning that s2 is contained within s1. I can do this with: -CODE- . I am pretty sure that contains() is case sensitive, however I can't determine this for sure from reading the documentation. If it is then I suppose my best method would be something like: -CODE- . All this aside, is there another (possibly better) way to accomplish this without caring about case-sensitivity?"
        ]

        dc = MultiFieldDocumentCollection()
        for index, text in enumerate(texts):
            doc = MultiFieldDocument(index, str(text), {"doc": text})
            dc.add_document(doc)

        return dc

    @staticmethod
    def fake_pre_dc():
        return PreprocessMultiFieldDocumentCollection.create_from_doc_collection_with_default_preprocessor(
            FakeDocumentCollectionData.fake_dc())
