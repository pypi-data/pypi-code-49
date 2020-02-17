import psycopg2



class weiser():
    def __init__(self):
        pass

    def throw_query(query):
        # DB 연결
        conn = psycopg2.connect(
            "dbname='inct_dev' user='inct' host='ec2-13-124-82-46.ap-northeast-2.compute.amazonaws.com' port=5432' password='inct'")
        cur = conn.cursor()

        # query 실행
        cur.execute(query)

        # 결과물 가져오기, list 형태
        rows = cur.fetchall()

        # column명을 key로 가지는 dictionary로 변환
        result = []
        for row in rows:
            tmp = dict()
            for i in range(len(row)):
                tmp[cur.description[i].name] = row[i]
            result.append(tmp)

        # DB 연결 종료
        conn.close()
        result = pd.DataFrame(result)

        return result

    def loc_tracer(df, euid):
        """
        단말기의 위치를 지도에 mapping
        input : df (dataframe), euid (str)
        output : folium 객체
        """

        lat_list = df[df['euid'] == euid]['lbs_lat'].astype(float)
        lng_list = df[df['euid'] == euid]['lbs_lng'].astype(float)
        company_nm_list = df[df['euid'] == euid]['company_nm']
        warranty_nm_list = df[df['euid'] == euid]['warranty_nm']
        updated_at_list = df[df['euid'] == euid]['updated_at']
        cell_id_list = df[df['euid'] == euid]['cell_id']

        data = pd.DataFrame({'lat': lat_list, 'lon': lng_list, 'company_nm': company_nm_list, \
                             'warranty_nm': warranty_nm_list, 'updated_at': updated_at_list, \
                             'cell_id': cell_id_list})

        m = folium.Map(location=[np.average(lat_list), np.average(lng_list)], tiles='OpenStreetMap', zoom_start=5)

        for i in range(0, len(data)):
            folium.Marker([data.iloc[i]['lat'], data.iloc[i]['lon']], \
                          popup=('위도: ' + str('{0: .4f}'.format(data.iloc[i]['lat'])) + '<br>' \
                                                                                        '경도: ' + str(
                              '{0: .4f}'.format(data.iloc[i]['lon'])) + '<br>' \
                                                                        '업체명: ' + str(
                              data.iloc[i]['company_nm']) + '<br>' \
                                                            '담보물명:' + str(data.iloc[i]['warranty_nm']) + '<br>' \
                                                                                                         '보고일시:' + str(
                              data.iloc[i]['updated_at']) + '<br>' \
                                                            'Cell ID:' + str(data.iloc[i]['cell_id']) + '<br>' \
                                 )).add_to(m)

        return m