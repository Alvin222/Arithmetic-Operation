import re
def getResult(mathOperation):
    if mathOperation["operator"] == "-":
       mathOperation["result"] = mathOperation["nums"][0] - mathOperation["nums"][1]
    elif mathOperation["operator"] == "+":
       mathOperation["result"] = mathOperation["nums"][0] + mathOperation["nums"][1]
    return mathOperation

def createStringOperation(mathOperation):
    theStringOperation = ""
    largest_length = 0
    for num in mathOperation["nums"]:
        if len(str(num))> largest_length:
           largest_length = len(str(num))
    if len(str(mathOperation["result"])) > largest_length:
        largest_length = len(str(mathOperation["result"]))
    for space in range(largest_length-len(str(mathOperation["nums"][0]))+2):
        theStringOperation += " "
    theStringOperation += "%s\n+ " % mathOperation["nums"][0]
    for space in range(largest_length-len(str(mathOperation["nums"][1]))):
        theStringOperation += " "
    theStringOperation += "%s\n" % mathOperation["nums"][1]
    for space in range(largest_length+2):
        theStringOperation += "-"
    theStringOperation += "\n"
    for space in range(largest_length-len(str(mathOperation["result"]))+2):
        theStringOperation += " "
    theStringOperation += "%s" % mathOperation["result"]
    return theStringOperation

def makeStringToSide(firstString,secondString):
    searchNewLine =  re.search("\n",firstString)
    firstSplit = firstString.split("\n")
    secondSplit = secondString.split("\n")
    newString = ""
    for i in range(0,len(firstSplit)):
        newString += firstSplit[i] + "\t" +secondSplit[i]
        if i < len(firstSplit) -1 :
           newString += "\n"
    return newString


def arithmetic_arranger(problems):
    operation_list = []
    solution = ""
    """check the arithmetic and digits first"""
    if len(problems) > 5:
       raise Exception("Error: Too many problems.")
    for math in problems:
      mathOperation = {}
      findArithmetic = re.search("[+-]",math)
      if findArithmetic:
         mathOperation["operator"] = math[findArithmetic.start()]
         mathOperation["nums"] = []
         for digit in re.findall("\d{1,4}",math):
            try:
                if int(digit) > 4000:
                   raise Exception("Error: Numbers cannot be more than four digits.")
                mathOperation["nums"].append(int(digit))
            except:
                raise Exception("Error: Numbers must only contain digits.")
         operation_list.append(mathOperation)
      else : 
        raise Exception("Error: Operator must be '+' or '-'.")
    result = list(map(getResult,operation_list))
    for operation in result:
        if solution:
           solution = makeStringToSide(solution,createStringOperation(operation))
        else:
           solution = createStringOperation(operation)
    return solution