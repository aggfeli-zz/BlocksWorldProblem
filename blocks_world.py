"""Blocks world problem"""

from search import * # This file imports utils.py so it should be in the same folder
import sys # System-specific parameters and functions

class blocks_world(Problem) :
	"""Subclass of search.Problem"""
	
	def __init__(self, i, g) :
		"""Sets initial state and goal."""
		self.initial = i; self.goal = g
#_______________________________________________________________
	
	def __isValidState(self, m, c, j) :
		"""Checks if a state is valid. """
		if len(c) == 0 and m == self.goal[j]: #If state is empty and possible action leads to goal return true
			return True
		if len(self.goal[j]) !=0 and m == ():  #If goal state isn't empty and possible action is then error
			return False
		if len(c) != 0 and len(m) > len(c):  #if state isn't empty and possible-action's length is bigger 
			if m[len(m)-1] != c[0] or self.goal[j] != m: #If state's first cube differs from possible-action's or possible action...  
				return False					#...differs from goal state error
			else:
				return True
		if len(m) != (len(c) - 1): 
			return False
		if len(m) == 0 and m != () : # Error ! 
			return False		
		if (len(m) == 1 and m[0] != c[1]) or (len(m) == 1 and m[0] == ()): # Error !
			return False	
		if (len(m) == 2 and m[0] != c[1]) or (len(m) == 2 and m[1] != c[2]): # Only the first block can be moved 
			return False
		return True
#_______________________________________________________________

	def actions(self, state) :
		"""Returns the actions that can be executed in the state"""
		# possibleActions are all actions that may be executed, but some of 
		# them may lead in invalid state. So possibleActions should be filtered
		possibleActions = [('a'),('b'),('c'),('d'),('e'),(), ('a','b'), ('a','c'), ('a','d'), ('a','e'), ('b','a'), ('b','c'),('b','d'), 					('b','e'), ('c','a'), ('c','b'), ('c','d'), ('c','e'), ('d','a'),('d','b'), ('d','c'), ('d','e'), ('e','a'), 					('e','b'), ('e','c')]
		validActions = [] # It will store only actions that lead in a valid state
		if state[0] != self.goal[0]:		
			for possibleAction in possibleActions :
				m = possibleAction
				c = state[0]
				if self.__isValidState(m, c, 0) :
					validActions.append(possibleAction)
					return validActions
		if state[1] != self.goal[1]:			
			for possibleAction in possibleActions :
				m = possibleAction
				c = state[1]
				if self.__isValidState(m, c, 1) :
					validActions.append(possibleAction)
					return validActions
		if state[2] != self.goal[2]:
			for possibleAction in possibleActions :
				m = possibleAction
				c = state[2]
				if self.__isValidState(m, c, 2) :
					validActions.append(possibleAction)
					return validActions
		if state[3] != self.goal[3]:			
			for possibleAction in possibleActions :
				m = possibleAction
				c = state[3]
				if self.__isValidState(m, c, 3) :
					validActions.append(possibleAction)
					return validActions
		if state[4] != self.goal[4]:
			for possibleAction in possibleActions :
				m = possibleAction
				c = state[4]
				if self.__isValidState(m, c, 4) :
					validActions.append(possibleAction)

#		print len(validActions), 1
#		for validAction in validActions :
#			print "\t", validAction, self.result(state, validAction)
#			raw_input("pause")
		return validActions
#_______________________________________________________________


	def result(self, state, action) :
		""""""
		s0 = state[0]
		s1 = state[1]
		s2 = state[2]
		s3 = state[3]
		s4 = state[4]

		if self.goal[2] != ():
			temp1 = self.goal[2][len(self.goal[2])-1]
		else:
			temp1 =()
		if self.goal[3] != ():
			temp2 = self.goal[3][len(self.goal[3])-1]
		else:
			temp2 =()
		if self.goal[4] != ():
			temp3 = self.goal[4][len(self.goal[4])-1]
		else:
			temp3 =()

		if s0 != self.goal[0] :
			a = s0[0]  			#Take the first cube and search the right place to put it
			if len(s0) > 0:
				if len(s1) == 0:
					s1 = a
				elif s2 == () and temp1 == a[0]:
					s2 = a
				elif s3 == () and temp2 == a[0]:
					s3 = a
				elif s4 == () and temp3 == a[0]:
					s4 = a
				else:
					a = 0
			
			s0 = action
		elif s1 != self.goal[1]:
			a = s1[0]			#Take the first cube and search the right place to put it
			if len(s1) > 1:			
				if len(s0) == 0:
					s0 = a
				elif s2 == () and temp1 == a:
					s2 = a
				elif s3 == () and temp2 == a:
					s3 = a
				elif s4 == () and temp3 == a:
					s4 = a
				else:
					a = 0
			s1 = action
		elif s2 != self.goal[2]:
			s2 = action
		elif s3 != self.goal[3]:
			s3 = action
		elif s4 != self.goal[4]:
			s4 = action
		else : 
			a = 0

		return (s0,s1,s2,s3,s4)
