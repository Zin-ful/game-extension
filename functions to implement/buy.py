import random
current_shop = {}
money = 100
shop_dict = {"sword":10, "dagger": 5, "chestplate": 10, "leather": 1,"water": 0, "meat": 2, "potion of idk": 50, "stick": 2, "spyglass": 25, "zins 'services'": 100}
shop_list = shop_dict.keys()
print("what item do you want?")
for _ in range(5):
    item, price = random.choice(list(shop_dict.items()))
    #current_shop.update({item: price}) #use for multiple items at once
    current_shop[item] = price #better way for single items
for key, value in current_shop.items():
    print(key, " ", value)
inp = input(">>>")
to_buy = current_shop[inp]
money -= to_buy
print(money)
