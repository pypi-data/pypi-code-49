# coding: utf-8
import os
from pyWebFramework import PageBase


class PageTaxInitFormBase(PageBase):
    url = ''

    def __init__(self):
        super(PageTaxInitFormBase, self).__init__()

    def InitPage(self):
        if not super(PageTaxInitFormBase, self).InitPage():
            return False

        self.AddScript('''
function queryXPathAll(xpath_str) {
    var xresult = document.evaluate(xpath_str, document, null, XPathResult.ANY_TYPE, null);
    var xnodes = [];
    var xres;
    while (xres = xresult.iterateNext()) {
        xnodes.push(xres);
    }

    return xnodes;
}

function queryXPath(xpath_str) {
    var xresult = document.evaluate(xpath_str, document, null, XPathResult.ANY_TYPE, null);
    var xnodes = [];
    var xres;
    while (xres = xresult.iterateNext()) {
        return xres
    }

    return null;
}

function queryXPathText(xpath_str) {
    var e = queryXPath(xpath_str);
    
    if (!e) {
        throw 'xpath not found: ' + xpath_str;
    }
    
    return e.innerText.trim();
}

function querySelectorText(selector_str) {
    if (typeof document.querySelector !== 'undefined') {
        var e = document.querySelector(selector_str);
        if (!e) {
            throw 'selector not found: ' + selector_str;
        }
        
        return e.innerText.trim();
    }
    
    if (typeof $ !== 'undefined') {
        var $e = $(selector_str);
        if ($e.length === 0) {
            throw 'selector not found: ' + selector_str;
        }
        return $e.text();
    }
    
    throw 'document.querySelector is undefined';
}

function isCellExistByXPath(xpath_str) {
    return !!queryXPath(xpath_str);
}

function isCellExistBySelector(selector_str) {
    if (typeof document.querySelector !== 'undefined') {
        return !!document.querySelector(selector_str);
    }
    
    if (typeof $ !== 'undefined') {
        var $e = $(selector_str);
        return $e.length !== 0;
    }
    
    throw 'document.querySelector is undefined';
}

function test(xpath_str) {
    r = queryXPathAll(xpath_str);
    
    LOG_INFO(r.length);
}

        ''')

        return True

    def GetCellTextByXPath(self, xpath):
        return self.InvokeScriptString('queryXPathText', xpath)

    def IsCellExistByXPath(self, xpath):
        return self.InvokeScriptBool('isCellExistByXPath', xpath)

    def GetCellTextBySelector(self, selector):
        return self.InvokeScriptString('querySelectorText', selector)

    def IsCellExistBySelector(self, selector):
        return self.InvokeScriptBool('isCellExistBySelector', selector)

    def test(self, xpath):
        self.InvokeScript('test', xpath)
