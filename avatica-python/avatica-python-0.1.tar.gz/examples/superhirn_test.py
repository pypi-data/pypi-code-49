from requests.auth import HTTPDigestAuth
import avatica

connection = avatica.connect(url="http://localhost:8989", max_retries=3,
                             auth=HTTPDigestAuth('username', 'password'))

cursor = connection.cursor()
cursor.execute("SELECT * FROM orders WHERE retailer_code = 'aitiantian'")
for row in cursor:
    print(row)