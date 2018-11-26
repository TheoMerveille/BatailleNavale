#!/usr/bin/python3
# -*-coding:Latin-1 -*
from random import *
from time import *
import os


def initialiser_grille():
	"""Fonction qui crée une grille de '-1' de taille 10*10.
		paramètres: - 
		sortie: tab - une grille 10*10
	"""
	tab=[]
	for i in range(10):
		ligne=[]
		for j in range(10):
			ligne.append(-1)
		tab.append(ligne)
	return tab


def placer_bateaux(grille):
	"""
		place les bateaux de manière aléatoire sur une grille. Les bateaux ne peuvent pas se chevaucher ni être les uns à coté des autres.
		paramètre: grille - une matrice de -1 (plateau de jeu vide)
		sortie: -
	"""
	bateau1=False
	bateau2=False
	bateau3=False
	bateau4=False
	bateau5=False
	while not bateau1:
	    x=randint(0,9)
	    y=randint(0,9)
	    sens=randint(0,1)
	    if sens==0 and x<=5:
	        if x!=0:
	          grille[x-1][y]=12
	        if x+5<=12:
	            grille[x+4][y]=12
	        for i in range(5):
	            grille[x+i][y]=1
	            if y!=0:
	                grille[x+i][y-1]=12
	            if y!=9:
	                grille[x+i][y+1]=12
	        bateau1=True
	    elif sens==1 and y<=5:
	        if y!=0:
	            grille[x][y-1]=12
	        if y+5<=12:
	            grille[x][y+4]=12
	        for i in range(5):
	            grille[x][y+i]=1
	            if x!=0:
	                grille[x-1][y+i]=12
	            if x!=9:
	                grille[x+1][y+i]=12
	        bateau1=True
	while not bateau2:
	    x=randint(0,9)
	    y=randint(0,9)
	    sens=randint(0,1)
	    if sens==1 and x<=6 and grille[x][y]==-1 and grille[x+1][y]==-1 and grille[x+2][y]==-1 and grille[x+3][y]==-1:
	        if x!=0:
	            grille[x-1][y]=12
	        if x+4<=9:
	            grille[x+4][y]=12
	        for i in range(4):
	            grille[x+i][y]=2
	            if y!=0:
	                grille[x+i][y-1]=12
	            if y!=9:
	                grille[x+i][y+1]=12
	        bateau2=True
	    if sens==2 and y<=6 and grille[x][y]==-1 and grille[x][y+1]==-1 and grille[x][y+2]==-1 and grille[x][y+3]==-1:
	        if y!=0:
	            grille[x][y-1]=12
	        if y+4<=9:
	            grille[x][y+4]=12
	        for i in range(4):
	            grille[x][y+i]=2
	            if x!=0:
	                grille[x-1][y+i]=12
	            if x!=9:
	                grille[x+1][y+i]=12
	        bateau2=True
	while not bateau3:
	    x=randint(0,9)
	    y=randint(0,9)
	    sens=randint(0,1)
	    if sens==1 and x<=7 and grille[x][y]==-1 and grille[x+1][y]==-1 and grille[x+2][y]==-1:
	        if x!=0:
	            grille[x-1][y]=12
	        if x+3<=9:
	            grille[x+3][y]=12
	        for i in range(3):
	            grille[x+i][y]=3
	            if y!=0:
	                grille[x+i][y-1]=12
	            if y!=9:
	                grille[x+i][y+1]=12
	        bateau3=True
	    if sens==2 and y<=7 and grille[x][y]==-1 and grille[x][y+1]==-1 and grille[x][y+2]==-1:
	        if y!=0:
	            grille[x][y-1]=12
	        if y+3<=9:
	            grille[x][y+3]=12
	        for i in range(3):
	            grille[x][y+i]=3
	            if x!=0:
	                grille[x-1][y+i]=12
	            if x!=9:
	                grille[x+1][y+i]=12
	        bateau3=True
	while not bateau4:
	    x=randint(0,9)
	    y=randint(0,9)
	    sens=randint(0,1)
	    if sens==1 and x<=7 and grille[x][y]==-1 and grille[x+1][y]==-1 and grille[x+2][y]==-1:
	        if x!=0:
	            grille[x-1][y]=12
	        if x+3<=9:
	            grille[x+3][y]=12
	        for i in range(3):
	            grille[x+i][y]=4
	            if y!=0:
	                grille[x+i][y-1]=12
	            if y!=9:
	                grille[x+i][y+1]=12
	        bateau4=True
	    if sens==2 and y<=7 and grille[x][y]==-1 and grille[x][y+1]==-1 and grille[x][y+2]==-1:
	        if y!=0:
	            grille[x][y-1]=12
	        if y+3<=9:
	            grille[x][y+3]=12
	        for i in range(3):
	            grille[x][y+i]=4
	            if x!=0:
	                grille[x-1][y+i]=12
	            if x!=9:
	                grille[x+1][y+i]=12
	        bateau4=True
	while not bateau5:
	    x=randint(0,9)
	    y=randint(0,9)
	    sens=randint(0,1)
	    if sens==1 and x<=8 and grille[x][y]==-1 and grille[x+1][y]==-1:
	        if x!=0:
	            grille[x-1][y]=12
	        if x+2<=9:
	            grille[x+2][y]=12
	        for i in range(2):
	            grille[x+i][y]=5
	            if y!=0:
	                grille[x+i][y-1]=12
	            if y!=9:
	                grille[x+i][y+1]=12
	        bateau5=True
	    if sens==2 and y<=8 and grille[x][y]==-1 and grille[x][y+1]==-1:
	        if y!=0:
	            grille[x][y-1]=12
	        if y+2<=9:
	            grille[x][y+2]=12
	        for i in range(2):
	            grille[x][y+i]=5
	            if x!=0:
	                grille[x-1][y+i]=12
	            if x!=9:
	                grille[x+1][y+i]=12
	        bateau5=True  
	for i in range(10):
		for j in range(10):
			if grille[i][j]==12:
				grille[i][j]=-1
                

def tir_valide(tirs,ligne,colonne):
	"""
		vérifie que le tir est dans la grille de tirs et si le coup n'a pas deja été choisi.
		paramètre: tirs - matrice des tirs effectués
				   ligne - entier
				   colonne - entier
		sortie: bool
	"""
	return ligne<10 and ligne>=0 and colonne<10 and colonne>=0 and tirs[ligne][colonne]==-1


def prochain_coup(tirs):
	"""
		Demande à l'utilisateur de choisir la prochaine position du coup et renvoie la valeur de ce coup après avoir vérifié que le coup est valide
		parmaètre: tirs - matrice des tirs
		sortie: (ligne,colonne-1) - couple de coordonnées de 0 à 9.
	"""
	coup=input("Saisissez la position du prochain tir (une lettre et un chiffre exemple:'A 5') : ")
	ligne=ord(coup[0])-65
	colonne=int(coup[2])
	if colonne==1:
		if len(coup)==4:
			colonne=10
	if tir_valide(tirs,ligne,colonne-1):
		return (ligne,colonne-1)

def resultat_tir(bateaux,ligne,colonne):
	"""
		Renvoie un entier: 0 si le coup est dans l'eau, 1 si le coup touche un bateau et 2 si le coup coule un bateau.
		paramètre: bateaux - matrice contenant les bateaux placés
				   ligne - entier
				   colonne - entier
		sortie: 0/1/2 - int 
	"""
	if bateaux[ligne][colonne]==-1:
		return 0
	if bateaux[ligne][colonne]!=-1:
		cpt=0
		nb=bateaux[ligne][colonne]
		for i in bateaux:
			for j in i:
				if j== nb:
					cpt+=1
		if cpt==1:
				return 2
		else:
			return 1


def tirer(tirs,bateaux,ligne,colonne):
	"""
		modifie la valeur de tirs pour annoncer si le bateau est touché, coulé ou si le coup est dans l'eau.
		paramètres:tirs - matrice contenant les coups deja effectués
				   bateaux - matrice contenant les bateaux placés
				   ligne - entier
				   colonne - entier
		sortie
	"""
	if resultat_tir(bateaux,ligne,colonne)==0:
		print("dans l'eau!")
		tirs[ligne][colonne]=0

	elif resultat_tir(bateaux,ligne,colonne)==1:
		tirs[ligne][colonne]=1
		print("Touche!")
		if bateaux[ligne][colonne]==1:
			bateaux[ligne][colonne]="t1"
		elif bateaux[ligne][colonne]==2:
			bateaux[ligne][colonne]="t2"
		elif bateaux[ligne][colonne]==3:
			bateaux[ligne][colonne]="t3"
		elif bateaux[ligne][colonne]==4:
			bateaux[ligne][colonne]="t4"
		elif bateaux[ligne][colonne]==5:
			bateaux[ligne][colonne]="t5"

	elif resultat_tir(bateaux,ligne,colonne)==2:
		print("Coule!")

		if bateaux[ligne][colonne]==1:
			t="t1"
		elif bateaux[ligne][colonne]==2:
			t="t2"
		elif bateaux[ligne][colonne]==3:
			t="t3"
		elif bateaux[ligne][colonne]==4:
			t="t4"
		elif bateaux[ligne][colonne]==5:
			t="t5"
		
		for i in range(len(bateaux)):
			for j in range(len(bateaux[i])):
				if bateaux[i][j]==t:
					bateaux[i][j]="c"
					tirs[i][j]=2
		bateaux[ligne][colonne]="c"
		tirs[ligne][colonne]=2



def partie_finie(tirs):
	"""
		compte le nombre de 2 dans la grille de tirs pour savoir si il y a autant de 2 que de cases de bateaux au totale.
		paramètre: tirs - matrice contenant les coups deja effectués
		sortie: bool 
	"""
	cpt=0
	for i in tirs:
		for j in i:
			if j==2:
				cpt+=1
			if cpt==17:
				return True
	return False

def affiche_grille(tirs):
	""" Fonction qui affiche le contenue de la grille avec les lignes et les colonnes.
		paramètres: tirs - une un tableau
		sortie: - 
	"""
	print("  ", end=' ')  # espace pour les numéros de colonnes
	for i in range(1,11): 	#affichage des numéros de colonnes
		print(i, end=' ')
	print("\n")
	for k in range(0,len(tirs)):
		print(chr(65+k),end='  ')		#affiche les lettres pour les lignes
		for j in range(len(tirs[0])):
			if tirs[k][j]==-1:
				print(".",end=' ')	#affiche les lignes du tableau
			if tirs[k][j]==0:
				print("*",end=' ')
			if tirs[k][j]==1:
				print("+",end=' ')
			if tirs[k][j]==2:
				print("X",end=' ')
		print("")						#retourne à la ligne


def jouer():
	"""
		Explique les regles du jeu et permet de jouer.
		paramètres: -
		sortie: -
	"""

	os.system('clear')
	print("Bienvenue dans la Bataille navale!\n")
	sleep(3)
	print("Votre adversaire possede 5 bateaux:\n1 bateau de 5 cases\n1 bateau de 4 cases\n2 bateaux de 3 cases\n1 bateau de 2 cases")
	print("\nPour couler un bateau vous devez detruire toutes ses parties.")
	sleep(3)
	print("\nsignification des symboles:\n . : cases non explores\n * : tirs dans l'eau\n + : tirs touches\n X : bateaux coules.")
	sleep(3)
	print("\nBonne chance!\n")
	lancer=input("Appuyer sur une ENTREZ pour lancer!")
	while lancer!="":
		lancer=input("Appuyer sur une ENTREZ pour lancer!")
	os.system('clear')


	tirs=initialiser_grille()
	bateaux=initialiser_grille()
	placer_bateaux(bateaux)
	while not partie_finie(tirs):
		print("\nsignification des symboles:\n . : cases non explores\n * : tirs dans l'eau\n + : tirs touches\n X : bateaux coules.\n")
		affiche_grille(tirs)
		print("")
		coordonees=prochain_coup(tirs)
		tirer(tirs,bateaux,coordonees[0],coordonees[1])
		sleep (3)
		os.system('clear')
	print("Vous avez gagne!")

jouer()