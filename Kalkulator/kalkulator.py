import os
import Kalkulator.podstawowy as podstawowy
import Menu.menuprogramu as menuprogramu
class MenuKalkulaotr:
    def __init__(self,boot,name_input )->str:
       self.boot=boot
       self.name_input=name_input

    def powitanie(self):
        print(f"{self.boot} > witam w  Menu Kalkulatora {self.name_input}\n"
              f"")


    def menu(self):
        kalkulatory=["1: Prosty Kalkulator", "2: Kalkulator statystyczny" , "3: Algebra Liniowa  " , "10 : powrot " ]
        print("Kalkulatory:")

        for x in kalkulatory:
            print(x)

        

    def button(self):
        try: 
            button_input=int(input(f"{self.boot}> {self.name_input} Mozesz teraz wybrać który mam kalkulator dla ciebie uruchomic: "))
        except ValueError:
            print("error") 
        else:
            match button_input:
                case 1: 
                    os.system("cls")
                    prosty=podstawowy.Prostykalkulator(self.boot,self.name_input)
                    prosty.menu()

                case 2: 
                     print("w budowie")

                case 3: 
                     print("w budowie")
                case 10: 
                    os.system("cls")
                    ret=menuprogramu.MenuProgramu(self.boot,self.name_input)
                    ret.menuglowen()
                    ret.button()
                    ret.error()
                case _ :
                    print("cos poszło nie tak ")          
    
   
