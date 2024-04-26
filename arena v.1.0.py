import pygame
from pygame.locals import *
from sys import exit
from time import sleep
from random import randint
from math import ceil

pygame.init()
screen=pygame.display.set_mode((1280,720))
pygame.display.set_caption('Miecze i Kalosze')

czarny=(0,0,0)
tekst=pygame.font.Font('PixeloidMono.ttf',20)

class PNG():
    gracz=[pygame.image.load('gracz/idle1.png'),
            pygame.image.load('gracz/idle2.png'),
            pygame.image.load('gracz/idle3.png'),
            pygame.image.load('gracz/idle4.png')]
    atak=[pygame.image.load('gracz/atak1.png'),
            pygame.image.load('gracz/atak2.png'),
            pygame.image.load('gracz/atak3.png'),
            pygame.image.load('gracz/atak4.png'),
            pygame.image.load('gracz/atak5.png'),
            pygame.image.load('gracz/atak6.png'),
            pygame.image.load('gracz/atak7.png'),]
    trafienie=[pygame.image.load('atak/atak1.png'),
            pygame.image.load('atak/atak2.png'),
            pygame.image.load('atak/atak3.png'),
            pygame.image.load('atak/atak4.png'),
            pygame.image.load('atak/atak5.png'),
            pygame.image.load('atak/atak6.png'),
            pygame.image.load('atak/atak7.png'),]
    class Przycisk():
        arena=pygame.image.load('przyciski/arena.png')
        atak=pygame.image.load('przyciski/atak.png')
        boss=pygame.image.load('przyciski/boss.png')
        miecz=pygame.image.load('przyciski/miecz.png')
        mikstura=pygame.image.load('przyciski/mikstura.png')
        mocny=pygame.image.load('przyciski/mocny.png')
        normalny=pygame.image.load('przyciski/normalny.png')
        powrot=pygame.image.load('przyciski/powrot.png')
        reset=pygame.image.load('przyciski/reset.png')
        sklep=pygame.image.load('przyciski/sklep.png')
        start=pygame.image.load('przyciski/start.png')
        staty=pygame.image.load('przyciski/stats.png')
        szybki=pygame.image.load('przyciski/szybki.png')
        tak=pygame.image.load('przyciski/tak.png')
        tawerna=pygame.image.load('przyciski/tawerna.png')
        trudny=pygame.image.load('przyciski/trudny.png')
        walka=pygame.image.load('przyciski/walka.png')
        wyjdz=pygame.image.load('przyciski/wyjdz.png')
        zbroja=pygame.image.load('przyciski/zbroja.png')
    przycisk=Przycisk()
    class Tlo():
        arena=pygame.image.load('tla/arena.png')
        menu=pygame.image.load('tla/menu.png')
        miasto=pygame.image.load('tla/miasto.png')
        sklep=pygame.image.load('tla/sklep.png')
        tawerna=pygame.image.load('tla/tawerna.png')
    tlo=Tlo()
    moneta=pygame.image.load('moneta.png')
    potka=pygame.image.load('potka.png')

class MP3():
    atak1=pygame.mixer.Sound("mp3/atak1.wav")
    atak2=pygame.mixer.Sound("mp3/atak2.wav")
    mikstura=pygame.mixer.Sound("mp3/mikstura.wav")
    przycisk=pygame.mixer.Sound("mp3/przycisk.wav")

class Gracz():
    hp=int(60)
    maxhp=int(60)
    zloto=int(20)
    poziom=int(1)
    exp=int(0)
    lvlup=int(125)
    potki=int(0)
    minatak=int(0)
    maxatak=int(7)
    pmiecza=int(0)
    pzbroi=int(0)
    szansa=int(100)

class stats_opp():
    hp=0
    maxhp=0
    atkmin=0
    atkmax=0
    potki=0
    szansa=0
    tura=0
    trudnosc=0

def textbox(x,y,a,b,w):
        pygame.draw.rect(screen,(0,0,0),(x+w*0.5,y+w*0.5,a-w,b-w),w)
        pygame.draw.rect(screen,(143,143,143),(x+w*1.5,y+w*1.5,a-w*3,b-w*3),w)
        pygame.draw.rect(screen,(224,224,224),(x+w*2.5,y+w*2.5,a-w*5,b-w*5),w)
        pygame.draw.rect(screen,(242,242,242),(x+w*3.5,y+w*3.5,a-w*7,b-w*7))

class Wstep():
    def __init__(self):
        self.przycisk_start=(550,560)

    def render(self):
        screen.fill((0,0,0))
        screen.blit(grafika.tlo.menu,(0,0))
        screen.blit(tekst.render('Witaj w Mieczach i Kaloszach!',True,czarny),(420,140))
        screen.blit(tekst.render('Jesteś nowym gladiatorem.',True,czarny),(420,220))
        screen.blit(tekst.render('Twoim zadaniem jest pokonać ',True,czarny),(420,270))
        screen.blit(tekst.render('bossa areny. Zajdź do sklepu',True,czarny),(420,300))
        screen.blit(tekst.render('po lepsze wyposażenie,',True,czarny),(420,330))
        screen.blit(tekst.render('bez niego nie przetrwasz',True,czarny),(420,360))
        screen.blit(tekst.render('na arenie.',True,czarny),(420,390))
        screen.blit(tekst.render('Wychodzisz na główną ulicę',True,czarny),(420,440))
        screen.blit(tekst.render('miasta, gotowy rozpocząć',True,czarny),(420,470))
        screen.blit(tekst.render('swoją przygodę.',True,czarny),(420,500))
        screen.blit(grafika.przycisk.start,self.przycisk_start)

    def buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_start[0],kursor[1]-self.przycisk_start[1])
        if 0<=przycisk[0]<=grafika.przycisk.start.get_width() and 0<=przycisk[1]<=grafika.przycisk.start.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='miasto'

class Miasto():
    def __init__(self):
        self.przycisk_sklep=(160,570)
        self.przycisk_tawerna=(1000,540)
        self.przycisk_arena=(400,100)
        self.przycisk_staty=(1150,20)

    def render(self):
        pygame.mixer.music.load("mp3/tlum.wav")
        pygame.mixer.music.play(-1)
        screen.fill((0,0,0))
        screen.blit(grafika.tlo.miasto,(0,0))
        screen.blit(grafika.przycisk.sklep,self.przycisk_sklep)
        screen.blit(grafika.przycisk.tawerna,self.przycisk_tawerna)
        screen.blit(grafika.przycisk.arena,self.przycisk_arena)
        screen.blit(grafika.przycisk.staty,self.przycisk_staty)
        
    def buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        
        przycisk=(kursor[0]-self.przycisk_sklep[0],kursor[1]-self.przycisk_sklep[1])
        if 0<=przycisk[0]<=grafika.przycisk.sklep.get_width() and 0<=przycisk[1]<=grafika.przycisk.sklep.get_height():
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='sklep'
            sklep.render()
        
        przycisk=(kursor[0]-self.przycisk_tawerna[0],kursor[1]-self.przycisk_tawerna[1])
        if 0<=przycisk[0]<=grafika.przycisk.tawerna.get_width() and 0<=przycisk[1]<=grafika.przycisk.tawerna.get_height():
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='tawerna'
            tawerna.render()

        przycisk=(kursor[0]-self.przycisk_arena[0],kursor[1]-self.przycisk_arena[1])
        if 0<=przycisk[0]<=grafika.przycisk.arena.get_width() and 0<=przycisk[1]<=grafika.przycisk.arena.get_height():
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='arena'
            arena.wejscie_render()
        
        przycisk=(kursor[0]-self.przycisk_staty[0],kursor[1]-self.przycisk_staty[1])
        if 0<=przycisk[0]<=grafika.przycisk.staty.get_width() and 0<=przycisk[1]<=grafika.przycisk.staty.get_height():
            pygame.mixer.music.stop()
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='statystyki'
            statystyki.render()

class Tawerna():
    def __init__(self):
        self.przycisk_tak=(340,340)
        self.przycisk_powrot=(800,340)
        
    def render(self):
        screen.fill((0,0,0))
        screen.blit(grafika.tlo.tawerna,(0,0))
        textbox(300,150,680,280,5)
        screen.blit(tekst.render('Noc w tawernie w pełni odnawia twoje zdrowie.',True,czarny),(340,180))
        screen.blit(tekst.render('Będzie cię to kosztowało 50 sztuk złota',True,czarny),(340,210))
        screen.blit(tekst.render('Czy chcesz przespać się w tawernie?',True,czarny),(340,240))
        
        screen.blit(grafika.przycisk.tak,self.przycisk_tak)
        screen.blit(grafika.przycisk.powrot,self.przycisk_powrot)

    def buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_tak[0],kursor[1]-self.przycisk_tak[1])
        if 0<=przycisk[0]<=grafika.przycisk.tak.get_width() and 0<=przycisk[1]<=grafika.przycisk.tak.get_height():
            if gracz.hp==gracz.maxhp:
                screen.blit(tekst.render('Jesteś już w pełni uzdrowiony!',True,czarny),(340,280))
            elif gracz.zloto<50:
                screen.blit(tekst.render('Nie masz wystarczająco dużo złota!',True,czarny),(340,280))
            else:
                gracz.hp=gracz.maxhp
                gracz.zloto-=50
                screen.blit(tekst.render('Zostałeś w pełni uzdrowiony!',True,czarny),(340,280))
                pygame.mixer.Sound.play(dzwiek.mikstura)
            pygame.display.update()
            sleep(1)
            tawerna.render()
        przycisk=(kursor[0]-self.przycisk_powrot[0],kursor[1]-self.przycisk_powrot[1])
        if 0<=przycisk[0]<=grafika.przycisk.powrot.get_width() and 0<=przycisk[1]<=grafika.przycisk.powrot.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='miasto'
            miasto.render()

class Sklep(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.przycisk_miecz=(340,260)
        self.przycisk_zbroja=(340,310)
        self.przycisk_mikstura=(340,360)
        self.przycisk_powrot=(680,360)

        self.mikstura_przycisk_tak=(340,360)
        
        self.miecz_przycisk_tak=(340,360)
        self.miecz_koszt=10

        self.zbroja_przycisk_tak=(340,360)
        self.zbroja_koszt=10
    
    def render_baza(self):
        screen.fill((0,0,0))
        screen.blit(grafika.tlo.sklep,(0,0))
        textbox(310,110,530,330,5)
        textbox(10,660,110,55,5)
        screen.blit(grafika.moneta,(29,679))
        screen.blit(tekst.render(f'{gracz.zloto}',True,czarny),(50,675))

    def render(self):
        self.render_baza()

        screen.blit(tekst.render('Witaj w sklepie, czego potrzebujesz?',True,czarny),(342,138))
        screen.blit(grafika.przycisk.miecz,self.przycisk_miecz)
        screen.blit(grafika.przycisk.zbroja,self.przycisk_zbroja)
        screen.blit(grafika.przycisk.mikstura,self.przycisk_mikstura)
        screen.blit(grafika.przycisk.powrot,self.przycisk_powrot)

    def buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_miecz[0],kursor[1]-self.przycisk_miecz[1])
        if 0<=przycisk[0]<=grafika.przycisk.miecz.get_width() and 0<=przycisk[1]<=grafika.przycisk.miecz.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='miecz'
            sklep.miecz_render()

        przycisk=(kursor[0]-self.przycisk_zbroja[0],kursor[1]-self.przycisk_zbroja[1])
        if 0<=przycisk[0]<=grafika.przycisk.zbroja.get_width() and 0<=przycisk[1]<=grafika.przycisk.zbroja.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='zbroja'
            sklep.zbroja_render()

        przycisk=(kursor[0]-self.przycisk_mikstura[0],kursor[1]-self.przycisk_mikstura[1])
        if 0<=przycisk[0]<=grafika.przycisk.mikstura.get_width() and 0<=przycisk[1]<=grafika.przycisk.mikstura.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='mikstura'
            sklep.mikstura_render()

        przycisk=(kursor[0]-self.przycisk_powrot[0],kursor[1]-self.przycisk_powrot[1])
        if 0<=przycisk[0]<=grafika.przycisk.powrot.get_width() and 0<=przycisk[1]<=grafika.przycisk.powrot.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='miasto'
            miasto.render()
        
    def mikstura_render(self):
        self.render_baza()

        screen.blit(tekst.render('Mikstura lecząca odnawia około',True,czarny),(342,138))
        screen.blit(tekst.render('50% twojego maksymalnego zdrowia.',True,czarny),(342,168))
        screen.blit(tekst.render(f'Masz przy sobie {gracz.potki} mikstur.',True,czarny),(342,198))
        
        if gracz.potki<4:
            screen.blit(tekst.render(f'Czy chcesz ją kupić za 20 złota?',True,czarny),(342,228))
            screen.blit(grafika.przycisk.tak,self.mikstura_przycisk_tak) 
        else:
            screen.blit(tekst.render('Masz maksymalną ilość mikstur!',True,czarny),(342,258))
        screen.blit(grafika.przycisk.powrot,self.przycisk_powrot)

    def mikstura_buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        if gracz.potki<4:
            przycisk=(kursor[0]-self.mikstura_przycisk_tak[0],kursor[1]-self.mikstura_przycisk_tak[1])
            if 0<=przycisk[0]<=grafika.przycisk.tak.get_width() and 0<=przycisk[1]<=grafika.przycisk.tak.get_height():
                if gracz.zloto<20:
                    screen.blit(tekst.render('Nie masz wystarczająco dużo złota!',True,czarny),(342,288))
                else:
                    gracz.potki+=1
                    gracz.zloto-=20
                    self.mikstura_render()
                    screen.blit(tekst.render('Kupiłeś miksturę leczącą!',True,czarny),(342,288))
                    pygame.mixer.Sound.play(dzwiek.mikstura)
                pygame.display.update()
                sleep(1)
                sklep.mikstura_render()
            
        przycisk=(kursor[0]-self.przycisk_powrot[0],kursor[1]-self.przycisk_powrot[1])
        if 0<=przycisk[0]<=grafika.przycisk.powrot.get_width() and 0<=przycisk[1]<=grafika.przycisk.powrot.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='sklep'
            sklep.render()
        
    def miecz_render(self):
        self.render_baza()
        if gracz.pmiecza<4:
            screen.blit(tekst.render(f'Miecz poziomu {gracz.pmiecza+1}',True,czarny),(342,138))
            screen.blit(tekst.render(f'Obrażenia: {gracz.minatak+2}-{gracz.maxatak+3}',True,czarny),(342,168))
            screen.blit(tekst.render(f'Szansa na trafienie: {gracz.szansa-5}%.',True,czarny),(342,198))
            screen.blit(tekst.render(f'Czy chcesz go kupić za {self.miecz_koszt} złota?',True,czarny),(342,228))
            screen.blit(grafika.przycisk.tak,self.miecz_przycisk_tak)
        else:
            screen.blit(tekst.render('Masz maksymalny poziom miecza!',True,czarny),(342,138))
        screen.blit(grafika.przycisk.powrot,self.przycisk_powrot)

    def miecz_buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        if gracz.pmiecza<4:
            przycisk=(kursor[0]-self.miecz_przycisk_tak[0],kursor[1]-self.miecz_przycisk_tak[1])
            if 0<=przycisk[0]<=grafika.przycisk.tak.get_width() and 0<=przycisk[1]<=grafika.przycisk.tak.get_height():
                if gracz.zloto<self.miecz_koszt:
                    screen.blit(tekst.render('Nie masz wystarczająco dużo złota!',True,czarny),(342,288))
                else:
                    gracz.zloto-=self.miecz_koszt
                    gracz.pmiecza+=1
                    gracz.minatak+=2
                    gracz.maxatak+=3
                    gracz.szansa-=5
                    self.miecz_koszt=int(125*pow(2,gracz.pmiecza))
                    self.miecz_render()
                    screen.blit(tekst.render(f'Kupiłeś miecz poziomu {gracz.pmiecza}!',True,czarny),(342,288))
                    pygame.mixer.Sound.play(dzwiek.mikstura)
                pygame.display.update()
                sleep(1)
                sklep.miecz_render()
        przycisk=(kursor[0]-self.przycisk_powrot[0],kursor[1]-self.przycisk_powrot[1])
        if 0<=przycisk[0]<=grafika.przycisk.powrot.get_width() and 0<=przycisk[1]<=grafika.przycisk.powrot.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='sklep'
            sklep.render()
        
    def zbroja_render(self):
        self.render_baza()
        if gracz.pzbroi<4:
            screen.blit(tekst.render(f'Zbroja poziomu {gracz.pzbroi+1}',True,czarny),(342,138))
            screen.blit(tekst.render(f'Maksymalne zdrowie: {gracz.maxhp+10}',True,czarny),(342,168))
            screen.blit(tekst.render(f'Czy chcesz ją kupić za {self.zbroja_koszt} złota?',True,czarny),(342,198))
            screen.blit(grafika.przycisk.tak,self.zbroja_przycisk_tak)
        else:
            screen.blit(tekst.render('Masz maksymalny poziom zbroi!',True,czarny),(342,138))
        screen.blit(grafika.przycisk.powrot,self.przycisk_powrot)

    def zbroja_buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        if gracz.pzbroi<4:
            przycisk=(kursor[0]-self.zbroja_przycisk_tak[0],kursor[1]-self.zbroja_przycisk_tak[1])
            if 0<=przycisk[0]<=grafika.przycisk.tak.get_width() and 0<=przycisk[1]<=grafika.przycisk.tak.get_height():
                if gracz.zloto<self.zbroja_koszt:
                    screen.blit(tekst.render('Nie masz wystarczająco dużo złota!',True,czarny),(342,228))
                else:
                    gracz.zloto-=self.zbroja_koszt
                    gracz.maxhp+=10
                    gracz.hp+=10
                    gracz.pzbroi+=1
                    self.zbroja_koszt=int(125*pow(2,gracz.pzbroi))
                    self.zbroja_render()
                    screen.blit(tekst.render(f'Kupiłeś zbroję poziomu {gracz.pzbroi}!',True,czarny),(342,228))
                    pygame.mixer.Sound.play(dzwiek.mikstura)
                pygame.display.update()
                sleep(1)
                sklep.zbroja_render()
        przycisk=(kursor[0]-self.przycisk_powrot[0],kursor[1]-self.przycisk_powrot[1])
        if 0<=przycisk[0]<=grafika.przycisk.powrot.get_width() and 0<=przycisk[1]<=grafika.przycisk.powrot.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='sklep'
            sklep.render()

class Statystyki(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.przycisk_powrot=(650,580)

    def render(self):
        screen.fill((0,0,0))
        screen.blit(grafika.tlo.menu,(0,0))
        screen.blit(tekst.render('Statystyki:',True,czarny),(430,150))
        screen.blit(tekst.render(f'Zdrowie: {gracz.hp}/{gracz.maxhp}',True,czarny),(430,180))
        screen.blit(tekst.render(f'Obrażenia: {gracz.minatak}-{gracz.maxatak}',True,czarny),(430,210))
        screen.blit(tekst.render(f'Szansa na trafienie: {gracz.szansa}%',True,czarny),(430,240))
        screen.blit(tekst.render(f'{gracz.poziom} poziom doświadczenia',True,czarny),(430,270))
        if gracz.poziom==4:
            screen.blit(tekst.render('Masz maksymalny poziom!',True,czarny),(430,300))
        else:
            screen.blit(tekst.render(f'{gracz.exp}/{gracz.lvlup} punktów doświadczenia',True,czarny),(430,300))
            screen.blit(tekst.render(f'do poziomu {gracz.poziom+1}',True,czarny),(430,330))
        screen.blit(tekst.render('Ekwipunek:',True,czarny),(430,380))
        screen.blit(tekst.render(f'Masz {gracz.zloto} sztuk złota',True,czarny),(430,410))
        if gracz.pmiecza==0:
            screen.blit(tekst.render('Nie posiadasz miecza!',True,czarny),(430,440))
        else:
            screen.blit(tekst.render(f'Posiadasz miecz poziomu {gracz.pmiecza}',True,czarny),(430,440))
        if gracz.pzbroi==0:
            screen.blit(tekst.render('Nie posiadasz zbroi!',True,czarny),(430,470))
        else:
            screen.blit(tekst.render(f'Posiadasz zbroję poziomu {gracz.pzbroi}',True,czarny),(430,470))
        if gracz.potki==0:
            screen.blit(tekst.render('Nie posiadasz mikstur!',True,czarny),(430,500))
        elif gracz.potki==1:
            screen.blit(tekst.render(f'Posiadasz {gracz.potki} miksturę',True,czarny),(430,500))
        else:
            screen.blit(tekst.render(f'Posiadasz {gracz.potki} mikstury',True,czarny),(430,500))

        screen.blit(grafika.przycisk.powrot,self.przycisk_powrot)

    def buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_powrot[0],kursor[1]-self.przycisk_powrot[1])
        if 0<=przycisk[0]<=grafika.przycisk.powrot.get_width() and 0<=przycisk[1]<=grafika.przycisk.powrot.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='miasto'
            miasto.render()

class Arena(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.przycisk_normalny=(440,400)
        self.przycisk_hard=(440,450)
        self.przycisk_boss=(440,500)
        self.przycisk_powrot=(650,580)
        self.przycisk_walka=(440,400)
        
    def wejscie_render(self):
        screen.fill((0,0,0))
        screen.blit(grafika.tlo.menu,(0,0))
        screen.blit(tekst.render('Dostępni przeciwnicy:',True,czarny),(430,120))
        
        if gracz.poziom<=2:
            screen.blit(tekst.render('Przeciwnik normalny',True,czarny),(430,180))
            screen.blit(tekst.render('(Nagrody x1)',True,czarny),(430,210))
            screen.blit(grafika.przycisk.normalny,self.przycisk_normalny)
        if gracz.poziom>=2 and gracz.poziom<=3:
            screen.blit(tekst.render('Przeciwnik trudny',True,czarny),(430,240))
            screen.blit(tekst.render('(Nagrody x3)',True,czarny),(430,270))
            screen.blit(grafika.przycisk.trudny,self.przycisk_hard)
        if gracz.poziom>=3:
            screen.blit(tekst.render('Boss',True,czarny),(430,300))
            screen.blit(tekst.render('(Ostateczny przeciwnik)',True,czarny),(430,330))
            screen.blit(grafika.przycisk.boss,self.przycisk_boss)
        
        screen.blit(grafika.przycisk.powrot,self.przycisk_powrot)

    def wejscie_buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_normalny[0],kursor[1]-self.przycisk_normalny[1])
        if 0<=przycisk[0]<=grafika.przycisk.normalny.get_width() and 0<=przycisk[1]<=grafika.przycisk.normalny.get_height() and gracz.poziom<=2:
            opp.trudnosc=1
        przycisk=(kursor[0]-self.przycisk_hard[0],kursor[1]-self.przycisk_hard[1])
        if 0<=przycisk[0]<=grafika.przycisk.trudny.get_width() and 0<=przycisk[1]<=grafika.przycisk.trudny.get_height() and gracz.poziom>=2 and gracz.poziom<=3:
            opp.trudnosc=2
        przycisk=(kursor[0]-self.przycisk_boss[0],kursor[1]-self.przycisk_boss[1])
        if 0<=przycisk[0]<=grafika.przycisk.boss.get_width() and 0<=przycisk[1]<=grafika.przycisk.boss.get_height() and gracz.poziom>=3:
            opp.trudnosc=3
        if opp.trudnosc!=0:
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='start'
            arena.start_render()

        przycisk=(kursor[0]-self.przycisk_powrot[0],kursor[1]-self.przycisk_powrot[1])
        if 0<=przycisk[0]<=grafika.przycisk.powrot.get_width() and 0<=przycisk[1]<=grafika.przycisk.powrot.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='miasto'
            miasto.render()

    def start_render(self):
        screen.fill((0,0,0))
        screen.blit(grafika.tlo.menu,(0,0))
        if opp.trudnosc==1:
            opp.hp=randint(30,40)
            opp.atkmin=randint(1,2)
            opp.atkmax=randint(7,9)
            opp.potki=randint(0,1)
            opp.szansa=randint(80,90)
        elif opp.trudnosc==2:
            opp.hp=randint(80,100)
            opp.atkmin=randint(8,10)
            opp.atkmax=randint(16,18)
            opp.potki=randint(0,2)
            opp.szansa=randint(70,80)
        else:
            opp.hp=125
            opp.atkmin=18
            opp.atkmax=28
            opp.potki=4
            opp.szansa=75
        opp.maxhp=opp.hp
        opp.tura=randint(0,1)

        screen.blit(tekst.render('Statystyki przeciwnika:',True,czarny),(430,120))
        screen.blit(tekst.render(f'Zdrowie: {opp.hp}',True,czarny),(430,150))
        screen.blit(tekst.render(f'Obrażenia: {opp.atkmin}-{opp.atkmax}',True,czarny),(430,180))
        screen.blit(tekst.render(f'Szansa na trafienie: {opp.szansa}',True,czarny),(430,210))
        screen.blit(tekst.render(f'Posiadane mikstury: {opp.potki}',True,czarny),(430,240))
        if opp.tura:
            screen.blit(tekst.render(f'Rozpoczyna przeciwnik',True,czarny),(430,270))
        else:
            screen.blit(tekst.render(f'Rozpoczyna gracz',True,czarny),(430,270))
        screen.blit(grafika.przycisk.walka,self.przycisk_walka)

    def start_buttons(self):
        global obszar
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_walka[0],kursor[1]-self.przycisk_walka[1])
        if 0<=przycisk[0]<=grafika.przycisk.walka.get_width() and 0<=przycisk[1]<=grafika.przycisk.walka.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            obszar='walka'
            walka.walka()

class Walka():
    def __init__(self):
        self.przycisk_szybki=(50,50)
        self.przycisk_normalny=(50,100)
        self.przycisk_mocny=(50,150)
        self.przycisk_mikstura=(50,200)
        
        self.przycisk_reset=(625,235)
        self.przycisk_wyjdz=(980,235)
        
        self.przycisk_p_reset=(125,235)
        self.przycisk_p_wyjdz=(380,235)
        self.przycisk_powrot=(1020,280)
        self.przycisk_w_powrot=(1050,450)
        
        self.czcionka=[pygame.font.Font('PixeloidMono.ttf',80),
                pygame.font.Font('PixeloidMono.ttf',70),
                pygame.font.Font('PixeloidMono.ttf',60)]

    def walka(self):
        animacje=[randint(0,3),randint(0,3)]
        klatki=0
        pygame.mixer.music.load("mp3/tlum.wav")
        pygame.mixer.music.play(-1)
        while True:
            if opp.tura:
                if opp.hp/opp.maxhp<0.5 and opp.potki>0 and randint(1,10)<2:
                    leczenie=int(ceil(opp.maxhp*(40+randint(0,20))/100))
                    if leczenie>opp.maxhp-opp.hp:
                        leczenie=opp.maxhp-opp.hp
                    opp.potki-=1
                    self.render_leczenie(leczenie)
                else:
                    akcja=randint(1,3)
                    if akcja==1:
                        moc_ataku=randint(70,90)/100
                        szansa_ataku=randint(15,25)
                    elif akcja==2:
                        moc_ataku=1
                        szansa_ataku=0
                    else:
                        moc_ataku=randint(110,130)/100
                        szansa_ataku=-randint(15,25)
                    atak=randint(ceil(opp.atkmin*moc_ataku),ceil(opp.atkmax*moc_ataku))
                    if opp.szansa+szansa_ataku<randint(1,100):
                        atak=0
                    self.render_atak(atak)
                opp.tura=0
            else:
                while True:
                    if klatki==7:
                        animacje[0]+=1
                        animacje[1]+=1
                        klatki=0
                    if animacje[0]==len(grafika.gracz):
                        animacje[0]=0
                    if animacje[1]==len(grafika.gracz):
                        animacje[1]=0

                    klatki+=1
                    akcja=0
                    self.render_gracz(animacje)
                    for event in pygame.event.get():
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            akcja=self.buttons()
                    if akcja!=0:
                        break
                if akcja<4:
                    if akcja==1:
                        moc_ataku=randint(70,90)/100
                        szansa_ataku=randint(15,25)
                    elif akcja==2:
                        moc_ataku=1
                        szansa_ataku=0
                    elif akcja==3:
                        moc_ataku=randint(110,130)/100
                        szansa_ataku=-randint(15,25)
                    atak=randint(ceil(gracz.minatak*moc_ataku),ceil(gracz.maxatak*moc_ataku))
                    if gracz.szansa+szansa_ataku<randint(1,100):
                        atak=0
                    self.render_atak(atak)
                else:
                    if gracz.potki>0:
                        leczenie=int(ceil(gracz.maxhp*(40+randint(0,20))/100))
                        if leczenie>gracz.maxhp-gracz.hp:
                            leczenie=gracz.maxhp-gracz.hp
                        gracz.potki-=1
                        self.render_leczenie(leczenie)
                opp.tura=1
            if gracz.hp<=0:
                self.przegrana()
                break
            if opp.hp<=0:
                self.wygrana()
                break

    def render_baza(self):
        screen.fill((0,0,0))
        screen.blit(grafika.tlo.arena,(0,0))
        screen.blit(grafika.potka,(30,540))
        screen.blit(tekst.render(f'{gracz.potki}',True,czarny),(70,630))
        pygame.draw.rect(screen,czarny,(160,650,400,40),3)
        pygame.draw.rect(screen,(255,0,0),(163,653,394*float(gracz.hp)/float(gracz.maxhp),34))
        screen.blit(tekst.render(f'{gracz.hp}/{gracz.maxhp}',True,czarny),(330,660))

        screen.blit(grafika.potka,(1150,540))
        screen.blit(tekst.render(f'{opp.potki}',True,czarny),(1190,630))
        pygame.draw.rect(screen,czarny,(712,650,400,40),3)
        pygame.draw.rect(screen,(255,0,0),(715,653,394*float(opp.hp)/float(opp.maxhp),34))
        screen.blit(tekst.render(f'{opp.hp}/{opp.maxhp}',True,czarny),(892,660))

    def render_gracz(self,animacje):
        self.render_baza()

        pygame.time.Clock().tick(120)

        screen.blit(grafika.gracz[animacje[0]],(80,80))
        screen.blit(pygame.transform.flip(grafika.gracz[animacje[1]],True,False),(680,80))

        screen.blit(grafika.przycisk.szybki,self.przycisk_szybki)
        screen.blit(grafika.przycisk.atak,(self.przycisk_szybki[0]+grafika.przycisk.szybki.get_width()+20,self.przycisk_szybki[1]))
        wyswietlana_szansa=gracz.szansa+20
        if wyswietlana_szansa>100:
            wyswietlana_szansa=100
        opis_akcji1=(self.przycisk_szybki[0]+grafika.przycisk.szybki.get_width()+60,self.przycisk_szybki[1]+8)
        opis_akcji2=(self.przycisk_szybki[0]+grafika.przycisk.szybki.get_width()+160,self.przycisk_szybki[1]+8)
        screen.blit(tekst.render(f'{ceil(gracz.minatak*0.8)}-{ceil(gracz.maxatak*0.8)}',True,czarny),opis_akcji1)
        screen.blit(tekst.render(f'~{wyswietlana_szansa}%',True,czarny),opis_akcji2)

        screen.blit(grafika.przycisk.normalny,self.przycisk_normalny)
        screen.blit(grafika.przycisk.atak,(self.przycisk_normalny[0]+grafika.przycisk.normalny.get_width()+20,self.przycisk_normalny[1]))
        wyswietlana_szansa=gracz.szansa
        if wyswietlana_szansa>100:
            wyswietlana_szansa=100
        opis_akcji1=(self.przycisk_normalny[0]+grafika.przycisk.normalny.get_width()+60,self.przycisk_normalny[1]+8)
        opis_akcji2=(self.przycisk_normalny[0]+grafika.przycisk.normalny.get_width()+160,self.przycisk_normalny[1]+8)
        screen.blit(tekst.render(f'{ceil(gracz.minatak)}-{ceil(gracz.maxatak)}',True,czarny),opis_akcji1)
        screen.blit(tekst.render(f'~{wyswietlana_szansa}%',True,czarny),opis_akcji2)

        screen.blit(grafika.przycisk.mocny,self.przycisk_mocny)
        screen.blit(grafika.przycisk.atak,(self.przycisk_mocny[0]+grafika.przycisk.mocny.get_width()+20,self.przycisk_mocny[1]))
        wyswietlana_szansa=gracz.szansa-20
        if wyswietlana_szansa>100:
            wyswietlana_szansa=100
        opis_akcji1=(self.przycisk_mocny[0]+grafika.przycisk.mocny.get_width()+60,self.przycisk_mocny[1]+8)
        opis_akcji2=(self.przycisk_mocny[0]+grafika.przycisk.mocny.get_width()+160,self.przycisk_mocny[1]+8)
        screen.blit(tekst.render(f'{ceil(gracz.minatak*1.2)}-{ceil(gracz.maxatak*1.2)}',True,czarny),opis_akcji1)
        screen.blit(tekst.render(f'~{wyswietlana_szansa}%',True,czarny),opis_akcji2)
        
        if gracz.potki>0:
            screen.blit(grafika.przycisk.mikstura,self.przycisk_mikstura)
        
        pygame.display.update()

    def buttons(self):
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_szybki[0],kursor[1]-self.przycisk_szybki[1])
        if 0<=przycisk[0]<=grafika.przycisk.szybki.get_width() and 0<=przycisk[1]<=grafika.przycisk.szybki.get_height():
            return 1

        przycisk=(kursor[0]-self.przycisk_normalny[0],kursor[1]-self.przycisk_normalny[1])
        if 0<=przycisk[0]<=grafika.przycisk.normalny.get_width() and 0<=przycisk[1]<=grafika.przycisk.normalny.get_height():
            return 2

        przycisk=(kursor[0]-self.przycisk_mocny[0],kursor[1]-self.przycisk_mocny[1])
        if 0<=przycisk[0]<=grafika.przycisk.mocny.get_width() and 0<=przycisk[1]<=grafika.przycisk.mocny.get_height():
            return 3

        if gracz.potki>0:
            przycisk=(kursor[0]-self.przycisk_mikstura[0],kursor[1]-self.przycisk_mikstura[1])
            if 0<=przycisk[0]<=grafika.przycisk.mikstura.get_width() and 0<=przycisk[1]<=grafika.przycisk.mikstura.get_height():
                return 4
        
        return 0

    def render_atak(self,atak):
        if randint(0,1):
            pygame.mixer.Sound.play(dzwiek.atak1)
        else:
            pygame.mixer.Sound.play(dzwiek.atak2)
        for i in range(7):
            self.render_baza()
            pygame.time.Clock().tick(10)
            if opp.tura:
                screen.blit(pygame.transform.flip(grafika.atak[i],True,False),(680,80))
                screen.blit(grafika.gracz[i%4],(80,80))
                if atak>0:
                    screen.blit(grafika.trafienie[i],(280,80))
            else:
                screen.blit(grafika.atak[i],(80,80))
                screen.blit(pygame.transform.flip(grafika.gracz[i%4],True,False),(680,80))
                if atak>0:
                    screen.blit(grafika.trafienie[i],(880,80))
            pygame.display.update()
        if opp.tura:
            gracz.hp-=atak
            if gracz.hp<0:
                gracz.hp=0
        else:
            opp.hp-=atak
            if opp.hp<0:
                opp.hp=0
        kolor1=czarny
        kolor2=(255,0,0)
        for i in range(12):
            self.render_baza()
            pygame.time.Clock().tick(10)
            screen.blit(grafika.gracz[i%4],(80,80))
            screen.blit(pygame.transform.flip(grafika.gracz[i%4],True,False),(680,80))
            if opp.tura:
                if atak==0:
                    screen.blit(self.czcionka[2].render('Chybiono!',True,kolor1),(100,80))
                screen.blit(self.czcionka[0].render(f'{atak}',True,kolor1),(300,160))
                screen.blit(self.czcionka[1].render(f'{atak}',True,kolor2),(304,166))
                screen.blit(self.czcionka[2].render(f'{atak}',True,kolor1),(308,172))
            else:
                if atak==0:
                    screen.blit(self.czcionka[2].render('Chybiono!',True,kolor1),(700,80))
                screen.blit(self.czcionka[0].render(f'{atak}',True,kolor1),(900,160))
                screen.blit(self.czcionka[1].render(f'{atak}',True,kolor2),(904,166))
                screen.blit(self.czcionka[2].render(f'{atak}',True,kolor1),(908,172))
            kolor1,kolor2=kolor2,kolor1
            pygame.display.update()

    def render_leczenie(self,leczenie):
        for i in range(4):
            self.render_baza()
            pygame.time.Clock().tick(10)
            if opp.tura:
                screen.blit(pygame.transform.flip(grafika.atak[i],True,False),(680,80))
                screen.blit(grafika.gracz[i%4],(80,80))
            else:
                screen.blit(grafika.atak[i],(80,80))
                screen.blit(pygame.transform.flip(grafika.gracz[i%4],True,False),(680,80))
            pygame.display.update()
        if opp.tura:
            opp.hp+=leczenie
        else:
            gracz.hp+=leczenie
        pygame.mixer.Sound.play(dzwiek.mikstura)            
        kolor1=czarny
        kolor2=(0,255,0)
        for i in range(16):
            self.render_baza()
            pygame.time.Clock().tick(10)
            if opp.tura:
                screen.blit(grafika.gracz[i%4],(80,80))
                if i<12:
                    screen.blit(pygame.transform.flip(grafika.atak[3],True,False),(680,80))
                else:
                    screen.blit(pygame.transform.flip(grafika.gracz[15-i],True,False),(680,80))
            else:
                screen.blit(pygame.transform.flip(grafika.gracz[i%4],True,False),(680,80))
                if i<12:
                    screen.blit(grafika.atak[3],(80,80))
                else:
                    screen.blit(grafika.atak[15-i],(80,80))
            if opp.tura:
                screen.blit(self.czcionka[0].render(f'{leczenie}',True,kolor1),(900,160))
                screen.blit(self.czcionka[1].render(f'{leczenie}',True,kolor2),(904,167))
                screen.blit(self.czcionka[2].render(f'{leczenie}',True,kolor1),(908,174))
            else:
                screen.blit(self.czcionka[0].render(f'{leczenie}',True,kolor1),(300,160))
                screen.blit(self.czcionka[1].render(f'{leczenie}',True,kolor2),(304,167))
                screen.blit(self.czcionka[2].render(f'{leczenie}',True,kolor1),(308,174))

            kolor1,kolor2=kolor2,kolor1
            pygame.display.update()

    def wygrana(self):
        for i in range(4):
            screen.fill((0,0,0))
            screen.blit(grafika.tlo.arena,(0,0))
            pygame.time.Clock().tick(12)
            screen.blit(grafika.atak[i],(80,80))
            pygame.display.update()
        pygame.mixer.music.stop()
        pygame.mixer.music.load("mp3/wygrana.wav")
        pygame.mixer.music.play()
        if opp.trudnosc==3:
            self.koniec()
        else:
            if opp.trudnosc==2:
                mnoznik=3
            else:
                mnoznik=1
            ZdobytyExp=mnoznik*randint(100,200)
            ZdobyteZloto=mnoznik*randint(150,250)
            gracz.exp+=ZdobytyExp
            gracz.zloto+=ZdobyteZloto
            if gracz.exp<gracz.lvlup:
                textbox(700,100,480,250,5)
                screen.blit(tekst.render('Wygrywasz!',True,czarny),(720,120))
                screen.blit(tekst.render(f'Otrzymujesz {ZdobytyExp} expa',True,czarny),(720,150))
                screen.blit(tekst.render(f'oraz {ZdobyteZloto} złota!',True,czarny),(720,180))
                screen.blit(tekst.render(f'Masz {gracz.exp} punktów doświadczenia.',True,czarny),(720,210))
                screen.blit(tekst.render(f'Brakuje ci {gracz.lvlup-gracz.exp} expa do poziomu {gracz.poziom+1}.',True,czarny),(720,240))
                screen.blit(grafika.przycisk.powrot,self.przycisk_powrot)
            else:
                if gracz.poziom==1:
                    gracz.lvlup=625
                elif gracz.poziom==2:
                    gracz.lvlup=2125
                gracz.poziom+=1
                gracz.maxhp+=10
                gracz.hp=gracz.maxhp
                gracz.exp=0
                gracz.minatak+=2
                gracz.maxatak+=2
                textbox(580,95,630,420,5)
                screen.blit(tekst.render('Wygrywasz!',True,czarny),(620,120))
                screen.blit(tekst.render(f'Otrzymujesz {ZdobytyExp} expa oraz {ZdobyteZloto} złota!',True,czarny),(620,150))
                screen.blit(tekst.render(f'Gratulacje!',True,czarny),(620,200))
                screen.blit(tekst.render(f'Osiągnąłeś {gracz.poziom} poziom doświadczenia!',True,czarny),(620,230))
                screen.blit(tekst.render(f'Twoje maksymalne zdrowie wzrasta o 10!',True,czarny),(620,260))
                screen.blit(tekst.render(f'Aktualnie masz go {gracz.maxhp}.',True,czarny),(620,290))
                screen.blit(tekst.render(f'Twoje ataki zadają 2 punkty obrażeń więcej!',True,czarny),(620,320))
                screen.blit(tekst.render(f'Aktualnie {gracz.minatak}-{gracz.maxatak}!',True,czarny),(620,350))
                screen.blit(tekst.render(f'Zyskujesz na celności!',True,czarny),(620,380))
                screen.blit(tekst.render(f'Masz {gracz.szansa}% szans na trafienie!',True,czarny),(620,410))
                screen.blit(grafika.przycisk.powrot,self.przycisk_w_powrot)
            global obszar
            obszar='wygrana'

    def przegrana(self):
        pygame.mixer.music.stop()
        pygame.mixer.music.load("mp3/przegrana.wav")
        pygame.mixer.music.play()
        for i in range(4):
            screen.fill((0,0,0))
            screen.blit(grafika.tlo.arena,(0,0))
            pygame.time.Clock().tick(12)
            screen.blit(pygame.transform.flip(grafika.atak[i],True,False),(680,80))
            pygame.display.update()
        textbox(100,100,420,200,5)
        screen.blit(tekst.render('Zginąłeś',True,czarny),(125,125))
        screen.blit(tekst.render('Chcesz spróbować jeszcze raz?',True,czarny),(125,155))
        screen.blit(grafika.przycisk.reset,self.przycisk_p_reset)
        screen.blit(grafika.przycisk.wyjdz,self.przycisk_p_wyjdz)
        global obszar
        obszar='przegrana'

    def koniec(self):
        textbox(600,100,520,200,5)
        screen.blit(tekst.render('Gratulacje!',True,czarny),(625,125))
        screen.blit(tekst.render('Zostałeś królem areny!',True,czarny),(625,155))
        screen.blit(tekst.render('Dziękujemy za grę w Miecze i Kalosze!',True,czarny),(625,185))
        screen.blit(grafika.przycisk.reset,self.przycisk_reset)
        screen.blit(grafika.przycisk.wyjdz,self.przycisk_wyjdz)
        pygame.display.update()
        global obszar
        obszar='koniec'
    
    def przegrana_buttons(self):
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_p_reset[0],kursor[1]-self.przycisk_p_reset[1])
        if 0<=przycisk[0]<=grafika.przycisk.reset.get_width() and 0<=przycisk[1]<=grafika.przycisk.reset.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            global gracz,obszar
            gracz=Gracz()
            obszar='wstep'
            wstep.render()
        przycisk=(kursor[0]-self.przycisk_p_wyjdz[0],kursor[1]-self.przycisk_p_wyjdz[1])
        if 0<=przycisk[0]<=grafika.przycisk.wyjdz.get_width() and 0<=przycisk[1]<=grafika.przycisk.wyjdz.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            pygame.quit()
            exit()

    def koniec_buttons(self):
        kursor=pygame.mouse.get_pos()
        przycisk=(kursor[0]-self.przycisk_reset[0],kursor[1]-self.przycisk_reset[1])
        if 0<=przycisk[0]<=grafika.przycisk.reset.get_width() and 0<=przycisk[1]<=grafika.przycisk.reset.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            global gracz,obszar
            gracz=Gracz()
            obszar='wstep'
            wstep.render()
        przycisk=(kursor[0]-self.przycisk_wyjdz[0],kursor[1]-self.przycisk_wyjdz[1])
        if 0<=przycisk[0]<=grafika.przycisk.wyjdz.get_width() and 0<=przycisk[1]<=grafika.przycisk.wyjdz.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            pygame.quit()
            exit()

    def wygrana_buttons(self):
        kursor=pygame.mouse.get_pos()
        if gracz.exp>0:
            przycisk=(kursor[0]-self.przycisk_powrot[0],kursor[1]-self.przycisk_powrot[1])
        else:
            przycisk=(kursor[0]-self.przycisk_w_powrot[0],kursor[1]-self.przycisk_w_powrot[1])
        if 0<=przycisk[0]<=grafika.przycisk.powrot.get_width() and 0<=przycisk[1]<=grafika.przycisk.powrot.get_height():
            pygame.mixer.Sound.play(dzwiek.przycisk)
            global obszar
            obszar='miasto'

gracz=Gracz()
wstep=Wstep()        
miasto=Miasto()
tawerna=Tawerna()
sklep=Sklep()
statystyki=Statystyki()
arena=Arena()
walka=Walka()
opp=stats_opp()
grafika=PNG()
dzwiek=MP3()
obszary={'wstep': wstep.buttons,
        'miasto': miasto.buttons,
        'tawerna': tawerna.buttons,
        'sklep': sklep.buttons,
        'mikstura': sklep.mikstura_buttons,
        'miecz': sklep.miecz_buttons,
        'zbroja': sklep.zbroja_buttons,
        'statystyki': statystyki.buttons,
        'arena': arena.wejscie_buttons,
        'start': arena.start_buttons,
        'wygrana': walka.wygrana_buttons,
        'koniec': walka.koniec_buttons,
        'przegrana': walka.przegrana_buttons}

obszar='wstep'
anim=0
klatki=0

wstep.render()
while True:
    pygame.time.Clock().tick(120)
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            exit()
        
        if event.type==pygame.MOUSEBUTTONDOWN:
            obszary[obszar]()

    if obszar=='miasto':
        miasto.render()
        if klatki==8:
            anim+=1
            klatki=0
        if anim==len(grafika.gracz):
            anim=0
        klatki+=1

        sprite=pygame.transform.scale(pygame.transform.flip(grafika.gracz[anim],True,False),(230,230))
        screen.blit(sprite,(500,400))
        
    pygame.display.update()