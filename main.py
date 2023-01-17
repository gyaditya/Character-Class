class character:
    def __init__(self, name, firstline, secondline):
        self.name = name
        self.firstline = firstline
        self.secondline = secondline
        self.rank = 0 
    
    def speak(self, line):
        if line == 1:
            print(self.firstline)
        else:
            print(self.secondline)
    
    def set_rank(self,new_rank): 
        self.rank = new_rank
        print(new_rank)
        
        
# Task1

character_1 = character("Naruto", "Rasengan", "Ramen")
character_2 = character("Sauske", "Chidori", "HIYA")


        
# Task 2 

character_1.speak(1)
character_2.set_rank(3)
character_1.speak(2)