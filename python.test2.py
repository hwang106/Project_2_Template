#testing pull request
# Guess that pokemon game
# 5 pokemon 
# 3 tries
# ending that tells you how many pokemon you guessed right. 
# question1 = input("What pokemon is this?")
score = 0

#Since all your functions are so similar, what could you do to simplify things?
#questions 
def question1(answer):
    if (answer == "Pikachu"):
        global score
        score = 0
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
#Your code is very well-organized and readable, so this isn't a big issue, but generally, functions are grouped together separately from the main code that calls the functions. 
answer = input("What pokemon is this? It is a small yellow mouse and can use thunder attacks: ").capitalize()
print(question1(answer))

def question2(answer2):
    if (answer2 == "Charmander"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer2 = input("What pokemon is this? It is small and orange lizard, and can breathe fire: ").capitalize()
print(question2(answer2))

def question3(answer3):
    if (answer3 == "Bulbasaur"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer3 = input("What pokemon is this? It is small and green dinosaur, and can use plant attacks: ").capitalize()
print(question3(answer3))

def question4(answer4):
    if (answer4 == "Squirtle"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer4 = input("What pokemon is this? It is a small and blue turtle, and can use water attacks: ").capitalize()
print(question4(answer4))

def question5(answer5):
    if (answer5 == "Meowth"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer5 = input("What pokemon is this? It is a small cat, and one of its kind can be seen talking: ").capitalize()
print(question5(answer5))

def question6(answer6):
    if (answer6 == "Mewtwo"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer6 = input("What pokemon is this? Is a clone version of Mew, and is Psychic type: ").capitalize()
print(question6(answer6))

def question7(answer7):
    if (answer7 == "Pidgeot"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer7 = input("What pokemon is this? A flying type that evolved from Pidgey ").capitalize()
print(question7(answer7))

def question8(answer8):
    if (answer8 == "Raichu"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer8 = input("What pokemon is this? Pikachu's evolution ").capitalize()
print(question8(answer8))

def question9(answer9):
    if (answer9 == "Charizard"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer9 = input("What pokemon is this? It is a large flying orange dragon that can breath deadly flames: ").capitalize()
print(question9(answer9))

def question10(answer10):
    if (answer10 == "Venusaur"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer10 = input("What pokemon is this? It is a large green dinosaur with a huge flower on its back. It uses aroma and vines to attack or stun foes: ").capitalize()
print(question10(answer10))

def question11(answer11):
    if (answer11 == "Blastoise"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer11 = input("What pokemon is this? It is a large blue turtle with two cannons on its back. Highly pressurized water can blast out from these cannons: ").capitalize()
print(question11(answer11))

def question12(answer12):
    if (answer12 == "Snorlax"):
        global score
        score += 1
        return "You're correct"
    else:
        return "Wrong answer"
answer12 = input("What pokemon is this? It is a massive furry bear. It enjoys sleeping and eating tons of food: ").capitalize()
print(question12(answer12))

#function that checks your score and gives you an result
def score_checker():
    if (score > 3): 
        return "Results: You know your Pokemon decently" 
    elif (score == 5): #I'm wondering what would happen if you actually scored 5 points
        return "Results: You know your Pokemon really well"
    else:
        return "Results: You need to practice your Pokemon"
print(score_checker())