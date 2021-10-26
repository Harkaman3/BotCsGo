import requests
import json
from SecKey import Key
from pprint import pprint
import re

ListItems = requests.get('https://market.csgo.com/api/v2/items?key=' + Key)
price = ListItems

ListItems = ListItems.text 

ItemId = json.loads(ListItems)

items = []
price_array = []
market_hash_name = []
instance_id = []
class_id = []
for item  in ItemId['items']:
    items.append(item['item_id'])

for item  in ItemId['items']:
    class_id.append(item['classid'])

for price  in ItemId['items']:
    price_array.append(price['price'])

for name in ItemId['items']:
    market_hash_name.append(name['market_hash_name'])

for Id in ItemId['items']:
    instance_id.append(Id['instanceid'])

sell_item_ifo = requests.get('https://market.csgo.com/api/SearchItemByName/'+ market_hash_name[1] +'/?key='+Key)
sell_item_ifo = sell_item_ifo.text
sell_item_ifo = json.loads(sell_item_ifo)

#pprint(sell_item_ifo)
pprint (items)
pprint (price_array)
pprint (class_id)
pprint (instance_id)
pprint (market_hash_name)
# print(Names)
# for name in Names:
#     a = re.search(r"\(.*\)", name)
#     print(a.group(0))
sell_item_price = sell_item_ifo['list'][0]['price']
print ('lowest price is: ',sell_item_price)

autobuy = requests.get('https://market.csgo.com/api/BuyOffers/'+ class_id[1] + instance_id[1] +'/?key='+ Key)
autobuy = autobuy.text
autobuy = json.loads(autobuy)

autobuy = autobuy['best_offer'][0] #не работает

if price_array[1] != autobuy + 100:
    sell_item_price[1] = sell_item_price[1] - 1
    requests.get('https://market.csgo.com/api/SetPrice/'+ items[1]+'/' + sell_item_price[1] +'/?key='+ Key)
    