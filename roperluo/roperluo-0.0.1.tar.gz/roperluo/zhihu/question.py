import requests
from pyquery import PyQuery as pq
import json
import time
import os
import urllib.request

class Question:
    def __init__(self, question_id, offset=0, limit=10, delay=3):
        self.question_id = question_id
        self.answer_url = 'https://www.zhihu.com/api/v4/questions/{}/answers'.format(self.question_id)
        
        self.session = requests.Session()
        self.offset = offset
        self.limit = limit
        self.delay = delay   #每次抓取的延时
        self.headers = {
              'User-Agent': "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
              'Accept-Encoding': 'gzip, deflate'
        }
        self.params = {
            'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
            'offset': self.offset,
            'limit': self.limit,
            'sort_by': 'default',
            'platform': 'desktop',
        }
        self.totals = 10
        self.answers = []   # 答案的文本
        
        self.dir = str(self.question_id)
        os.makedirs(self.dir, exist_ok=True)  #创建保存问题答案的目录
        
    def req_answer_api(self, offset, limit):
        self.params['offset'] = offset
        self.params['limit'] = limit
        try:
            r = requests.get(self.answer_url, params=self.params, headers= self.headers)
            res = json.loads(r.text)
            if 'paging' in res:
                self.totals = int(res['paging']['totals'])
            return res['data']
        except Exception as e:
            print("[ERROR]get offset:{}, limit:{} fail.err:{}, res:{}".format(offset, limit, e, res))
            return {}
        
    def fetch_answers(self):
        while self.offset < self.totals:
            print('fetch offset:{}, limit:{}, totals:{}'.format(self.offset, self.limit, self.totals))
            data = self.req_answer_api(self.offset, self.limit)
            self.answers.extend(data)
            
            self.offset += self.limit
            
            time.sleep(self.delay)
    
    def save_answers(self):
        file = os.path.join(self.dir, '{}_answer_all.json'.format(self.question_id))
        with open(file, 'w', encoding='utf-8') as f:
            f.write(json.dumps(self.answers))
            
    def save_answer_txt(self):
        file = os.path.join(self.dir, '{}_answer_text.json'.format(self.question_id))
        with open(file, 'w', encoding='utf-8') as f:
            for ans in self.answers:
                doc = pq(ans['content'])
                f.write(doc.text())
                f.write('\n\n')

    def save_answer_images(self):
        # 创建images目录
        image_dir = os.path.join(self.dir, 'images')
        os.makedirs(image_dir, exist_ok=True)
        # 保存所有图片
        for ans in self.answers:
            doc = pq(ans['content'])
            for img in doc('.origin_image').items():
                url = img.attr.src
                print('save image:{}'.format(url))
                if url.startswith('http') and url.find('pic3') == -1:  #pic3的图片没法访问
                    picture_name = url.split('/')[-1]
                    filename=os.path.join(image_dir, picture_name)
                    urllib.request.urlretrieve('https://pic2.zhimg.com/50/30e773af3b7a3d6c1c700b633507e815_hd.jpg',filename=filename)

            