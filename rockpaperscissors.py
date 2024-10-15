# Elijah Sarver 2022-2024
import random as r
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

cls()
rps = ["rock", "paper", "scissors"]
cpuchoice = r.choice(rps)

userchoice = input("rock, paper, or scissors?:" )
    
if userchoice == cpuchoice:
    print("TIE")
elif userchoice == rps[0] and cpuchoice == rps[1]: 
    print("CPU picked", cpuchoice, ". You lost! ")
elif userchoice == rps[0] and cpuchoice == rps[2]:
    print("CPU picked", cpuchoice, ". You won! ")
elif userchoice == rps[1] and cpuchoice == rps[0]:
    print("CPU picked", cpuchoice, ". You won! ")
elif userchoice == rps[1] and cpuchoice == rps[2]:
    print("CPU picked", cpuchoice, ". You lost! ")
elif userchoice == rps[2] and cpuchoice == rps[1]:
     print("CPU picked", cpuchoice, ". You won! ")
elif userchoice == rps[2] and cpuchoice == rps[0]:
     print("CPU picked", cpuchoice, ". You lost! ")
else:
    print("Invalid Choice")
