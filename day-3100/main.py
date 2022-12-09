print("""
###############################
The Ultimate Wacky Recipe Maker
###############################
""")
print()
food = input("Name a food > ")
plant = input("Name a plant > ")
cooking = input("Name a method of cooking > ")
burned = input("Name a word that describes burnt food > ")
item = input("Name a household item > ")
print()
print("MENU")
print(cooking, food, "with", burned, plant, "on a bed of", item + "s.")
print()
print("""
#######################
The Actual Recipe Maker
#######################
""")
print()
starter = input("What would you like as a starter > ")
main_course = input("What would you like for the main course > ")
dessert = input("What would you like for dessert > ")
print()
print("MENU")
print("For starter we have", starter + ",",
      "as for the main course, we have got the finest", main_course,
      "and lastly for dessert, there's nothing better than a", dessert + ".")
