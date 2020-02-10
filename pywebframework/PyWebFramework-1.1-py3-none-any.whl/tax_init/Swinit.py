#! /usr/bin/env python
# coding=utf-8

# 猫池客户端
import random
import json
import datetime
import time
import hashlib
import pyDes
import urllib.request
import base64
import ssl
import hmac
import json


class SwInitInterface(object):
    def __init__(self):
        # 请求的url
        self.url = "https://ddapi-p.bigfintax.com/declareports/declareDataFile/submit"
        # 流水号
        self.serial_number = ''.join(random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 20))
        # 用户名
        self.user = "history"
        # 密码
        self.passwd = "lehooBej"
        # 操作重试上限
        self.retry_max_times = 20

    def md5_encrypt(self, data) -> str:
        hl = hashlib.md5()
        hl.update(data.encode(encoding='utf-8'))
        print(hl.hexdigest())
        return hl.hexdigest()

    def md5_encrypt_bytes(self, data) -> str:
        #_data = bytes(data, encoding="utf-8")
        hl = hashlib.md5()
        hl.update(data)
        print(hl.hexdigest())
        return hl.hexdigest()

    def hmac_encrypt(self, key, data) -> str:
        hmac_key = bytes(key, encoding="utf-8")
        hmac_data = bytes(data, encoding="utf-8")
        #print(key,hmac_key)
        #print(data,hmac_data)
        h = hmac.new(hmac_key, hmac_data, hashlib.sha1)
        print(h.digest())
        return h.digest()

    def ecb_encrypt(self, key, data) -> bytes:
        # Des加密
        des_key = key.encode('utf-8')
        k = pyDes.des(des_key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
        EncryptStr = k.encrypt(data.encode('utf-8'))
        hl = hashlib.md5()
        hl.update(EncryptStr)
        return hl.hexdigest()

    def ecb_decrypt(self, key, data):
        # print(base64.b64decode(str))
        des_key = base64.b64decode(key)
        des_key = des_key[:8]
        # des_key = triple_des(des_key, ECB, padmode=PAD_PKCS5)
        k = pyDes.des(des_key, pyDes.ECB, pad=None, padmode=pyDes.PAD_PKCS5)
        y = k.decrypt(base64.b64decode(data))
        return y.decode('utf-8')

    def send_xml(self, strxml:str) -> bool:
       request_url = '''AccessKeyID={AccessKeyID}&SignatureNonce={SignatureNonce}&TimeStamp={TimeStamp}&Version=1.0'''
       request_url = request_url.replace('{AccessKeyID}', self.user)
       request_url = request_url.replace('{SignatureNonce}', ''.join(
           random.sample('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 12)))
       timestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
       request_url = request_url.replace('{TimeStamp}', timestamp)
       #request_url = "AccessKeyID=history&SignatureNonce=jFfKqrOLHtxc&TimeStamp=2019-07-09T17:33:29Z&Version=1.0"
       pswd = self.md5_encrypt(self.passwd).upper()
       hmacpwd = self.hmac_encrypt(pswd, request_url)
       signature = self.md5_encrypt_bytes(hmacpwd).upper()
       request_url += "&Signature=" + signature
       print(request_url)
       request_url = self.url + "?" + request_url
       print(request_url)
       context = ssl._create_default_https_context()
       request = urllib.request.Request(request_url)
       request.add_header("Content-Type", "application/json; charset=utf-8")
       request.data = bytes(strxml, encoding="utf-8")
       request.method = "POST"

       response = urllib.request.urlopen(request, context=context)
       body = response.read()
       if "<HTML>" in str(body) or response.status != 200:
           return False

       text = str(body, encoding="utf-8")
       #res = json.dumps(text)
       dict_data = json.loads(text)
       print(dict_data)
       return dict_data["Code"] == "200" and dict_data["Message"] =="数据上传成功！"

if __name__ == '__main__':
    strxml = '''<?xml version="1.0" encoding="UTF-8"?>
<Root>
	<TaskSet>
		<OrgInfo>
			<OrgName>恩施九州通医药有限公司</OrgName>
			<OrgTaxNum>91422800676461077D</OrgTaxNum>
		</OrgInfo>
		<LoginInfo LoginName="" LoginPassword=""/>
		<TaxInfo>
			<TableSet id="010100" ssqType="1" ssqs="2019-07-01" ssqz="2019-07-31" taxType="" type="SB">
				<Table name="主表">
					<Param>
						<Item location="AN03001">39071270.59</Item>
						<Item location="AN03002">287806753.02</Item>
						<Item location="AN03003">287806753.02</Item>
						<Item location="AN03004">287806753.02</Item>
						<Item location="AN03005">39071270.59</Item>
						<Item location="AN03006">287469028.14</Item>
						<Item location="AN03007">287469028.14</Item>
						<Item location="AN03008">287469028.14</Item>
						<Item location="AN03009">0.00</Item>
						<Item location="AN03010">0.00</Item>
						<Item location="AN03011">0.00</Item>
						<Item location="AN03012">0.00</Item>
						<Item location="AN03013">0.00</Item>
						<Item location="AN03014">0.00</Item>
						<Item location="AN03015">0.00</Item>
						<Item location="AN03016">0.00</Item>
						<Item location="AN03017">3671378.62</Item>
						<Item location="AN03018">22121862.76</Item>
						<Item location="AN03019">0.00</Item>
						<Item location="AN03020">0.00</Item>
						<Item location="AN03021">0.00</Item>
						<Item location="AN03022">0.00</Item>
						<Item location="AN03023">0.00</Item>
						<Item location="AN03024">0.00</Item>
						<Item location="AN03025">0.00</Item>
						<Item location="AN03026">0.00</Item>
						<Item location="AN03027">0.00</Item>
						<Item location="AN03028">0.00</Item>
						<Item location="AN03029">63428.82</Item>
						<Item location="AN03030">536263.44</Item>
						<Item location="AN03031">536263.44</Item>
						<Item location="AN03032">536263.44</Item>
						<Item location="AN03033">63428.82</Item>
						<Item location="AN03034">536263.44</Item>
						<Item location="AN03035">536263.44</Item>
						<Item location="AN03036">536263.44</Item>
						<Item location="AN03037">0.00</Item>
						<Item location="AN03038">0.00</Item>
						<Item location="AN03039">0.00</Item>
						<Item location="AN03040">0.00</Item>
						<Item location="AN03041">5059616.70</Item>
						<Item location="AN03042">40951716.93</Item>
						<Item location="AN03043">40951716.93</Item>
						<Item location="AN03044">40951716.93</Item>
						<Item location="AN03045">5230084.32</Item>
						<Item location="AN03046">40892525.24</Item>
						<Item location="AN03047">40892525.24</Item>
						<Item location="AN03048">40892525.24</Item>
						<Item location="AN03049">0.00</Item>
						<Item location="AN03050">0.00</Item>
						<Item location="AN03051">0.00</Item>
						<Item location="AN03052">0.00</Item>
						<Item location="AN03053">507169.40</Item>
						<Item location="AN03054">2768468.18</Item>
						<Item location="AN03055">2768468.18</Item>
						<Item location="AN03056">2768468.18</Item>
						<Item location="AN03057">0.00</Item>
						<Item location="AN03058">0.00</Item>
						<Item location="AN03059">0.00</Item>
						<Item location="AN03060">0.00</Item>
						<Item location="AN03061">0.00</Item>
						<Item location="AN03062">0.00</Item>
						<Item location="AN03063">0.00</Item>
						<Item location="AN03064">0.00</Item>
						<Item location="AN03065">4722914.92</Item>
						<Item location="AN03066"></Item>
						<Item location="AN03067"></Item>
						<Item location="AN03068"></Item>
						<Item location="AN03069">4722914.92</Item>
						<Item location="AN03070">0.00</Item>
						<Item location="AN03071">0.00</Item>
						<Item location="AN03072">0.00</Item>
						<Item location="AN03073">336701.78</Item>
						<Item location="AN03074">2827659.87</Item>
						<Item location="AN03075">2827659.87</Item>
						<Item location="AN03076">2827659.87</Item>
						<Item location="AN03077">0.00</Item>
						<Item location="AN03078">0.00</Item>
						<Item location="AN03079">0.00</Item>
						<Item location="AN03080">0.00</Item>
						<Item location="AN03081">110141.35</Item>
						<Item location="AN03082">663655.81</Item>
						<Item location="AN03083">663655.81</Item>
						<Item location="AN03084">663655.81</Item>
						<Item location="AN03085">0.00</Item>
						<Item location="AN03086">0.00</Item>
						<Item location="AN03087">0.00</Item>
						<Item location="AN03088">0.00</Item>
						<Item location="AN03089">0.00</Item>
						<Item location="AN03090">1026.02</Item>
						<Item location="AN03091">1026.02</Item>
						<Item location="AN03092">1026.02</Item>
						<Item location="AN03093">446843.13</Item>
						<Item location="AN03094">3490289.66</Item>
						<Item location="AN03095">3490289.66</Item>
						<Item location="AN03096">3490289.66</Item>
						<Item location="AN03097">546724.20</Item>
						<Item location="AN03098">664854.46</Item>
						<Item location="AN03099">664854.46</Item>
						<Item location="AN03100">664854.46</Item>
						<Item location="AN03101">0.00</Item>
						<Item location="AN03102">0.00</Item>
						<Item location="AN03103">0.00</Item>
						<Item location="AN03104">0.00</Item>
						<Item location="AN03105">403069.45</Item>
						<Item location="AN03106">3564646.24</Item>
						<Item location="AN03107">3564646.24</Item>
						<Item location="AN03108">3564646.24</Item>
						<Item location="AN03109">0.00</Item>
						<Item location="AN03110"></Item>
						<Item location="AN03111"></Item>
						<Item location="AN03112"></Item>
						<Item location="AN03113">0.00</Item>
						<Item location="AN03114"></Item>
						<Item location="AN03115"></Item>
						<Item location="AN03116"></Item>
						<Item location="AN03117">403069.45</Item>
						<Item location="AN03118">3564646.24</Item>
						<Item location="AN03119">3564646.24</Item>
						<Item location="AN03120">3564646.24</Item>
						<Item location="AN03121">0.00</Item>
						<Item location="AN03122">0.00</Item>
						<Item location="AN03123">0.00</Item>
						<Item location="AN03124">0.00</Item>
						<Item location="AN03125">590497.88</Item>
						<Item location="AN03126">590497.88</Item>
						<Item location="AN03127">590497.88</Item>
						<Item location="AN03128">590497.88</Item>
						<Item location="AN03129">143654.75</Item>
						<Item location="AN03130"></Item>
						<Item location="AN03131"></Item>
						<Item location="AN03132"></Item>
						<Item location="AN03133">446843.13</Item>
						<Item location="AN03134"></Item>
						<Item location="AN03135"></Item>
						<Item location="AN03136"></Item>
						<Item location="AN03137"></Item>
						<Item location="AN03138"></Item>
						<Item location="AN03139"></Item>
						<Item location="AN03140"></Item>
						<Item location="AN03141">0.00</Item>
						<Item location="AN03142">0.00</Item>
						<Item location="AN03143">0.00</Item>
						<Item location="AN03144">0.00</Item>
						<Item location="AN03145">0.00</Item>
						<Item location="AN03146">0.00</Item>
						<Item location="AN03147">0.00</Item>
						<Item location="AN03148">0.00</Item>
						<Item location="AN03149">0.00</Item>
						<Item location="AN03150">0.00</Item>
						<Item location="AN03151">0.00</Item>
						<Item location="AN03152">0.00</Item>
					</Param>
				</Table>
				<Table name="附表一">
					<Param>
						<Item location="AN27001">5118221.19</Item>
						<Item location="AN27002">665368.80</Item>
						<Item location="AN27003">37937347.97</Item>
						<Item location="AN27004">5072109.33</Item>
						<Item location="AN27005">-4378482.56</Item>
						<Item location="AN27006">-713334.18</Item>
						<Item location="AN27007">0.00</Item>
						<Item location="AN27008">0.00</Item>
						<Item location="AN27009">38677086.60</Item>
						<Item location="AN27010">5024143.95</Item>
						<Item location="AN27011"></Item>
						<Item location="AN27012"></Item>
						<Item location="AN27013"></Item>
						<Item location="AN27014"></Item>
						<Item location="AN27015">0.00</Item>
						<Item location="AN27016">0.00</Item>
						<Item location="AN27017">0.00</Item>
						<Item location="AN27018">0.00</Item>
						<Item location="AN27019">0.00</Item>
						<Item location="AN27020">0.00</Item>
						<Item location="AN27021">0.00</Item>
						<Item location="AN27022">0.00</Item>
						<Item location="AN27023">0.00</Item>
						<Item location="AN27024">0.00</Item>
						<Item location="AN27025">0.00</Item>
						<Item location="AN27026">0.00</Item>
						<Item location="AN27027">0.00</Item>
						<Item location="AN27028">0.00</Item>
						<Item location="AN27029">45506.73</Item>
						<Item location="AN27030">4081.77</Item>
						<Item location="AN27031">949594.88</Item>
						<Item location="AN27032">89065.88</Item>
						<Item location="AN27033">-600917.62</Item>
						<Item location="AN27034">-57674.9</Item>
						<Item location="AN27035">0</Item>
						<Item location="AN27036">0</Item>
						<Item location="AN27037">394183.99</Item>
						<Item location="AN27038">35472.75</Item>
						<Item location="AN27039"></Item>
						<Item location="AN27040"></Item>
						<Item location="AN27041"></Item>
						<Item location="AN27042"></Item>
						<Item location="AN27043">0.00</Item>
						<Item location="AN27044">0.00</Item>
						<Item location="AN27045">0.00</Item>
						<Item location="AN27046">0.00</Item>
						<Item location="AN27047">0.00</Item>
						<Item location="AN27048">0.00</Item>
						<Item location="AN27049">0.00</Item>
						<Item location="AN27050">0.00</Item>
						<Item location="AN27051">0.00</Item>
						<Item location="AN27052">0.00</Item>
						<Item location="AN27053">0.00</Item>
						<Item location="AN27054">0.00</Item>
						<Item location="AN27055">0.00</Item>
						<Item location="AN27056">0.00</Item>
						<Item location="AN27071">0.00</Item>
						<Item location="AN27072">0.00</Item>
						<Item location="AN27073">0.00</Item>
						<Item location="AN27074">0.00</Item>
						<Item location="AN27075">0.00</Item>
						<Item location="AN27076">0.00</Item>
						<Item location="AN27077">0.00</Item>
						<Item location="AN27078">0.00</Item>
						<Item location="AN27079">0.00</Item>
						<Item location="AN27080">0.00</Item>
						<Item location="AN27081">0.00</Item>
						<Item location="AN27082">0.00</Item>
						<Item location="AN27083">0.00</Item>
						<Item location="AN27084">0.00</Item>
						<Item location="AN27085"></Item>
						<Item location="AN27086"></Item>
						<Item location="AN27087"></Item>
						<Item location="AN27088"></Item>
						<Item location="AN27089"></Item>
						<Item location="AN27090"></Item>
						<Item location="AN27091"></Item>
						<Item location="AN27092"></Item>
						<Item location="AN27093">0.00</Item>
						<Item location="AN27094">0.00</Item>
						<Item location="AN27095"></Item>
						<Item location="AN27096"></Item>
						<Item location="AN27097"></Item>
						<Item location="AN27098"></Item>
						<Item location="AN27099"></Item>
						<Item location="AN27100"></Item>
						<Item location="AN27101"></Item>
						<Item location="AN27102"></Item>
						<Item location="AN27103"></Item>
						<Item location="AN27104"></Item>
						<Item location="AN27105"></Item>
						<Item location="AN27106"></Item>
						<Item location="AN27107">0.00</Item>
						<Item location="AN27108">0.00</Item>
						<Item location="AN27109">0.00</Item>
						<Item location="AN27110">0.00</Item>
						<Item location="AN27111">0.00</Item>
						<Item location="AN27112">0.00</Item>
						<Item location="AN27113">0.00</Item>
						<Item location="AN27114">0.00</Item>
						<Item location="AN27115">0.00</Item>
						<Item location="AN27116">0.00</Item>
						<Item location="AN27117">0.00</Item>
						<Item location="AN27118">0.00</Item>
						<Item location="AN27119"></Item>
						<Item location="AN27120"></Item>
						<Item location="AN27121">0.00</Item>
						<Item location="AN27122">0.00</Item>
						<Item location="AN27123"></Item>
						<Item location="AN27124"></Item>
						<Item location="AN27125"></Item>
						<Item location="AN27126"></Item>
						<Item location="AN27127">0.00</Item>
						<Item location="AN27128">0.00</Item>
						<Item location="AN27129">0.00</Item>
						<Item location="AN27130">0.00</Item>
						<Item location="AN27131">0.00</Item>
						<Item location="AN27132">0.00</Item>
						<Item location="AN27133"></Item>
						<Item location="AN27134"></Item>
						<Item location="AN27135">0.00</Item>
						<Item location="AN27136">0.00</Item>
						<Item location="AN27137"></Item>
						<Item location="AN27138"></Item>
						<Item location="AN27139"></Item>
						<Item location="AN27140"></Item>
						<Item location="AN27141">0.00</Item>
						<Item location="AN27142">0.00</Item>
						<Item location="AN27143">0.00</Item>
						<Item location="AN27144">0.00</Item>
						<Item location="AN27145">0.00</Item>
						<Item location="AN27146">0.00</Item>
						<Item location="AN27147"></Item>
						<Item location="AN27148"></Item>
						<Item location="AN27149">0.00</Item>
						<Item location="AN27150">0.00</Item>
						<Item location="AN27151">0.00</Item>
						<Item location="AN27152">0.00</Item>
						<Item location="AN27153">0.00</Item>
						<Item location="AN27154">0.00</Item>
						<Item location="AN27155">0.00</Item>
						<Item location="AN27156">0.00</Item>
						<Item location="AN27157">0.00</Item>
						<Item location="AN27158">0.00</Item>
						<Item location="AN27159">0.00</Item>
						<Item location="AN27160">0.00</Item>
						<Item location="AN27161"></Item>
						<Item location="AN27162"></Item>
						<Item location="AN27163">0.00</Item>
						<Item location="AN27164">0.00</Item>
						<Item location="AN27165"></Item>
						<Item location="AN27166"></Item>
						<Item location="AN27167"></Item>
						<Item location="AN27168"></Item>
						<Item location="AN27169">0.00</Item>
						<Item location="AN27170">0.00</Item>
						<Item location="AN27171">4239867.37</Item>
						<Item location="AN27172">127196.11</Item>
						<Item location="AN27173">-568488.75</Item>
						<Item location="AN27174">-17054.76</Item>
						<Item location="AN27175"></Item>
						<Item location="AN27176"></Item>
						<Item location="AN27177">3671378.62</Item>
						<Item location="AN27178">110141.35</Item>
						<Item location="AN27179"></Item>
						<Item location="AN27180"></Item>
						<Item location="AN27181"></Item>
						<Item location="AN27182"></Item>
						<Item location="AN27183">0.00</Item>
						<Item location="AN27184">0.00</Item>
						<Item location="AN27185">0.00</Item>
						<Item location="AN27186">0.00</Item>
						<Item location="AN27187">0.00</Item>
						<Item location="AN27188">0.00</Item>
						<Item location="AN27189"></Item>
						<Item location="AN27190"></Item>
						<Item location="AN27191">0.00</Item>
						<Item location="AN27192">0.00</Item>
						<Item location="AN27193">0.00</Item>
						<Item location="AN27194">0.00</Item>
						<Item location="AN27195">0.00</Item>
						<Item location="AN27196">0.00</Item>
						<Item location="AN27197">0.00</Item>
						<Item location="AN27198">0.00</Item>
						<Item location="AN27199">0.00</Item>
						<Item location="AN27200">0.00</Item>
						<Item location="AN27201">0.00</Item>
						<Item location="AN27202">0.00</Item>
						<Item location="AN27203"></Item>
						<Item location="AN27204"></Item>
						<Item location="AN27205">0.00</Item>
						<Item location="AN27206">0.00</Item>
						<Item location="AN27207">0.00</Item>
						<Item location="AN27208">0.00</Item>
						<Item location="AN27209">0.00</Item>
						<Item location="AN27210">0.00</Item>
						<Item location="AN27211">0.00</Item>
						<Item location="AN27212">0.00</Item>
						<Item location="AN27213">0.00</Item>
						<Item location="AN27214">0.00</Item>
						<Item location="AN27215">0.00</Item>
						<Item location="AN27216">0.00</Item>
						<Item location="AN27217"></Item>
						<Item location="AN27218"></Item>
						<Item location="AN27219">0.00</Item>
						<Item location="AN27220">0.00</Item>
						<Item location="AN27221">0.00</Item>
						<Item location="AN27222">0.00</Item>
						<Item location="AN27223">0.00</Item>
						<Item location="AN27224">0.00</Item>
						<Item location="AN27225">0.00</Item>
						<Item location="AN27226">0.00</Item>
						<Item location="AN27227">0.00</Item>
						<Item location="AN27228">0.00</Item>
						<Item location="AN27229">0.00</Item>
						<Item location="AN27230">0.00</Item>
						<Item location="AN27231"></Item>
						<Item location="AN27232"></Item>
						<Item location="AN27233">0.00</Item>
						<Item location="AN27234">0.00</Item>
						<Item location="AN27235">0.00</Item>
						<Item location="AN27236">0.00</Item>
						<Item location="AN27237">0.00</Item>
						<Item location="AN27238">0.00</Item>
						<Item location="AN27239"></Item>
						<Item location="AN27240"></Item>
						<Item location="AN27241"></Item>
						<Item location="AN27242"></Item>
						<Item location="AN27243"></Item>
						<Item location="AN27244"></Item>
						<Item location="AN27245"></Item>
						<Item location="AN27246"></Item>
						<Item location="AN27247">0.00</Item>
						<Item location="AN27248">0.00</Item>
						<Item location="AN27249"></Item>
						<Item location="AN27250"></Item>
						<Item location="AN27251"></Item>
						<Item location="AN27252"></Item>
						<Item location="AN27253"></Item>
						<Item location="AN27254"></Item>
						<Item location="AN27255"></Item>
						<Item location="AN27256"></Item>
						<Item location="AN27257"></Item>
						<Item location="AN27258"></Item>
						<Item location="AN27259"></Item>
						<Item location="AN27260"></Item>
						<Item location="AN27261">0.00</Item>
						<Item location="AN27262">0.00</Item>
						<Item location="AN27263">0.00</Item>
						<Item location="AN27264">0.00</Item>
						<Item location="AN27265">0.00</Item>
						<Item location="AN27266">0.00</Item>
						<Item location="AN27267"></Item>
						<Item location="AN27268"></Item>
						<Item location="AN27269">0.00</Item>
						<Item location="AN27270"></Item>
						<Item location="AN27271">0.00</Item>
						<Item location="AN27272"></Item>
						<Item location="AN27273"></Item>
						<Item location="AN27274"></Item>
						<Item location="AN27275">0.00</Item>
						<Item location="AN27276"></Item>
						<Item location="AN27277"></Item>
						<Item location="AN27278"></Item>
						<Item location="AN27279"></Item>
						<Item location="AN27280"></Item>
						<Item location="AN27281"></Item>
						<Item location="AN27282"></Item>
						<Item location="AN27283">0.00</Item>
						<Item location="AN27284"></Item>
						<Item location="AN27285">0.00</Item>
						<Item location="AN27286"></Item>
						<Item location="AN27287"></Item>
						<Item location="AN27288"></Item>
						<Item location="AN27289">0.00</Item>
						<Item location="AN27290"></Item>
						<Item location="AN27291">0.00</Item>
						<Item location="AN27292">0.00</Item>
						<Item location="AN27293">0.00</Item>
						<Item location="AN27294"></Item>
						<Item location="AN27295">0.00</Item>
						<Item location="AN27296">0.00</Item>
						<Item location="AN27297">63809.06</Item>
						<Item location="AN27298"></Item>
						<Item location="AN27299">-380.24</Item>
						<Item location="AN27300"></Item>
						<Item location="AN27301"></Item>
						<Item location="AN27302"></Item>
						<Item location="AN27303">63428.82</Item>
						<Item location="AN27304"></Item>
						<Item location="AN27305"></Item>
						<Item location="AN27306"></Item>
						<Item location="AN27307"></Item>
						<Item location="AN27308"></Item>
						<Item location="AN27309"></Item>
						<Item location="AN27310"></Item>
						<Item location="AN27311">0.00</Item>
						<Item location="AN27312"></Item>
						<Item location="AN27313">0.00</Item>
						<Item location="AN27314"></Item>
						<Item location="AN27315"></Item>
						<Item location="AN27316"></Item>
						<Item location="AN27317">0.00</Item>
						<Item location="AN27318"></Item>
						<Item location="AN27319">0.00</Item>
						<Item location="AN27320">0.00</Item>
						<Item location="AN27321">0.00</Item>
						<Item location="AN27322"></Item>
					</Param>
				</Table>
				<Table name="附表二">
					<Param>
						<Item location="AN29001">1635</Item>
						<Item location="AN29002">40116549.50</Item>
						<Item location="AN29003">5229544.91</Item>
						<Item location="AN29004">1635</Item>
						<Item location="AN29005">40116549.50</Item>
						<Item location="AN29006">5229544.91</Item>
						<Item location="AN29007">0</Item>
						<Item location="AN29008">0.00</Item>
						<Item location="AN29009">0.00</Item>
						<Item location="AN29010">0</Item>
						<Item location="AN29011">0.00</Item>
						<Item location="AN29012">539.41</Item>
						<Item location="AN29013">0</Item>
						<Item location="AN29014">0.00</Item>
						<Item location="AN29015">0.00</Item>
						<Item location="AN29016">0</Item>
						<Item location="AN29017">0.00</Item>
						<Item location="AN29018">0.00</Item>
						<Item location="AN29019">0</Item>
						<Item location="AN29020"></Item>
						<Item location="AN29021">0.00</Item>
						<Item location="AN29022"></Item>
						<Item location="AN29023"></Item>
						<Item location="AN29024">0</Item>
						<Item location="AN29025">0</Item>
						<Item location="AN29026">0.00</Item>
						<Item location="AN29027">539.41</Item>
						<Item location="AN29028">0</Item>
						<Item location="AN29029">0.00</Item>
						<Item location="AN29030">0.00</Item>
						<Item location="AN29031">0</Item>
						<Item location="AN29032">5942.33</Item>
						<Item location="AN29033">534.81</Item>
						<Item location="AN29034"></Item>
						<Item location="AN29035"></Item>
						<Item location="AN29036">0.00</Item>
						<Item location="AN29037">1635</Item>
						<Item location="AN29038">40116549.50</Item>
						<Item location="AN29039">5230084.32</Item>
						<Item location="AN29040">507169.40</Item>
						<Item location="AN29041">0.00</Item>
						<Item location="AN29042">297.83</Item>
						<Item location="AN29043">40.51</Item>
						<Item location="AN29044">0.00</Item>
						<Item location="AN29045">0.00</Item>
						<Item location="AN29046">0.00</Item>
						<Item location="AN29047">496808.39</Item>
						<Item location="AN29048">0.00</Item>
						<Item location="AN29049">0.00</Item>
						<Item location="AN29050">10022.67</Item>
						<Item location="AN29051"></Item>
						<Item location="AN29052"></Item>
						<Item location="AN29053"></Item>
						<Item location="AN29054">0</Item>
						<Item location="AN29055">0.00</Item>
						<Item location="AN29056">0.00</Item>
						<Item location="AN29057">0</Item>
						<Item location="AN29058">0.00</Item>
						<Item location="AN29059">0.00</Item>
						<Item location="AN29060">0</Item>
						<Item location="AN29061">0.00</Item>
						<Item location="AN29062">0.00</Item>
						<Item location="AN29063">0</Item>
						<Item location="AN29064">0.00</Item>
						<Item location="AN29065">0.00</Item>
						<Item location="AN29066">0</Item>
						<Item location="AN29067">0.00</Item>
						<Item location="AN29068">0.00</Item>
						<Item location="AN29069">0</Item>
						<Item location="AN29070">0.00</Item>
						<Item location="AN29071">0.00</Item>
						<Item location="AN29072">0</Item>
						<Item location="AN29073">0.00</Item>
						<Item location="AN29074">0.00</Item>
						<Item location="AN29075">0</Item>
						<Item location="AN29076"></Item>
						<Item location="AN29077">0.00</Item>
						<Item location="AN29078">0.00</Item>
						<Item location="AN29079">0.00</Item>
						<Item location="AN29081"></Item>
						<Item location="AN29082"></Item>
						<Item location="AN29083"></Item>
						<Item location="AN29084">1635</Item>
						<Item location="AN29085">40116549.5</Item>
						<Item location="AN29086">5229544.91</Item>
						<Item location="AN29087"></Item>
						<Item location="AN29088"></Item>
						<Item location="AN29089">0</Item>
					</Param>
				</Table>
				<Table name="附表三">
					<Param>
						<Item location="AN28001">0.00</Item>
						<Item location="AN28002">0.00</Item>
						<Item location="AN28003">0.00</Item>
						<Item location="AN28004">0.00</Item>
						<Item location="AN28005">0.00</Item>
						<Item location="AN28006">0.00</Item>
						<Item location="AN28007">0.00</Item>
						<Item location="AN28008">0.00</Item>
						<Item location="AN28009">0.00</Item>
						<Item location="AN28010">0.00</Item>
						<Item location="AN28011">0.00</Item>
						<Item location="AN28012">0.00</Item>
						<Item location="AN28013">0.00</Item>
						<Item location="AN28014">0.00</Item>
						<Item location="AN28015">0.00</Item>
						<Item location="AN28016">0.00</Item>
						<Item location="AN28017">0.00</Item>
						<Item location="AN28018">0.00</Item>
						<Item location="AN28019">0.00</Item>
						<Item location="AN28020">0.00</Item>
						<Item location="AN28021">0.00</Item>
						<Item location="AN28022">0.00</Item>
						<Item location="AN28023">0.00</Item>
						<Item location="AN28024">0.00</Item>
						<Item location="AN28025">0.00</Item>
						<Item location="AN28026">0.00</Item>
						<Item location="AN28027">0.00</Item>
						<Item location="AN28028">0.00</Item>
						<Item location="AN28029">0.00</Item>
						<Item location="AN28030">0.00</Item>
						<Item location="AN28031">0.00</Item>
						<Item location="AN28032">0.00</Item>
						<Item location="AN28033">0.00</Item>
						<Item location="AN28034">0.00</Item>
						<Item location="AN28035">0.00</Item>
						<Item location="AN28036">0.00</Item>
						<Item location="AN28037">0.00</Item>
						<Item location="AN28038">0.00</Item>
						<Item location="AN28039">0.00</Item>
						<Item location="AN28040">0.00</Item>
						<Item location="AN28041">0.00</Item>
						<Item location="AN28042">0.00</Item>
						<Item location="AN28043">0.00</Item>
						<Item location="AN28044">0.00</Item>
						<Item location="AN28045">0.00</Item>
						<Item location="AN28046">0.00</Item>
						<Item location="AN28047">0.00</Item>
						<Item location="AN28048">0.00</Item>
					</Param>
				</Table>
				<Table name="附表四">
					<Param>
						<Item location="AN31001">0.00</Item>
						<Item location="AN31002">0.00</Item>
						<Item location="AN31003">0.00</Item>
						<Item location="AN31004">0.00</Item>
						<Item location="AN31005">0.00</Item>
						<Item location="AN31006">0.00</Item>
						<Item location="AN31007">0.00</Item>
						<Item location="AN31008">0.00</Item>
						<Item location="AN31009">0.00</Item>
						<Item location="AN31010">0.00</Item>
						<Item location="AN31011">0.00</Item>
						<Item location="AN31012">0.00</Item>
						<Item location="AN31013">0.00</Item>
						<Item location="AN31014">0.00</Item>
						<Item location="AN31015">0.00</Item>
						<Item location="AN31016">0.00</Item>
						<Item location="AN31017">0.00</Item>
						<Item location="AN31018">0.00</Item>
						<Item location="AN31019">0.00</Item>
						<Item location="AN31020">0.00</Item>
						<Item location="AN31021">0.00</Item>
						<Item location="AN31022">0.00</Item>
						<Item location="AN31023">0.00</Item>
						<Item location="AN31024">0.00</Item>
						<Item location="AN31025">0.00</Item>
						<Item location="AN31026">0</Item>
						<Item location="AN31027">0</Item>
						<Item location="AN31028">0</Item>
						<Item location="AN31029">0</Item>
						<Item location="AN31030">0</Item>
						<Item location="AN31031">0</Item>
						<Item location="AN31032">0</Item>
						<Item location="AN31033">0</Item>
						<Item location="AN31034">0</Item>
						<Item location="AN31035">0</Item>
						<Item location="AN31036">0</Item>
						<Item location="AN31037">0</Item>
						<Item location="AN31038">0</Item>
						<Item location="AN31039">0</Item>
						<Item location="AN31040">0</Item>
						<Item location="AN31041">0</Item>
						<Item location="AN31042">0</Item>
						<Item location="AN31043">0</Item>
					</Param>
				</Table>
				<Table name="增值税减免税申报明细表">
					<Param>
						<Float name="float1" rowNum="1">
							<Item location="AN090001">0001129999 | |SXA031900732|避孕药品和用具免征增值税优惠|其他</Item>
							<Item location="AN090101">63428.82</Item>
							<Item location="AN090201">0</Item>
							<Item location="AN090301">63428.82</Item>
							<Item location="AN090401">0.13</Item>
							<Item location="AN090501">0</Item>
						</Float>
					</Param>
				</Table>
				<Table name="必填报税表列表">
					<Param>
						<Item col="无列标题" row="无行标题">主表</Item>
						<Item col="无列标题" row="无行标题">附表一</Item>
						<Item col="无列标题" row="无行标题">附表二</Item>
						<Item col="无列标题" row="无行标题">附表三</Item>
						<Item col="无列标题" row="无行标题">附表四</Item>
						<Item col="无列标题" row="无行标题">增值税减免税申报明细表</Item>
					</Param>
				</Table>
			</TableSet>
		</TaxInfo>
	</TaskSet>
</Root>
'''
    # mac = hmac.new(b'A1B81B0051FCB1657DA0FD4733DB7259', b'AccessKeyID=history&SignatureNonce=jFfKqrOLHtxc&TimeStamp=2019-07-09T17:33:29Z&Version=1.0', hashlib.sha1)
    # print(mac.digest(),len(mac.digest()),type(mac.digest()))
    # data1 = mac.digest()
    # hl1 = hashlib.md5()
    # hl1.update(data1)
    # print(str(hl1.hexdigest()).upper())  #26D7D1C6C12C82BB7D19F7F20BC3C470

    api = SwInitInterface()
    ret = api.send_xml(strxml)
    print(ret)
