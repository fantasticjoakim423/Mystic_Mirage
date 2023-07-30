#Introduction
print("Welcome to MYSTIC MIRAGE\n")
print("As an avid traveler, you have decided to visit the infamous Mythwood Maze.\n")
print("However, during your exploration, you find yourself lost in the forest.\n")
print("You can choose to walk in multiple directions to find a way out.\n")

#input player name
while True:
  name = input("Before we begin, what is your name, adventurer?\n")
  if name == "":
    print("Please enter a valid name.\n")
  else:
    break

print("\nGreetings, " + name + ". Let us go on a quest!")

# Start of game
while True:
  response = input("Will you take up the challenge of navigating through the forest? \nyes/no\n")
  if response.lower() == "yes":
    print("\nYou are stuck in the middle of the forest. You hear crows cawwing in the distance.\n")
    break
  elif response.lower() == "no":
    print("\nIt seems like you are not ready for this quest. Goodbye, " + name + ".")
    quit()
  else:
    print("Please enter a valid response.\n")
  
 
# Next part of game
print("You find yourself on the edge of a dark forest.")
print("Can you find your way out? Good luck!\n")
print("To your left, you see a bear.")
print("To your right, there is more trees.")
print("There is a wooden shed directly in front of you.")
print("Behind you is a river.\n")

response = ""
while True:
  response = input("What direction do you move?   \nleft/right/forward/backward\n")

#If player chooses left
  if response.lower() == "left":
    print("\nThe bear growls at you aggressively.")
    response = input("Do you choose to challenge the bear or flee the scene? \nfight/run\n")
    if response.lower() == "fight":
      print("\nGrr. The bear gobbles you up. Farewell, " + name + ".")
      quit()
    elif response.lower() == "run":
      print("\nYou managed to escape, phew.")
      response = input("*grumble* You're starving, luckily there are two berry bushes in front of you. Which do you choose? \nleft/right\n")
      if response.lower() == "left":
        print("\nUh oh, the berries were poisonous, how unlucky. Farewell " + name + ".")
        quit()
      elif response.lower() == "right":
        print("\nMmmm... yummy.")
        response = input("\nA wandering wizard comes up to you and asks to share the berries. Will you spare him some? \nyes/no\n")
        if response.lower() == "no":
          print("\nThe wizard whips out his wand and yells 'AVADA KEDAVRA'. Farewell " + name + ".")
          quit()
        elif response.lower() == "yes":
            print("\nHow kind, he gifts you a special potion and you continue along the way.")
            response = input("\nYou come across a river filled with crocodiles. Go left onto the bridge or right across the rocks? \nleft/right\n ")
            if response.lower() == "right":
              print("\nYou slip and fall into the river. Chomp chomp. Farewell " + name + ".")
              quit()
            elif response.lower() == "left":
                print("\nCrocodile food expired.")
                print("\nYou look up, noticing that the sun is about to set")
                response = input("Build a tent to sleep? \nyes/no\n")
                if response.lower() == "yes":
                  print("\nThere was a huge thunderstorm at night and it soaked your tent. BOOM. You were struck by lightning. Farewell " + name + ".")
                  quit()
                elif response.lower() == "no":
                  print("\nYou continue searching and you stumble upon a wooden shed. Ah yes, goodnight!")
                  print("\nMorning arrives and you wake up to somebody banging on the door of the shed.")
                  response = input("Will you answer the door? \nyes/no")
                  if response.lower() == "no":
                    print("\nA troll busts open the door and picks you up. It crushes you with its bare hands. Oof. Farewell " + name + ".")
                    quit()
                  elif response.lower() == "yes":
                    print("\nYou pick up an axe lying on the table. You open door and come face to face with a troll. You use your quick instincts and slice the troll's legs off. QUICK RUN!!!")
                    response = input("\nYou escape safely and come to two paths. The left path reads 'EXIT' and the right one reads 'EKSSSIT'. Which path will you take? \nleft/right\n")
                    if response.lower() == "left" or response.lower() == "right":
                      print("\nYou trip and fall into a pit of venomous snakes. They bite you. HISSSS!")
                      response = input("\nYou quickly rummage in your bag and found the potion. Would you like to use it? \nyes/no\n")
                      if response.lower() == "no":
                        print("\nLooks like someone can't read. Farewell " + name + ".")
                        quit()
                      elif response.lower() == "yes":
                        print("\nYou quickly drink it and climb out of the pit. You should probably go to the left path now...")
                        print("\nYou continue along the path and see something red in the bushes")
                        print("Oooh a flare gun! I wonder what happens if you... You fire it into thea air.")
                        print("Suddenly, something breaks through the sky, zooming down towards you.")
                        print("The Unidentified Flying Object lands on the ground and a strange creature steps out. 'PEACE IN COME WE'")
                        print("You step into the UFO and it flies away towards the exit.")
                        print("YAY! you escaped the forest and hit the griddy")
                    #End of game
                        print("\nEHMAZING! NEVER BACK DOWN, NEVER GIVE UP. FOR THE MEME, THE DREAM, THE STREAM AND THE EHHHH TEAMM!")
                        print("\nCongratulations " + name + ", you have successfully completed your journey through the Mythwood Maze. Until we meet again, goodbye!")
                        quit()

#If player chooses right
  elif response.lower() == "right":
    print("\nYou head deeper into the forest.\n")
    print("Along the way, you meet a mysterious man.")
    print("Shady Man: You shouldn't be wandering around this place... Come, follow me.")
    response = input("Will you follow the man? \nyes/no\n")
    if response.lower() == "yes":
      print("\nDid your parents not tell you not to listen to strangers? Farewell " + name + ".")
      quit()
    elif response.lower() == "no":
      print("\nYou ran away from the man and got on safely.")
      print("\n*grumble* You realise you have not eaten for a while.")
      response = input("*sniff* Something delicious seems to be coming from a house. Will you go inside? \nyes/no\n")
      if response.lower() == "no":
        print("\nYou starve after a few days without food. Farewell " + name + ".")
        quit()
      elif response.lower() == "yes":
        print("\nYou find a nice old lady living inside and she serves you pie. Yummy")
        print("You were continuing through the forest when a wild dog suddenly jumps out off the bushes. It growls at you aggressively.")
        response = input("Will you fight it or run away? \nfight/run\n")
        if response.lower() == "ru ":
          print("\nToo slow. You didn't manage to outrun the dog. Farewell " + name + ".")
          quit()
        elif response.lower() == "fight":
          print("\nYou barely managed to fight it off, but you severely injured your leg.")
          print("You discover two strange trees that are able to talk. The left tree presents a door to a seemingly perfect path. The right one presents a door to some challenges you have to face.")
          response = input("Which door will you step through \nleft/right\n")
          if response.lower() == "left":
            print("\nYou walk into it and the door slams shut behind you. Oops, it was a trap. Farewell " + name + ".")
            quit()
          elif response.lower() == "right":
            print("\nYou encountered a giant spider but you managed to escape from it.")
            response = input("\nA glowing flower catches your eye. It could possibly heal your wounds and provide rejuvenation, but it is risky. Will you consume it? \nyes/no\n")
            if response.lower() == "no":
              print("\nYou chose not to eat it and did not survive your injuries. Farewell " + name + ".")
              quit()
            elif response.lower() == "yes":
              print("\nYou eat it and quickly recover from your injuries.")
              print("Deep in the forest, you discover a sparkling fountain and two streams. The left stream grants wisdom if you drink it. The right one grants strength.")
              response = input("Which stream will you drink from? \nleft/right\n")
              if response.lower() == "right":
                print("\nYou were attacked by bandits and there was too many of them to fight off. Unwise choice. Farewell " + name + ".")
                quit()
              elif response.lower() == "left":
                print("\nYou were attacked by bandits, but you managed to outsmart them. Wise choice.")
                response = input("An eerie fog rolls into the forest, obstructing your vision. Will you continue through the forest? \nyes/no\n")
                if response.lower() == "yes":
                  print("\nYou acsssidentally fell into a pit of venomous snakes. Farewell " + name + ".")
                  quit()
                elif response.lower() == "no":
                  print("\nYou seek shelter and wait for the fog to disappear.")
                  print("\nYou spot a basket lying behind some bushes. You open and and discover a magical purple potion.")
                  print("Desperate to find a way out of the forest, you drink it without hesitation.")
                  print("Your stomach starts to feel strange and the things aeound you start to grow bigger.")
                  print("You look around and realise that you shrunk to the size of an insect. That's cool!")
                  print("A beetle suddenly swoops down and picks you up, carrying you to the forest exit. Hooray!")

                #End of game
                  print("\nEHMAZING! NEVER BACK DOWN, NEVER GIVE UP. FOR THE MEME, THE DREAM, THE STREAM AND THE EHHHH TEAMM!")
                  print("\nCongratulations " + name + ", you have successfully completed your journey through the Mythwood Maze. Until we meet again, goodbye!")
                  quit()
                
#If player chooses forward
  elif response == "forward":
    print("\nYou slowly open the door into the shed.\n")
    print("Upon looking around the room, you find an axe lying on the table and picked it up.")
    print("While moving deeper into the forest, you encounter some dancing mushrooms. They invite you to join them.")
    response = input("Will you join them? \nyes/no\n")
    if response.lower() == "no":
      print("\nThe mushrooms got angry and released deadly spores. Farewell " + name + ".")
      quit()
    elif response.lower() == "yes":
      print("\nYou had an enjoyable time dancing with the mushrooms. Yay.")
      response = input("\nUh oh, you fell into a pit of quicksand! Hurry, which way will you jump to? \nleft/right\n")
      if response.lower() == "left":
        print("\nYou were swallowed by the sinking sand. Farewell " + name + ".")
        quit()
      elif response.lower() == "right":
        print("\nYou jumped and got to safety! Guess you chose the RIGHT direction.")
        print("\nYou notice that it is getting dark and decided to make a campfire to keep warm during the night.")
        print("You remember that you have an axe in your backpack which you could use to gather logs.")
        response = input("Will you use the axe? \nyes/no\n")
        if response.lower() == "no":
          print("\nYou start to feel unusually cold in the forest. You couldn't make a fire and froze. Farewell " + name + ".")
          quit()
        elif response.lower() == "yes":
          print("\nYou used the axe to cut down some trees and built a campfire. Nice and cozy...")
          print("\nYou wake up to strange sounds in the forest.")
          print("A goblin gang appeared from the trees and attacked you!")
          response = input("Will you fight the goblins or run for your life? \nfight/run\n")
          if response.lower() == "fight":
            print("\nYou didn't manage to overcome the goblins and their spears. Hehehehaw. Farewell " + name + ".")
            quit()
          elif response.lower() == "run":
            print("\nYou shrieked and ran as fast as you could. You barely managed to escape the creepy creatures.")
            print("Along the way, you stumbled upon a leprechaun who offers you a gold coin that grants extaordinary luck.")
            response = input("Will you accept his gracious gift? \nyes/no\n")
            if response.lower() == "no":
              print("\nYou declined his offer and went on your way. Suddenly an anvil feel from the air and... BOOM! How unlucky. Farewell " + name + ".")
              quit()
            elif response.lower() == "yes":
              print("\nYou recieved the gold coin, but it didn't seem to do anything. Oh well.")
              print("\nAn eerie fog starts to roll into the forest, obstructing your vision.")
              print("You discover a fork in the path. The left route leads towards the sound of rushing water, while the right one leads deeper into the darkness of the forest.")
              response = input("Which route will you take? \nleft/right\n")
              if response.lower() == "left":
                print("\nYou were swept away by a strong current. Blub blub. Farewell " + name + ".")
                quit()
              elif response.lower() == "right":
                print("\nYou head into the darkness but after walking for some time, you got out into the light. No puns this time.")
                print("\nSuddenly, you spot something running towards you in the distance. As it gets closer, you realise that it's a rainbow llama!")
                print("The rainbow llama stops in front of you and bows, signalling to you to get on top of it.")
                print("You climb on its back and it soars above the treetops towards the forest exit. Looks like the gold coin did something after all!")

            #End of game
                print("\nEHMAZING! NEVER BACK DOWN, NEVER GIVE UP. FOR THE MEME, THE DREAM, THE STREAM AND THE EHHHH TEAMM!")
                print("\nCongratulations " + name + ", you have successfully completed your journey through the Mythwood Maze. Until we meet again, goodbye!")
                quit()

#If player chooses backward
  elif response.lower() == "backward":
    print("\nYou head towards the river.")
    print("Suddenly, a leprechaun jumps out of a bush.")
    print("He asks you to follow the rainbow to discover a surprise.")
    response = input("Will you follow the rainbow? \nyes/no\n")
    if response.lower() == "yes":
      print("\nYou follow the rainbow but it was trap! You ended up in a bear cave. Farewell " + name + ".")
      quit()
    elif response.lower() == "no":
      print("\nYou ignored the leprechaun and continued through the forest.")
      print("It sky begins to get dark. *grumble* You're starving. The river may have fishes, but it is difficult to see.")
      response = input("Go fishing? \nyes/no\n")
      if response.lower() == "no":
        print("\nYou couldn't find food for days and starved. Farewell " + name + ".")
        quit()
      elif response.lower() == "yes":
        print("\nYou managed to catch a big fish! Look at the size of that... Yum.")
        response = input("\n*Brr* It's getting cold. There's a pile of firewood you could use and a mysterious hut nearby. Which will you choose? \nwood/hut\n")
        if response.lower() == "wood":
          print("\nYou were picking up the firewood when a pack of coyotes surrounded you! Uh oh. Farewell " + name + ".")
          quit()
          print("\nYou go into the hut and you realise that it's a bar. Cool.")
          print("A man with an eyepatch starts chatting with you, he seems friendly.")
          response = input("The man offers you a drink. Will you take it? \nyes/no\n")
          if response.lower() == "yes":
            print("\nThe drink was laced with poison. Are you serious right now? Farewell " + name + ".")
            quit()
          elif response.lower() == "no":
            print("\nYou reject his offer. The barkeeper tells the man to leave you alone. Phew, close call.")
            print("\nBarkeeper: Hey, I've got a room in the back where you can stay for the night, as long as you give me a hand tomorrow.")
            print("In the morning, you wake up early to help the barkeeper clean his bar.")
            print("The barkeeper asks what you are doing in the forest.")
            response = input("Tell him that you are trying to escape? \nyes/no\n")
            if response.lower() == "no":
              print("\nYou told him you were just expolring the place. You leave the bar and never found the forest exit. What were you even doing? Farewell " + name + ".")
              quit()
            elif response.lower() == "yes":
              print("\nYou told him the truth and he tells you that he knows the way to the exit. Hooray!")
              print("\nThe barkeeper tells you the directions... Listen closely! \n Barkeeper: When you reach the paths, it's right, right, left, right, left.")
              print("You thanked the barkeeper for his help and continued on your journey.")
              response = input("\nYou reached the first crossroad. Which path do you take? \nleft/right\n")
              if response.lower() == "left":
                print("\nYou went the wrong way and got lost! You eventually go crazy. Farewell " + name + ".")
                quit()
              elif response.lower() == "right":
                print("\nCorrect!")
                print("\nShortly, you arrive at the second crossroad. Which path do you take? \left/right\n")
                if response.lower() == "left":
                  print("\nYou went the wrong way and got lost! You eventually go crazy. Farewell " + name + ".")
                  quit()
                elif response.lower() == "right":
                  print("\nThat's right!")
                  print("\nYou reached the third one. Which path do you take? \nleft/right\n")
                  if response.lower() == "right":
                    print("\nYou went the wrong way and got lost! You eventually go crazy. Farewell " + name + ".")
                    quit()
                  elif response.lower() == "left":
                    print("\nFacts.")
                    print("\nYou arrive at the fourth crossroad, almost there! Which path do you take? \nleft/right\n")
                    if response.lower() == "left":
                      print("\nYou went the wrong way and got lost! You eventually go crazy. Farewell " + name + ".")
                      quit()
                    elif response.lower() == "right":
                      print("\nPERFECT!")
                      print("\nYou finally reach the last crossroad. Which path do you take? \nleft/right\n")
                      if response.lower() == "right":
                        print("\nYou went the wrong way and got lost! You eventually go crazy. Farewell " + name + ".")
                        quit()
                      elif response.lower() == "left":
                        print("\nThe forest exit is right in front of you. You did it!")

                      #End of game
                        print("\nEHMAZING! NEVER BACK DOWN, NEVER GIVE UP. FOR THE MEME, THE DREAM, THE STREAM AND THE EHHHH TEAMM!")
                        print("\nCongratulations " + name + ", you have successfully completed your journey through the Mythwood Maze. Until we meet again, goodbye!")
                        quit()

else:
    print("Please enter a valid response\n")
