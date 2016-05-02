'''
__author__: Aishat Olowoshile
__date__: 04/26/2016

DESCRIPTION:
'''

class CustomSet:

    '''
    description: intializes the object of class customSet. setElement is a list
    precondition: setList is a list of a set of numbers
    post-condition: Stores private data that intialized to the values provided
    Function by Aishat Olowoshile
    '''
    def __init__(self, setList):
        self._setElement = []
        for num in setList:
            if num not in self._setElement:
                self._setElement.append(num)

        self._setElement.sort()

    '''
    description: getter method to retrieve the setList
    precondition: object of the class self
    post-condition: none
    Function by Aishat Olowoshile
    '''

    def getsetElement(self):
        return self._setElement
    
    '''
    description: appends integers common in tmpList and somList to intersectList
    precondition: tmpList and som list are lists of integers
    post-condition: intersectList becomes a list of integers
    Function by Aishat Olowoshile
    '''

    def __and__(self, tmpList):
        intersectList = []
        for num in tmpList.getsetElement():
            if num in self._setElement:
                intersectList.append(num)
        return CustomSet(intersectList)
    '''
    description: appends the union of two lists of integers to make a set of integers
    precondition: tmpList and som list are lists of integers
    post-condition: unionList becomes a list of integers
    Function by Aishat Olowoshile

    '''
        
    def __add__(self, tmpList):
        unionSet = tmpList.getsetElement() + self._setElement
        return CustomSet(unionSet)
    
    '''
    description: appends the union of two lists of integers to make a set of integers
    precondition: tmpList and som list are lists of integers
    post-condition: unionList becomes a list of integers
    Function by Aishat Olowoshile

    '''
         

    def __str__(self):
        tmp = ""
        #tmp += "The set is: " + str(self._setElement)
        for element in self._setElement:
            tmp += (str(element) + " ")
        return tmp
    
    '''
    description: makes a list of integers in tmpList that is not in somList
    precondition: tmpList and som list are lists of integers
    post-condition: diffSets becomes a list of integers
    Function by Aishat Olowoshile
    '''

    def __sub__(self, tmpList):
        diffSets = []
        for num in self._setElement:
            if num not in tmpList.getsetElement():
                diffSets.append(num)
        return CustomSet(diffSets)
        

#===================================================================
#Test program
#===================================================================

x = [1,2,3,4,5,6,7,8,9]
y = [7,9,6,9,0]
z = x + y
s1 = CustomSet(z)
print("The set of number is: ", s1)
print()
s2 = CustomSet([2,4,5,6,3,4,7])
print("Printing a list with no duplicate: ", s2)
print()

print("="*45)
print("TESTING THE FUNCTIONS ON THE TWO SETS BELOW")
print("="*45)
print()
print("The sets are: ", "[", s1, "] &", "[" ,s2 ,"]")
print() 
s3 = s1 + s2
print("The union of the sets: ", s3)
print()
s4 = s1  & s2
print("The intersection of the sets: ", s4)
print()
s5 = s1 - s2
print("The difference of the sets: ", s5) 

  
