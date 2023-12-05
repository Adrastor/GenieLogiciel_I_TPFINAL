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
        self.hauteur = 800
        self.largeur = 1200
        # CREEPS
        self.delaisCreeps = 0
        self.delaisCreepsMax = 24 #1 seconde
        self.creeps = []
        self.creepsVue = []
        # TOURS
        self.tour = []
        # CHEMIN
        self.troncons = [[150, 0, 150, 500], 
                        [150, 500, 400, 500],
                        [400, 500, 400, 100],
                        [400, 100, 1000, 100],
                        [1000, 100, 1000, 300],
                        [1000, 300, 700, 300],
                        [700, 300, 700, 500],
                        [700, 500, 1000, 500]]
        # MÉTHODES
        self.creer_creep()

    def creer_creep(self):
        n = 20
        for i in range(n):
            creep = Creep(self,self.troncons[0])
            self.creeps.append(creep)       

    def jouer_coup(self):
        for i in self.creeps: #creepsVue
            i.deplacer()
            
        if self.delaisCreeps == 0:
            c = self.creeps.pop()
            self.creepsVue.append(c)
            self.delaisCreeps = self.delaisCreepsMax
        else:
            self.delaisCreeps -= 1

class Creep():
    def __init__(self, parent, troncon):
        self.parent = parent
        self.compteurTroncon = 0
        self.tronconActuel = troncon
        self.posX, self.posY, self.cx, self.cy = troncon
        self.angleActuelle = hp.calcAngle(self.posX, self.posY, self.cx, self.cy)
        self.distance = 0
        self.vitesse = 5
        self.taille = 50
        self.couleur = "rouge"

    def deplacer(self):   
        self.posX, self.posY = hp.getAngledPoint(self.angleActuelle,self.vitesse,self.posX,self.posY)
        self.distance = hp.calcDistance(self.posX, self.posY, self.cx, self.cy)
        if self.distance < self.vitesse:
            self.compteurTroncon += 1
            if self.compteurTroncon == len(self.parent.troncons):
                pass # RENDU AU CHATEAU
            else:
                self.tronconActuel = self.parent.troncons[self.compteurTroncon]
                self.posX, self.posY, self.cx, self.cy = self.tronconActuel
                self.angleActuelle = hp.calcAngle(self.posX, self.posY, self.cx, self.cy)
        

class Vue():
    def __init__(self, parent, modele):

        self.parent = parent
        self.modele = modele
        self.root = tk.Tk()
        self.root.title("Tower Defense")
        
        self.canevas = tk.Canvas(self.root,width = self.modele.largeur, height = self.modele.hauteur)
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

    #     for creep in self.modele.creeps:
    #         x1, y1 = creep.posX1, creep.posY1
    #         x2, y2 = x1 + creep.largeur * 2, y1 + creep.hauteur
    #         creepVue = self.canevas.create_oval(x1, y1, x2, y2, fill="red", width=0, tags="creep")
    #         self.modele.creepsVue.append(creepVue)

    # def creer_aire_de_jeu(self):
    #     self.cadre_jeu = tk.Frame(self.root)
    #     self.canevas = tk.Canvas(self.root, width=self.modele.largeur, height=self.modele.hauteur, bg="white")
    
    #     #Tronçon
    
        for i in self.modele.troncons:
            x,y,x1,y1 = i
            self.canevas.create_line(x,y,x1,y1, width=4)
            
        translationY = -99
        translationX = 320        
    #     #Chateau
        self.canevas.create_rectangle(678+ translationX, 500 + translationY, 778+ translationX, 600+ translationY, fill="grey")
        self.canevas.create_rectangle(678+ translationX, 460+ translationY, 638+ translationX, 500+ translationY, fill="grey")
        self.canevas.create_rectangle(778+ translationX, 460+ translationY, 818+ translationX, 500+ translationY, fill="grey")
        self.canevas.pack()



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
