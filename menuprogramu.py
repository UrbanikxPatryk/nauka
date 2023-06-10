import os
class MenuProgramu:
    
    def __init__(self,name_input , boot) -> None:
         self.name_input=name_input
         self.boot=boot
    
    
    def welcomMenu(self):   # do dopracowanie przywitania 
         os.system("cls")
         print(f"{self.boot} > Witam cie jeszcze raz serdecznie   {self.name_input} ale już  w Menu Glownym tutaj znajdziesz zeczy ktore cie interesują  \n ")
         
         
    def menuglowen(self):
      # dodanie zegara 
     print(f"\t\t\t\t\t\t\t\t\t Uzytkownnik : {self.name_input}")
     print("\t\t\t\tMenu Glowne\n"
           "1: Kalkulator\n"
           "2: Wykresy\n"
           "3: Wprowadzaine danych\n"
           "\t\t\t0: Zakoniczenie Programu\n"
           "\t\t\t|-----------------------------| ")