print(
    "\033[33m", '''
█░█░█ █▀█ █░█░█   █▀▀ █░░ ▄▀█ █▀ █▀   █▀▀ █▀▀ █▄░█ █▀▀ █▀█ ▄▀█ ▀█▀ █▀█ █▀█
▀▄▀▄▀ █▄█ ▀▄▀▄▀   █▄▄ █▄▄ █▀█ ▄█ ▄█   █▄█ ██▄ █░▀█ ██▄ █▀▄ █▀█ ░█░ █▄█ █▀▄
''', "\033[0m")
print()
print("Controls: Yes or No")
print()
print("Let's see which class in WoW suits you best!")
print()

#Druid
druid = input("Do you like shapeshifting? ")
if druid == "Yes":
    print("\033[30m"
          "You are a Druid! Jack of all trades, master of none..", "\033[0m")
else:
    print("Let's find another class..")
print()

#Hunter
hunter = input("Do you like controlling beasts? ")
if hunter == "Yes":
    print(
        "\033[32m"
        "You are a Hunter! You control beasts and use ranged attacks.",
        "\033[0m")
else:
    print("Let's find another class..")
print()

#Mage
mage = input("Do you like using frost or fire, or even arcane spells? ")
if mage == "Yes":
    print("\033[34m"
          "You are a Mage! Easy class, noobs only!", "\033[0m")
else:
    print("Let's find another class..")
print()

#Paladin
paladin = input("Do you like using light as your source of power? ")
if paladin == "Yes":
    print("\033[30m"
          "You are a Paladin! You made Arthas proud.", "\033[0m")
else:
    print("Let's find another class..")
print()

#Priest
priest = input("Do you like healing, but also dealing damage? ")
if priest == "Yes":
    print(
        "You are a Priest! You can use light to heal or shadow to deal damage."
    )
else:
    print("Let's find another class..")
print()

#Rogue
rogue = input("Do you like using stealth to take down your enemies? ")
if rogue == "Yes":
    print(
        "\033[33m"
        "You are a Rogue! You can use either Swords or Daggers as your weapons.",
        "\033[0m")
else:
    print("Let's find another class..")
print()

#Shaman
shaman = input("Do you like to use totems to aid you in battle? ")
if shaman == "Yes":
    print(
        "\033[36m"
        "You are a Shaman! You mainly heal but could also deal damage.",
        "\033[0m")
else:
    print("Let's find another class..")
print()

#Warlock
warlock = input("Do you like controlling demons to take down your enemies? ")
if warlock == "Yes":
    print("\033[35m"
          "You are a Warlock! Hated by everyone, kills everyone..", "\033[0m")
else:
    print("This can't be..")
print()

#Warrior
warrior = input("Do you have rage instead of blood in your veins? ")
if warrior == "Yes":
    print("\033[31m"
          "You are a Warrior! The master class, unbeatable!", "\033[0m")
else:
    print("Don't play the game..")