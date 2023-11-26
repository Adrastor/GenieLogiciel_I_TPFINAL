from tkinter import *
import random
import time
from helper import Helper as hp

class Modele():
    def __init__(self, parent):
        self.parent = parent
        self.hauteur = 720
        self.largeur = 900
        self.creeps = []
        self.creepsVue =[]
        self.creep = Creep(self)
        self.creer_creep()

    def creer_creep(self):
        n = 1
        for i in range(n):
            print(1)
            x = random.randrange(self.largeur)
            y = random.randrange(self.hauteur)
            creep = Creep(self)
            self.creeps.append(creep)

    def jouer_coup(self):
        for i in self.creeps:
            i.deplacer()

class Creep():
    def __init__(self, parent):
        self.parent = parent
        self.largeur = 55/4
        self.hauteur = 55/2
        self.cx = 0
        self.cy = 0
        self.angleActuelle = 0
        self.posX1 = 75 + self.largeur #deplace axe horizon
        self.posY1 = 0           #deplace axe verticale
        self.posX2 = self.posX1 + self.largeur * 2
        self.posY2 = self.posY1 + self.hauteur
        self.vitesse = 5
        self.trouver_cible()
        self.deplacer()

    def trouver_cible(self):
        self.cx = self.posX1
        self.cy = 460 - self.hauteur
        self.angleActuelle = hp.calcAngle(self.posX1, self.posY1, self.cx, self.cy)

    def deplacer(self):
        self.posX1, self.posY1 = hp.getAngledPoint(self.angleActuelle, self.vitesse, self.posX1, self.posY1)
        print(self.posX1,self.posY1)
        self.distance = hp.calcDistance(self.posX1, self.posY1, self.cx, self.cy)
        if self.distance < self.vitesse:
            self.trouver_cible()


class Vue():
    def __init__(self, parent, modele):
        self.parent = parent
        self.modele = modele
        self.root = Tk()
        self.root.title("Tower Defense")
        self.creer_aire_de_jeu()

    def afficher_creep(self):
        if self.modele.creepsVue:
            self.canevas.delete(self.modele.creepsVue[0])
            self.modele.creepsVue.pop(0)
        for creep in self.modele.creeps:
            creepVue = self.canevas.create_oval(creep.posX1, creep.posY1, creep.posX2, creep.posY2, fill="red", width=0,
                                     tags="creep")
            self.modele.creepsVue.append(creepVue)

    def creer_aire_de_jeu(self):
        self.cadre_jeu = Frame(self.root)
        self.canevas = Canvas(self.root, width=self.modele.largeur, height=self.modele.hauteur, bg="white")
        #Tronçon
        self.canevas.create_rectangle(75, 0, 130, 460, fill="black")
        self.canevas.create_rectangle(75, 460, 269, 529, fill="blue")
        self.canevas.create_rectangle(214, 100, 269, 529, fill="black")
        self.canevas.create_rectangle(214, 100, 778, 159, fill="blue")
        self.canevas.create_rectangle(723, 100, 778, 280, fill="black")
        self.canevas.create_rectangle(387, 221, 778, 280, fill="blue")
        self.canevas.create_rectangle(387, 280, 447, 500, fill="black")
        self.canevas.create_rectangle(387, 460, 778, 529, fill="blue")

        #Chateau
        self.canevas.create_rectangle(678, 450, 778, 550, fill="grey")
        self.canevas.create_rectangle(678, 410, 638, 450, fill="grey")
        self.canevas.create_rectangle(778, 410, 818, 450, fill="grey")
        self.canevas.pack()
        self.cadre_jeu.pack()


class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        self.vue.afficher_creep()
        self.bouclerJeu()
        self.vue.root.mainloop()

    def bouclerJeu(self):
        self.modele.jouer_coup()
        self.vue.afficher_creep()
        self.vue.root.after(100, self.bouclerJeu)


if __name__ == "__main__":
    c = Controleur()
