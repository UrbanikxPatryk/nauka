import os
import Kalkulator.kalkulator as kalkulator
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
     print("\t\t\t\t\tMenu Glowne\n")
     listpoleceni=["1: Kalulator", "2: Generator Wykresu " , "0: Exit "]
     
     for x in listpoleceni:
         print(x)

     self.button()

    def button(self):
        try : 
             
               button_input=int(input(f"{self.boot} > Prosze {self.name_input} : "))

        except:
               
               self.error()   
        else:
            match button_input:
                case 1 : 
                    os.system("cls")
                    kal=kalkulator.MenuKalkulaotr(self.boot,self.name_input)
                    kal.powitanie()
                    kal.menu()
                    kal.button()
                case 2 : 
                    os.system("cls")
                    print(f" {self.boot}  W  budowie")   
                case 3 : 
                    os.system("cls")
                    print(f" {self.boot}  W  budowie")
                case 0 : 
                     os.system("cls")
                     exit("Zakoniczenie Programu .......")
                         
 

    def error(self):
        os.system("cls")
        print(f"{self.boot} > error ")

