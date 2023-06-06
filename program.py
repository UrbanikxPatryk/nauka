import os
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
        
        else:
          self.powrot()   
         

    def powrot(self):
        print(f"{boot} > cos poszło nie tak moze chcesz sprobować jeszcze raz  lub  czy  nie chcesz wpisywać iminia ? \n"
              f"{boot} > wybierz co chcesz zrobić   ") 
        try: 
            button_input=int(input(f"{boot} > 1: Sproboj jeszcze raz  2: Nie chce wpisywać iminia "))
        except ValueError:
            os.system("cls")
            print(f"{boot} > mała podpowiedż musisz uzywać liczb anie liter :) ")
            self.powrot()
        else:
            match button_input:
                case 1: 
                    m=SystemStart()
                    m.przywitanie()
                    m.name()   
                case 2:
                    print(f"{boot} > przykro mi ze nie chcesz podać swojego iminia ale rozumiem to bedziesz jako anonimowy urzytkownikien")
                
         

m=SystemStart()
m.przywitanie()
m.name()