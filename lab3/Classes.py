class Up():
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = input("Input smth: ")
    
    def printString(self):
        print(self.s.upper())


s = Up()

s.getString()
s.printString()
