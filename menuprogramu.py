import os
class MenuProgramu:
    
    def __init__(self,name_input , boot) -> None:
         self.name_input=name_input
         self.boot=boot
    

    def menuglowne(self):
         os.system("cls")
         print(f"{self.boot} >  wyglada na to ze ten kanał jest jeszcze  w budowie {self.name_input}")