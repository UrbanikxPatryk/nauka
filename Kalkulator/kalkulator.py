class MenuKalkulaotr:
    def __init__(self,boot,name_input )->str:
       self.boot=boot
       self.name_input=name_input

    def menu(self):
        print(f"{self.boot} > witam w  Menu Kalkulatora {self.name_input}")
            