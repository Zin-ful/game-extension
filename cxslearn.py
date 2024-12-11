import random
import sys

mon_lvl = 3
mon_hp = 100
mon_atk = 5
mon_spd = 1
plr_nm = input("name?\n\n>>>")
plr_lvl = 1
plr_hp = 100
plr_atk = 7
plr_spd = 1
        
def battle():
    global plr_lvl, plr_hp, plr_atk, plr_spd
    cache_monlvl = mon_lvl
    cache_monhp = mon_hp
    cache_monatk = mon_atk + random.randint(0,mon_lvl)
    cache_monspd = mon_spd + random.randint(0,mon_lvl)
    recent_atkmon = False
    recent_atkplr = False
    while True:
        cache_monatk = mon_atk + random.randint(0,mon_lvl)
        cache_monspd = mon_spd + random.randint(0,mon_lvl)
        print("\nattack the monster? defend? or run?\n")
        plr_input = input("\n>>>")
        if "a" in plr_input.lower() or "1" in plr_input:
            if plr_spd > cache_monspd:
                if recent_atkplr == False:
                    recent_atkplr = True
                    cache_monhp -= plr_atk
                    print(f"{plr_nm} attacked for {plr_atk} damage.\nmonster has {cache_monhp} left.")
                else:
                    recent_atkplr = False
                    plr_hp -= cache_monatk
                    print(f"{plr_nm} got attacked for {cache_monatk} damage.\n{plr_nm} has {plr_hp} left.")
            elif plr_spd <= cache_monspd:
                if recent_atkmon == False:
                    recent_atkmon = True
                    plr_hp -= cache_monatk
                    print(f"{plr_nm} got attacked for {cache_monatk} damage.\n{plr_nm} has {plr_hp} left.")

                else:
                    recent_atkmon = False
                    cache_monhp -= plr_atk
                    print(f"{plr_nm} attacked for {plr_atk} damage.\nmonster has {cache_monhp} left.")
        if plr_hp <= 0:
            print(f"{plr_nm} suffered a horrible death at the hands of\nball crusher™ and got his balls crushed")
            break 
        elif cache_monhp <= 0:
            print(f"{plr_nm} vanquished the angel dooming this world")
            break
            
print("youve encountered a moster\nwould you like to fight it?\n")
while True:
    plr_input = input("\n>>>")
    if "y" in plr_input.lower() or "f" in plr_input.lower():
        battle()
        if plr_hp <= 0:
            plr_input = input("retry? >>>")
            if "y" in plr_input.lower():
                battle()
            else:
                sys.exit()
        elif plr_hp > 0:
            print("the world succumed to gods absence")
            sys.exit()
    elif "n" in plr_input.lower() or "r" in plr_input.lower():
        sys.exit()                    