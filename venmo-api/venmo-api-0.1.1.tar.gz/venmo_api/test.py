from venmo_api import Client

venmo = Client("Bearer da9c0bb555605ca51ecebc4788424b8eb2f318c8970f9e4d3f78adeece0bd842")

# users = venmo.user.get_user_friends_list(user_id="1667787298701312020")
# venmo.payment.send_money(1, "dots", "2353116875849728644")
# users = venmo.user.search_for_users("mark mohades")
users = venmo.user.get_user_transactions(user_id="1667787298701312020")
# users = venmo.user.get_user("1667787298701312020")
# print(users)
for user in users:
    print(user)
#

