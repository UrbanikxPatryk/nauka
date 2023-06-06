import os
import menuprogramu
boot = "Marsx"
class SystemStart:
 
    
    def przywitanie(self):
        os.system("cls")
        print(" \t\t\t\t witam cie w oprogramowaniu Varo \n"
              f"\t\t{boot} > witam cie jestem {boot} zostałem stworzony przez programistow \n"
              f"\t\t{boot} > By pomoc ci w  korzystaniu aplikacji ale chętnie bym chciał pozanć twoje imie   " )
              
       
        
    def name(self):
         name_input=input("Podaj swoje imie : ")
         self.odpowiedzi(name_input)

    def sprawdznie(self, name_input ):
         if len(name_input)<=2:
             return False 
         else:
            return True
    
             
    def odpowiedzi(self,name_input):
        
        if self.sprawdznie(name_input)==True:
            print(f"{boot} > miło cie poznac {name_input}")
            self.przejscie(name_input)
        else:
          self.return_function()   


    def przejscie(self,name_input):
        try:
            button_input=int(input(f"{boot} > mozesz przejsz {name_input} do menu \n1 : menu Główne \n "))
        except ValueError:
            os.system("cls")
            print(f"{boot} > upss cos poszło nie tak mała podpowiez  musisz uzywać liczb a  nie liter :)  sproboj jeszcze raz ")
            self.przejscie(name_input)
        else:
            match button_input:
                case 1 :
                    menu=menuprogramu.MenuProgramu(name_input, boot)
                    menu.menuglowne() 
             


#-------------------------------------------------------------------
    def return_function(self):
        print(f"{boot} > cos poszło nie tak moze chcesz sprobować jeszcze raz  lub  czy  nie chcesz wpisywać iminia ? \n"
              f"{boot} > wybierz co chcesz zrobić   ") 
        try: 
       
            button_input=int(input(f"{boot} > 1: Sproboj jeszcze raz  2: Nie chce wpisywać iminia "))
       
        except ValueError:
          
            os.system("cls")
            print(f"{boot} > mała podpowiedż musisz uzywać liczb anie liter :) \n"
                  "#########################################################")
            self.return_function()
      
        else:
            match button_input:
                case 1: 
                    m=SystemStart()       
                    m.przywitanie()
                    m.name()   
                case 2:
                    print(f"{boot} > przykro mi ze nie chcesz podać swojego iminia ale rozumiem to bedziesz jako anonimowy urzytkownikien")
                    name_input="bez nazwy  "
                    next=menuprogramu.MenuProgramu(name_input, boot)
                    next.menuglowne()

                
                case _ : 
                    print(f"{boot} > przykro mi nie odnalazłem przyciksu :()")
                    self.return_function()
         

m=SystemStart()
m.przywitanie()
m.name()