import sys, time

names = {1: 'Jack', 2: 'Michael', 3: 'Mark', 4: 'Bill', 5: 'Type your own name'}
space = "\n"
life = 100
i = 0

print "The big adventure!"
print space
time.sleep(2)
print "What's your name, my young adventurer?"
print "Options are:"
while i != 5:
    i = i + 1
    print i, names[i]

name = raw_input("My name is... ")

if len(name) == 0:
    print space
    time.sleep(2)
    exit("Didn't specify a name.")
else:    
    print space
    time.sleep(2)
    print "Welcome %s! Your adventure is about to start. Are you ready? y/n" % name

    ready = raw_input("> ")

    if ready == "y" or ready == "yes":
            time.sleep(2)
            print space
            print "You're in the evil forest of Akivia. You're looking for the Princess of Talkia who disappeared a few  days ago. All your clues lead you here. As you're walking by, you notice a wild wolf in front of you. The wolf doesn't notice your presence so you have a chance to strike first. What weapon do you choose? Your bow (type 'bow') or your sword (type 'sword')?"
            print space
            print "Choose carefully. The decision could cost you your life..."
    elif ready == "n" or ready == "no":
            print space
            time.sleep(2)
            print "By then :)"
            sys.exit()

    weapon = raw_input("> ")

    print space
            
    if weapon == "bow":
                time.sleep(2)
                print "You pick up your bow carefully. Well done %s, you just killed the wild wolf with your powerful bow. You keep walking down the forest." % name
    elif weapon == "sword":
                time.sleep(2)
                print "You choose to use your sword. That wasn't very smart of you %s, since the one-on-one combat is very difficult. You have won the battle but you got injured. your %s HP has gone down to %s HP." % (name, life, life - 20)

    else:
                time.sleep(2)
                print "You fool! You just ran away of the forest like a little girl. Your punishment is death!"
                time.sleep(2)
                sys.exit("You lose...")

    print space
    time.sleep(5)
    print "You continue your path through the dangerous forest. You're really close to find where the Princess is. Now your destiny is marked, you can't go back. As you walk by, you stumble across a river. The water has a monstrous speed and you can't just swim. You find a boat, but it might be too light to support the strength of the river. Maybe you should find another route. What do you do, %s? Walk around it (type 'walk') or use the boat (type 'boat')?" % name

    river = raw_input("> ")

    print space
            
    if river == "walk":
                time.sleep(2)
                print "Your choice has saved you from almost dying, %s. The boat gets destroyed minutes after you left your position. It only took you half an hour to find a bridge. Well done, you're a smart adventurer, after all." % name
    elif river == "boat":
                time.sleep(2)
                print "Stupid choice you've made %s. That decision almost takes your life. You're luck you made it through almost all the river. But you get seriously injured in the swim. Your life of %s HP has been reduced to %s HP. You rest for a few minutes and then keep walking." % (name, life, life - 30)
    else:
                time.sleep(2)
                print "The wolf had an entire group looking for him. You should have ran away. Now you're dead..."
                time.sleep(2)
                sys.exit("You lose...")

    print space
    time.sleep(5)
    print "After the long walk, you find the old mansion you were looking for. But watch out, there are skull soldiers watching the main gate. You see a small window in the other side of the mansion, you could easily climb it. But you have no idea what you will find inside. Maybe It's time to use your sword, since the bow won't do them nothing. But before you decide, you find a heavy rock in a great position. You could push the rock and destroy the guards. What would you do, %s? Climb the window (type 'window'), attack the guards (type 'attack') or push the rock (type 'rock')?" % name

    mansion = raw_input("> ")

    print space
                
    if mansion == "window":
                    time.sleep(2)
                    print "The smart choice isn't always the best one. As you climb the window, you fall inside the mansion and find yourself covered with guards. You have failed the Princess and Talkia. Sometimes you have to face fears and fight!"
                    time.sleep(2)
                    sys.exit("You lose...")

    elif mansion == "attack":
                    time.sleep(2)
                    print "You have done well facing those guards. They were slow and easy to beat. Now you're inside the castle and the only thing you need to do is find the Princess. Move carefully and don't make any noise!"

    elif mansion == "rock":
                    time.sleep(2)
                    print "The rock tricked you, young adventurer. You push the rock and succesfully destroy the guards, but the door locks you out. Now the guards are alerted and you have lost the element of surprise. They will be looking for you and kill you at first sight. You have failed us, %s." % name
                    time.sleep(2)
                    sys.exit("You lose...")

    else:
                    time.sleep(2)
                    print "Why do you run? The guards have spotted you and send an entire army. As you try to cross the river, the army finds you and kills you."
                    time.sleep(2)
                    sys.exit("You lose...")

    print space
    time.sleep(5)
    print "You're almost there. You just need to find the Princess. You walk downstairs and kill the guard that's watching the cells. You can't hear nor see the Princess. You don't have time to open the three doors. You better pick one, which one will be? #1, #2 or #3?"

    door = raw_input("> ")

    print space

    if door == "1" or door == "3":
                    time.sleep(2)
                    print "This wasn't it. This was empty and now all the effort you have done to save the Princess is useless. The guards find you and kill you. I'm sorry %s, but this is the end for you." % name
                    time.sleep(2)
                    sys.exit("You lose...")

    elif door == "2":
                    time.sleep(2)
                    print "The Princess is here! You made it, %s!. Now it's time to save her!" % name
                    print space
                    time.sleep(2)
                    print "\"Who are you, what's your name brave adventurer?\" - The Princess said."
                    print space
                    time.sleep(2)
                    print "\"I'm %s, Princess. I came here to rescue you. It's time to leave, let's hurry!\" You said and both run away." % name
                    print space
                    time.sleep(2)
                    print "Once you got her out of the castle. you follow your steps and got her back to her family. As a sign of thank you, the King of Talkia lets you marry her beautiful daughter. Now you're a Prince and future king of Talkia. Well done, adventurer, you have finished this adventure with wit and courage. I hope you accomplish all your endeavours as a king!"

    version = sys.version[:6]
    copyright = sys.copyright[:30]

    print space
    time.sleep(10)
    print "Game created by Leandro Poblet using Python %s. %s :)" % (version, copyright)
    sys.exit("Thank you for playing!")
