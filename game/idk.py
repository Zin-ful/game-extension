import time
import random
import json
import sys
#import keyboard
counter = 0
#debug = input("trees >>>")
#debug = int(debug)
effort = 0
index = round(0.0,1)
result = ""
current_day = ""
days = ["monday","tuesday","wednsday","thursday","friday","saturday","sunday"]
unlocked_local = {}
guide = 'Guide: '
Throttle = True
limit = 0.0001

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

class MakeHostile():
    hostile = True
    def __init__(self, min_sizex, max_sizex, min_sizey, max_sizey, event_count, name, lvl, hp, atk, spd, deff):
        self.min_sizex = min_sizex
        self.max_sizex = min_sizex
        self.min_sizey = min_sizex
        self.max_sizey = min_sizex
        self.event_count = event_count
        self.name = name
        self.lvl = lvl
        self.hp = hp + random.randint(0, lvl)
        self.atk = atk + random.randint(0, lvl)
        self.spd = spd + random.randint(0, lvl)
        self.deff = deff + random.randint(0, lvl)
        self.h_coord_listx =[]
        self.h_coord_listy =[]
        self.hostile_spawn =[]


    def attack_player():
        return
    
    
    def generate_hostilemap(self):
        global counter
        self.h_coord_listx =[]
        self.h_coord_listy =[]
        while counter < self.event_count: #create general max to increase variety
            self.h_coord_listx.append(random.randint(self.min_sizex, self.max_sizex))
            self.h_coord_listy.append(random.randint(self.min_sizey,self.max_sizey))
            if Throttle:
                time.sleep(limit)
            counter += 1
            self.h_coord_listx = list(set(self.h_coord_listx))
            self.h_coord_listy = list(set(self.h_coord_listy))
            percent_complete = (counter / self.event_count) * 100  # Calculate dynamic percent
            print(f"{percent_complete:.2f}% complete")  # Print with two decimal places for precision
        data = [{"x": self.h_coord_listx, #for _ in range is essentally saying to repeate this loop this many times ignoring the for variable
            "y": self.h_coord_listy}]
        with open("hostile_gen.json", "w") as file:
            json.dump(data, file)
            
    def generate_hostile(self):
        hostile_rangex = len(self.h_coord_listx)
        hostile_rangey = len(self.h_coord_listy)
        hostile_spwn_crdsx = random.sample(self.h_coord_listx, hostile_rangex)
        hostile_spwn_crdsy = random.sample(self.h_coord_listy, hostile_rangey)
        self.hostile_spwn = list(zip(hostile_spwn_crdsx, hostile_spwn_crdsy))
        with open("tree_spwn.json", "r") as file:
            tree_chk_spwn = json.load(file)
            for spwn in self.hostile_spwn:
                if spwn in tree_chk_spwn:
                    self.hostile_spwn.remove(spwn)
        data = [{"hostile_spwn": self.hostile_spwn}]
        with open("hostile.json", "w") as file:
            json.dump(data, file)
    

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
    intro()

"""world gen"""

class MakeWorld():
    def __init__(self, name, min_sizex, max_sizex, min_sizey, max_sizey, spawnx, spawny, spawnz, event_count):
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
        self.event_count = event_count #generated obsticals
        self.event_coord = []
        self.t_coord_listx = []
        self.t_coord_listy = []
        self.tree_spwn = []
    def left(self, player):
        global effort, result
        if player.x >= self.min_sizex:
            player.x -= 1   
        elif player.x <= self.min_sizex: #replace static max size with makeworld max size
            result = "\nlooks dangerous, im not going further\n"
            player.x += 1
            effort = effort + 1
            if effort >= 5:
                player.intro = 2
        if (player.x, player.y) in self.tree_spwn:
            result = result = f"\ndamn tree in my way at y: {player.x}, {player.y}"
            player.x += 1
        for hostile in hostiles:
            hostile_check(player, hostile)
                    
  

    def right(self, player):
        global result, effort
        MakeHostile.hostile_check()
        if player.x <= self.max_sizex:
            player.x += 1
        elif player.x >= self.max_sizex: 
            result = "\nlooks dangerous, im not going further\n"
            player.x -= 1
            effort = effort + 1
            if effort >= 5:
                player.intro = 2
        if (player.x, player.y) in self.tree_spwn:
            result = f"\ndamn tree in my way at y: {player.x}, {player.y}"
            player.x -= 1
            for hostile in hostiles:
                hostile_check(player, hostile)
            
    def up(self, player):
        global result, effort
        if player.y <= self.max_sizey:
            player.y += 1
        elif player.y >= self.max_sizey:
            result = "\nlooks dangerous and its cold, im not going further\n"
            player.y -= 1
            effort = effort + 1
            if effort >= 5:
                player.intro = 2
        if (player.x, player.y) in self.tree_spwn:
            result = f"\ndamn tree in my way at y: {player.x}, {player.y}"
            player.y -= 1
            for hostile in hostiles:
                hostile_check(player, hostile)
        
    def down(self, player):
        global result, effort
        if player.y >= self.min_sizey:
            player.y -= 1
        elif player.y <= self.min_sizey:
            result = "\nlooks dangerous, im not going further\n"
            player.y += 1
            effort = effort + 1
            if effort >= 5:
                player.intro = 2
        if (player.x, player.y) in self.tree_spwn:
            result = f"\ndamn tree in my way at y: {player.x}, {player.y}"
            player.y += 1
        for hostile in hostiles:
            hostile_check(player, hostile)
        
    def generate_treemap(self):
        global counter
        self.t_coord_listx =[]
        self.t_coord_listy =[]
        while counter < self.event_count: #create general max to increase variety
            self.t_coord_listx.append(random.randint(self.min_sizex, self.max_sizex))
            self.t_coord_listy.append(random.randint(self.min_sizey,self.max_sizey))
            if Throttle:
                time.sleep(limit)
            counter += 1
            self.t_coord_listx = list(set(self.t_coord_listx))
            self.t_coord_listy = list(set(self.t_coord_listy))
            percent_complete = (counter / self.event_count) * 100  # Calculate dynamic percent
            print(f"{percent_complete:.2f}% complete")  # Print with two decimal places for precision
        data = [{"x": self.t_coord_listx, #for _ in range is essentally saying to repeate this loop this many times ignoring the for variable
            "y": self.t_coord_listy}]
        with open("tree_gen.json", "w") as file:
            json.dump(data, file)
            
    def generate_tree(self):
        tree_rangex = len(self.t_coord_listx)
        tree_rangey = len(self.t_coord_listy)
        tree_spwn_crdsx = random.sample(self.t_coord_listx, tree_rangex)
        tree_spwn_crdsy = random.sample(self.t_coord_listy, tree_rangey)
        self.tree_spwn = list(zip(tree_spwn_crdsx, tree_spwn_crdsy))
        data = [{"tree_spwn": self.tree_spwn}]
        with open("tree_spwn.json", "w") as file:
            json.dump(data, file)
    
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
        print("1. Play\n2. Config\n")
        exist = input(">>>")
        exist = exist.lower()
        if "p" in exist or "1" in exist:
            print("load game?")
            exist = input(">>>")
            exist = exist.lower()
            menu(exist)
            if result:
                print(result)
        elif "c" in exist or "2" in exist:
            print("select with numbers and arguments")
            print("\n1. throttle (true, false) (info)\n")
            exist = input(">>>")
            exist = exist.lower()
            config(exist)

def config(option):
    global Throttle
    if "1 false" in option:
        Throttle = False
    elif "1 info" in option:
        print("throttle controls how fast the game loads\nsetting to false will set the speed to your cpu")
    else:
        Throttle = True
            
def menu(option):
    global player, play_name
    if "y" in option:
        player = Player.load_save()
        locations_update()
        game()
    elif "n" in option:
        play_name = input("name? ")
        player = Player(play_name)
        game()
    else:
        result = "yes or no."
        return result
        
def intro():

    palace_actions = {
        "explore": travel,
        "chat": chat_guide,
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
        phrase = random.randint(0,249)
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
    print("generating world")
    fland.generate_treemap()
    fland.generate_tree()
    print("generating enemies")
    fland_hostile_rouge.generate_hostilemap()
    fland_hostile_rouge.generate_hostile()
    fland_hostile_scavanger.generate_hostilemap()
    fland_hostile_scavanger.generate_hostile()
    player.day += 1
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
        global result
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

def battle(player, hostiles): 
    cache_lvl = hostiles.lvl
    cache_hp = hostiles.hp
    cache_deff = hostiles.deff
    recent_atkhos = False
    recent_atkplr = False
    while True:
        cache_atk = hostile.atk + random.randint(0,mon_lvl)
        cache_spd = hostile.spd + random.randint(0,mon_lvl)
        print(f"\n\n{player.name}:\n{player.hp}\n{player.strgth}\n{player.spd}\n{player.deff}\n")
        print("\nattack? defend? or run?n")
        plr_input = input("\n>>>")
        if "a" in plr_input.lower() or "1" in plr_input:
            if player.spd > cache_monspd:
                if recent_atkplr == False:
                    recent_atkplr = True
                    cache_monhp -= plr_atk
                    print(f"{player.name} attacked for {player.strgth} damage.\n{hostile.name} has {cache_hp} left.")
                else:
                    recent_atkplr = False
                    plr_hp -= cache_monatk
                    print(f"{player.name} got attacked for {cache_atk} damage.\n{player.name} has {player.hp} left.")
            elif player.spd <= cache_monspd:
                if recent_atkmon == False:
                    recent_atkmon = True
                    plr_hp -= cache_monatk
                    print(f"{player.name} got attacked for {cache_atk} damage.\n{player.name} has {player.hp} left.")
                else:
                    recent_atkmon = False
                    cache_monhp -= plr_atk
                    print(f"{player.name} attacked for {player.strgth} damage.\n{hostile.name} has {cache_hp} left.")
        if player.hp <= 0:
            print(f"{plr_nm} suffered a horrible death at the hands of\nball crusher™ and got his balls crushed")
            break 
        elif cache_monhp <= 0:
            print(f"{plr_nm} vanquished the angel dooming this world")
            break

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
                "\n\nthere are many gods, above all though is lucy, the god of favor.\nif you meet him you might just find good luck!\n",
                "\n\nabandoned stuctures litter the freelands, they are that common in other places\n",
                "\n\noutside of the freelands are 9 other unique areas!\nive only been to the third area, wasteland\n",
                "\n\ni dont like to spoil the fun, so as you progress\nill tell you more about the new things you discover!\n",
                "\n\nif you ever need to heal, you should sleep\nluna(god of dreams) restores all physical injuries during the night.\n\nnot mental ones though\n",
                "\n\nits been told that each time a god dies\na human is blessed with a portion of their power\n"
                "\n\nheard any good stories from adventurers lately?\ni love a good tale of bravery\n",
                "\n\nthe stars look brighter at the edge of the fields.\n'science' says its cause were in a different\nspot in the galaxy, whatever that means\n",
                "\n\nsometimes, if your quiet, you can listen.\nto adventurers leak information\nkeep your ears open\n",
                "\n\nif you're looking for crafting material, try slaying monsters\n",
                "\n\ndid you know there's a special tree in the forest\nthat glows blue under the full moon?\n",
                "\n\nadventurers seem restless today.\nits said the day can effect your luck\n",
                "\n\napparently theres a shop around here.\nmaybe you should try it\n",
                "\n\nthe gear you find here might not look fancy,\nbut it’s built to last\n",
                "\n\nlegends speak of a god of gods,\nbut no one who’s seen it has ever returned\n",
                "\n\nonce you start exploring, you'll realize\nhow small the village really is\n",
                "\n\nif you want to learn about crafting,\nask the shop keep\n",
                "\n\npeople talk about hidden passageways in the wasteland.\nmaybe there's a way to unlock them\n",
                "\n\ni dont talk about it often, but,\ntheres a god above gods.\nthose who meet it, dont die, they dont exist\n",
                "\n\ndon’t underestimate the power of kindness.\nit might save your life someday\n",
                "\n\nthere’s a place you can fall into.\nbe careful not to get stuck\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                "\n\nhave you ever wondered why the clouds move faster\nover the freelands?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                "\n\nif you pay the shop keep\nhe might just leak locations of structures",
                "\n\nlook closely at the ground when you travel.\nyou never know what you might stumble upon\n",
                "\n\nif your head is telling you not to explore something\nitd be smart to listen, the ones before you didnt.\n\ni dont remember much about them anymorr\n",
                "\n\nevery now and then, I hear footsteps outside the store.\nbut no one ever goes in\n",
                "\n\nthe enviorment will tell you things.\nsomething might be close\n",
                "\n\nfreeland is unique for how open it is\n",
                "\n\nthe days of the week are important.\nsol, the god of the sun decides these days\nhes powerful enough to expand freeland depending on the day!",
                "\n\nlegends say that the moon has a dark side.\nbut ive never seen the moon turn around, so\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                "\n\nyour wondering about the gods?\nill tell you another time\n",
                "\n\nthere are many gods. the more well known, the more powerful\nwell except for one\n",
                "\n\nthe most common gods and the ones i know are\nthe god of sleep, the sun, the earth, fortune, creation, and erasure\n",
                "\n\nluck is important, it could decide life or death\n",
                "\n\nthe ocean seems endless but apparently\ntheres land on the other side of it\n",
                "\n\nhowd it go out there?\n",
                "\n\nfind anything decent?\nthe shop keep dropped a coin i may or may not have",
                "\n\nwho ever made me, gave me a lot to say.\n",
                "\n\nthe current day can decide a lot\nit’s worth paying attention\n",
                "\n\nsome humans can use magic\nits because someone in their family slayed a god",
                "\n\nif you ever kill a god, you should check the mirror\n",
                "\n\nthe shop has many items\nit grows as you explore",
                "\n\nsome enemies drop items from other areas\ncause thats how walking works",
                "\n\nif you find a broken weapon you might be able to salvage it\n",
                "\n\ndont have much to say, do you?\n",
                "\n\nthe wastelands look far, but sol might help you walk less\n",
                "\n\nit’s rare, but i do things besides waiting to greet you\n",
                "\n\nsome idiot came in here babling about an iphone\n\nwhat?\n",
                "\n\nwatch the patterns in the sand.\nthey might show you the way\n",
                "\n\nsometimes i want to be the generic guide\nwho says things like\n\n'the deeper you go into the caves,\nthe less light reaches you'\n\n but i have pride in my work\n",
                "\n\nevery tool has a purpose, but watching the shop keep be nice\nis like cutting a cake with a hammer\n",
                "\n\npeople say the gods walk among us in disguise.\nbut how would we know?\n",
                "\n\n'some doors are locked for a reason.\nbut that doesn’t mean they shouldn’t be opened'\n\n what a stupid thing to say.\n",
                "\n\nyou brought back food, right?\n",
                "\n\ndarkwoods isnt full of a ton of trees despite the name\nits actually sparse, large trees with very wide leaf-spans\n",
                "\n\nyou sure sleep a lot\n",
                "\n\nwhat even are levels?\n",
                "\n\nyour about as much fun to talk to as a wall\n",
                "\n\nyou see the guy that just left?\nnoone from nowheresville lookin ass\n",
                "\n\nyou think you could find me a wife out there?\n",
                "\n\nthey expand this place every now and then\n",
                "\n\nunlike warping back to the woods (here)\nyou can physically walk from place to place. or not\n",
                "\n\ngods effect all creatures equally.\nfor every human to slay a god and obtain its powers\ntheres a monter whos done the same",
                "\n\nkilling a mortal with a gods power does not bless you with that ability\nits just passed to the next in their family\na real cause for power struggles now that i think about it\n",
                "\n\nsome maniac yellimg about another adver- advortes- ad? i dont know\n",
                "\n\nthe worst guy i know is some.idiot named logan\noh, and his idiot brother jake\n",
                "\n\nyou sure are fun to have a conversation with.\ndont worry, im an empath. i can feel your responses\n",
                "\n\nthe strongest mortals have powers from multiple gods\nfamilies dont start out with them but once\na family member slays a god, the whole family line is blessed\nbut only one can use that power. if multiple are slain\nthen you get a family member with multiple powers\n"
                "\n\nhey, welcome back.\nhow was it out there?\n",
                "\n\nfind anything cool on your trip?\n",
                "\n\nthe shop’s got some new stuff. might be worth a look\n",
                "\n\nlooks like a good day to explore, huh?\n",
                "\n\nif you need supplies, monsters are a good way to find stuff\n",
                "\n\nwhat the hell is a youtube... beef?\nweird ass people, weird ass food.\n",
                "\n\nthe freelands are full of old ruins.\nmight be something useful there\n",
                "\n\npeople still talk about the gods, but who knows if they’re real\n",
                "\n\nthe shop has a crafting station if you need to make anything\n",
                "\n\nnew adventurers always seem to come through here.\nit’s part of the freelands, I guess\n",
                "\n\nyou can get better gear at the shop.\nit won’t look flashy, but it works\n",
                "\n\nthere’s a barrier at the edge of the field.\nmakes you wonder what’s out there\nwell i know, obviously\n",
                "\n\nrumor has it, mortal gods could be among us.\nwho knows, though\n",
                "\n\nthis place feels big, but after a while, it feels small, doesn’t it?\n",
                "\n\namong us?\n",
                "\n\nthe shop grows its inventory as adventurers explore.\nit works out well\n",
                "\n\nsleeping restores your injuries. luna takes care of that while you rest\n",
                "\n\nthere are stories about adventurers meeting gods in the woods.\nit’s probably better to avoid them\n",
                "\n\nluck is always a factor out here.\nsometimes you win, mostly you don’t\n",
                "\n\nthe wastelands are threatening and strange. i’ll tell you about it sometime\n",
                "\n\nif you keep wandering, you’ll usually find something interesting\n",
                "\n\nthe shopkeeper charged me for using his water cup.. why?\n",
                "\n\nif you run into lucy, the god of favor,\nwell…maybe you’ll get lucky\n",
                "\n\nkarma can pile up.\npersonally, i try to stay neutral\n",
                "\n\nfreeland’s open spaces are rare. it’s nothing like other areas\n",
                "\n\nour measuring system? um.. its metric. why?\n",
                "\n\nthe shop has a crafting area. you can put stuff together\n",
                "\n\nthe gods have weird rules and strange powers.\nno one’s really figured them all out\n",
                "\n\nsometimes you’ll hear adventurers whispering about valuable locations.\nit’s worth listening\n",
                "\n\ndid you know we have a sixth sense?\nwe can sense a small area around ourselves\n",
                "\n\nkilling a god could change a lot. it might get a bounty on your head\n",
                "\n\nthe freelands are quiet most of the time. not much happens, but that’s okay\n",
                "\n\nhey, did you see that tree? it looked odd… probably nothing\n",
                "\n\npeople always mention the moons, the sun, and luck.\npeople being me\n",
                "\n\ni finally ripped the tag off this shirt, thank the gods\nwait, tag? i sowed it?\n",
                "\n\ndon’t stress too much about the edge of the fields. take your time\n",
                "\n\nthe shop has a lot of items, and they grow the stock the more you explore\n",
                "\n\npeople here talk about gods and their stories all the time.\nmaybe they’re real, maybe not\nive never met one\n",
                "\n\nevery now and then you’ll find ruins out here.\n",
                "\n\nthe days feel like they mean something. sol, the god of the sun, has that effect\n",
                "\n\nno, im not really sure why items dont break naturally.\nmaybe thats our power haha\n",
                "\n\ni might repeat myself, but you’ll learn them eventually\n",
                "\n\nsome people are sure the gods have had their hands in human lives for centuries.\nyou decide what you believe\n",
                "\n\na traveler talked about a way to summon food without leaving your seat. i didn’t ask further\n",
                "\n\nsomeone was mumbling about 'videos' they watched while resting by the fire. couldn’t follow what they meant\n",
                "\n\na traveler swore by some mechanical transportation that rolled and didn't walk.\ni think i need a drink\n",
                "\n\nthey had this excited look talking about their parchment they called 'the news.' felt off, really\n",
                "\n\nsomeone talked about carrying their 'shining coin book' to barter. What?\n"
                "\n\nThe shopkeep charged me for sitting in a chair this morning.\n",
                "\n\nI spent two hours sweeping because the shopkeep said it looked 'messy.'\n",
                "\n\nHad to clean the storeroom again. Seems like that’s always a task.\n",
                "\n\nThe shopkeep handed me a mop and said it was part of 'meditation.'\n",
                "\n\nWhy is standing idle considered 'poor customer service' by the shopkeep?\n",
                "\n\nI had to clean the path after a breeze. The shopkeep said it was important.\n",
                "\n\nWhy does walking past a door cost me coins according to the shopkeep?\n",
                "\n\nI had to clean broken pathways twice this week because of the shopkeep's requests.\n",
                "\n\nWhy does staring at clouds or taking breaks a taxable activity by the shopkeep?\n",
                "\n\nI patched the roof this morning because of wind and the shopkeep’s insistence.\n",
                "\n\nWhy is repairing random supplies always so tedious and expensive with the shopkeep involved?\n",
                "\n\nThe shopkeep expects me to spend all my time on pointless maintenance.\n",
                "\n\nI cleaned out firewood this morning because the shopkeep said the path would stay better.\n",
                "\n\nThe shopkeep scolded me for 'too much thinking' this morning.\n",
                "\n\nThe shopkeep said that cleaning dust from the pathway would 'ensure good luck.'\n",
                "\n\nSometimes, I wonder if cleaning all these random things is a form of punishment.\n",
                "\n\nI fixed a broken lantern because the shopkeep said no one would come near otherwise.\n",
                "\n\nWhy does the shopkeep always find new things that need 'light maintenance' around here?\n",
                "\n\nToday, I cleaned the fire pit because the shopkeep said it had bad vibes.\n",
                "\n\nEverything I do feels like it has a price attached with the shopkeep watching.\n",
                "\n\nI spent three hours fixing a broken shelf because the shopkeep swore I was the only one who could.\n",
                "\n\nWhy does the shopkeep think that polishing random stones has purpose?\n",
                "\n\nI rearranged random boxes because the shopkeep thought it would look 'more appealing.'\n",
                "\n\nSometimes I think the shopkeep just wants me to never stop doing something.\n",
                "\n\nI swept the front steps because the shopkeep said it would 'improve morale.'\n",
                "\n\nWhy is maintaining flowerbeds apparently a divine duty, according to the shopkeep?\n",
                "\n\nI put away a stack of papers after the shopkeep decided they 'needed organizing.'\n",
                "\n\nI had to fix the campfire because the shopkeep mentioned that 'morale was declining.'\n",
                "\n\nWhy does the shopkeep always manage to tie every random task to luck somehow?\n",
                "\n\nI cleaned out the water barrels because the shopkeep said 'clean water ensures prosperity.'\n",
                "\n\nWhy is patching a random broken window considered a priority by the shopkeep?\n",
                "\n\nThe shopkeep finds a way to make me do the most mundane things seem important.\n",
                "\n\nI swept and cleaned up the toolshed just because the shopkeep wanted it done.\n",
                "\n\nWhy does sweeping always end with the shopkeep finding more ways for me to sweep?\n",
                "\n\nI fixed the paths again this morning because the shopkeep said 'footprints matter.'\n",
                "\n\nToday felt like it was 50% cleaning and 50% cleaning requests from the shopkeep.\n",
                "\n\nI straightened up random logs because apparently it’s a symbolic act of 'organization.'\n",
                "\n\nThe shopkeep believes that taking a few minutes to do nothing is a bad idea.\n",
                "\n\nI trimmed branches near the path because the shopkeep said they were 'off-putting.'\n",
                "\n\nI had to haul extra firewood because apparently I needed to 'maintain seasonal readiness.'\n",
                "\n\nWhy does the shopkeep equate cleaning to luck, fate, and preparation so often?\n",
                "\n\nI patched a hole in the wall just because the shopkeep said it would 'prevent bad omens.'\n",
                "\n\nSometimes I get the feeling that cleaning random things is just a way to pass time.\n",
                "\n\nI made another round clearing dirt from random cracks because the shopkeep said it looked bad.\n",
                "\n\nThe shopkeep had me spend time checking random pathways because 'weather damage can sneak up on you.'\n",
                "\n\nWhy is fixing lanterns always the first thing when things get a bit stormy, according to the shopkeep?\n",
                "\n\nI moved a few crates because apparently the shopkeep thought 'they'd look better there.'\n",
                "\n\nSometimes I clean out random spots just because it feels like I’ll hear about it otherwise.\n",
                "\n\nI dug out debris near the pathway because the shopkeep mentioned it could lead to 'bad weather.'\n",
                "\n\nI replaced some wood panels because the shopkeep mentioned 'basic upkeep ensures survival.'\n",
                "\n\nWhy does sweeping seem to turn into 'ritualistic upkeep' every time the shopkeep is involved?\n",
                "\n\nI fixed broken fences again because it was part of another morning's request from the shopkeep.\n",
                "\n\nWhy does every random broken thing in this area get labeled as urgent maintenance by the shopkeep?\n",
                "\n\nI cleaned some pots this morning after the shopkeep said they would 'improve readiness.'\n",
                "\n\nI made another round organizing things just because the shopkeep thought 'things should always align.'\n",
                "\n\nWhy does clearing dust always involve needing some kind of justification from the shopkeep?\n",
                "\n\nI spent the afternoon cleaning stone paths after yet another request from the shopkeep.\n",
                "\n\nSometimes I think the shopkeep just wants me to always stay busy.\n",
                "\n\nI spent another hour with firewood because of a random request from the shopkeep.\n",
                "\n\nI repaired another broken shelf because it 'could affect future morale,' or so the shopkeep said.\n",
                "\n\nWhy does it always come back to basic repairs with the shopkeep? Like fixing wood and stone.\n",
                "\n\nI spent time clearing random supplies because the shopkeep prefers 'clean aisles.'\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n",
                f"\n\nwelcome back!\nits a fine {current_day}, isnt it?\n"
]



"""actions"""

def status():
    print(f"\ncoins: {player.money}\nhealth: {player.hp}\nstr: {player.strgth}\nspeed: {player.spd}\ndef: {player.deff}\nexp: {player.xp}\nlevel: {player.level}\nstat points: {player.statpnt}\n")

def chat_guide():
    phrase = random.randint(0,195)
    print(guide_list_1[phrase])

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

"""utility"""

def hostile_check(player, hostiles):
    if (player.x, player.y) in hostile.hostile_spwn:
        battle()
        if player.hp == 0:
            print("you lossed")

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
fland = MakeWorld("freeland", -100, 100, -100, 100, 0, 0, 0, 1000)#debug
hp_pot = Item("H-pot", 25, 20, effect=hp_effect)
fland_hostile_rouge = MakeHostile(-100, 100, -100, 100, 1000, "rouge", 1, 100, 10, 5, 0)
fland_hostile_scavanger = MakeHostile(-100, 100, -100, 100, 1000, "scavanger", 1, 100, 10, 5, 0)
hostiles = [fland_hostile_rouge, fland_hostile_scavanger]
main()
game() 

#player.use_item('H-pot')
