from random import randint
from math import ceil
from os import system
import statystyki

staty=statystyki.staty(50,50,20,1,0,0,0,7,0,0,90)

def walka():
	global staty
	system("cls")
	while True:
		print("Wchodzisz na arenę. Dostępni przeciwnicy:")
		if staty.poziom<=2:
			print("-Przeciwnik normalny (Dostępny dla staty.poziomów 1-2)")
		if staty.poziom>=2 and staty.poziom<=3:
			print("-Przeciwnik trudny (Dostępny dla staty.poziomów 2-3)")
		if staty.poziom>=3:
			print("-Boss (Dostępny dla staty.poziomów 3-4)")
		trudnosc=input('Wybierz przeciwnika wpisując "Normalny", "Trudny", "Boss", lub "Powrót", aby wrócić do miasta:\n')
		system("cls")
		if trudnosc=="Powrót":
			return
		if (staty.poziom>0 and staty.poziom<3 and trudnosc =="Normalny") or (staty.poziom>1 and staty.poziom<4 and trudnosc =="Trudny") or (staty.poziom>2 and trudnosc =="Boss"):
			break
	system("cls")
	if trudnosc=="Normalny":
		hpopp=randint(40,55)
		atkminopp=randint(1,3)
		atkmaxopp=randint(8,11)
		potkiopp=randint(0,1)
		staty.szansaopp=randint(80,90)
	elif trudnosc=="Trudny":
		hpopp=randint(80,100)
		atkminopp=randint(8,10)
		atkmaxopp=randint(16,18)
		potkiopp=randint(0,2)
		staty.szansaopp=randint(70,80)
	elif trudnosc=="Boss":
		hpopp=125
		atkminopp=18
		atkmaxopp=28
		potkiopp=4
		staty.szansaopp=75
	hpmaxopp=hpopp
	tura=randint(0,1)
	if tura==0:
		tura="gracz"
	else:
		tura="przeciwnik"
	print(f"Statystyki przeciwnika:\nZdrowie: {hpopp}\nObrażenia: {atkminopp}-{atkmaxopp}\nstaty.Szansa na trafienie: {staty.szansaopp}\nPojedynek rozpocznie {tura}\nWalka!\n")
	system("pause")
	while True:
		system("cls")
		print(f"Masz {staty.akthp}/{staty.maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia")
		if tura=="gracz":
			while True:
				ch=input('\nWpisz "Atak", aby zaatakować, lub "Mikstura" aby się uleczyć!\n')
				if ch=="Atak":
					ratak=0
					while(True):
						system("cls")
						print(f"Masz {staty.akthp}/{staty.maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia\n")
						ratak=input('Wybierz rodzaj ataku:\n-"Szybki" - większa staty.szansa na trafienie, mniejsze obrażenia,\n-"Normalny" - domyślne statystyki,\n-"Mocny" - mniejsz staty.szansa na trafienie, większe obrażenia\n')
						if(ratak=="Szybki" or ratak=="Normalny" or ratak=="Mocny"):
							break
					system("cls")
					print(f"Masz {staty.akthp}/{staty.maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia\n")
					if(ratak=="Szybki"):
						atakpower=randint(70,90)/100
						staty.szansapower=randint(15,25)
					elif(ratak=="Normalny"):
						atakpower=1
						staty.szansapower=0
					elif(ratak=="Mocny"):
						atakpower=randint(110,130)/100
						staty.szansapower=-randint(15,25)
					atak=randint(ceil(staty.minatak*atakpower),ceil(staty.maxatak*atakpower))
					print(f"Atakujesz {ratak.lower()}m atakiem!")
					if(staty.szansa+staty.szansapower<randint(1,100)):
						print("Chybiono!")
						atak=0
					hpopp-=atak
					print(f"Zadano {atak} punktów obrażeń przeciwnikowi!")
					break
				elif ch=="Mikstura":
					system("cls")
					print(f"Masz {staty.akthp}/{staty.maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia\n")
					if staty.napoje>0:
						leczenie=int(ceil(staty.maxhp*(40+randint(0,20))/100))
						print(f"\nUleczono {leczenie} punktów zdrowia!")
						staty.akthp+=leczenie
						staty.napoje-=1
					else:
						print("\nBrak mikstur leczniczych! Przeciwnik wykorzystuje okazję!")
					break
			if(hpopp<=0):
				wynik='w'
				break
			tura="przeciwnik"
		else:
			if hpopp/hpmaxopp<0.5 and potkiopp>0 and randint(1,10)<2:
				leczenie=int(ceil(hpmaxopp*(40+randint(0,20))/100))
				print(f"\nPrzeciwnik używa mikstury leczenia, uleczono {leczenie} punktów zdrowia!")
				hpopp+=leczenie
				potkiopp-=1
			else:
				ratak=randint(1,3)
				if(ratak==1):
					atakpower=randint(70,90)/100
					staty.szansapower=randint(15,25)
					ratak="szybkim"
				elif(ratak==2):
					atakpower=1
					staty.szansapower=0
					ratak="normalnym"
				elif(ratak==3):
					atakpower=randint(110,130)/100
					staty.szansapower=-randint(15,25)
					ratak="mocnym"
				atak=randint(ceil(atkminopp*atakpower),ceil(atkmaxopp*atakpower))
				print(f"\nPrzecuwnik atakuje {ratak} atakiem!")
				if(staty.szansaopp+staty.szansapower<randint(1,100)):
					print("Chybiono!")
					atak=0
				staty.akthp-=atak
				print(f"Otrzymujesz {atak} punktów obrażeń!")
			if(staty.akthp<=0):
				wynik='p'
				break
			tura="gracz"
		system("pause")
	print(f"Wygrywa {tura}!")
	if wynik=="w":
		if trudnosc=="Boss":
			print("Pokonałeś bossa areny!")
			staty.poziom=5
			system("pause")
			return
		elif trudnosc=="Trudny":
			mnoznik=int(3)
		else:
			mnoznik=int(1)
		system("pause")
		ZdobytyExp=mnoznik*randint(100,200)
		ZdobyteZloto=mnoznik*randint(150,250)
		staty.exp+=ZdobytyExp
		staty.zloto+=ZdobyteZloto
		print(f"Za wygraną otrzymujesz {ZdobytyExp} punktów doświadczenia oraz {ZdobyteZloto} złota!\n")
		statystyki.CheckLvl()
	system("pause")
	system("cls")

def wstep():
	print("Witaj w Mieczach i Kaloszach!\nJesteś gladiatorem, twoim zadaniem jest pokonać bossa areny.")
	print("Walcz z przeciwnikami, aby zdobywać złoto i doświadczenie!")
	print("Tawerna oferuje noclegi, dzięki którym odnowisz swoje zdrowie!")
	print("Zajdź do handlarza aby kupić uzbrojenie lub mikstury lecznicze, które pomogą ci podczas walki!")
	print("\nOto statystyki twojego gladiatora:")
	print(f"\nMasz {staty.akthp}/{staty.maxhp} punktów zdrowia.")
	print(f"Twoje ataki zadają {staty.minatak}-{staty.maxatak} punktów obrażeń.")
	print(f"Twoje ataki mają {staty.szansa}% szans na trafienie")
	print(f"Masz {staty.poziom} staty.poziom doświadczenia.")
	statystyki.Brakstaty.Exp()
	print(f"Masz {staty.zloto} sztuk złota oraz {staty.napoje} mikstur leczniczych.")
	print("\nWychodzisz na główną ulicę miasta, gotowy rozpocząć swoją przygodę.")
	print("Udaj się do sklepu, aby kupić swój pierwszy miecz!\n")
	system("pause")

def tawerna():
	system("cls")
	global staty
	if staty.zloto<50:
		print("Koszt przespania się w tawernie to 50 sztuk złota, noc w tawernie w pełni odnawia twoje zdrowie.")
		print("Masz za mało złota, aby to zrobić.")
	else:
		ch=0
		while True:
			print("Koszt przespania się w tawernie to 50 sztuk złota, noc w tawernie w pełni odnawia twoje zdrowie.")
			print("Czy chcesz przespać się w tawernie?(Tak/Nie)")
			ch=input("")
			system("cls")
			if ch=="Tak":
				staty.zloto-=50
				staty.akthp=staty.maxhp
				print("Przespałeś się w tawernie, twoje zdrowie zostało odnowione!")
				break
			elif ch=="Nie":
				return
	print("\n")
	system("pause")

def potka():
	global staty
	system("cls")
	if staty.zloto<20:
		print("Mikstura lecząca kosztuje 20 sztuk złota i leczy około 50% maksymalnego zdrowia.")
		print("Masz za mało złota, aby to kupić.")
	else:
		if staty.napoje<4:
			while True:
				print("Mikstura lecząca leczy około 50% maksymalnego zdrowia.")
				print("Czy chcesz kupić miksturę leczącą za 20 sztuk złota?(Tak/Nie)")
				ch=input("")
				system("cls")
				if ch=="Tak":
					staty.zloto-=20
					staty.napoje+=1
					print(f"Kupiłeś jedną miksturę, aktualnie masz ich {staty.napoje}.")
					break
				elif ch=="Nie":
					return
		else:
			print("Masz maksymalną liczbę mikstur!")
	print("\n")
	system("pause")

def miecz():
	global staty
	system("cls")
	if staty.pmiecza<4:
		koszt=int(125*pow(2,staty.pmiecza))
		if(staty.pmiecza==0):
			koszt=10
		if staty.zloto<koszt:
			print(f"staty.Poziom twojego miecza to {staty.pmiecza}.")
			print("Każdy staty.poziom miecza dodaje 2-3 do twojego ataku!")
			print("Jednak lepszy miecz dużo waży, a cięższym mieczem ciężej trafić...")
			print(f"Miecz następnego staty.poziomu kosztuje {koszt}.")
			print("Masz za mało złota, aby to kupić.")
		else:
			while True:
				print(f"staty.Poziom twojego miecza to {staty.pmiecza}.")
				print("Każdy staty.poziom miecza dodaje 2-3 do twojego ataku!")
				print("Jednak lepszy miecz dużo waży, a cięższym mieczem ciężej trafić...")
				print(f"Miecz następnego staty.poziomu kosztuje {koszt} sztuk złota.")
				print(f"Czy chcesz kupić miecz staty.poziomu {staty.pmiecza+1} za {koszt} sztuk złota?(Tak/Nie)")
				ch=input()
				system("cls")
				if ch=="Tak":
					staty.zloto-=koszt
					staty.pmiecza+=1
					staty.minatak+=2
					staty.maxatak+=3
					staty.szansa-=5
					print(f"Kupiłeś miecz staty.poziomu {staty.pmiecza}!\nTwoje ataki zadają teraz {staty.minatak}-{staty.maxatak}")
					print(f"Twoje ataki mają {staty.szansa}% szans na trafienie!")
					break
				elif ch=="Nie":
					return
	else:
		print("Posiadasz już maksymalny staty.poziom miecza!")
	system("pause")

def zbroja():
	global pzbroi,staty.zloto,staty.maxhp,staty.akthp
	system("cls")
	if pzbroi<3:
		koszt=int(250*pow(2,pzbroi))
		if staty.zloto<koszt:
			print(f"staty.Poziom twojej zbroi to {pzbroi}.")
			print("Każdy staty.poziom zbroi dodaje 10 do twojego maksymalnego zdrowia!")
			print(f"Zbroja następnego staty.poziomu kosztuje {koszt} sztuk złota.")
			print("Masz za mało złota, aby to kupić.")
		else:
			while True:
				print(f"staty.Poziom twojej zbroi to {pzbroi}.")
				print("Każdy staty.poziom zbroi dodaje 10 do twojego maksymalnego zdrowia!")
				print(f"Zbroja następnego staty.poziomu kosztuje {koszt}.")
				print(f"Czy chcesz kupić zbroję staty.poziomu {pzbroi+1} za {koszt} sztuk złota?(Tak/Nie)")
				ch=input("")
				system("cls")
				if ch=='Tak':
					staty.zloto-=koszt
					staty.maxhp+=10
					staty.akthp+=10
					pzbroi+=1
					print(f"Kupiłeś zbroję staty.poziomu {pzbroi}!\nTwoje maksymalne zdrowie wzrosło do {staty.maxhp}!")
					break
				elif ch=="Nie":
					pzbroi-=1
					return
	else:
		print("Posiadasz już maksymalny staty.poziom zbroi!")
	print("\n")
	system("pause")

def sklep():
	while True:
		system("cls")
		print(f'Witaj w sklepie, co cię interesuje?')
		wsklep=input(f'Masz {staty.zloto} sztuk zlota\nWpisz "Miecz", "Zbroja", "Mikstura", lub "Powrót", aby wrócić na ulicę.\n')
		if wsklep == 'Powrót':
			return
		elif wsklep=="Miecz":
			miecz()
		elif wsklep=="Zbroja":
			zbroja()
		elif wsklep=="Mikstura":
			potka()

def debug():
	global staty.akthp,staty.maxhp,staty.minatak,staty.maxatak,staty.poziom,staty.zloto,staty.napoje,staty.pmiecza,pzbroi,staty.exp,staty.szansa
	print("wpisz z aby zmienic statystyke")
	x=input("staty.maxhp")
	if x=='z':
		staty.maxhp=int(input(""))
	x=input("staty.akthp")
	if x=='z':
		staty.akthp=int(input(""))
	x=input("staty.zloto")
	if x=='z':
		staty.zloto=int(input(""))
	x=input("staty.poziom")
	if x=='z':
		staty.poziom=int(input(""))
	x=input("staty.exp")
	if x=='z':
		staty.exp=int(input(""))
	x=input("staty.napoje")
	if x=='z':
		staty.napoje=int(input(""))
	x=input("staty.minatak")
	if x=='z':
		staty.minatak=int(input(""))
	x=input("staty.maxatak")
	if x=='z':
		staty.maxatak=int(input(""))
	x=input("staty.szansa")
	if x=='z':
		staty.szansa=int(input(""))

wstep()
while True:
	system("cls")
	print('Co zamierzasz zrobić? Wpisz:\n-"Arena", aby pojść na walkę,\n-"Tawerna", aby skorzystać z tawerny,\n-"Mikstura", aby wypić miksturę leczniczą\n-"Sklep", aby kupić nowe przedmioty,\n-"Statystyki", aby zobaczyć swoje statystyki')
	wybor=input()
	if wybor=="Arena":
		walka()
	elif wybor=="Tawerna":
		tawerna()
	elif wybor=="Mikstura":
		if staty.napoje>0:
			leczenie=int(ceil(staty.maxhp*(35+randint(0,20))/100))
			if leczenie>staty.maxhp-staty.akthp:
				leczenie=staty.maxhp-staty.akthp
			print(f"Uleczono {leczenie} punktów zdrowia!")
			staty.akthp+=leczenie
			staty.napoje-=1
		else:
			print("Brak mikstur leczniczych! Kup więcej w sklepie!")
		system("pause")
	elif wybor=="Sklep":
		sklep()
	elif wybor=="Statystyki":
		statystyki()
	elif wybor=="debug":
		debug()
	if staty.akthp<=0:
		print("Zginąłeś. Zagraj jeszcze raz!")
		break
	elif staty.poziom==5:
		print("Gratulacje! Zostałeś królem areny! Dziękujemy za grę w Miecze i Kalosze!")
		break