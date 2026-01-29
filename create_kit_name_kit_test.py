import requests

import sender_stand_request as sender

def testLowerBoundaryName():
    sender.positiveAssert(sender.nameKit('a'))

def testUpperBoundaryName():
#Crea un nombre de 511 carácteres
    name = "A"
    for i in range(1,511):
        name += 'a'

    sender.positiveAssert(sender.nameKit(name))
    

def testNotAllowedLowerBoundaryName():
    sender.negativeAssert(sender.nameKit(""))

def testNotAllowedUpperBoundaryName():
#Crea un nombre de 512 carácteres
    name = "A"
    for i in range(1,512):
        name += 'a'

    sender.negativeAssert(sender.nameKit(name))

def testSpecialCharactersName():
    sender.positiveAssert(sender.nameKit("№%@\""))

def testNameWithSpaces():
    sender.positiveAssert(sender.nameKit("A Aaa"))

def testNameWithNumbers():
    sender.positiveAssert(sender.nameKit("123"))

def testEmptyBodyName():
    sender.negativeAssert({})

def testNameIsNumber():
    sender.negativeAssert(sender.nameKit(123))
