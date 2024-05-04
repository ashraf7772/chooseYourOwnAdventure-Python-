name = input("Hi, whats your name? ")
print("Hi", name, "Lets start this adventure!")

print("ESCAPE")
print("Welcome prisoner", name, "to Ark Prison where you will live the rest of your days unless you ESCAPE!")
choice1 = input("You walk into your cell where you see your cellmate. Are you going to ask him to be an ally or escape alone? (*Ask* to ask him or *Alone* to go alone)").lower()

if choice1 == "ask":
    choice2 = input("He agrees... Together you two make a plan. He is going to create A DISTRACTION! while you slip past the guards navigating the corridors of Ark. You find a small door leading to a tunnel. Do you go down this tunnel or keep wandering the corridors? (*down* to go down the tunnel and *wandering* to keep wandering down the corridors) ").lower()
    if choice2 == "down":
        print("You go down this tunnel. In the darkness you rely on instinct and luck to guide you")
        print("You find a hole leading to freedom, but theres a GAP.")
        choice4 = input ("Do you jump or wait to think for something? (*jump* to jump or *think* to think)").lower()
        if choice4 == "jump":
                print("YOU MADE THE JUMP")
                print("WELL DONE. You have ESCAPED")
                quit()
        elif choice4 == "think":
             print("The guards came from behind and grabbed you while you hesitated....")
             print("YOU LOSE")
             quit()
        else:
             print("option not valid. GAME OVER")
             quit()

    elif choice2 == "wandering":
        print("You were caught by the guards...")
        print("GAME OVER")
        quit()
    else:
        print("You need to type *down* or *wandering*. You fail")
        quit()

    

elif choice1 == "alone":
    print("You decide to work alone... You watch the guards taking note of their shifts")
    print("After a few days you learn the shifts by heart and notice when the prison has the least amount of staff around")
    print("You go through the kitchen during lunch and see the backdoors open to the food truck")
    choice3 = input("Do you hide in the food truck or wait until the food truck leaves and attempt to escape by foot? (*food truck* for food truck or *foot* to try escape by foot)").lower()
    if choice3 == "food truck":
         print("You hop on to the back of the food truck in a spot where no one will see you")
         print("You roll through the gates of ARK prison. You breathe a sigh of relief knowing you have ESCAPED")
         print("WELL DONE. You have Escaped")
         quit()
    elif choice3 == "foot":
        print("You make a run for it. You SEE THE GATE OPEN")
        print("Just as you pass through the gate you are shot and killed....")
        print("GAME OVER. YOU LOSE")
        quit()
    else:
         print("Option not valid. GAME OVER")
         quit()
         

else:
    print("You need to type *ask* or *alone*. You fail")
    quit()