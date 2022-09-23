#The interactive visualization package Plotly is particularly well suited for visualizations that will be displayed in the browser because the image is automatically scaled to fit the viewer's screen.
#In addition, Plotly generates interactive visualizations - when the user hovers the mouse over some elements, extended information about this element appears on the screen.
#Dice rolls are used in mathematics to explain different types of data analysis, in real-world applications (: casinos) and in regular games (: Monopoly, role-playing games, etc.').
from random import randint

class Die():
 	"""A class that represents one die."""
 	def __init__(self, number_sides=6):
 		"""The default is a six-sided dice."""
 		self.number_sides = number_sides

 	def roll(self):
 		""""Returns a random number between 1 and the number of faces."""
 		return randint(1, self.number_sides)



