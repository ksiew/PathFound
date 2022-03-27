import json
import os
import random

for filename in os.listdir("Characters"):
    if filename.endswith('.json'):
        with open(os.path.join("Characters", filename), 'r') as f:
            data = json.load(f)

currentHp = int(data['hp']['total'])
def m_attack_roll():
    if not 'melee' in data:
        print("No melee weapons")
        return
    roll = int(random.randrange(1,21))
    bonus = int((int(data['abilities']['str']) - 10)/2) + int(data['bab'])
    print("Attack roll: " + str(roll) + " + " + str(bonus) + " = " + str(roll + bonus))
    if roll == 20:
        print("CRIT!")
        m_damage_roll(True)
    else:
        m_damage_roll(False)

def m_damage_roll(crit):
    for weapon in data['melee']:
        damage = weapon['damage']
        for i in range(int(damage[0])): #damage[0] = # of rolls
            roll = int(random.randrange(1,(1 + int(damage[2])))) 
            bonus = int((int(data['abilities']['str']) - 10)/2)
            print(weapon['weapon'] + ": " + str(roll) +  " + " + str(bonus) + " = " + str(bonus + roll))

def r_attack_roll():
    if not 'ranged' in data:
        print("No ranged weapons")
        return
    roll = int(random.randrange(1,21))
    bonus = int((int(data['abilities']['dex']) - 10)/2) + int(data['bab'])
    print("Attack roll: " + str(roll) + " + " + str(bonus) + " = " + str(roll + bonus))
    if roll == 20:
        print("CRIT!")
        r_damage_roll(True)
    else:
        r_damage_roll(False)

def r_damage_roll(crit):
    for weapon in data['ranged']:
        damage = weapon['damage']
        for i in range(int(damage[0])): #damage[0] = # of rolls
            roll = int(random.randrange(1,(1 + int(damage[2])))) 
            bonus = int((int(data['abilities']['dex']) - 10)/2)
            print(weapon['weapon'] + ": " + str(roll) +  " + " + str(bonus) + " = " + str(bonus + roll))

def get_ac():
    bonus = data['ac']
    shield = 0
    if 'shieldBonus' in bonus:
        shield = int(bonus['shieldBonus'])
    total = int(bonus['armorBonus']) + int(shield) + int((int(data['abilities']['dex']) - 10)/2)
    print("AC: 10 " + bonus['armorBonus'] + " + " + str(shield) + " + " + 
        str(int((int(data['abilities']['dex']) - 10)/2)) + " = " + str(data['ac']['total']))

def roll_intiative():
    roll = int(random.randrange(1,21))
    bonus = int(data['initiative']['total'])
    print("Initiative: " + str(roll) + " + " + str(bonus) + " = " + str(roll + bonus))

def hp_stuff():
    global currentHp
    change = input("current hp: " + str(currentHp) + ". How much does hp change? (0 for reset)")
    if change == '0':
        currentHp = int(data['hp']['total'])
    else:
        if change[0] == '-':
            
            currentHp -= int(change[1:99])
        else:
            currentHp += int(change)
    print("New Hp: " + str(currentHp))

def start():
    commandDict = {
        "1": m_attack_roll,
        "2": r_attack_roll,
        "3": get_ac,
        "4": roll_intiative,
        "5": hp_stuff
    }
    print("Character: " + data['name'])
    while(True):
        for i, va in commandDict.items():
            print(i + ") " + commandDict[i].__name__)
        command = input("innput function: ")
        print("")
        try:
            commandDict[command]()
        except:
            print("command not recognized")
        print("")

start()