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
        roll = 0
        damage = weapon['damage']
        rolls = int(damage[0])
        if crit:
            rolls = rolls * int(weapon['critical'][1])
        for i in range(rolls): #damage[0] = # of rolls
            rol = int(random.randrange(1,(1 + int(damage[2])))) 
            print("Roll " + str(i + 1) +": " + str(rol))
            roll += rol
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
        roll = 0
        damage = weapon['damage']
        rolls = int(damage[0])
        if crit:
            rolls = rolls * int(weapon['critical'][1])
        for i in range(rolls): #damage[0] = # of rolls
            rol = int(random.randrange(1,(1 + int(damage[2])))) 
            print("Roll " + str(i + 1) +": " + str(rol))
            roll += rol
        print(weapon['weapon'] + ": " + str(roll) + " = " + str(roll))

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
    print("Total hp: " + data['hp']['total'])
    change = input("current hp: " + str(currentHp) + ". How much does hp change? (0 for reset)")
    if change == '0':
        currentHp = int(data['hp']['total'])
    else:
        if change[0] == '-':
            
            currentHp -= int(change[1:99])
        else:
            currentHp += int(change)
    print("New Hp: " + str(currentHp))

def roll_save():
    typeDict = {
        '1': 'fort', #night
        '2': 'reflex',
        '3': 'will'
    }
    type = input("What type of save? \n 1) Fortitude \n 2) Reflex \n 3) Will\n")
    roll = random.randrange(1, 21)
    bonus = data['saves'][typeDict[type]]['total']
    print(str(roll) + " + " + str(bonus) + " = " +  str(int(roll) + int(bonus)))

def roll_skill():
    typeDict = {
        '1': 'acrobatics', #night
        '2': 'intimidate',
        '3': 'bluff',
        '4': 'stealth',
        '5': 'appraise',
        '6': 'swim',
        '7': 'ride'
    }
    print("What type of check?")
    for i, va in typeDict.items():
        print(i + ") " + va)
    type = input("")
    roll = random.randrange(1, 21)
    bonus = data['skills'][typeDict[type]]['total']
    print(str(roll) + " + " + str(bonus) + " = " +  str(int(roll) + int(bonus)))


def start():
    commandDict = {
        "1": m_attack_roll,
        "2": r_attack_roll,
        "3": get_ac,
        "4": roll_intiative,
        "5": hp_stuff,
        "6": roll_save,
        "7": roll_skill
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