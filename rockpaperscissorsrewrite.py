#Elijah Sarver 2024
import random as r
RPS = ["rock", "paper", "scissors"] 

def intro() :
	cpuchoice = r.choice(RPS)
	userchoice = input("rock, paper, or scissors? q to quit: ")
	if userchoice == cpuchoice:
		print("TIE"); intro()
	elif userchoice == RPS[0] and cpuchoice == RPS[1]: 
		print("CPU picked", cpuchoice, ". You lost! "); intro()
	elif userchoice == RPS[0] and cpuchoice == RPS[2]:
		print("CPU picked", cpuchoice, ". You won! "); intro()
	elif userchoice == RPS[1] and cpuchoice == RPS[0]:
		print("CPU picked", cpuchoice, ". You won! "); intro()
	elif userchoice == RPS[1] and cpuchoice == RPS[2]:
		print("CPU picked", cpuchoice, ". You lost! "); intro()
	elif userchoice == RPS[2] and cpuchoice == RPS[1]:
		 print("CPU picked", cpuchoice, ". You won! "); intro()
	elif userchoice == RPS[2] and cpuchoice == RPS[0]:
		 print("CPU picked", cpuchoice, ". You lost! "); intro()
	elif userchoice == "q":
		 print("Have a nice day!")
		 exit()
	else:
		print("Invalid Choice")
		intro()
intro()