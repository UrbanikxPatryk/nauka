class Prostykalkulator:
    def __init__(self,boot, name_input) -> str:
        self.boot=boot
        self.name_input=name_input
        
    def menu(self):
        print(f" {self.boot} >  {self.name_input} zaraz poprosze cie o liczby i co mam zrobić z nimi ")