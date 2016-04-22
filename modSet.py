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
