import tkinter as tk
import random
import time
from helper import Helper as hp

class Modele():
    def __init__(self, parent):
        self.parent = parent
        # STATS
        self.argent = 100
        # CANVAS
        self.hauteur = 720
        self.largeur = 900
        # CREEPS
        self.delaisCreeps = 0
        self.delaisCreepsMax = 24 #1 seconde
        self.creeps = []
        self.creepsVue = []
        # TOURS
        self.tour = []
        # CHEMIN
        self.troncon = [[75, 0, 130, 460], 
                        [75, 460, 269, 529],
                        [214, 100, 269, 529],
                        [214, 100, 778, 159],
                        [723, 100, 778, 280],
                        [387, 221, 778, 280],
                        [387, 280, 447, 500],
                        [387, 460, 778, 529]]
        
        # MÉTHODES
        self.creer_creep()

    def creer_creep(self):
        n = 20
        for i in range(n):
            creep = Creep(self)
            creep.posX = self.troncon[0][0]
            creep.posY = self.troncon[0][1]
            creep.tronconActuel[0] = self.troncon[0]
            creep.prochainTroncon = self.troncon[0]
            self.creeps.append(creep)       

    # def jouer_coup(self):
    #     for i in self.creeps: #creepsVue
    #         i.deplacer()
            
    #     if self.delaisCreeps == 0:
    #         c = self.creeps.pop()
    #         self.creepsVue.append(c)
    #         self.delaisCreeps = self.delaisCreepsMax
    #     else:
    #         self.delaisCreeps -= 1

class Creep():
    def __init__(self, parent):
        self.parent = parent
        self.posX = 0
        self.posY = 0
        self.cx = 0
        self.cy = 0
        self.compteurTroncon = 0
        self.prochainTroncon = []
        self.tronconActuel = []
        self.angleActuelle = 0
        self.distance = 0
        self.vitesse = 5
        self.taille = 50
        self.couleur = "rouge"

    def trouver_cible(self):
        self.prochainTroncon = Modele.troncon[self.compteurTroncon + 1]

    def deplacer(self):   
        self.posX, self.posY = hp.getAngledPoint(self.angleActuelle,self.vitesse,self.posX,self.posY)
        self.distance = hp.calcDistance(self.tronconActuel[0], self.tronconActuel[1], self.prochainTroncon[0], self.prochainTroncon[1])
        if self.distance < self.vitesse:
            self.trouver_cible()
        
        # self.posX1, self.posY1 = hp.getAngledPoint(self.angleActuelle, self.vitesse, self.posX1, self.posY1)
        # self.distance = hp.calcDistance(self.posX1, self.posY1, self.cx, self.cy)
        # if self.distance < self.vitesse:
        #     self.trouver_cible()

class Vue():
    def __init__(self, parent, modele):

        self.canevas: tk.Canvas
        self.parent = parent
        self.modele = modele
        self.root = tk.Tk()
        self.root.title("Tower Defense")
        # self.creer_aire_de_jeu()
        # self.creer_bouton_tour("Tour Projectile", "blue")
        # self.creer_bouton_tour("Tour Éclair", "yellow")
        # self.creer_bouton_tour("Tour Poison", "green")
        # self.canevas.bind("<Button-1>", self.parent.clic_souris)


    # def selectionner_type_tour(self, couleur):
    #     self.parent.type_tour = couleur

    # def creer_bouton_tour(self, nom, couleur):
    #     # Créez un bouton pour créer une tour de type spécifié
    #     bouton = tk.Button(self.root, text=nom, command=lambda: self.selectionner_type_tour(couleur))
    #     bouton.pack()

    # def afficher_creep(self):
    #     for creepVue in self.modele.creepsVue:
    #         self.canevas.delete(creepVue)  # Supprimer l'ancien cercle

        #self.modele.creepsVue = []  # Réinitialiser la liste des vues des creeps

        # for creep in self.modele.creeps:
        #     x1, y1 = creep.posX1, creep.posY1
        #     x2, y2 = x1 + creep.largeur * 2, y1 + creep.hauteur
        #     creepVue = self.canevas.create_oval(x1, y1, x2, y2, fill="red", width=0, tags="creep")
        #     self.modele.creepsVue.append(creepVue)

    # def creer_aire_de_jeu(self):
    #     self.cadre_jeu = tk.Frame(self.root)
    #     self.canevas = tk.Canvas(self.root, width=self.modele.largeur, height=self.modele.hauteur, bg="white")
    #     #Tronçon
        self.canevas.create_rectangle(75, 0, 130, 460, fill="black")
        self.canevas.create_rectangle(75, 460, 269, 529, fill="blue")
        self.canevas.create_rectangle(214, 100, 269, 529, fill="black")
        self.canevas.create_rectangle(214, 100, 778, 159, fill="blue")
        self.canevas.create_rectangle(723, 100, 778, 280, fill="black")
        self.canevas.create_rectangle(387, 221, 778, 280, fill="blue")
        self.canevas.create_rectangle(387, 280, 447, 500, fill="black")
        self.canevas.create_rectangle(387, 460, 778, 529, fill="blue")

    #     #Chateau
    #     self.canevas.create_rectangle(678, 450, 778, 550, fill="grey")
    #     self.canevas.create_rectangle(678, 410, 638, 450, fill="grey")
    #     self.canevas.create_rectangle(778, 410, 818, 450, fill="grey")
    #     self.canevas.pack()
    #     self.cadre_jeu.pack()



class Controleur():
    def __init__(self):
        self.modele = Modele(self)
        self.vue = Vue(self, self.modele)
        # self.vue.afficher_creep()
        self.bouclerJeu()
        self.vue.root.mainloop()


    # def clic_souris(self, event):
    #     x, y = event.x, event.y
    #     print("clicsouris")
    #     self.emplacement_tour = (x, y)
    #     self.placer_tour()



    # def placer_tour(self):
    #     if self.emplacement_tour and self.type_tour:
    #         # Créez un carré de tour à l'emplacement choisi avec la couleur sélectionnée
    #         x, y = self.emplacement_tour
    #         taille = 50  # Taille du carré de la tour
    #         tour = self.vue.canevas.create_rectangle(x - taille / 2, y - taille / 2, x + taille / 2, y + taille / 2,
    #                                             fill=self.type_tour)
    #         self.modele.tour.append(tour)
    #         self.modele.argent -= 20  # Réduisez l'argent du joueur lorsqu'une tour est placée


    def bouclerJeu(self):
        # self.modele.jouer_coup()
        # self.vue.afficher_creep()
        self.vue.root.after(40, self.bouclerJeu)


if __name__ == "__main__":
    c = Controleur()
