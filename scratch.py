from character import NPC, Player
# from obj_scratch import Item, Room
#
# li = Player('Li', 'A developer working on this game', guilt=True)\
#
# class_room = Room('PDX Code Guild Classroom')
# bathroom = Room('A place to pee')
# apple = Item('Apple')
# class_room.add_inv(li)
# class_room.add_inv(apple)
# class_room.print_inv()



interactions = {'Mrs. Frizzle': {'game_offer': 'Would you like to play trivia? ', 'conclusion': 'Ok, here\'s the key.'}}

science_teacher = NPC('Mrs. Frizzle', 'Frazzled', interactions)

q = input(science_teacher.talk()).lower()  # mini-game offer
if NPC.essential
    if q == 'y':
        print('TRIVIA GAME')  # here we would run the mini-game module.
        reward = 1  # this would be returned by the mini-game
        science_teacher.conclude(reward)  # prize or no prize
        player.notebook.write(npc.give())
    else:
        print('Ok, see you later.')  # chose not to play
else:
    print(npc.talk())

