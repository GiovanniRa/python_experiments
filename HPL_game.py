# -*- coding: utf-8 -*-

from sys import exit

import time
current_date = time.asctime(time.localtime(time.time()))

import random

def die(why):
    print why
    exit(0)
    
def arkham():
    print "It is %s." % current_date
    print "A dark and desert road in the city of Arkham."
    print "An old friend has asked you to meet him at the Miskatonic University."
    print "Where do you go? left or right?"
    
    direction = raw_input("< ")
    
    if direction == "left":
        print "You are going towards the sea."
        sea()
    elif direction == "right":
        print "After a short walk you can see the tall, dark building of the Miskatonic University."
        miskatonic()
    else:
        die("You realize it was just a dream and wake up suddenly.")

def miskatonic():
    print "There are two doors in front of you. One is very large, the other one is smaller."
    print "Which door do you choose?"
    
    while True:
        
        door = raw_input("< ")
    
        if "large" in door:
            print "A huge hallway. A weird creature seems to be waiting for you."
            creature()
        elif "smaller" in door:
            print "A long tight corridor. A light at the end."
            corridor()
        else:
            print "You cannot go back at this point and MUST make your choice."
            
def creature():
    print "Do you come closer or run away?"
    
    while True:
    
        weird = raw_input("< ")
        
        if "closer" in weird:
            die("The creature is going to quickly dismember you before you can even realize it.")
        elif "run" in weird:
            print "Back where you started. Maybe better make a different choice."
            miskatonic()
        else:
            print "No, not the answer I was waiting for."
            die("And because of this, you die.")
            
def corridor():
    print "Do you go back or walk into the light?"
    
    tight_corridor = raw_input("< ")
    
    if "back" in tight_corridor:
        print "So, you want to go back. Ok."
        miskatonic()
    elif "light" in tight_corridor:
        print "You are in a small library."
        library()
    else:
        die("You MUST make the right choice to stay alive. And you didn't. Good bye.")
        
def library():
    print "You go near one of the shelves and start reading some of the titles."
     
    books = []
    books.extend(["De vermis misteriis", "Necronomicon", "De magis", "Teurgia de mortuis"])
    
    for book in books:
        print "%s is a cursed and dangerous book." % book
    
    print "You take one of the books."
    print books.pop(1)
    
    print """Do you 
    a - start reading from the book
    b - throw the book away because you hear an inhuman voice whispering behind you
    """
    
    nec = raw_input("< ")
    
    if nec == "a":
        print "The last thing you see is the almighty Cthulhu appearing in front of you, while you pronounce the words..."
        raw_input("Do you want to see the words? Type something here. ")
        die("Ià   Ià   Cthulhu   fthaghn  " * 1000)
    elif nec == "b":
        die("It is too late to go back...")
    else:
        print "No other choices left, a or b, that's all."
        
def sea():
    print "After a short walk you reach the seashore."
    num = random.randint(1, 10)
    print "Suddenly %d horrendous creatures emerge from the sea." % num
    
    if num <= 3:
        print "You fight strenuosly against them until..."
        print "You wake up in your bed. It is %s." % current_date
        print "It was a dream."
        print "   MAYBE   " * 100
    else:
        print "This is the end, my friend."
        print "  IA'  IA'  CTHULHU   FTHAGHN   " * 10
        
    
    
    
arkham()
    
