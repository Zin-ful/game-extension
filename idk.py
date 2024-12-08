import time
import random
import json
import sys
effort = 0
result = ""
current_day = ""
unlocked_local = {}
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
        self.x = 0
        self.y = 0 #can add these to save file to maintain position on larger adventures
        self.z = 0
    def level_up(self, xp):
        if self.xp >= self.levelreq:
            self.statpnt += round(level / 2)
            self.xp = self.xp - self.xp
            self.levelreq += self.levelreq
    def bag(self):
        inventory = {
        
        }
    
    
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
        
class MakeWorld():
    def __init__(self, max_size):
        return #populate with structures, obsticals
        
class Dungeon(): #spawn in world
    return
        
class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
class Weapon():
    def __init__(self, name, dmg, price):
        self.name = name
        self.dmg = dmg
        self.price = price
        
        
def game():
    main()
    intro()
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
        "save":lambda:player.save_to_file,
        "players":lambda:print(Player.player_list),
        "calendar":lambda:print(current_day),
        "shop": store   
        "sleep": rest,  
        "exit":sys.exit,   
        "help":lambda:print(f"your actions are:\nexplore, status, sleep, mirror, level, points, save, players, calendar, exit")
    }
    if player.intro == 0:
        player.locations = []
        print("welcome to the woods, here is home.\nthis is where you can see your stats,\nlevel up, look yourself over, and explore")
        print("you can summon yourself back here anytime using 'palace'\nbut that doesnt work in a fight")
        player.intro = 1
    else:
        print("welcome back! ask me for help if you cant figure things out")
        
    while True:
        prompt =input("what would you like to do?\n>>>")
        prompt = prompt.lower()
        xcute = palace_actions.get(prompt)
        if xcute:
            xcute()
def travel():
    global unlocked_local
    locations_update()
    while True:
        print(f"unlocked locations: {player.locations}")
        prompt = input("where to?\n>>>")
        prompt = prompt.lower()
        xcute = unlocked_local.get(prompt)
        if xcute:
            xcute()
def store():
    mon_items = { #from intro 0-1, new items will be added from 2-3
        "health potion": 0,
        "speed potion": 0,
        "defense potion": 0, #temporary, assign to item class
        "oak staff": 0,
        "leather":0  #make craft func.
        }
    if player.day == 0 or player.day == 2:
        return #days decide the price/quality of items
        
    
def freeland():
    freeland_actions = {
        "west":left,
        "east": right,
        "north": up,
        "south": down,
        "pos":lambda:print(pos),
        "position":lambda:print(pos),
        "location":lambda:print(pos),
        "palace":intro   
    }
    print("explore in any direction!\nsyntax: west")
    while True:
        prompt = input(">>>")
        prompt = prompt.lower()
        xcute = freeland_actions.get(prompt)
        if xcute:
            xcute()
        print(f"{screen_clear}{player.pos}")
def darkwood():
    return
    
    player.intro = 3   
def status():
    print(f"coins: {player.money}\nhealth: {player.hp}\nstr: {player.strgth}\nspeed: {player.spd}\ndef: {player.deff}\nexp: {player.xp}\nlevel: {player.level}\nstat points: {player.statpnt}")
    
def check_self():
    if player.hp <= 100 and player.hp > 75:
        print("not too shabby.")
    elif player.hp < 75 and player.hp > 50:
        print("maybe i need to rest.")
    elif player.hp < 50 and player.hp > 20:
        print("i cant feel my skin.")
    elif player.hp < 5:
        print("if i cant feel my skin ill just tear it off.")
    
    
def point_allocate():
    return #for stats
    
def weekdays():
    global current_day
days = ["monday","tuesday","wednsday","thursday","friday","saturday","sunday"] #start @0
current_day = days[player.day] #saves day progress so each boot isnt a complete restart
def rest():
    global result
    player.day += 1
    while player.health <= 100:
        player.health += 1
    result = "you are well rested"    
        
def left():
    global result, effort
    if player.x >= -100:
        player.x -= 1 
    elif player.x < -100: #replace static max size with makeworld max size
        result = "looks dangerous, im not going further"
        player.x = -100
        effort = effort + 1
        if effort >= 5:
            player.intro = 2
        
        
def right():
    global result, effort
    if player.x <= 100:
        player.x += 1
    elif player.x > 100: 
        result = "looks dangerous, im not going further"
        player.x = 100
        effort = effort + 1
        if effort >= 5:
            player.intro = 2    

def up():
    global result, effort
    if player.y <= 100:
        player.y += 1
    elif player.y > 100:
        result = "looks dangerous and its cold, im not going further"
        player.y = 100
        effort = effort + 1
        if effort >= 5:
            player.intro = 2    

def down():
    global result, effort
    if player.y >= -100:
        player.y -= 1
    elif player.y < -100:
        result = "looks dangerous, im not going further"
        player.y = -100
        effort = effort + 1
        if effort >= 5:
            player.intro = 2
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

screen_clear = f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
game()    