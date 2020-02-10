# coding: utf-8
from pyWebFramework.dll.IeWebFramework import PageBase as PageBase_
from .exception import wrap_callback, dispatch_page_func


class PageBase(PageBase_):
    url = ''
    params = []
    matcher = None

    def __init__(self):
        self.orig_url = ''
        super(PageBase, self).__init__()

    def PyOnRelease(self):
        dispatch_page_func(self, self.OnRelease)

    def PyInitPage(self):
        return dispatch_page_func(self.InitPage)

    def InitPage(self):
        return True

    def SetTimeout(self, callback, millisec):
        return super(PageBase, self).SetTimeout(wrap_callback(callback), millisec)

    def WaitUntil(self, callback, script, interval=300):
        return super(PageBase, self).WaitUntil(wrap_callback(callback), script, interval)

    def HookAjax(self, callback, url_starts_with='', once=True):
        return super(PageBase, self).HookAjax(wrap_callback(callback), url_starts_with, once)

    def HookAjaxWithParam(self, callback, url_starts_with='', once=True):
        return super(PageBase, self).HookAjaxWithParam(wrap_callback(callback), url_starts_with, once)

    def HookAjaxWithReturn(self, callback, url_starts_with=''):
        return super(PageBase, self).HookAjaxWithReturn(wrap_callback(callback), url_starts_with)

    def HookMiniAlert(self, funcBefore, funcAfter):
        return super(PageBase, self).HookMiniAlert(wrap_callback(funcBefore), wrap_callback(funcAfter))

    def HookMiniConfirm(self, funcBefore, funcAfter):
        return super(PageBase, self).HookMiniConfirm(wrap_callback(funcBefore), wrap_callback(funcAfter))

    def HookLayerOpen(self, funcBefore, funcAfter):
        return super(PageBase, self).HookLayerOpen(wrap_callback(funcBefore), wrap_callback(funcAfter))

    def HookLayerAlert(self, funcBefore, funcAfter):
        return super(PageBase, self).HookLayerAlert(wrap_callback(funcBefore), wrap_callback(funcAfter))

    def HookLayerConfirm(self, funcBefore, funcAfter):
        return super(PageBase, self).HookLayerConfirm(wrap_callback(funcBefore), wrap_callback(funcAfter))

    def HookMessagerAlert(self, funcBefore, funcAfter):
        return super(PageBase, self).HookMessagerAlert(wrap_callback(funcBefore), wrap_callback(funcAfter))

    def HookMessagerConfirm(self, funcBefore, funcAfter):
        return super(PageBase, self).HookMessagerConfirm(wrap_callback(funcBefore), wrap_callback(funcAfter))

    def InvokeScript(self, script, param1='', param2='', param3='', param4=''):
        return super(PageBase, self).InvokeScript(script, str(param1), str(param2), str(param3), str(param4))

    def InvokeScriptInt(self, script, param1='', param2='', param3='', param4=''):
        return super(PageBase, self).InvokeScriptInt(script, str(param1), str(param2), str(param3), str(param4))

    def InvokeScriptBool(self, script, param1='', param2='', param3='', param4=''):
        return super(PageBase, self).InvokeScriptBool(script, str(param1), str(param2), str(param3), str(param4))

    def InvokeScriptString(self, script, param1='', param2='', param3='', param4=''):
        return super(PageBase, self).InvokeScriptString(script, str(param1), str(param2), str(param3), str(param4))
