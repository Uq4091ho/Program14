"""
Program 14: Sets and GIT
"""

__author__="Jared Lidenberg, Aishat Olowoshile"
__date__="4/22/2016"


class CustomSet:

   def __str__(self):
        """
        Description: returns a string, Coded by  Jared Lidenberg.
        Pre-Conditions: none
        Post-Conditions: converts attributes into str's for printing
        """
        tmp = "{"
        for el in self._setElements:
            tmp += el + ","
        tmp += "}"
        return tmp
        
   def __le__(self, secList):
        """
        Description: Checks for a subset, Coded by  Jared Lidenberg.
        Pre-Conditions: self and secList must be sets
        Post-Conditions: none
        """
        s1 = self
        s2 = secList
        for ele in s1:
            if not ele in s2:
                return False
        return True
        
   def __ge__(self, secList): #set 7
        """
        Description: Checks for superset, Coded by  Jared Lidenberg.
        Pre-Conditions: self and secList must be sets
        Post-Conditions: none
        """
        s1 = self
        s2 = secList
        for ele in s2:
            if not ele in s1:
                return False
        return True
