import random
import signal
import sys
import time

__base__PlayerTimer = 10
__base__WaitTimer = 180

def __times__Up__(signum, frame):
	raise Exception()

signal.signal(signal.SIGALRM, __times__Up__)

class DiceGen:

	def __init__ (self, lowbound, uppbound, numDice):
		self.l = lowbound
		self.u = uppbound
		self.nD = numDice

	def play(self, numberPlayer, listPlayer):

		print "Rolling", self.nD, "[", self.l,"-", self.u, "] dice"

		for x in range(0, numberPlayer):
			time.sleep(1)
			out = []

			for k in range(0, self.nD):
				out.append(random.SystemRandom().randint(self.l,self.u))

			print listPlayer[x], "rolled", out

lB = 1
uB = 6
nD = 1
print "Hello, This is DiceBot. Lets play!"
print "Type \"c\" to customize the game, type \"d\" to roll one 6-sided Die!"

customize = False

signal.alarm(__base__WaitTimer)
timesUp = False
while (not timesUp):
	try:
		inp = raw_input()

		if (inp == "d"):
			customize = False
			timesUp = True
			signal.alarm(0)
		elif (inp == "c"):
			customize = True
			timesUp = True
			signal.alarm(0)

	except:
		customize = False
		timesUp = True

if customize:
	lB = input("Smallest number on Die [default = 1]: ")
	uB = input("Largest number on Die [default = 6]: ")
	nD = input("Number of Dice to Roll [default = 1]: ")

Dice = DiceGen(lB, uB, nD)

play = True
while (play):

	numberPlayer = 0
	listPlayer = []

	
	print "Please type \"j\" if you wish to play, you have", __base__PlayerTimer, "seconds."
	
	signal.alarm(__base__PlayerTimer)
	timesUp = False
	while(not timesUp):
		try:
			playerName = raw_input()
			numberPlayer = numberPlayer + 1
			listPlayer.append(playerName)

		except:
			timesUp = True

	if (numberPlayer != 0):
		print "Times Up!"
		Dice.play(numberPlayer, listPlayer)
	else:
		print "No Players :("


	signal.alarm(__base__WaitTimer)
	timesUp = False
	while (not timesUp):
		try:
			print "Roll more? Type \"y\" or \"n\". Auto-Exiting in", __base__WaitTimer, "seconds" 
			more = raw_input()

			if (more == "n"):
				play = False
				timesUp = True
			elif (more == "y"):
				play = True
				timesUp = True

		except:
			play = False
			timesUp = True



