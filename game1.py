import time
import random
import json
import sys
#import keyboard
effort = 0
index = 0.0
result = ""
current_day = ""
days = ["monday","tuesday","wednsday","thursday","friday","saturday","sunday"]
unlocked_local = {}
guide = 'Guide: '

class Player():
    player_list =[] 
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.strgth = 5
        self.spd = 5
        self.deff = 0
        self.xp = 0
        self.level = 0
        self.levelreq = 1000
        self.money = 0
        self.statpnt = 0
        self.intro = 0
        self.day = 0
        self.locations = []
        self.bag = []
        self.x = fland.spawny
        self.y = fland.spawny
        self.z = fland.spawnz
    def level_up(self, xp):
        if self.xp >= self.levelreq:
            self.statpnt += round(self.level / 2)
            self.xp = self.xp - self.xp
            self.levelreq += self.levelreq
    
    def add_item(self, item):
        self.bag.append(item)
        
    def use_item(self, item_name):
        for item in self.bag:
            if item.name.lower() == item.name.lower():
                item.use(self)
                self.bag.remove(item)
                break
            else:
                print("item not found")
        
    def save_to_file(self):
        global result
        data = {
            "name": self.name,
            "hp": self.hp,
            "strgth": self.strgth,
            "spd": self.spd,
            "deff": self.deff,
            "xp": self.xp,
            "level": self.level,
            "levelreq": self.levelreq,
            "statpnt": self.statpnt,
            "intro": self.intro,
            "day": self.day,
            "money": self.money
        }
        with open("players.json", "w") as file:
            json.dump(data, file)
        Player.player_list.append(self.name)
        bag_data = { #item, damage
        
        }
        result = "game saved."
    @classmethod
    def load_save(cls): #cls refers to class itself, this way we can pass multiple players thru simce cls is essentally equal to the current instance of self
        global unlocked_local
        try:
            with open("players.json", "r") as file:
                load_attr = json.load(file)
                load_player = cls(name=load_attr["name"])
                load_player.hp = load_attr["hp"]
                load_player.strgth = load_attr["strgth"]
                load_player.spd = load_attr["spd"]
                load_player.deff = load_attr["deff"]
                load_player.xp = load_attr["xp"]
                load_player.level = load_attr["level"]
                load_player.levelreq = load_attr["levelreq"]
                load_player.statpnt = load_attr["statpnt"]
                load_player.intro = load_attr["intro"]
                load_player.day = load_attr["day"]
                load_player.money = load_attr["money"]
                #load_inventory =
                Player.player_list.append(cls(load_attr["name"]))
                return load_player 
        except FileNotFoundError as nferror:
            print("no players created")  
            game()   
            
    @property
    def pos(self):
        return self.x, self.y, self.z

class Hostile():
    hostile = True
    def __init__(self):
        self.name = Hostile
        self.hp = 25
        self.atk = random.randint(1,3)
        
        
    def attack_player():
        return

class Item():
    def __init__(self, name, price, points, effect):
        self.name = name
        self.price = price
        self.points = points
        self.effect = effect
    
    

    def use(self,player):
        active = False
        if self.effect:
            self.effect(player, self.points, *active)

class Weapon():
    def __init__(self, name, dmg, price):
        self.name = name
        self.dmg = dmg
        self.price = price

def game():
    main()
    player.add_item(hp_pot)
    player.hp -= 50
    intro()

"""world gen"""

class MakeWorld():
    def __init__(self, name, min_sizex, max_sizex, min_sizey, max_sizey, spawnx, spawny, spawnz):
        self.name = name
        self.min_sizex = min_sizex
        self.max_sizex = max_sizex
        self.min_sizey = min_sizey
        self.max_sizey = max_sizey
        self.spawnx = spawnx
        self.spawny = spawny
        self.spawnz = spawnz
        self.result = result
        self.effort = effort
    
    def left(self, player):
        global effort, result
        if player.x >= self.min_sizex:
            player.x -= 1   
        elif player.x <= self.min_sizex: #replace static max size with makeworld max size
            result = "\nlooks dangerous, im not going further\n"
            player.x = self.min_sizex
            effort = effort + 1
            if effort >= 5:
                player.intro = 2

    def right(self, player):
        global result, effort
        if player.x <= self.max_sizex:
            player.x += 1
        elif player.x >= self.max_sizex: 
            result = "\nlooks dangerous, im not going further\n"
            player.x = self.max_sizex
            effort = effort + 1
            if effort >= 5:
                player.intro = 2    

    def up(self, player):
        global result, effort
        if player.y <= self.max_sizey:
            player.y += 1
        elif player.y >= self.max_sizey:
            result = "\nlooks dangerous and its cold, im not going further\n"
            player.y = self.max_sizey
            effort = effort + 1
            if effort >= 5:
                player.intro = 2    

    def down(self, player):
        global result, effort
        if player.y >= self.min_sizey:
            player.y -= 1
        elif player.y <= self.min_sizey:
            result = "\nlooks dangerous, im not going further\n"
            player.y = self.min_sizey
            effort = effort + 1
            if effort >= 5:
                player.intro = 2
    def generate_world(self):
        global index
        while True:
            x1 = []
            y1 = []
            x2 = []
            y2 = []
            x1.append(random.randint(self.min_sizex, self.max_sizex))
            x2.append(random.randint(self.min_sizey, self.max_sizey))
            y1.append(random.randint(self.min_sizey, self.max_sizey))
            y2.append(random.randint(self.min_sizex, self.max_sizex))
            index = index + 0.1
            index = int(index)
            print(f"{index}% complete")
            if index == 100:
                break

        with open("world_gen.json", "w") as file:
            json.dump(x1, file)
            json.dump(x2, file)
            json.dump(y1, file)
            json.dump(y2, file)
class Dungeon(): #spawn in world
    def __init__(self):
        return

"""item effects"""
def hp_effect(player, points):
    if player.hp <= 100:
        while points >= 0 and player.hp <= 100:
            if player.hp >= 100 or points <= 0:
                print("health full")
                break
            else:
                player.hp += 1
                points -= 1
def spd_effect(player, points, active):
    if active == False:
        player.spd += 3
        active = True
        x = player.x + 5
        y = player.y + 5
        x2 = player.x - 5
        y2 = player.y - 5
    if player.x == x or player.y == y or player.x == x2 or player.y == y2:
    
        player.spd -= 3
        active = False

"""places"""

def main():
    global player
    while True:
        exist = input("Load save? ")
        exist = exist.lower()
        if "y" in exist:
            player = Player.load_save()
            locations_update()
            break
        elif "n" in exist:
            play_name = input("name? ")
            player = Player(play_name)
            break
        else:
            print("yes or no.")

def intro():
    
    palace_actions = {
        "explore": travel,
        "status": status,
        "mirror": check_self,
        "level":lambda:print(player.level),
        "points": point_allocate,
        "save":player.save_to_file,
        "players":lambda:print(Player.player_list),
        "calendar":weekdays,
        "shop": store, 
        "sleep": rest,
        "view bag": view_bag,
        "exit":sys.exit,
        "help":lambda:print(f"your actions are:\nexplore, status, sleep\nmirror, level, points\nsave, players, calendar\nexit")
    }
    if player.intro == 0:
        player.locations = []
        print(f"\n\n{guide}welcome to the woods, here is home.\nthis is where you can see your stats,\nlevel up, look yourself over, and explore\n")
        print(f"\n{guide}you can summon yourself back anytime using 'palace'\nbut that doesnt work in a fight\n")
        player.intro = 1
    else:
        phrase = random.randint(1,20)
        print(guide_list_1[phrase])
        
    while True:
        prompt =input("\nwhat would you like to do?\n>>>")
        prompt = prompt.lower()
        xcute = palace_actions.get(prompt)
        if xcute:
            xcute()

def travel():
    global unlocked_local
    locations_update()
    while True:
        print(f"\nunlocked locations: {player.locations}\n")
        prompt = input("\nwhere to?\n>>>")
        prompt = prompt.lower()
        xcute = unlocked_local.get(prompt)
        if xcute:
            xcute()

def store():
    mon_items = { #from intro 0-1, new items will be added from 2-3.
        
        }
    if player.day == 0 or player.day == 2:
        return #days decide the price/quality of items

def freeland():
    arg = ''
    freeland_actions = {
        "west":lambda:fland.left(player),
        "east":lambda: fland.right(player),
        "north":lambda: fland.up(player),
        "south":lambda: fland.down(player),
        "w":lambda: fland.up(player),
        "a":lambda: fland.left(player), #improve movement with keyboard.is_pressed()
        "s":lambda: fland.down(player),
        "d":lambda: fland.right(player),
        "pos":lambda:print(player.pos),
        "position":lambda:print(player.pos),
        "location":lambda:print(player.pos),
        "palace":intro,
        "view-bag":view_bag,
        f"use {arg}":lambda:player.use_item(prompt)
    }
    print("\nexplore in any direction!\nsyntax: west\n")
    while True:
        prompt = input("\n>>>")
        prompt = prompt.lower()
        if ' ' in prompt:
            prompt, arg = prompt.split(' ')
        xcute = freeland_actions.get(prompt)
        if xcute:
            xcute()
            if result:
                print(result)
                result = ''
def darkwood():
    return
    
    player.intro = 3   

"""npc phrase"""
guide_list_1 = ["\n\nwelcome back!\nask me for help if you cant figure things out\n",
                "\n\nhow was your trip?\nlooks great out there\n\n",
                "\n\nwhile you were gone i went ahead and picked up around the store\n",
                "\n\nharsh weather today, eh?\n",
                "\n\nthere are a lot of adventurers around.\nthe further you go the more sparce they get\n",
                "\n\nrumor is, on the edge of the field\nthere is a barrier preventing people from going further\nmaybe someone stubborn enough needs to have a go\n",
                "\n\nfun fact, its a controversial opinion but\nthis world is a giant orb, and we are in the center on its surface\nmeaning the further out in any direction you go, the more there is to explore\n",
                "\n\nthe one before you was quite nice\njust like you are\n",
                "\n\nif you want to get stronger, you have to fight enemies.\ngear can only get you so far\n",
                "\n\nbe careful of the edge, if are you arent ready to venture passed\nthen you could be killed or worse!\n",
                "\n\napparently theres a deity far passed these fields and forest\nif you encounter it, its best to run. apparently it doesnt kill\nit just wipes beings away from existance\n",
                "\n\ndid you know you could encounter other adventurers out in the wild\nif they happen to die, that loot is finders keepers!\n",
                "\n\nharming other humans can bring bad karma, its a balance of luck and gear to maintain\n",
                "\n\nyou can always see what the shop has in stock for gear!\nwe dont gather material other than the animals\nbut the shop has a crafting area for whatever you may find\n",
                "\n\nthere are many gods, above all though is soj, the god of favor.\nif you meet him you might just find good luck!\n",
                "\n\nabandoned stuctures litter the freelands, they are that common in other places\n",
                "\n\noutside of the freelands are 9 other unique areas!\nive only been to the third area, wasteland\n",
                "\n\ni dont like to spoil the fun, so as you progress\nill tell you more about the new things you discover!\n",
                "\n\nif you ever need to heal, you should sleep\nluna(god of dreams) restores all physical injuries during the night.\n\nnot mental ones though\n",
                "\n\nits been told that each time a god dies\na human is blessed with a portion of their power\n"
]

"""actions"""

def status():
    print(f"\ncoins: {player.money}\nhealth: {player.hp}\nstr: {player.strgth}\nspeed: {player.spd}\ndef: {player.deff}\nexp: {player.xp}\nlevel: {player.level}\nstat points: {player.statpnt}\n")
    
def check_self():
    if player.hp <= 100 and player.hp >= 75:
        print("\nnot too shabby.\n")
    elif player.hp <= 75 and player.hp >= 50:
        print("\nmaybe i need to rest.\n")
    elif player.hp <= 50 and player.hp >= 20:
        print("\ni cant feel my skin.\n")
    elif player.hp <= 3:
        print("\n....\n")

def point_allocate():
    return #for stats

def rest():
    global result
    if player.day <= 6:
        player.day += 1
        if player.day > 6:
            player.day = 0
    while player.hp <= 100:
        player.hp += 1
    result = "you are well rested"    

def view_bag():
    index = 0
    for item in player.bag:
        print(item.name)
        if index >= len(player.bag):
            break
        else:
            index += 1
        
"""movement"""

"""update"""

def weekdays():
    global current_day
    if player.day > 6:
        player.day = 0
    current_day = days[player.day]
    print(current_day) #saves day progress so each boot isnt a complete restart

def locations_update(): #we dont use var = set(player.locations) cause the original will grow every update
   if player.intro == 0: #its more efficient to check for duplicates and pass
       player.locations = []
   elif player.intro == 1:
       player.locations.append("The Woods")
       player.locations.append("Freeland")
       unlocked_local.update({"the woods": intro, "freeland":freeland})
   elif player.intro == 2:
       player.locations.append("Darkwood")
       unlocked_local.update({"darkwood":darkwood})
   player.locations = list(set(player.locations))   

"""item create"""
screen_clear = f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
fland = MakeWorld("freeland", -100, 100, -100, 100, 0, 0, 0) 
print('building world') 
fland.generate_world()
hp_pot = Item("H-pot", 25, 20, effect=hp_effect)
game() 
#player.use_item('H-pot')

