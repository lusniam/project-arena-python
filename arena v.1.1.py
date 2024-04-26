from random import randint
from math import ceil
from os import system

maxhp=int(50)
akthp=int(maxhp)
zloto=int(20)
poziom=int(1)
exp=int(0)
napoje=int(0)
minatak=int(0)
maxatak=int(7)
pmiecza=int(0)
pzbroi=int(0)
szansa=int(90)

def wstep():
	print("Witaj w Mieczach i Kaloszach!\nJesteś gladiatorem, twoim zadaniem jest pokonać bossa areny.")
	print("Walcz z przeciwnikami, aby zdobywać złoto i doświadczenie!")
	print("Tawerna oferuje noclegi, dzięki którym odnowisz swoje zdrowie!")
	print("Zajdź do handlarza aby kupić uzbrojenie lub mikstury lecznicze, które pomogą ci podczas walki!")
	print("\nOto statystyki twojego gladiatora:")
	print(f"\nMasz {akthp}/{maxhp} punktów zdrowia.")
	print(f"Twoje ataki zadają {minatak}-{maxatak} punktów obrażeń.")
	print(f"Twoje ataki mają {szansa}% szans na trafienie")
	print(f"Masz {poziom} poziom doświadczenia.")
	BrakExp()
	print(f"Masz {zloto} sztuk złota oraz {napoje} mikstur leczniczych.")
	print("\nWychodzisz na główną ulicę miasta, gotowy rozpocząć swoją przygodę.")
	print("Udaj się do sklepu, aby kupić swój pierwszy miecz!\n")
	system("pause")

def tawerna():
	system("cls")
	global zloto,akthp,maxhp
	if zloto<50:
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
				zloto-=50
				akthp=maxhp
				print("Przespałeś się w tawernie, twoje zdrowie zostało odnowione!")
				break
			elif ch=="Nie":
				return
	print("\n")
	system("pause")

def potka():
	global zloto,napoje
	system("cls")
	if zloto<20:
		print("Mikstura lecząca kosztuje 20 sztuk złota i leczy około 50% maksymalnego zdrowia.")
		print("Masz za mało złota, aby to kupić.")
	else:
		if napoje<4:
			while True:
				print("Mikstura lecząca leczy około 50% maksymalnego zdrowia.")
				print("Czy chcesz kupić miksturę leczącą za 20 sztuk złota?(Tak/Nie)")
				ch=input("")
				system("cls")
				if ch=="Tak":
					zloto-=20
					napoje+=1
					print(f"Kupiłeś jedną miksturę, aktualnie masz ich {napoje}.")
					break
				elif ch=="Nie":
					return
		else:
			print("Masz maksymalną liczbę mikstur!")
	print("\n")
	system("pause")

def miecz():
	global pmiecza,zloto,minatak,maxatak,szansa
	system("cls")
	if pmiecza<4:
		koszt=int(125*pow(2,pmiecza))
		if(pmiecza==0):
			koszt=10
		if zloto<koszt:
			print(f"Poziom twojego miecza to {pmiecza}.")
			print("Każdy poziom miecza dodaje 2-3 do twojego ataku!")
			print("Jednak lepszy miecz dużo waży, a cięższym mieczem ciężej trafić...")
			print(f"Miecz następnego poziomu kosztuje {koszt}.")
			print("Masz za mało złota, aby to kupić.")
		else:
			while True:
				print(f"Poziom twojego miecza to {pmiecza}.")
				print("Każdy poziom miecza dodaje 2-3 do twojego ataku!")
				print("Jednak lepszy miecz dużo waży, a cięższym mieczem ciężej trafić...")
				print(f"Miecz następnego poziomu kosztuje {koszt} sztuk złota.")
				print(f"Czy chcesz kupić miecz poziomu {pmiecza+1} za {koszt} sztuk złota?(Tak/Nie)")
				ch=input()
				system("cls")
				if ch=="Tak":
					zloto-=koszt
					pmiecza+=1
					minatak+=2
					maxatak+=3
					szansa-=5
					print(f"Kupiłeś miecz poziomu {pmiecza}!\nTwoje ataki zadają teraz {minatak}-{maxatak}")
					print(f"Twoje ataki mają {szansa}% szans na trafienie!")
					break
				elif ch=="Nie":
					return
	else:
		print("Posiadasz już maksymalny poziom miecza!")
	system("pause")

def zbroja():
	global pzbroi,zloto,maxhp,akthp
	system("cls")
	if pzbroi<3:
		koszt=int(250*pow(2,pzbroi))
		if zloto<koszt:
			print(f"Poziom twojej zbroi to {pzbroi}.")
			print("Każdy poziom zbroi dodaje 10 do twojego maksymalnego zdrowia!")
			print(f"Zbroja następnego poziomu kosztuje {koszt} sztuk złota.")
			print("Masz za mało złota, aby to kupić.")
		else:
			while True:
				print(f"Poziom twojej zbroi to {pzbroi}.")
				print("Każdy poziom zbroi dodaje 10 do twojego maksymalnego zdrowia!")
				print(f"Zbroja następnego poziomu kosztuje {koszt}.")
				print(f"Czy chcesz kupić zbroję poziomu {pzbroi+1} za {koszt} sztuk złota?(Tak/Nie)")
				ch=input("")
				system("cls")
				if ch=='Tak':
					zloto-=koszt
					maxhp+=10
					akthp+=10
					pzbroi+=1
					print(f"Kupiłeś zbroję poziomu {pzbroi}!\nTwoje maksymalne zdrowie wzrosło do {maxhp}!")
					break
				elif ch=="Nie":
					pzbroi-=1
					return
	else:
		print("Posiadasz już maksymalny poziom zbroi!")
	print("\n")
	system("pause")

def sklep():
	while True:
		system("cls")
		print(f'Witaj w sklepie, co cię interesuje?')
		wsklep=input(f'Masz {zloto} sztuk zlota\nWpisz "Miecz", "Zbroja", "Mikstura", lub "Powrót", aby wrócić na ulicę.\n')
		if wsklep == 'Powrót':
			return
		elif wsklep=="Miecz":
			miecz()
		elif wsklep=="Zbroja":
			zbroja()
		elif wsklep=="Mikstura":
			potka()

def BrakExp():
	global poziom,exp
	print(f"Masz {exp} punktów doświadczenia.")
	if poziom<4:
		print(f"Brakuje ci {int(500*pow(poziom-1,2)+125-exp)} doświadczenia do poziomu {poziom+1}.")
	else:
		print("Masz maksymalny poziom!")

def CheckLvl():
	global exp,poziom,maxhp,akthp,minatak,maxatak,szansa
	if (poziom==1 and exp>=125) or (poziom==2 and exp>=625) or (poziom==3 and exp>=2125):
		exp=0
		poziom+=1
		maxhp+=10
		akthp=maxhp
		minatak+=2
		maxatak+=2
		print(f"Gratulacje! Osiągnąłeś {poziom} poziom doświadczenia!")
		print(f"Twoje maksymalne zdrowie wzrasta o 10! Aktualnie masz go {maxhp}.")
		print(f"Twoje ataki zadają 2 punkty obrażeń więcej! Aktualnie {minatak}-{maxatak}!")
		print(f"Zyskujesz na celności! Twoje ataki mają {szansa}% szans trafienie!")
	else:
		BrakExp()

def statystyki():
	global akthp,maxhp,minatak,maxatak,poziom,zloto,napoje,pmiecza,pzbroi,szansa
	system("cls")
	print(f"Masz {akthp}/{maxhp} punktów zdrowia.")
	if pzbroi==0:
		print("Nie posiadasz zbroi.")
	else:
		print(f"Posiadasz zbroję poziomu {pzbroi}.") 
	print(f"\nTwoje ataki zadają {minatak}-{maxatak} punktów obrażeń.")
	print(f"Twoje ataki mają {szansa}% szans na trafienie\n")
	if pmiecza==0:
		print("Nie posiadasz miecza!")
	else:
		print(f"Posiadasz miecz poziomu {pmiecza}.")
	print(f"\nMasz {poziom} poziom doświadczenia.")
	BrakExp()
	print(f"Masz {zloto} sztuk złota oraz {napoje} mikstur leczniczych.")


	system("pause")

def debug():
	global akthp,maxhp,minatak,maxatak,poziom,zloto,napoje,pmiecza,pzbroi,exp,szansa
	print("wpisz z aby zmienic statystyke")
	x=input("maxhp")
	if x=='z':
		maxhp=int(input(""))
	x=input("akthp")
	if x=='z':
		akthp=int(input(""))
	x=input("zloto")
	if x=='z':
		zloto=int(input(""))
	x=input("poziom")
	if x=='z':
		poziom=int(input(""))
	x=input("exp")
	if x=='z':
		exp=int(input(""))
	x=input("napoje")
	if x=='z':
		napoje=int(input(""))
	x=input("minatak")
	if x=='z':
		minatak=int(input(""))
	x=input("maxatak")
	if x=='z':
		maxatak=int(input(""))
	x=input("szansa")
	if x=='z':
		szansa=int(input(""))

def walka():
	global akthp,maxhp,minatak,maxatak,poziom,zloto,napoje,exp,szansa
	system("cls")
	while True:
		print("Wchodzisz na arenę. Dostępni przeciwnicy:")
		if poziom<=2:
			print("-Przeciwnik normalny (Dostępny dla poziomów 1-2)")
		if poziom>=2 and poziom<=3:
			print("-Przeciwnik trudny (Dostępny dla poziomów 2-3)")
		if poziom>=3:
			print("-Boss (Dostępny dla poziomów 3-4)")
		trudnosc=input('Wybierz przeciwnika wpisując "Normalny", "Trudny", "Boss", lub "Powrót", aby wrócić do miasta:\n')
		system("cls")
		if trudnosc=="Powrót":
			return
		if (poziom>0 and poziom<3 and trudnosc =="Normalny") or (poziom>1 and poziom<4 and trudnosc =="Trudny") or (poziom>2 and trudnosc =="Boss"):
			break
	system("cls")
	if trudnosc=="Normalny":
		hpopp=randint(40,55)
		atkminopp=randint(1,3)
		atkmaxopp=randint(8,11)
		potkiopp=randint(0,1)
		szansaopp=randint(80,90)
	elif trudnosc=="Trudny":
		hpopp=randint(80,100)
		atkminopp=randint(8,10)
		atkmaxopp=randint(16,18)
		potkiopp=randint(0,2)
		szansaopp=randint(70,80)
	elif trudnosc=="Boss":
		hpopp=125
		atkminopp=18
		atkmaxopp=28
		potkiopp=4
		szansaopp=75
	hpmaxopp=hpopp
	tura=randint(0,1)
	if tura==0:
		tura="gracz"
	else:
		tura="przeciwnik"
	print(f"Statystyki przeciwnika:\nZdrowie: {hpopp}\nObrażenia: {atkminopp}-{atkmaxopp}\nSzansa na trafienie: {szansaopp}\nPojedynek rozpocznie {tura}\nWalka!\n")
	system("pause")
	while True:
		system("cls")
		print(f"Masz {akthp}/{maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia")
		if tura=="gracz":
			while True:
				ch=input('\nWpisz "Atak", aby zaatakować, lub "Mikstura" aby się uleczyć!\n')
				if ch=="Atak":
					ratak=0
					while(True):
						system("cls")
						print(f"Masz {akthp}/{maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia\n")
						ratak=input('Wybierz rodzaj ataku:\n-"Szybki" - większa szansa na trafienie, mniejsze obrażenia,\n-"Normalny" - domyślne statystyki,\n-"Mocny" - mniejsz szansa na trafienie, większe obrażenia\n')
						if(ratak=="Szybki" or ratak=="Normalny" or ratak=="Mocny"):
							break
					system("cls")
					print(f"Masz {akthp}/{maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia\n")
					if(ratak=="Szybki"):
						atakpower=randint(70,90)/100
						szansapower=randint(15,25)
					elif(ratak=="Normalny"):
						atakpower=1
						szansapower=0
					elif(ratak=="Mocny"):
						atakpower=randint(110,130)/100
						szansapower=-randint(15,25)
					atak=randint(ceil(minatak*atakpower),ceil(maxatak*atakpower))
					print(f"Atakujesz {ratak.lower()}m atakiem!")
					if(szansa+szansapower<randint(1,100)):
						print("Chybiono!")
						atak=0
					hpopp-=atak
					print(f"Zadano {atak} punktów obrażeń przeciwnikowi!")
					break
				elif ch=="Mikstura":
					system("cls")
					print(f"Masz {akthp}/{maxhp} punktów zdrowia, przeciwnik ma {hpopp}/{hpmaxopp} punktów zdrowia\n")
					if napoje>0:
						leczenie=int(ceil(maxhp*(40+randint(0,20))/100))
						print(f"\nUleczono {leczenie} punktów zdrowia!")
						akthp+=leczenie
						napoje-=1
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
					szansapower=randint(15,25)
					ratak="szybkim"
				elif(ratak==2):
					atakpower=1
					szansapower=0
					ratak="normalnym"
				elif(ratak==3):
					atakpower=randint(110,130)/100
					szansapower=-randint(15,25)
					ratak="mocnym"
				atak=randint(ceil(atkminopp*atakpower),ceil(atkmaxopp*atakpower))
				print(f"\nPrzecuwnik atakuje {ratak} atakiem!")
				if(szansaopp+szansapower<randint(1,100)):
					print("Chybiono!")
					atak=0
				akthp-=atak
				print(f"Otrzymujesz {atak} punktów obrażeń!")
			if(akthp<=0):
				wynik='p'
				break
			tura="gracz"
		system("pause")
	print(f"Wygrywa {tura}!")
	if wynik=="w":
		if trudnosc=="Boss":
			print("Pokonałeś bossa areny!")
			poziom=5
			system("pause")
			return
		elif trudnosc=="Trudny":
			mnoznik=int(3)
		else:
			mnoznik=int(1)
		system("pause")
		ZdobytyExp=mnoznik*randint(100,200)
		ZdobyteZloto=mnoznik*randint(150,250)
		exp+=ZdobytyExp
		zloto+=ZdobyteZloto
		print(f"Za wygraną otrzymujesz {ZdobytyExp} punktów doświadczenia oraz {ZdobyteZloto} złota!\n")
		CheckLvl()
	system("pause")
	system("cls")

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
		if napoje>0:
			leczenie=int(ceil(maxhp*(35+randint(0,20))/100))
			if leczenie>maxhp-akthp:
				leczenie=maxhp-akthp
			print(f"Uleczono {leczenie} punktów zdrowia!")
			akthp+=leczenie
			napoje-=1
		else:
			print("Brak mikstur leczniczych! Kup więcej w sklepie!")
		system("pause")
	elif wybor=="Sklep":
		sklep()
	elif wybor=="Statystyki":
		statystyki()
	elif wybor=="debug":
		debug()
	if akthp<=0:
		print("Zginąłeś. Zagraj jeszcze raz!")
		break
	elif poziom==5:
		print("Gratulacje! Zostałeś królem areny! Dziękujemy za grę w Miecze i Kalosze!")
		break