#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PySide2.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PySide2.QtCore import QUrl
from PySide2.QtWebEngineCore import QWebEngineUrlRequestInterceptor
import webbrowser
import PySide2


class WebEnginePage(QWebEnginePage):

    def javaScriptConsoleMessage(self, level, message, lineNumber,
                                 sourceID):  # real signature unknown; restored from __doc__
        """ javaScriptConsoleMessage(self, level: PySide2.QtWebEngineWidgets.QWebEnginePage.JavaScriptConsoleMessageLevel, message: str, lineNumber: int, sourceID: str) """
        print("javaScriptConsoleMessageCall#message = %s" % (message))

    def acceptNavigationRequest(self, url, _type, isMainFrame):
        if _type == QWebEnginePage.NavigationTypeLinkClicked:
            webbrowser.open(url.url(), new=1, autoraise=True)
            return False
        return True

    # 处理https错误提示
    def certificateError(self, certificateError: PySide2.QtWebEngineWidgets.QWebEngineCertificateError) -> bool:
        return True


class WebEngineUrlRequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, parent=None):
        QWebEngineUrlRequestInterceptor.__init__(self, parent)

    def interceptRequest(self, info: PySide2.QtWebEngineCore.QWebEngineUrlRequestInfo):
        print(info.requestUrl().url())
        return False


class PreView(QWebEngineView):

    def __init__(self, *args, **kwargs):
        super(PreView, self).__init__(*args, **kwargs)
        # self.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        self.init()
        self.setPage(WebEnginePage(self))
        self.page().profile().setUrlRequestInterceptor(self.requestInterceptor)
        self.page().profile().setUseForGlobalCertificateVerification(False)
        self.loadFinishStatus = False
        self.needCall = list()
        self.preContent = None
        self.loadFinished.connect(self.loadFinishCall)

        self.percentageOfTop = 0

    def init(self):
        self.requestInterceptor = WebEngineUrlRequestInterceptor(self)
        self.leftHtml = '''<!DOCTYPE html>
        <html lang="zh-cn">
        <head>
            <meta charset="UTF-8"/>
            <meta content="width=device-width, initial-scale=1.0" name="viewport"/>
            <meta content="IE=edge, chrome=1" http-equiv="X-UA-Compatible"/>
            <meta content="text/html;charset=utf-8" http-equiv="content-type"/>
            <link href="https://www.catbro.cn/css/matery.css" rel="stylesheet">
            <link href="https://cdn.bootcss.com/github-markdown-css/3.0.1/github-markdown.min.css" rel="stylesheet">
            <link rel="stylesheet"
                  href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.16.2/build/styles/default.min.css">
            <script type="text/javascript"
                    src="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release@9.16.2/build/highlight.min.js"></script>
            <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mermaid/8.4.4/mermaid.min.js"></script>
            <script type="text/javascript"
                    src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/MathJax.js?config=TeX-MML-AM_CHTML"></script>
            <script type="text/javascript">
                MathJax.Hub.Config({
                    tex2jax: {
                        inlineMath: [
                            ['$', '$'],
                            ['(', ')']
                        ]
                    }
                });
            </script>
            <style>
                img {
                    max-width: 100%;
                }
                pre {
                    padding: 1.5rem !important;
                    margin: 1rem 0 !important;
                    background: #272822;
                    overflow: auto;
                    border-radius: 0.35rem;
                    tab-size: 4;
                    display: block;
                    font-size: 87.5%;
                    color: #212529;
                }
                pre code {
                    border-radius: 2px;
                    font-family: Inconsolata, Monaco, Consolas, 'Courier New', Courier, monospace;
                    word-break: normal;
                    font-size: inherit;
                    padding: 0;
                    color: #e8eaf6;
                    background-color: #272822;
                }
                body {
                    margin: 8px !important;
                }
            </style>
        </head>
        <body id="preArea">
        <div id="preMkContent">'''

        self.rightHtml = '''
        </div>
          <script>
              var config = {
                theme:'default',
                logLevel:'fatal',
                securityLevel:'strict',
                startOnLoad:true,
                arrowMarkerAbsolute:false,
            
                flowchart:{
                  htmlLabels:true,
                  curve:'linear',
                },
                sequence:{
                  diagramMarginX:50,
                  diagramMarginY:10,
                  actorMargin:50,
                  width:150,
                  height:65,
                  boxMargin:10,
                  boxTextMargin:5,
                  noteMargin:10,
                  messageMargin:35,
                  mirrorActors:true,
                  bottomMarginAdj:1,
                  useMaxWidth:true,
                  rightAngles:false,
                  showSequenceNumbers:false,
                },
                gantt:{
                  titleTopMargin:25,
                  barHeight:20,
                  barGap:4,
                  topPadding:50,
                  leftPadding:75,
                  gridLineStartPadding:35,
                  fontSize:11,
                  fontFamily:'"Open-Sans", "sans-serif"',
                  numberSectionStyles:4,
                  axisFormat:'%Y-%m-%d',
                }
              };
              mermaid.initialize(config);
          window.reloadMermaid = function reloadMermaid() {
            mermaid.init({
                noteMargin: 10
            }, ".mermaid");
          
          }
          </script>

        </body>
        </html>
        '''

    def urlChanged(self, *args, **kwargs):  # real signature unknown
        print("urlChanged# args:%s and kwargs:%s" % (args, kwargs))
        QWebEngineView.urlChanged(self, *args, **kwargs)

    def loadStarted(self, *args, **kwargs):  # real signature unknown
        print("loadStarted# args:%s and kwargs:%s" % (args, kwargs))
        QWebEngineView.loadStarted(self, *args, **kwargs)

    def loadFinishCall(self, *args, **kwargs):  # real signature unknown
        print("loadFinishCall# args:%s and kwargs:%s" % (args, kwargs))
        self.loadFinishStatus = True
        for call in self.needCall:
            call()
        self.needCall.clear()

    def setPreContent(self, data, force: bool = False):
        if force:
            self.loadFinishStatus = False
            self.preContent = data
            html = self.leftHtml + data + self.rightHtml
            self.page().setHtml(html)
            self.scrollContent(self.percentageOfTop)
        elif not self.preContent:
            self.preContent = data
            html = self.leftHtml + data + self.rightHtml
            self.page().setHtml(html)
        else:
            self.preContent = data
            if self.loadFinishStatus:
                self.realLoadPreContent()
            else:
                self.needCall.append(self.realLoadPreContent)

    def realLoadPreContent(self):
        if self.loadFinishStatus:
            # self.preContent = str(self.preContent).replace("'", "\\\'")
            # self.preContent = str(self.preContent).replace('"', "\\\"")

            javascriptStr = 'window.document.getElementById("preMkContent").innerHTML = `%s`' % str(
                self.preContent)
            self.page().runJavaScript(javascriptStr)

    def scrollContent(self, percentageOfTop=None):
        self.percentageOfTop = percentageOfTop

        if self.loadFinishStatus:
            self.realScrollContent()
        else:
            self.needCall.append(self.realScrollContent)

    def realScrollContent(self):
        if self.loadFinishStatus:
            javascriptStr = '''var scrollingElement = (document.scrollingElement || document.body);
scrollingElement.scrollTop = scrollingElement.scrollHeight * %s;''' % self.percentageOfTop
        self.page().runJavaScript(javascriptStr)
        self.page().runJavaScript('window.reloadMermaid()')
