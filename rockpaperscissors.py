# Elijah Sarver 2022
import random as r

rps = ["rock", "paper", "scissors"]
cpuchoice = r.choice(rps)
userchoice = input("rock, paper, or scissors?:" )

if userchoice == cpuchoice:
    print("CPU picked", cpuchoice , ". You won!"  )
elif userchoice != rps:
    print("CPU picked", cpuchoice, ". You lost! ")
else:
    quit()