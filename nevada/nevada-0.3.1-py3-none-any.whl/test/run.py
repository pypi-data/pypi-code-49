import sys
sys.path.append(r'/Users/mintaegyu/PycharmProjects/nevada')
from nevada.API.RelKwdStat import *
from nevada.API.Ad import *
from nevada.API.Estimate import *

if __name__=="__main__":
    base_url = 'https://api.naver.com'
    api_key = '010000000006b395250f1116b4a4e2c817ec0c1ab5d2aadf3911ee4494e33c266ace517843'
    secret_key = 'AQAAAAAGs5UlDxEWtKTiyBfsDBq150HUUna4ueVv0LLF6A3r4w=='
    customer_id = '1810030'


    class GetPerformanceObject:
        def __init__(self, device, keywordplus, key, bids):
            self.device = device
            self.keywordplus = keywordplus
            self.key = key
            self.bids = bids

    estimate = Estimate(base_url=base_url, api_key=api_key, secret_key=secret_key, customer_id=customer_id)

    obj1 = GetPerformanceBulkObject(device='BOTH', keywordplus=False, keyword='종이빨대', bid=100)
    obj2 = GetPerformanceBulkObject(device='BOTH', keywordplus=False, keyword='종이빨대', bid=200)
    obj3 = GetPerformanceBulkObject(device='BOTH', keywordplus=False, keyword='종이빨대', bid=300)
    obj = [obj1,obj2,obj3]
    result = estimate.get_performance_many_json(GetPerformanceBulkObjectList=obj)
    print(result)

    #입찰가:
    #매체구분: PC/모바일, PC, 모바일
    #키워드확장: ?

    #키워드 string keyword 스테인레스빨대 NULL
    # 입찰가 int bid [100,200,300,400,500] or 100 NULL
    # 매체구분 string device 'PC','MOBILE','BOTH' 'BOTH'
    #키워드_확장 적용/미적용 boolean keyword_expansion True/False None(Default value)

    # device = 'PC'
    # period = 'DAY'
    # items = ['종이빨대','스테인레스빨대']

    # GetExposureMinimumBid(device, period, items)
    # keyword = '스테인레스빨대'
    # bid = [100,200,300,400,500]

    # ms = MasterReport(base_url, api_key, secret_key, customer_id)
    # m = ms.get_master_report_list()
    # print(m[0].managerLoginId)

    # ad = Ad(base_url, api_key, secret_key, customer_id)
    # tt = ad.get_ad_list_by_ids(['nad-a001-01-000000009598016'])
    # print(tt)

    # key_and_position = KeyAndPositionObject('빨대', '1')
    # medi = GetAvgPositionBidObject('PC', key_and_position)
    # result = estimate.get_median_bid_json('keyword', medi)
    # print(result)

    """
    #애드(소재) 소재고유번호를 통해 리스트 받아오기
    tt = ad.get_ad_list_by_ids('nad-a001-01-000000009598016') pprint.pprint(tt[0].nccAdId)

    애드그룹고유번호를 통해 리스트 받아오기
    tt = ad.get_ad_list('grp-a001-01-000000002412336') pprint.pprint(tt[0].ad.pc)

    소재고유번호를 통해 소재정보 받아오기
    tt = ad.get_ad('nad-a001-01-000000009598016') pprint.pprint(tt.nccAdgroupId)

    소재등록하기
    filed_obj = AdFieldObject() filed_obj.description = "이것은 에이피아이 테스트의 일종으로 테스트입니다."
    filed_obj.headline = "에이피아이 에드클라우드"
    filed_obj.pc = filed_obj.make_pc_easy('http://www.naver.com')
    filed_obj.mobile = filed_obj.make_mobile_easy('http://www.naver.com')

    add_obj = CreateAdObject(filed_obj, 'grp-a001-01-000000002412336', 'TEXT_45')

    return_obj = ad.create_ad(add_obj)

    소재 수정하기
    filed_obj = AdFieldObject()
    filed_obj.description = "이것은 에이피아이 테스트의 일종으로 테스트"
    filed_obj.headline = "에이피아이 에드클라우드"
    filed_obj.pc = filed_obj.make_pc_easy('http://www.naver.com')
    filed_obj.mobile = filed_obj.make_mobile_easy('http://www.naver.com')

    update_obj = UpdateAdObject(filed_obj,'nad-a001-01-000000010072369')
    update_obj.userLock = 1 ad.update_ad('nad-a001-01-000000010072369', 'userLock', update_obj)

    소재 복사
    ad.copy_ad('nad-a001-01-000000009598016', 'grp-a001-01-000000002548182', '0')

    소재 삭제
    ad.delete_ad('nad-a001-01-000000010072402')
    """
