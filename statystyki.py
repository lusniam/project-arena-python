from os import system

class staty:
    def __init__(self,maxhp,akthp,zloto,poziom,exp,napoje,minatak,maxatak,pmiecza,pzbroi,szansa):
        self.maxhp=maxhp
        self.akthp=akthp
        self.zloto=zloto
        self.poziom=poziom
        self.exp=exp
        self.napoje=napoje
        self.minatak=minatak
        self.maxatak=maxatak
        self.pmiecza=pmiecza
        self.pzbroi=pzbroi
        self.szansa=szansa

    def BrakExp(self):
        print(f"Masz {self.exp} punktów doświadczenia.")
        if self.poziom<4:
            print(f"Brakuje ci {int(500*pow(self.poziom-1,2)+125-self.exp)} doświadczenia do poziomu {self.poziom+1}.")
        else:
            print("Masz maksymalny poziom!")

    def CheckLvl(self):
        if (self.poziom==1 and self.exp>=125) or (self.poziom==2 and self.exp>=625) or (self.poziom==3 and self.exp>=2125):
            self.exp=0
            self.poziom+=1
            self.maxhp+=10
            self.akthp=self.maxhp
            self.minatak+=2
            self.maxatak+=2
            print(f"Gratulacje! Osiągnąłeś {self.poziom} poziom doświadczenia!")
            print(f"Twoje maksymalne zdrowie wzrasta o 10! Aktualnie masz go {self.maxhp}.")
            print(f"Twoje ataki zadają 2 punkty obrażeń więcej! Aktualnie {self.minatak}-{self.maxatak}!")
            print(f"Zyskujesz na celności! Twoje ataki mają {self.szansa}% szans trafienie!")
        else:
            self.BrakExp()

    def statystyki(self):
        system("cls")
        print(f"Masz {self.akthp}/{self.maxhp} punktów zdrowia.")
        if self.pzbroi==0:
            print("Nie posiadasz zbroi.")
        else:
            print(f"Posiadasz zbroję poziomu {self.pzbroi}.") 
        print(f"\nTwoje ataki zadają {self.minatak}-{self.maxatak} punktów obrażeń.")
        print(f"Twoje ataki mają {self.szansa}% szans na trafienie\n")
        if self.pmiecza==0:
            print("Nie posiadasz miecza!")
        else:
            print(f"Posiadasz miecz poziomu {self.pmiecza}.")
        print(f"\nMasz {self.poziom} poziom doświadczenia.")
        self.BrakExp()
        print(f"Masz {self.zloto} sztuk złota oraz {self.napoje} mikstur leczniczych.")

        system("pause")
