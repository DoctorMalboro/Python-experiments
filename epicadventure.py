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
elif len(name) >= 10:
    print space
    time.sleep(2)
    exit("Name too long.")

elif name == '1':
    name = 'Jack'
elif name == '2':
    name = 'Michael'
elif name == '3':
    name = 'Mark'
elif name == '4':
    name = 'Bill'

print space
time.sleep(2)
print "Welcome %s! Your adventure is about to start. Are you ready? y/n" % name

ready = raw_input("> ")

if ready == "y" or ready == "yes":
    time.sleep(2)
elif ready == "n" or ready == "no":
    print space
    time.sleep(2)
    print "Bye then :)"
    sys.exit()

print space
print "You're in the evil forest of Akivia. You're looking for the Princess of Talkia\nwho disappeared a few  days ago. All your clues lead you here. As you're\nwalking by, you notice a wild wolf in front of you. The wolf doesn't notice\nyour presence so you have a chance to strike first. What weapon do you choose?\nYour bow (type 'bow') or your sword (type 'sword')?"
print space
print "Choose carefully. The decision could cost you your life..."
weapon = raw_input("> ")

print space

if weapon == "bow":
    time.sleep(2)
    print "You pick up your bow carefully. Well done %s, you just killed the wild\nwolf with your powerful bow. You keep walking down the forest." % name
elif weapon == "sword":
    time.sleep(2)
    print "You choose to use your sword. That wasn't very smart of you %s, since\nthe one-on-one combat is very difficult. You have won the battle but you got\ninjured. your %s HP has gone down to %s HP." % (name, life, life - 20)
    life -= 20

else:
    time.sleep(2)
    print "You fool! You just ran away of the forest like a little girl. Your punishment\nis death!"
    time.sleep(2)
    sys.exit("You lose...")

print space
time.sleep(5)
print "You continue your path through the dangerous forest. You're really close to\nfinding out where the Princess is. Now your destiny is marked, you can't go\nback. As you walk by, you stumble across a river. The water has a monstrous\nspeed and you can't just swim. You find a boat, but it might be too light to\nsupport the strength of the river. Maybe you should find another route. What do\nyou do, %s? Walk around it (type 'walk') or use the boat (type 'boat')?" % name

river = raw_input("> ")

print space
            
if river == "walk":
    time.sleep(2)
    print "Your choice has saved you from almost dying, %s. The boat gets destroyed\nminutes after you left your position. It only took you half an hour to find a\nbridge. Well done, you're a smart adventurer, after all." % name
elif river == "boat":
    time.sleep(2)
    print "Stupid choice you've made %s. That decision almost takes your life.\nYou're lucky you made it through almost all the river. But you get seriously\ninjured in the swim. Your life of %s HP has been reduced to %s HP. You rest\nfor a few minutes and then keep walking." % (name, life, life - 30)
    life -= 30
else:
    time.sleep(2)
    print "The wolf had an entire group looking for him. You should have ran away.\nNow you're dead..."
    time.sleep(2)
    sys.exit("You lose...")

print space
time.sleep(5)
print "After the long walk, you find the old mansion you were looking for. But watch\nout, there are skull soldiers watching the main gate. You see a small window in\nthe other side of the mansion, you could easily climb it. But you have no idea\nwhat you will find inside. Maybe It's time to use your sword, since the bow\nwon't do them nothing. But before you decide, you find a heavy rock in a great\nposition. You could push the rock and destroy the guards. What would you do,\n%s? Climb the window (type 'window'), attack the guards (type 'attack')\nor push the rock (type 'rock')?" % name

mansion = raw_input("> ")

print space

if mansion == "window":
    time.sleep(2)
    print "The smart choice isn't always the best one. As you climb the window, you fall\ninside the mansion and find yourself covered with guards. You have failed the\nPrincess and Talkia. Sometimes you have to face fears and fight!"
    time.sleep(2)
    sys.exit("You lose...")

elif mansion == "attack":
    time.sleep(2)
    print "You have done well facing those guards. They were slow and easy to beat. Now\nyou're inside the castle and the only thing you need to do is find the\nPrincess. Move carefully and don't make any noise!"

elif mansion == "rock":
    time.sleep(2)
    print "The rock tricked you, young adventurer. You push the rock and succesfully\ndestroy the guards, but the door locks you out. Now the guards are alerted and\nyou have lost the element of surprise. They will be looking for you and kill\nyou at first sight. You have failed us, %s." % name
    time.sleep(2)
    sys.exit("You lose...")

else:
    time.sleep(2)
    print "Why do you run? The guards have spotted you and send an entire army. As you try\nto cross the river, the army finds you and kills you."
    time.sleep(2)
    sys.exit("You lose...")

print space
time.sleep(5)
print "You're almost there. You just need to find the Princess. You walk downstairs\nand kill the guard that's watching the cells. You can't hear nor see the\nPrincess. You don't have time to open the three doors. You better pick one,\nwhich one will be? #1, #2 or #3?"

door = raw_input("> ")

print space

if door == "1" or door == "3":
    time.sleep(2)
    print "This wasn't it. This was empty and now all the effort you have done to save the\nPrincess is useless. The guards find you and kill you. I'm sorry %s, but\nthis is the end for you." % name
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
    print "\"I'm %s, Princess. I came here to rescue you. It's time to leave, let's\nhurry!\" You said and both run away." % name
    print space
    time.sleep(2)
    print "Once you got her out of the castle, you follow your steps and got her back to\nher family. As a sign of thank you, the King of Talkia lets you marry his\nbeautiful daughter. Now you're a Prince and future king of Talkia. Well done,\nadventurer, you have finished this adventure with wit and courage. I hope you\naccomplish all your endeavours as a king!"

else:
    time.sleep(2)
    print "Your indecisiveness has cost you! While staring at the doors a guard finds a\ndead body and sounds the alarm. You are trapped!"
    time.sleep(2)
    sys.exit("You lose...")

version = sys.version[:6]
copyright = sys.copyright[:30]

print space
time.sleep(10)
print "Game created by Leandro Poblet using Python %s\n%s :)" % (version, copyright)
sys.exit("Thank you for playing!")
