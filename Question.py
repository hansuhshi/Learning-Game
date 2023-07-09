class Question:
	#defines attributes of question and stores information about question
	def __init__(self, prompt, answer):
		self.prompt = prompt
		self.answer = answer
		
#array for maths multiple questions
mathsquestionmultipleprompts = [
	"1. Factorise 3x^2 - 27 completely\n\n(A) 3(x - 9)(x + 3)\n(B) 3(x^2 - 9)\n(C) 3(x - 3)(x + 3)\n(D) 3(x - 9)(x + 9)\n\nAnswer: ",
	"2. The largest integer n for which 2n/5 < 19/3 is\n\n(A) 16\n(B) 47\n(C) 6\n(D) 15\n\nAnswer: ",
	"3. How many solutions does the equation 38 - 2x^2 = -34 have?\n\n(A) 3\n(B) 2\n(C) 1\n(D) 0\n\nAnswer: ",
	"4. The solution of (x + 5)/3 = 10 is\n\n(A) x = 5\n(B) x = 25\n(C) x = -5\n(D) x = -20\n\nAnswer: ",
	"5. (m + 1)m/2 = m(m - 1)/2 is equivalent to\n\n(A) m + 1\n(B) m\n(C) 0\n(D) m - 1\n\nAnswer: ",
	"Use the information given below to answer questions 6 and 7.\n\nThe following list shows the time, in minutes, taken for Michael to finish all his practice exams.\n\n18, 19, 19, 21, 22, 25, 25, 25, 27, 29, 30, 31, 31, 36, 38\n\n6. Michael's median time is\n\n(A) 25 minutes\n(B) 18 minutes\n(C) 25 and a half minutes\n(D) 26 minutes\n\nAnswer: ",
	"Use the information given below to answer questions 6 and 7.\n\nThe following list shows the time, in minutes, taken for Michael to finish all his practice exams.\n\n18, 19, 19, 21, 22, 25, 25, 25, 27, 29, 30, 31, 31, 36, 38\n\n7. What is the interquartile range of the given data?\n\n(A) 4\n(B) 9\n(C) 5\n(D) 10\n\nAnswer: ",
	"8. An item is priced at $300 (including a 10% GST), what is the GST charged on this item?\n\n(A) $27.27\n(B) $272.73\n(C) $30\n(D) $270\n\nAnswer: ",
	"9. On a hot day, 30% of a tank's water was lost due to evaporation. A farmer then measures how much water is remaining in the tank and decides to increase this volume by 30% so the tank does not dry up.\n\nAssuming no other water was added except by the farmer, which of the following statements is true about the amount of water in the tank now?\n\n(A) There is now more water in the tank than at the start\n(B) There is now less water in the tank than at the start\n(C) There is now the same amount of water in the tank as the start\n(D) A conclusion cannot be made because the amount of water in the tank at the start was not given\n\nAnswer: ",
	"10. In a bag, there are red marbles, green marbles and blue marbles. The ratio of the coloured marbles are as follows:\n\nred:green = 4:5 and green:blue = 3:2\n\nWhat is the ratio of red marbles to blue marbles in this bag?\n\n(A) 2:1\n(B) 5:2\n(C) 4:3\n(D) 6:5\n\nAnswer: "
]

#array for elements of maths multiple questions
mathsquestionsmultiple = [
	Question(mathsquestionmultipleprompts[0], "c"),
	Question(mathsquestionmultipleprompts[1], "d"),
	Question(mathsquestionmultipleprompts[2], "b"),
	Question(mathsquestionmultipleprompts[3], "b"),
	Question(mathsquestionmultipleprompts[4], "b"),
	Question(mathsquestionmultipleprompts[5], "a"),
	Question(mathsquestionmultipleprompts[6], "d"),
	Question(mathsquestionmultipleprompts[7], "a"),
	Question(mathsquestionmultipleprompts[8], "b"),
	Question(mathsquestionmultipleprompts[9], "d")
]

#array for maths typed questions
mathstypedquestionprompts = [
	"1. 1/(x√x) = x^k, find the value of k.\n\nAnswer: ",
	"To convert between temperature in degrees Celsius (C) and degrees Farenheit, the formula is:\nC = 5/9(F - 32)\n\nUse this formula to answer questions 2 and 3.\n\n2. Find the boiling point of water (100 degrees Celcius) in degrees Farenheit.\n\nAnswer: ",
	"To convert between temperature in degrees Celsius (C) and degrees Farenheit, the formula is:\n\nC = 5/9(F - 32)\n\nUse this formula to answer questions 2 and 3.\n\n3. Convert 0 degrees Farenheit to degrees celcius.\n\nAnswer: ",
	"An investment of $800 earns simple interest at a rate of 4% per annum.\n\n4. How much simple interest would the investment gain in 5 years?\n\nAnswer: ",
	"An investment of $800 earns simple interest at a rate of 4% per annum.\n\n5. What is the toal value of the investment at the end of 5 years?\n\nAnswer: ",
	"6. A different bank offers a simple interest rate of 6% per annum, for how many years must $800 be invested so that it earns the same amount of simple interest as in question 3?\n\nAnswer: ",
	"7. √(2x - 3) = 9\n\nAnswer: ",
	"8. A rectangle with length L cm and width W cm, has a perimeter 40 cm. When 2 cm is deducted from its length and 2 cm s added to its width the rectangle becomes a square.\n\nFind the values of L/W.\n\nAnswer: ",
	"If x - 1/x = 3, find the value of x^2 + 1/x^2\n\nAnswer: ",
	"9. Solve: (3y - 14)/5 = 2y\n\nAnswer: ",
	"10. If (a + b)/(a - b) = 7/4, find a^2/b^2\n\nAnswer: "
]

#array for elements of maths typed questions
mathstypedquestions = [
	Question(mathstypedquestionprompts[0], float(-1.5)),
	Question(mathstypedquestionprompts[1], float(212.0)),
	Question(mathstypedquestionprompts[2], float(-18.0)),
	Question(mathstypedquestionprompts[3], float(160.0)),
	Question(mathstypedquestionprompts[4], float(960.0)),
	Question(mathstypedquestionprompts[5], float(3.33)),
	Question(mathstypedquestionprompts[6], float(42.0)),
	Question(mathstypedquestionprompts[7], float(1.5)),
	Question(mathstypedquestionprompts[8], float(-2.0)),
	Question(mathstypedquestionprompts[9], float(13.44))
]

#array for science multiple questions
sciencequestionpromptsmultiple = [
	"1. Living thing that are made from only one cell are called\n\n(A) Multicellular\n(B) Monocellular\n(C) Unicellular\n(D) Intracellular\n\nAnswer: ",
	"2. The job of the mitochondria in cells is to\n\n(A) Repair cell damage\n(B) Store cell waste\n(C) Control the cell's activities\n(D) Release energy\n\nAnswer: ",
	"3. On the microscope, the objective lens is found on the\n\n(A) Eyepiece\n(B) Nosepiece\n(C) Mouthpiece\n(D) Chin piece\n\nAnswer: ",
	"4. If the eyepiece lens has a magnification of 10 times, and the objective lens has a magnification of 4 times, the total magnification is\n\n(A) 2.5 times\n(B) 6 times\n(C) 14 times\n(D) 40 times\n\nAnswer: ",
	"5. Anton van Leeuwenhoek is credited with developing the first microscope. He worked as a\n\n(A) Textile trader\n(B) Scientist\n(C) Doctor\n(D) Optician\n\nAnswer: ",
	"6. Which of the following single-celled organisms is NOT a protist?\n\n(A) Bacteria\n(B) Amoeba\n(C) Sporozoa\n(D) Flagellate\n\nAnswer: ",
	"7. The major organ of the urinary system is\n\n(A) The kidney\n(B) The liver\n(C) The pancreas\n(D) The gall bladder\n\nAnswer: ",
	"8. Which of the following should NOT be present in you urine?\n\n(A) Water\n(B) Sugar\n(C) Urea\n(D) Salt\n\nAnswer: ",
	"9. The male part of the flower, or stamen, consists of the\n\n(A) Petal and sepals\n(B) Stigma and style\n(C) Ovules and ovary\n(D) Anther and filament\n\nAnswer: ",
	"10. The action of the male sex cell joinig with the female sex cell is called\n\n(A) Fertillisation\n(B) Pollination\n(C) Seeding\n(D) Flowering\n\nAnswer: ",
	"11. When a material cools down, its particles\n\n(A) Vibrate slower and make it contract\n(B) VIbrate faster and make it expand\n(C) Vibrate slower and make it expand\n(D) Vibrate faster and make it contract\n\nAnswer: ",
	"12. My particles are lined up in a regular repeating pattern and cannot change position. I am a:\n\n(A) Plasma\n(B) Gas\n(C) Liquid\n(D) Solid\n\nAnswer: ",
	"13. Sublimation is the name given to the change from:\n\n(A) Solid to liquid\n(B) Liquid to gas\n(C) Liquid to solid\n(D) Solid to gas\n\nAnswer: ",
	"14. Which of the following is a physical change?\n\n(A) Methane burning in air\n(B) Magnesium fizzing in hydrochloric acid\n(C) Salt dissolving in water\n(D) Glucose releasing energy in respiration\n\nAnswer: ",
	"15. Water contains 2 hydrogen atoms bonded on to 1 oxygen atom. Water is\n\n(A) An element\n(B) A compound\n(C) A mixture\n(D) None of the above\n\nAnswer: ",
	"16. If a perfume bottle is opened at the front of the classroom, eventually people at the back of the room can smell it. This is due to\n\n(A) Dissolution\n(B) Deflection\n(C) Diffusion\n(D) Distraction\n\nAnswer: ",
	"17. Kim measured the temperature change during a chemical reaction. The temperature went up. His experiment was:\n\n(A) Exothermic\n(B) Hyperthermic\n(C) Endothermic\n(D) Hypothermic\n\nAnswer: ",
	"18. The correct way to write the chemical formula for water is\n\n(A) H_2O\n(B) H2O\n(C) H^2O\n(D) H2o\n\nAnswer: ",
  "19. When the bathroom mirror steams up it is an example of\n\n(A) Melting\n(B) Boiling\n(C) Condensing\n(D) Freezing\n\nAnswer: ",
  "20. If a material can be compressed, it means it can\n\n(A) Change its shape\n(B) Be squeezed into a smaller space\n(C) Be poured through a tube\n(D) Be heated to a very high temperature\n\nAnswer: "
]

#array for elements of science questions
sciencequestionsmultiple = [
	Question(sciencequestionpromptsmultiple[0], "c"),
  Question(sciencequestionpromptsmultiple[1], "d"),
  Question(sciencequestionpromptsmultiple[2], "b"),
  Question(sciencequestionpromptsmultiple[3], "d"),
  Question(sciencequestionpromptsmultiple[4], "b"),
  Question(sciencequestionpromptsmultiple[5], "a"),
  Question(sciencequestionpromptsmultiple[6], "a"),
  Question(sciencequestionpromptsmultiple[7], "b"),
  Question(sciencequestionpromptsmultiple[8], "d"),
  Question(sciencequestionpromptsmultiple[9], "a"),
  Question(sciencequestionpromptsmultiple[10], "a"),
  Question(sciencequestionpromptsmultiple[11], "d"),
  Question(sciencequestionpromptsmultiple[12], "d"),
  Question(sciencequestionpromptsmultiple[13], "c"),
  Question(sciencequestionpromptsmultiple[14], "b"),
  Question(sciencequestionpromptsmultiple[15], "c"),
  Question(sciencequestionpromptsmultiple[16], "a"),
  Question(sciencequestionpromptsmultiple[17], "a"),
  Question(sciencequestionpromptsmultiple[18], "c"),
  Question(sciencequestionpromptsmultiple[19], "b")
]