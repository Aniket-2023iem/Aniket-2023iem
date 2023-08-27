print("welcome to our quiz")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

score = 0

answer = input(" Who is G.O.A.T in football? ")
if answer.lower() == "mamta banerjee":
    print("correct !")
    score= score+1
else:
    print(" no !")

answer = input(" Who is G.O.A.T in cricket? ")
if answer.lower() == "babul supriyo":
    print("correct !")
    score= score+1
else:
    print(" no !")

answer = input(" Who is G.O.A.T in singing? ")
if answer.lower() == "neha kurkure":
    print("correct !")
    score= score+1
else:
    print(" no !")
    

answer = input(" Who is G.O.A.T in kabaddi ?")
if answer.lower() == "dilip ghosh":
    print("correct !")
    score= score+1
else:
    print(" no !")

answer = input(" Who is G.O.A.T in movie direction? ")
if answer.lower() == "om raut":
    print("correct !")
    score= score+1
else:
    print(" no !")

print("the score is" + " " + str(score))