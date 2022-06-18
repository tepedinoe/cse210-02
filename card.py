import random

class Card:
    """display the cards radnomly.Atributes:
    value (int): random number
    nextValue (int): second number to compare"""
    def __init__(self):
        self.value = 0
        self.nextValue = 0
    
    def newNumber(self):
        """Generates a new number"""
        self.value = random.randint(1, 13)
        print(f"The Card is: {self.value} ")

        """Generates a second random number to compare with the first one"""
    def nextNumber(self):
        self.nextValue = random.randint(1, 13)
        print(f"Next Card was: {self.nextValue} ")

 
        
    


            

    

        
