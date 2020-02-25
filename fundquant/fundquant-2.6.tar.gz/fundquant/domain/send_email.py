import pymysql


class SendEmail:
    @staticmethod
    def get_email_list():
        email_list = []

        conn = pymysql.connect(user='root', password='', database='quant', charset='utf8')
        cursor = conn.cursor()

        sql = "select username, email from send_email where monitor=1"

        cursor.execute(sql)
        conn.commit()

        for item in cursor.fetchall():
            username = item[0]
            email = item[1]

            email_list.append(email)

        return email_list


if __name__ == '__main__':
    print(SendEmail.get_email_list())
