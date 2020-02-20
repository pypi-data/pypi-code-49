import sys
sys.path.append('../../ccai')

from ccai.client import Client

def test_create_smart_order():
  #  create smart order that will
  #  entry with market order
  #  set take-profit targets at 8% profit with 40% of amount and 15% with 60% of amount
  #  set stop-loss at 10%

  client = Client('a1cb94dab42cd389ce7327a147a5acb4bc92fc66207b09a105ade2e186025239a51572cab8bcb0f5103cbe2115e462846ad721ae5ebf947d2ddfde4172352775ac8ca97ec6994b3abc1aee1169327bf97feca9abe7ceee84a7f8f2b7057b21432362e403ab59874615ee7be01ae4ea93a3fd977095bb3bad97dcc0ec1e9a7633c4b2e7e6839b6712f73666f46e5c4041a633ceab2702ca235fa5f588eac059608cb3b8546a248a7ff3ec6521d3d89f8246baa3ba87d3a8641c99d29b3f37ab0d70550b97b6ca079b54f52fff14900e78a7e932fe22d2bfa2778a956477aab88adfa883c09b2cf291f7c7630bbbc6c60ba9c40edd700796668ed916455b46699c',
                  '5ded5307240b81f3012372de')
  smart_order = {
    "marketType": 1,  # 0 - spot, 1 - futures
    "pair": "BTC_USDT",
    "stopLoss": 10.0,  # 10% loss
    "stopLossType": "limit",  # will place stop-limit or stop-market for stop-loss
    "leverage": 125,  # leverage
    "waitingEntryTimeout": 100,   # if didnt get in entry for 100 seconds - cancel SM
    "activationMoveStep": 1,      # move activatePrice 1% closed
    "activationMoveTimeout": 5,   # waiting 5 seconds before moving activatePrice
    "entryOrder": {
      "side": "buy",
      "orderType": "market",
      "activatePrice": 9950,
      "entryDeviation": 15,
      "type": 0,  # not using yet, just place 0
      "amount": 0.001  # btc amount (after leverage)
    },
    "exitLevels": [
      {
        "price": 8, # 8% profit
        "amount": 40, # 40% from entry
        "type": 1, # 1 - means amount and price is in percentage
        "orderType": "limit"
      }
    ]
  }
  response = client.create_order(params=smart_order)
  print(response)

test_create_smart_order()

