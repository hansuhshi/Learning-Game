#use this for countdown timer and slowtype
import time

#use for checking what system type and for quitting code
import os

#used for quitting and restarting the code
import sys

#used to make timer run side by side with quiz
import threading

#used to trace whenever the thread needs to be killed
import trace

#questions and class for questions
from Question import *

#this function will check if there is a valid input for multiple choice and yes or no style questions
def userinput(answer, conditions):
	print()
	error = ""
	while True:
		#prints the first/previous error
		if error:
			print(error)
			print()
		userinput = input(answer)
		#if there is no input continue the loop
		if userinput == None:
			continue
		for condition, errormessage in conditions:
			#if the user input is invalid under this condition, save the error message for this condition to be printed next time in the loop
			if not condition(userinput.strip()):
				error = errormessage
				break
		#if there are no errors return the input
		else:
			return userinput

#validates input so user can only input 'yes' or 'no'
def confirmyesno(input):
	return input.lower() == "yes" or input.lower() == "no"

#response to the input
def askyesno(question):
	yesnooutput = userinput(question, [[confirmyesno, "Please answer Yes or No"]])
	return yesnooutput

#validates input so user can only input chosen repsonses
def confirmmultiple(input):
	return input.lower() == "a" or input.lower() == "b" or input.lower() == "c" or input.lower() == "d"

#response to the input
def askmultiple(question):
	multipleoutput = userinput(question, [[confirmmultiple, "Please answer A, B, C or D"]])
	return multipleoutput

#this function will end or restart the code
def restart():
	restart = askyesno("Do you want to restart the program?\n(Yes|No)\n\nSelection: ")
	#this will unconditionally restart the running program from scratch
	if restart.lower() == "yes":
		clearscreen()
		os.execl(sys.executable, '"{}"'.format(sys.executable), *sys.argv)
	#this will exit the running program
	elif restart.lower() == "no":
		sys.exit()

#this class uses traces to kill threads found on stackoverflow
class threadwithtrace(threading.Thread):
	def __init__(self, *args, **keywords):
		threading.Thread.__init__(self, *args, **keywords)
		self.killed = False

	#start() is slightly modified to set the system trace function using settrace(). the local trace function is defined such that, whenever the kill flag (killed) of the respective thread is set, a SystemExit exception is raised upon the excution of the next line of code, which end the execution of the target function func. now the thread can be killed with join().
	def start(self):
		self.__run_backup = self.run
		self.run = self.__run      
		threading.Thread.start(self)

	def __run(self):
		sys.settrace(self.globaltrace)
		self.__run_backup()
		self.run = self.__run_backup
	def globaltrace(self, frame, event, arg):
		if event == 'call':
			return self.localtrace
		else:
			return None

	def localtrace(self, frame, event, arg):
		if self.killed:
			if event == 'line':
					raise SystemExit()
		return self.localtrace

	def kill(self):
		self.killed = True

#this function clears the screen
def clearscreen(numlines=100):
	#checks if it is Unix/Linux/MacOS/BSD/etc
	if os.name == "posix":
		os.system("clear")
	#checks if it is DOS/Windows
	elif os.name in ("nt", "dos", "ce"):
		os.system("CLR")
	#fallback for operating system
	else:
		print("\n" * numlines)

#this function starts a countdown feature for easy
def countdowneasy():
	global timer
	timer = 900
	for t in range(900):
		timer = timer - 1
		time.sleep(1)
	clearscreen()
	print("Sorry you didn't make it in time.")
	time.sleep(2.5)
	clearscreen()
	#quits the code
	os._exit(0)

#this function starts a countdown feature for normal
def countdownnormal():
	global timer
	timer = 600
	for t in range(600):
		timer = timer - 1
		time.sleep(1)
	clearscreen()
	print("Sorry you didn't make it in time.")
	time.sleep(2.5)
	clearscreen()
	os._exit(0)

#this function starts a countdown feature for hard
def countdownhard():
	global timer
	timer = 300
	for t in range(300):
		timer = timer - 1
		time.sleep(1)
	clearscreen()
	print("Sorry you didn't make it in time.")
	time.sleep(2.5)
	clearscreen()
	os._exit(0)

#this function selects the difficulty
def difficultyselector():
	global difficultythread
	print("Difficulties:")
	print()
	print("A: Easy")
	print("B: Normal")
	print("C: Hard")
	print("D: Main menu")
	difficulty = askmultiple("Selection: ")
	if difficulty.lower() == "a":
    #converts timer to a thread so it can run while the quiz is running
		difficultythread = threadwithtrace(target=countdowneasy)
		difficultythread.start()
	elif difficulty.lower() == "b":
		difficultythread = threadwithtrace(target=countdownnormal)
		difficultythread.start()
	elif difficulty.lower() == "c":
		difficultythread = threadwithtrace(target=countdownhard)
		difficultythread.start()
	elif difficulty.lower() == "d":
		clearscreen()
		mainmenu()

#this function is for maths test questions
def runmathsmultipletest(mathsquestionsmultiple):
	global mathsscore
	mathsscore = 0
	#loops through each question gets user input and check if user is right and if input type is correct
	for question in mathsquestionsmultiple:
		answer = askmultiple(question.prompt)
		if answer == question.answer:
			print()
			print("Correct")
			#adds to score if correct
			mathsscore += 1
			time.sleep(0.5)
		else:
			print()
			print("Incorrect")
			time.sleep(0.5)
		clearscreen()

#this function is for the typed maths test
def runmathstypedtest(mathstypedquestions):
	global mathsscore
	for question in mathstypedquestions:
	#loops through each question gets user input and checks if user is right and if input type is correct
		while True:
			try:
				answer = float(input(question.prompt))
				break
			except ValueError or TypeError or RuntimeError:
				print()
				print("Please type a number in.")
				print()
				continue
		if answer == question.answer:
			print()
			print("Correct")
			mathsscore += 1
			time.sleep(0.5)
		else:
			print()
			print("Incorrect")
			time.sleep(0.5)
		clearscreen()
	difficultythread.kill()
	difficultythread.join()

#this function is for science test questions
def runsciencemultipletest(sciencequestionsmultiple):
	global sciencescore
	sciencescore = 0
	#loops through each question getn user input and check if user is right and if input type is correct
	for question in sciencequestionsmultiple:
		answer = askmultiple(question.prompt)
		if answer == question.answer:
			print()
			print("Correct")
			sciencescore += 1
			time.sleep(0.5)
		else:
			print()
			print("Incorrect")
			time.sleep(0.5)
		clearscreen()
	difficultythread.kill()
	difficultythread.join()

#this function prints out the rules
def rules():
	print("1. If there is a multiple choice style question please type A, B, C or D based on your answer.")
	print("2. If there is a typed response please type an integer only without units and if it is a fraction make it a decimal number to 2 decimal places.")
	print("3. If the number you calculate has reccuring/infinite decimal places round the number to 2 decimal places.")
	print("4. If it asks for a typed response then only put letters in.")
	print("5. There will be an input box so wait for it to appear.")
	print("6. Don't spam enter because it will only make it harder for you as there will be too much text on the screen.")
	print("7. Make sure that you don't input an answer right after you answer one because it may cause the next question to be answered without you answering your answer.")
	print("8. ^ means to the power of, _ means subscript, / means division and pay attention to these symbols and brackets.")
	print("9. Easy mode is 15 minutes. Normal mode is 10 minutes. Hard mode is 5 minutes. Please choose one that suits your abilities.")
	print("10. If you do not finish the quiz in time please do not be angry and spam enters. Just don't spam enters at all. The code will exit and re run it to do the quiz again")
	print()
	print("Press enter to go back to main menu.")
	input()
	clearscreen()
	mainmenu()

#this function is for the main menu
def mainmenu():
	print("Welcome to Ahn Academy")
	print("Khan Academy but without the K. A world class education for anyone, anywhere. 100% free.")
	print("Join Ahn Academy to get personalized help with what you’re studying or to learn something completely new.")
	print()
	print("Press enter to continue.")
	input()
	clearscreen()
	print("Main menu:")
	print()
	print("A: Maths")
	print("B: Science")
	print("C: Rules")
	print("D: Quit")
	selection = askmultiple("Selection: ")
	if selection.lower() == "a":
		clearscreen()
		maths()
	elif selection.lower() == "b":
		clearscreen()
		science()
	elif selection.lower() == "c":
		clearscreen()
		rules()
	elif selection.lower() == "d": 
		sys.exit()

#this function is for the maths introduction then lead into questions
def maths():
	print("Welcome to the maths section.")
	print("Please select the difficulty.")
	print("")
	difficultyselector()
	while timer > 0:
		clearscreen()
		print("Section 1: Multiple choice response.")
		print()
		runmathsmultipletest(mathsquestionsmultiple)
		print("Section 2: Numeric response.")
		print()
		runmathstypedtest(mathstypedquestions)
		#tallies total score out of total questions
		print("You got " + str(mathsscore) + "/" + str(len(mathsquestionsmultiple) + len(mathstypedquestions)))
		break
	restart()

#this function is for the science introduction then lead into questions
def science():
	print("Welcome to the science section.")
	print("Please select the difficulty")
	print("")
	difficultyselector()
	while timer > 0:
		clearscreen()
		print("Section 1: Multiple choice response.")
		print() 
		runsciencemultipletest(sciencequestionsmultiple)
		#tallies total score out of total questions
		print("You got " + str(sciencescore) + "/" + str(len(sciencequestionsmultiple)))
		break
	restart()

mainmenu()