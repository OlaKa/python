class InputOutString:
    def __init__(self):
        self.s = ""

    def getName(self):
        self.s=raw_input("What is your name? Followed by [ENTER]:")
        

    def printString(self,name):
        print "No Python code here yet! %s" %name

strObj = InputOutString()
strObj.getName()
strObj.printString(strObj.s)
