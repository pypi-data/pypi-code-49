# -*- encoding: utf-8 -*-
'''
Current module: rock4.softtest.web.actions

Rough version history:
v1.0    Original version to use
v2.0    use rtsf for web driver

********************************************************************
    @AUTHOR:  Administrator-Bruce Luo(罗科峰)
    MAIL:    lkf20031988@163.com
    RCS:      rock4.softtest.web.actions,v 2.0 2018年8月21日
    FROM:   2017年2月18日
********************************************************************

======================================================================

UI and Web Http automation frame for python.

'''

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time,os,re,json,ast

def _parse_string_value(str_value):
    try:
        return ast.literal_eval(str_value)
    except ValueError:
        return str_value
    except SyntaxError:
        return str_value
           
    
class Web(object):
    driver = None    
    
    @staticmethod
    def NavigateTo(url):
        Web.driver.get(url)
        
    @staticmethod
    def PageSource():
        ''' page source for this web '''
        return Web.driver.page_source
        
    @staticmethod
    def Refresh():
        Web.driver.refresh()
    
    @staticmethod
    def Forward():
        Web.driver.forward()        
    
    @staticmethod
    def Back():
        Web.driver.back()
            
    @staticmethod
    def IESkipCertError():
        ''' IE Skip SSL Cert Error '''
        Web.driver.get("javascript:document.getElementById('overridelink').click();")
    
    @staticmethod
    def Maximize():
        """ 浏览器最大化       """
        Web.driver.maximize_window()
    
    @staticmethod
    def SetWindowSize(width, height):
        """ 设定浏览器宽高   """
        Web.driver.set_window_size(width, height)
                
    @staticmethod
    def SwitchToDefaultFrame():        
        try:
            Web.driver.switch_to.default_content()
        except:
            return False
    
    @staticmethod
    def SwitchToNewFrame(frame_name):
        try:            
            WebDriverWait(Web.driver, 10).until(lambda driver: getattr(driver,"switch_to.frame")(frame_name))          
        except:            
            print("Waring: Timeout at %d seconds.Frame %s was not found." %frame_name)
            return False       
    
    @staticmethod
    def NewTab(url=""):
        Web.Js("window.open('%s')" %url)
        Web.SwitchToNewWindow()        
    
    @staticmethod
    def SwitchToDefaultWindow():             
        try:
            default_win = Web.driver.window_handles[0]
            Web.driver.switch_to.window(default_win)
        except:
            return False
            
    @staticmethod
    def SwitchToNewWindow(): 
        try:
            WebDriverWait(Web.driver, 10).until(lambda driver: len(driver.window_handles) >= 2)            
            new_win = Web.driver.window_handles[-1]
            Web.driver.switch_to.window(new_win)
        except:            
            print("Waring: Timeout at %d seconds. Pop Window Not Found.")
            return False
    
    @staticmethod
    def SwitchToDefaultContext():
        ''' APP应用，切换到默认上下文 '''
        try:
            Web.driver.switch_to.context(Web.driver.contexts[0])
        except:
            return False
        
    @staticmethod
    def SwitchToNewContext():
        ''' APP应用，切换到新的上下文 '''
        try:
            WebDriverWait(Web.driver, 10).until(lambda driver: len(driver.contexts) >= 2)
            new_context = Web.driver.contexts[-1]
            Web.driver.switch_to.context(new_context)       
        except:            
            print("Waring: Timeout at 10 seconds. New context Not Found.")
            return False
        
    @staticmethod
    def SwitchToAlert(): 
        ''' <input value="Test" type="button" onClick="alert('OK')" > '''
        try:            
            alert = WebDriverWait(Web.driver, 10).until(lambda driver: driver.switch_to_alert())
            return alert            
        except:            
            print("Waring: Timeout at %d seconds.Alert was not found.")
            return False
            
    @staticmethod
    def AlertAccept():                
        alert = Web.SwitchToAlert()
        if alert:
            alert.accept()        
        Web.SwitchToDefaultFrame()
               
    @staticmethod
    def AlertDismiss():
        alert = Web.SwitchToAlert()
        if alert:
            alert.dismiss()
        Web.SwitchToDefaultFrame()
                        
    @staticmethod
    def AlertSendKeys(value):
        alert = Web.SwitchToAlert()
        if alert:
            alert.send_keys(value)
        Web.SwitchToDefaultFrame()
    
    @staticmethod
    def Js(script):
        """ 执行  js script       """
        getattr(Web.driver,"execute_script")(script)
        
    @staticmethod
    def ScrollTo(x, y):
        #p_log.step_info("normal",u"Element [%s]: Scroll To [%s, %s]" % (cls.__name__, x, y))
        # X-Y-top: window.scrollTo("0","0")
        # X-bottom:  window.scrollTo("10000","0"),   Y-bottom:  window.scrollTo("0","10000")           
        Web.driver.execute_script("window.scrollTo(%s, %s);" % (x, y))
            
    @staticmethod
    def ScreenShoot(f_path):
        return Web.driver.save_screenshot(f_path)
    
    @staticmethod
    def WebClose():
        try:
            Web.driver.close()
            Web.SwitchToDefaultWindow()       
        except:
            pass
            
    @staticmethod
    def WebQuit():
        try:
            Web.driver.quit()            
        except:
            pass
        finally:
            Web.driver=None    
                    
class WebElement(object):
    
    _control = {
        "by":None,
        "value":None, 
        "index":0,
        "timeout":10,
        } 
                
    @classmethod
    def SetControl(cls,**kwargs):
        cls._control.update(kwargs)
    
    @classmethod
    def GetControl(cls):
        return cls._control
                
    @classmethod
    def _element(cls):
        '''   find the element with controls '''
        if not cls._is_selector():
            raise Exception("Invalid selector[%s]." %cls._control["by"])
        
        driver = Web.driver
        try:            
            elements = WebDriverWait(driver, cls._control["timeout"]).until(lambda driver: getattr(driver,"find_elements")(cls._control["by"], cls._control["value"]))
        except:                        
            raise Exception("Timeout at %d seconds.Element(%s) not found." %(cls._control["timeout"],cls._control["by"]))
        
        if len(elements) < cls._control["index"] + 1:                    
            raise Exception("Element [%s]: Element Index Issue! There are [%s] Elements! Index=[%s]" % (cls.__name__, len(elements), cls._control["index"]))
        
        if len(elements) > 1:              
            print("Element [%s]: There are [%d] elements, choosed index=%d" %(cls.__name__,len(elements),cls._control["index"]))
        
        elm = elements[cls._control["index"]]
        cls._control["index"] = 0        
        return elm
    
    @classmethod
    def _elements(cls):
        '''   find the elements with controls '''
        if not cls._is_selector():
            raise Exception("Invalid selector[%s]." %cls._control["by"])
        
        driver = Web.driver
        try:            
            elements = WebDriverWait(driver, cls._control["timeout"]).until(lambda driver: getattr(driver,"find_elements")(cls._control["by"], cls._control["value"]))
        except:            
            raise Exception("Timeout at %d seconds.Element(%s) not found." %(cls._control["timeout"],cls._control["by"]))
            
        return elements
       
    
    @classmethod
    def _is_selector(cls):
        all_selectors = (By.CLASS_NAME, By.CSS_SELECTOR, By.ID, By.LINK_TEXT, By.NAME, By.PARTIAL_LINK_TEXT, By.TAG_NAME, By.XPATH)
                        
        if cls._control["by"] in all_selectors:
            return True
        
        print("Warning: selector[%s] should be in %s" %(cls._control["by"],all_selectors))
        return False

class WebContext(WebElement):
    
    glob = {}
            
    @classmethod
    def SetVar(cls, name, value):
        ''' set static value
        :param name: glob parameter name
        :param value: parameter value
        '''
        cls.glob.update({name:value})
                
    @classmethod
    def GetVar(cls, name):
        return cls.glob.get(name)     
    
    @classmethod
    def DyStrData(cls, name, regx, index = 0):
        ''' set dynamic value from the string data of response  
        @param name: glob parameter name
        @param regx: re._pattern_type
            e.g.
            DyStrData("a",re.compile('123'))
        '''
        text = Web.PageSource()
        if not text:
            return
        if not isinstance(regx, re._pattern_type):
            raise Exception("DyStrData need the arg which have compiled the regular expression.")
            
        values = regx.findall(text)
        result = ""
        if len(values)>index:
            result = values[index]        
        cls.glob.update({name:result})
                            
    @classmethod
    def DyJsonData(cls,name, sequence):
        ''' set dynamic value from the json data of response
        @note: 获取innerHTML json的数据 如，   <html><body>{  "code": 1,"desc": "成功"}</body></html>
        @param name: glob parameter name
        @param sequence: sequence for the json
            e.g.
            result={"a":1,
               "b":[1,2,3,4],
               "c":{"d":5,"e":6},
               "f":{"g":[7,8,9]},
               "h":[{"i":10,"j":11},{"k":12}]
               }
            
            sequence1 ="a" # -> 1
            sequence2 ="b.3" # -> 4
            sequence3 = "f.g.2" # -> 9
            sequence4 = "h.0.j" # -> 11
        '''
        
        cls.SetControl(by = "tag name", value = "body")        
        json_body  = cls._element().get_attribute('innerHTML')
                
        if not json_body:
            return
                
        resp = json.loads(json_body)                    
        sequence = [_parse_string_value(i) for i in sequence.split('.')]    
        for i in sequence:
            try:
                if isinstance(i, int):
                    resp = resp[i]   
                else:
                    resp = resp.get(i)
            except:            
                cls.glob.update({name:None})
                return        
        cls.glob.update({name:resp})
        
    @classmethod
    def DyAttrData(cls,name, attr):
        attr_value = cls._element().get_attribute(attr)
        cls.glob.update({name:attr_value})
                
    @classmethod
    def GetText(cls):        
        return cls._element().text
    
    @classmethod
    def GetAttribute(cls, attr):
        return cls._element().get_attribute(attr)

class WebWait(WebElement):    
    
    @classmethod
    def TimeSleep(cls, seconds):
        time.sleep(seconds)
        
    @classmethod
    def WaitForAppearing(cls):        
        try:
            result = True if cls._element() else False                            
        except:
            result = False
        return result
        
    @classmethod
    def WaitForDisappearing(cls):        
        try:
            result = False if cls._element() else True
        except:
            result = True
        return result
        
    @classmethod
    def WaitForVisible(cls):
        try:
            result = cls._element().is_displayed()
        except:
            result = False        
        return result
    
class WebVerify(WebElement):
    
    @classmethod
    def VerifyVar(cls, name, expect_value):
        if WebContext.GetVar(name) == expect_value:
            return True
        else:
            return False
        
    @classmethod
    def VerifyText(cls, text):
        # 元素text值，为text
        try:
            result = cls._element().text == text
        except:
            result = False
        return result
        
    @classmethod
    def VerifyTitle(cls, title):
        # 当前页面的title
        if Web.driver.title == title:
            return True
        else:
            print("VerifyTitle: %s" % Web.driver.title)
            return False
    
    @classmethod
    def VerifyURL(cls, url):
        """ 获取当前页面的url """
          
        if Web.driver.current_url == url:
            return True
        else:
            print("VerifyURL: %s" % Web.driver.current_url)
            return False
    
    @classmethod
    def VerifyAlertText(cls, txt_value):        
        alert = Web.SwitchToAlert()
        result = False    
        if alert and txt_value in alert.text:                        
            result = True
        Web.SwitchToDefaultFrame()
        
        if result == False:
            print("VerifyAlertText: %s" % alert.text)
            
        return result
        
    @classmethod
    def VerifyElemEnabled(cls):
        try:
            result = cls._element().is_enabled()                          
        except:
            result = False
        return result   
    
    @classmethod
    def VerifyElemNotEnabled(cls):
        try:
            result = False if cls._element().is_enabled() else True                          
        except:
            result = True
        return result   
    
    @classmethod
    def VerifyElemVisible(cls):
        #p_log.step_info("normal","Element [%s]: IsVisible?" % (cls.__name__))
        try:
            result = cls._element().is_displayed()
        except:
            result = False
        return result
    
    @classmethod
    def VerifyElemNotVisible(cls):
        #p_log.step_info("normal","Element [%s]: IsVisible?" % (cls.__name__))
        try:
            result = False if cls._element().is_displayed() else True
        except:
            result = True
        return result       
    
    @classmethod
    def VerifyElemInnerHtml(cls, expect_text):
        '''
        @note: verify content of inner html is expected.  
        @param expect_text: expect inner html value
        '''
        if expect_text == "": return
                
        inner_html = cls._element().get_attribute('innerHTML')
        if expect_text in inner_html:
            return True
        else:
            print("VerifyElemInnerHtml: %s" % inner_html)
            return False    
    
    @classmethod
    def VerifyElemAttr(cls, attr_name, expect_value):
        '''
        @note:  verify content of attribute is expected content
        @param attr_name: name of element attribute 
        @param expet_value: expect attribute value
        '''
        try:
            result = expect_value in cls._element().get_attribute(attr_name)
        except:
            result = False
        return result
    
    @classmethod
    def VerifyElemCounts(cls, num):        
        if len(cls._elements()) == num:
            return True
        else:
            return False
        

class WebActions(WebElement):
    ''' Web Element.(selenium)'''
            
    @classmethod
    def SendKeys(cls, value):
        '''
        @param value: 文本框，输入的文本
        '''
        if value == "":
            return
        
        element = cls._element()
        element.clear()        
        action = ActionChains(Web.driver)
        action.send_keys_to_element(element, value)
        action.perform()
        
        
    @classmethod    
    def SelectByText(cls, text):
        ''' 通过文本值，选择下拉框选项，
        @param text: 下拉框  文本
        '''
        try:
            Select(cls._element()).select_by_visible_text(text)
        except:
            return False
        
    @classmethod    
    def DeSelectByText(cls, text):
        ''' 通过文本值，取消选择下拉框选项，
        @param text: 下拉框  文本
        '''
        try:
            Select(cls._element()).deselect_by_visible_text(text)
        except:
            return False
    
    
    @classmethod    
    def SelectByIndex(cls, index):
        ''' 通过索引，选择下拉框选项，
        @param index: 下拉框  索引
        '''
        try:
            Select(cls._element()).select_by_index(int(index))
        except:
            return False
                
    @classmethod    
    def DeSelectByIndex(cls, index):
        ''' 通过索引，取消选择下拉框选项，
        @param index: 下拉框  索引
        '''
        try:
            Select(cls._element()).deselect_by_index(int(index))
        except:
            return False
            
    @classmethod    
    def SelectByValue(cls, value):
        ''' 通过value值，选择下拉框选项，
        @param value: 下拉框  value属性 值
        '''
        try:
            Select(cls._element()).select_by_value(value)
        except:
            return False
                
    @classmethod    
    def DeSelectByValue(cls, value):
        ''' 通过value值，取消选择下拉框选项，
        @param value: 下拉框  value属性 值
        '''
        try:
            Select(cls._element()).deselect_by_value(value)
        except:
            return False
    
    @classmethod
    def MouseOver(cls):
        ''' 鼠标悬浮 '''      
        element = cls._element()                
        action = ActionChains(Web.driver)
        action.move_to_element(element)
        action.perform()
        time.sleep(1)    
    
    @classmethod
    def Click(cls):
        ''' 左键 点击 1次   '''
        
        element= cls._element()        
        action = ActionChains(Web.driver)
        action.click(element)
        action.perform()
        
    @classmethod
    def DoubleClick(cls):
        ''' 左键点击2次 '''
        
        element = cls._element()        
        action = ActionChains(Web.driver)
        action.double_click(element)
        action.perform()
                    
    @classmethod
    def EnhancedClick(cls):
        '''
        Description:
            Sometimes, one click on the element doesn't work. So wait more time, then click again and again.
        Risk:
            It may operate more than one click operations.
        '''
        
        element = cls._element()
        for _ in range(3):
            action = ActionChains(Web.driver)
            action.move_to_element(element)
            action.perform()           
            time.sleep(0.5)
    
    @classmethod
    def RightClick(cls):
        ''' 右键点击1次 '''
        
        element = cls._element()        
        action = ActionChains(Web.driver)
        action.context_click(element)
        action.perform()
       
    
    @classmethod
    def ClickAndHold(cls):
        ''' 相当于 按压，press '''
        
        element = cls._element()        
        action = ActionChains(Web.driver)
        action.click_and_hold(element)
        action.perform()
    
    
    @classmethod
    def ReleaseClick(cls):
        ''' 释放按压操作   '''
        
        element = cls._element()        
        action = ActionChains(Web.driver)
        action.release(element)
        action.perform()
        
    
    @classmethod
    def MoveAndDropTo(cls):
        '''
        @todo: move an elm to an elm where drop it to 
        '''
        raise Exception('to do')
    
    @classmethod
    def Enter(cls):
        '''     在指定输入框发送回回车键
        @note: key event -> enter
        '''
        
        element = cls._element()        
        action = ActionChains(Web.driver)
        action.send_keys_to_element(element, Keys.ENTER)
        action.perform()
            
    @classmethod
    def Ctrl(cls, key):
        """     在指定元素上执行ctrl组合键事件
        @note: key event -> control + key
        @param key: 如'X'
        """
        element = cls._element()        
        element.send_keys(Keys.CONTROL, key)
        
        
    @classmethod
    def Alt(cls, key):
        """    在指定元素上执行alt组合事件
        @note: key event ->  alt + key
        @param key: 如'X'
        """
        element = cls._element()
        element.send_keys(Keys.ALT, key)
        
    
    @classmethod
    def Space(cls):
        """     在指定输入框发送空格
        @note: key event ->  space
        """
        element = cls._element()
        element.send_keys(Keys.SPACE)
        
    
    @classmethod
    def Backspace(cls):
        """        在指定输入框发送回退键
        @note: key event ->  backspace
        """
        element = cls._element()
        element.send_keys(Keys.BACK_SPACE)
        
    
    @classmethod
    def Tab(cls):
        """        在指定输入框发送回制表键
        @note: key event ->  tab
        """
        element = cls._element()
        element.send_keys(Keys.TAB)
        
    
    @classmethod
    def Escape(cls):
        """        在指定输入框发送回退出键
        @note: key event ->  esc
        """
        element = cls._element()
        element.send_keys(Keys.ESCAPE)
            
    
    @classmethod
    def Focus(cls):
        """        在指定输入框发送 Null， 用于设置焦点
        @note: key event ->  NULL
        """
        
        element = cls._element()        
#         element.send_keys(Keys.NULL)        
        action = ActionChains(Web.driver)
        action.send_keys_to_element(element, Keys.NULL)
        action.perform()
        
    
    @classmethod
    def Upload(cls, filename):
        """        文件上传， 非原生input
        @todo:  some  upload.exe not  prepared
        @param file: 文件名(文件必须存在在工程resource目录下), upload.exe工具放在工程tools目录下
        """
        raise Exception("to do")
    
        TOOLS_PATH = ""
        RESOURCE_PATH = ""
        tool_4path = os.path.join(TOOLS_PATH, "upload.exe")        
        file_4path = os.path.join(RESOURCE_PATH, filename)
        #file_4path.decode('utf-8').encode('gbk')
        
        if os.path.isfile(file_4path):
            cls.Click()
            os.system(tool_4path + ' ' + file_4path)
        else:
            raise Exception('%s is not exists' % file_4path)
    
    @classmethod
    def UploadType(cls, file_path):
        """    上传，  一般，上传页面如果是input,原生file文件框, 如： <input type="file" id="test-image-file" name="test" accept="image/gif">，像这样的，定位到该元素，然后使用 send_keys 上传的文件的绝对路径        
        @param file_name: 文件名(文件必须存在在工程resource目录下)
        """
        if not os.path.isabs(file_path):
            return False
        
        if os.path.isfile(file_path):
            cls.SendKeys(file_path)
        else:            
            return False
        

      
    
    
    
    