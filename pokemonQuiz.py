# Pokemon Quiz
# Author: Justin Li
# Date: Dec 4th
import time

score = 0
print("Welcome to Justin's Pogger's Pokemon Quiz")
time.sleep(1.5)
name = input("Could I get your name? ")
print(f"Alright {name} let's start!")
time.sleep(1)

q1 = input("Which of these pokemon evolve from Wooper? A,B,C,or D\n A.Hoopa\n B.Swampert\n C.Quagsire\n D.Stunfisk\n").upper().strip("!,.?")
if q1 == "C":
    print("Nice one!")
    score += 1
else:
    print("Dang nice try.")

q2 = (input("What level does Weedle evolve at? (NUMBER)\n")).upper().strip("!,.?")
if q2 == "7" or q2 == "SEVEN":
    print("Good job!")
    score += 1
else:
    print("Good try.")

q3 = input("Who is the 5th Gym Leader in Gen 3?\n").upper().strip("!,.?")
if q3 == "NORMAN":
    print("Wow!")
    score += 1
else:
    print("Unlucky.")

q4 = input("Who is the main villan in Pokemon Black and White?\n").upper().strip("!,.?")
if q4 == "GHETSIS":
    print("Holy nice job!")
    score += 1
else:
    print("Aw good try")

q5 = (input("What is the base pp of Roost?\n")).upper().strip("!,.?")
if q5 == "10" or q5 == "TEN":
    print("Ayy")
    score += 1
else:
    print("Man.")

print(f"Okay that's the end of the quiz.\n Your final score is {score}/5\n That's {int(score / 5 * 100)}%!")