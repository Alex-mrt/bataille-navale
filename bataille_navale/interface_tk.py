from tkinter import*
from tkinter import font
from jeu import*

############################################## Initialisation du jeu ###########################################
bateau_en_cours_de_placement=None # variable qui contiendra le bateau que le joueur est en train de placer
case_depart=None # case de départ du bateau en cours de placement
nombre_bateaux_places=0 # variable qui contient le nombre de bateaux placés du joueur
bateaux_places=[0 for i in range(5)] # liste de 0 et 1 : dans l'ordre des numéros de bateaux, 1 si le bateau est placé, 0 sinon
combat=False # variable de type booléen qui passe à True lorsque tous les bateaux du joueur lorsque tous les bateaux du joueur sont placés (début du combat)
             # et que c'est au tour du joueur de tirer
grille_ordi = init_grille_hasard() # initialisation de la grille de l'ordinateur
nombre_attaque_joueur=0

nombre_attaque_ennemi=0


############################################## Création de la fenêtre ###########################################
fenetre= Tk() 
fenetre.configure(bg='white') # couleur d'arrière plan
fenetre.geometry("1400x850") #taille de la fenêtre
maPolice1=font.Font(family='Calibri', size=14, weight='bold') # police de caractères

############################### Création des 2 cadres composant la fenêtre graphique ############################

################## Cadre 1 : la grille du joueur ##################

###### création et placement du cadre ######
cadre1=Frame(master=fenetre,width=780,height=850, bg ='#FFF7E7',highlightbackground="gray", highlightthickness=4) # création du cadre
cadre1.grid_propagate(0) # cadre de taille fixe dans la fenêtre
cadre1.grid(row=0, column=0) # placement du cadre dans la fenêtre

###### création et placement du cadre pour le nombre d'attaque ######
zone_texte_nombre_attaques_joueur = Label(cadre1, text="", font=maPolice1, bg='#FFF7E7')
zone_texte_nombre_attaques_joueur.grid(row=5, column=0, padx=10, pady=10)
zone_texte_nombre_attaques_ennemi = Label(cadre1, text="", font=maPolice1, bg='#FFF7E7')
zone_texte_nombre_attaques_ennemi.grid(row=6, column=0, padx=10, pady=10)

zone_texte_nombre_attaques_joueur['text'] = "Nombre d'attaque du joueur: ",nombre_attaque_joueur
zone_texte_nombre_attaques_ennemi['text'] = "Nombre d'attaque de l'ordinateur: ",nombre_attaque_ennemi


##### cadre en haut pour les consignes ######
consigne = Label(cadre1,text="Placez vos bateaux sur la grille",font=maPolice1, bg ='#FFF7E7')
consigne.grid(row=0,column=0,padx=10,pady=10)


##### affichage de la grille du joueur ######
terrain_joueur= Canvas(cadre1,height=400,width=400) # permet de définir les dimensions du canevas => largeur, hauteur
terrain_joueur.grid(row=1,column=0,padx=100,pady=10) # affiche le canevas et définit sa place
grille_joueur_ecran=[[terrain_joueur.create_rectangle(i*40,j*40,(i+1)*40,(j+1)*40,fill="#efeeec") for i in range(10)] for j in range(10)] # création et affichage de la grille

##### cadre pour les commentaires sous la grille du joueur ######
commentaire_joueur= Label(cadre1,text="",font=maPolice1, bg ='#FFF7E7')
commentaire_joueur.grid(row=2,column=0,padx=10,pady=10)

##### affichage des bateaux à placer ######
bateaux= Canvas(cadre1,height=200,width=700,bg='#FFF7E7',highlightbackground="#FFF7E7", highlightthickness=4) # permet de définir les dimensions du canevas => largeur, hauteur
bateaux.grid(row=3,column=0,padx=50,pady=10)  # affiche le canevas et définit sa place

bateaux.create_text(100,20, text="1 porte-avion", fill="black", font=maPolice1)
porte_avion=[bateaux.create_rectangle(25+i*30,35,25+(i+1)*30,65,fill="light gray") for i in range(5)] # affichage du porte-avion
bateaux.create_text(100,80, text="5 cases", fill="black", font=maPolice1)

bateaux.create_text(100,130, text="1 croiseur", fill="black", font=maPolice1)
croiseur=[bateaux.create_rectangle(40+i*30,145,40+(i+1)*30,175,fill="light gray") for i in range(4)] # affichage du croiseur
bateaux.create_text(100,190, text="4 cases", fill="black", font=maPolice1)

bateaux.create_text(370,20, text="2 sous-marins", fill="black", font=maPolice1)
sous_marin_1=[bateaux.create_rectangle(270+i*30,35,270+(i+1)*30,65,fill="light gray") for i in range(3)] # affichage du premier sous-marin
sous_marin_2=[bateaux.create_rectangle(390+i*30,35,390+(i+1)*30,65,fill="light gray") for i in range(3)] # affichage du deuxième sous-marin
bateaux.create_text(315,80, text="3 cases", fill="black", font=maPolice1)
bateaux.create_text(435,80, text="3 cases", fill="black", font=maPolice1)


bateaux.create_text(370,130, text="1 torpilleur", fill="black", font=maPolice1)
torpilleur=[bateaux.create_rectangle(340+i*30,145,340+(i+1)*30,175,fill="light gray") for i in range(2)] # affichage du torpilleur
bateaux.create_text(370,190, text="2 cases", fill="black", font=maPolice1)

# Affichage de la légende
bateaux.create_oval(590,65,610,45,width=2,fill="white")
bateaux.create_text(650,55, text="à l'eau", fill="black", font=maPolice1)
bateaux.create_oval(590,145,610,125,width=2,fill="red")
bateaux.create_text(650,135, text="touché", fill="black", font=maPolice1)
################## Cadre 2 : la grille de l'ordinateur ##################

##### création et placement du cadre ######
cadre2=Frame(master=fenetre,width=760,height=850, bg ='#ffeeee') # création du cadre
cadre2.grid_propagate(0) # cadre de taille fixe dans la fenêtre
cadre2.grid(row=0, column=1) # placement du cadre dans la fenêtre

##### cadre en haut pour les consignes ######
consigne_tir = Label(cadre2,text="",font=maPolice1, bg ='#ffeeee')
consigne_tir.grid(row=0,column=0,padx=10,pady=10)

##### affichage de la grille dd l'ordinateur ######
terrain_ordi= Canvas(cadre2,height=400,width=400) #permet de définir les dimensions du canevas => largeur, hauteur
terrain_ordi.grid(row=1,column=0,padx=100,pady=10) #affiche le canevas et définit sa place
grille_ordi_ecran=[[terrain_ordi.create_rectangle(i*40,j*40,(i+1)*40,(j+1)*40,fill="#efeeec") for i in range(10)] for j in range(10)] #création et affichage de la grille

##### cadre pour les commentaires sous la grille de l'ordinateur ######
commentaire_tir = Label(cadre2,text="",font=maPolice1, bg ='#ffeeee')
commentaire_tir.grid(row=2,column=0,padx=10,pady=10)

##### affichage de l'issue de la partie ######
issue = Label(cadre2,text="",font=maPolice1, bg ='#ffeeee')
issue.grid(row=3,column=0,padx=10,pady=100)

######################################## Le joueur place ses bateaux ###########################################

##### sélection du bateau à placer ######

def choix_bateau(event): # fonction liée à la détection d'un click sur le bouton gauche de la souris
    """ La fonction choix_bateau est liée à la détection d'un click sur le bouton gauche de la souris  
              - prend pour paramètre un évènement souris
              - colorie le bateau sélectionné 
              - met à jour les variables globales :
                       * bateau_en_cours_de_placement : prend la valeur du bateau sélectionné
                       * bateaux_places : l'élément de la liste correspondant au bateau placé prend la valeur 1
                       * nombre_bateaux_placés : s'incrémente de 1
    """
    global bateau_en_cours_de_placement
    global bateaux_places
    global nombre_bateaux_places
    if bateau_en_cours_de_placement is None: # si aucun bateau n'est en cours de placement
        x = event.x # on récupère les coordonnées de la souris
        y = event.y
        if 25<=x<=175 and 35<=y<=65 and bateaux_places[0]==0: # si le joueur a cliqué sur le porte-avion
                                                              # et que le porte-avion n'a pas encore été placé 
            bateau_en_cours_de_placement=liste_bateaux[0] # le bateau en cours de placement est le porte-avion
            bateaux_places[0]=1 # le porte-avion est placé
            nombre_bateaux_places+=1 # on incrémente de 1 le nombre de bateaux placés            
            for i in range(len(porte_avion)): # on colorie le bateau sélectionné
                bateaux.itemconfigure(porte_avion[i], outline='black', fill="gray")
        if 40<=x<=160 and 145<=y<=175 and bateaux_places[1]==0: # si le joueur a cliqué sur le croiseur
                                                                # et que le croiseur n'a pas encore été placé 
            bateau_en_cours_de_placement=liste_bateaux[1] # le bateau en cours de placement est le croiseur
            bateaux_places[1]=1 # le croiseur est placé
            nombre_bateaux_places+=1 # on incrémente de 1 le nombre de bateaux placés 
            for i in range(len(croiseur)): # on colorie le bateau sélectionné
                bateaux.itemconfigure(croiseur[i], outline='black', fill="gray")
        if 270<=x<=360 and 35<=y<=65 and bateaux_places[2]==0: # si le joueur a cliqué sur le sous-marin 1
                                                               # et que le sous-marin 1 n'a pas encore été placé 
            bateau_en_cours_de_placement=liste_bateaux[2] # le bateau en cours de placement est le sous-marin 1
            bateaux_places[2]=1 # le sous-marin 1 est placé
            nombre_bateaux_places+=1 # on incrémente de 1 le nombre de bateaux placés 
            for i in range(len(sous_marin_1)): # on colorie le bateau sélectionné
                bateaux.itemconfigure(sous_marin_1[i], outline='black', fill="gray")
        if 390<=x<=480 and 35<=y<=65 and bateaux_places[3]==0: # si le joueur a cliqué sur le sous-marin 2
                                                               # et que le sous-marin 2 n'a pas encore été placé 
            bateau_en_cours_de_placement=liste_bateaux[3] # le bateau en cours de placement est le sous-marin 2
            bateaux_places[3]=1 # le sous-marin 2 est placé
            nombre_bateaux_places+=1 # on incrémente de 1 le nombre de bateaux placés 
            for i in range(len(sous_marin_2)): # on colorie le bateau sélectionné
                bateaux.itemconfigure(sous_marin_2[i], outline='black', fill="gray")
        if 340<=x<=400 and 145<=y<=175 and bateaux_places[4]==0: # si le joueur a cliqué sur le torpilleur
                                                                 # et que le torpilleur n'a pas encore été placé 
            bateau_en_cours_de_placement=liste_bateaux[4] # le bateau en cours de placement est le torpilleur
            bateaux_places[4]=1 # le torpilleur est placé
            nombre_bateaux_places+=1 # on incrémente de 1 le nombre de bateaux placés 
            for i in range(len(torpilleur)): # on colorie le bateau sélectionné
                bateaux.itemconfigure(torpilleur[i], outline='black', fill="gray")
        
# Pour détecter un click sur le bouton gauche de la souris, on va relier (bind en anglais) cet évenement (<Button-1>) à la fonction choix_bateau             
bateaux.bind("<Button-1>", choix_bateau)

##### sélection des cases de la grille de jeu pour placer le bateau sélectionné ######

def choix_case_bateau(event):
    """ La fonction choix_case_bateau est liée à la détection d'un click sur le bouton gauche de la souris  
              - prend pour paramètre un évènement souris
              - s'il s'agit du choix de la première case pour le bateau en cours de placement : colorie la case si elle est valide
              - s'il s'agit du choix de la deuxième case pour le bateau en cours de placement : efface la première case sélectionnée si le choix de la
                deuxième case entraine un placement non valide pour le bateau en cours de placement, colorie la case sinon
              - colorie la case sélectionnée dans tous les autres cas à condition qu'elle soit adjacente à la précédente
              - met à jour le bateau en cours de placement en ajoutant chacune des positions sélectionnées à la liste le définissant
              - met à jour les variables globales :
                    * grille_joueur : met à jour la grille avec le numéro du bateau à toutes les positions sélectionnées
                    * bateau_en_cours_de_placement : prend la valeur None dès que le bateau en cours de placement est placé
                    * case_depart : prend la valeur de la première case sélectionnée par le joueur, puis la valeur None quand le bateau est placé
                    * combat : prend la valeur True dès que tous les bateaux ont été placés
    """
    global grille_joueur
    global bateau_en_cours_de_placement
    global case_depart
    global combat
    commentaire_joueur['text']= "" # on efface la zone de commentaire du joueur

    if bateau_en_cours_de_placement is not None: # si un bateau est en cours de placement
        x = event.x # on récupère les coordonnées de la souris
        y = event.y
        colonne=x//40 # puis la ligne et la colonne correspondantes dans le tableau
        ligne=y//40
        if case_depart is None : # choix de la première case 
            case_depart=[ligne,colonne] # case_depart est la première case choisie par le joueur
            if choix_premiere_case_valide(grille_joueur,case_depart): # cas où le choix est valide
                terrain_joueur.itemconfigure(grille_joueur_ecran[ligne][colonne], outline='black', fill="light gray") # on accepte le choix du joueur
                                                                                                                      # et on colorie la case sélectionnée dans la grille
            else: # cas où le choix n'est pas valide
                case_depart=None # on permet au joueur de choisir à nouveau la première case
        else : # cas de la deuxième case choisie par le joueur
            if choix_deuxieme_case_valide(grille_joueur,bateau_en_cours_de_placement,case_depart,[ligne,colonne]) : # cas où le choix est valide
                sens=orientation_bateau(case_depart,[ligne,colonne]) # on récupère l'orientation du bateau
                grille_joueur=positionne_bateau(grille_joueur, bateau_en_cours_de_placement, case_depart,sens) # on met à jour la grille du joueur
                if sens=="h":
                    terrain_joueur.create_rectangle(case_depart[1]*40, case_depart[0]*40, (case_depart[1]+longueur(bateau_en_cours_de_placement))*40, (case_depart[0]+1)*40,fill="#b3b2af",outline="black",width=3) #on fait apparaître le bateau
                if sens=="v":
                    terrain_joueur.create_rectangle(case_depart[1]*40, case_depart[0]*40, (case_depart[1]+1)*40, (case_depart[0]+longueur(bateau_en_cours_de_placement))*40,fill="#b3b2af",outline="black",width=3) #on fait apparaître le bateau
                if nombre_bateaux_places==5 and not combat: # cas où tous les bateaux sont placés
                    consigne['text']=""
                    consigne_tir['text']="L'ennemi a aussi placé ses bateaux. Vous pouvez tirer"
                    combat=True # le combat peut commencer
                else: # sinon on réinitialise le bateau en cours de placement pour pouvoir en placer un autre 
                    bateau_en_cours_de_placement=None                    
                    case_depart=None
            else: # cas où le choix n'est pas valide
                terrain_joueur.itemconfigure(grille_joueur_ecran[case_depart[0]][case_depart[1]], outline='black', fill="#efeeec") # on efface le choix de la première case
                commentaire_joueur['text']= "Ce placement n'est pas possible. Recommencez"
                case_depart=None # on permet au joueur de choisir à nouveau la première case
            

# Pour détecter un click sur le bouton gauche de la souris, on va relier (bind en anglais) cet évenement (<Button-1>) à une fonction  
terrain_joueur.bind("<Button-1>", choix_case_bateau)


################################################## Phase de jeu : attaque des bateaux ###############################################################
  
def dessine_a_l_eau(canevas,ligne,col):
    """ La fonction dessine_a_l_eau  
              - prend pour paramètre un canevas (dessin d'une grille), une ligne et une colonne
              - dessine un rond blanc dans le canevas aux lignes et colonnes indiquées
    """
    canevas.create_oval(40*col+10,40*ligne+10,40*(col+1)-10,40*(ligne+1)-10,width=2,fill="white")

def dessine_touche(canevas,ligne,col):
    """ La fonction dessine_touche
              - prend pour paramètre un canevas (dessin d'une grille), une ligne et une colonne
              - dessine un rond rouge dans le canevas aux lignes et colonnes indiquées
    """
    canevas.create_oval(40*col+10,40*ligne+10,40*(col+1)-10,40*(ligne+1)-10,width=2,fill="red")

def dessine_attaque(grille,ligne,col,canevas,commentaire,num_bateau):
    """ La fonction dessine_attaque  
              - prend pour paramètre une grille de jeu, une ligne, une colonne, un canevas (dessin d'une grille), une zone de commentaire et un numéro de bateau
              - affiche le résultat de l'attaque : rond blanc ou rouge + texte associé dans la zone de commentaire
    """
    if est_touche(grille,[ligne,col]): # cas où le un bateau a été touché lors de l'attaque 
        dessine_touche(canevas,ligne,col) # on dessine un rond rouge sur la case
        if est_coule(num_bateau,grille): # cas où le bateau a été coulé
            commentaire['text']=nom_bateau(num_bateau)," coulé !"             
        else: # cas où le bateau est seulement touché
            commentaire['text']="Touché"
    else: # cas où aucun bateau n'a été touché lors de l'attaque
        dessine_a_l_eau(canevas,ligne,col)
        commentaire['text']="A l'eau"
        
# L'enchaînement des tirs du joueur et de l'ennemi est structurée avec les 4 fonctions suivantes:
        # choix_case_tir (tir du joueur) appelle 1000 ms aprèès la fin de son exécution la fonction attaque_ennemi qui doit donc être définie au préalable
        # attaque_ennemi appelle 1000 ms aprèès la fin de son exécution la fonction continuer_attaque_ennemi qui doit donc être définie au préalable
        # continuer_attaque_ennemi appelle 1000 ms aprèès la fin de son exécution la fonction finir_attaque_ennemi qui doit donc être définie au préalable
        # finir_attaque_ennemi  

def finir_attaque_ennemi():
    """ La fonction finir_attaque_ennemi s'exécute 1000 ms après la fin de l'exécution de la fonction continuer_attaque_ennemi
              - ne prend aucun paramètre en entrée
              - met à jour les zones de commentaires correspondant à la fin de l'attaque de l'ennemi
              - met à jour la variable globale combat : passe à True dès que l'ennemi à finit de jouer afin de permettre au joueur de tirer
    """
    global combat
    global nombre_attaque_ennemi
    nombre_attaque_ennemi+=1
    zone_texte_nombre_attaques_ennemi['text']="Nombre d'attaque de l'ordinateur:",nombre_attaque_ennemi # on actualise la variable nombre_attaque_joueur

    combat=True # pour donner la main au joueur afin qu'il puisse tirer à son tour
    consigne_tir['text']="A vous d'attaquer"
    commentaire_joueur['text']=""  

def continuer_attaque_ennemi():
    """ La fonction continuer_attaque_ennemi s'exécute 1000 ms après la fin de l'exécution de la fonction attaque_ennemi
              - ne prend aucun paramètre en entrée
              - dessine l'attaque sur la case sélectionnée et met à jour les zones de commentaires 
              - met à jour les variables globales :
                    * grille_joueur : s'il y a un bateau sur la case sélectionnée, la case correspondante dans grille_joueur prend la valeur 6
                    * grille_coup_ordi : met à jour la grille des coups joués par l'ordinateur
                          -1 si la case n'est plus explorable
                          sinon 0 s'il n'y a pas de bateau sur la case choisie 
                                6 s'il y a un bateau sur la case choisie
              - affiche "fin de la partie" si tous les bateaux du joueur ont été coulés
              - appelle la fonction finir_attaque_ennemi 1000 ms après la fin de son exécution sinon 
    """
    global grille_joueur
    global grille_coup_ordi
    case=coup_ordi() # case jouée par l'ordinateur : liste de deux entiers
    ligne=case[0] # numéro de la ligne
    colonne=case[1] # numéro de la colonne
    consigne['text']="nombre torpille joueur:"
    num_bateau=num_bateau_attaque(grille_joueur,case) # numéro du bateau attaqué (None si aucun bateau)
    grille_joueur=attaque(grille_joueur,case) # mise à jour de la grille de jeu du joueur : si il y a un bateau sur la case attaquée, elle prend la valeur 6
    grille_coup_ordi[ligne][colonne]=grille_joueur[ligne][colonne] # mise à jour de la grille des coups joués par l'ordinateur
                                                                   # 0 s'il n'y a pas de bateau sur la case choisie , 6 s'il y a un bateau sur la case choisie
    dessine_attaque(grille_joueur,ligne,colonne,terrain_joueur,commentaire_joueur,num_bateau) # affichage graphique de l'attaque
    if num_bateau is not None and est_coule(num_bateau,grille_joueur): # si le bateau est coulé, on "désactive" toutes les cases touchées de la grille
                                                                       # des coups joués par l'ordinateur pour ne plus les explorer
        for i in range(len(grille_coup_ordi)): 
            for j in range(len(grille_coup_ordi[0])):
                if grille_coup_ordi[i][j]==6:
                    grille_coup_ordi[i][j]=-1    
    if a_perdu(grille_joueur): # cas où l'ordinateur a gagné la partie
        commentaire_joueur['text']=""
        issue['text']="Fin de la partie : l'ennemi a gagné, vous avez perdu !"            
    else: # cas où la partie continue
        cadre1.after(1000,finir_attaque_ennemi) # appel de la fonction finir_attaque_ennemi après 1000 ms

def attaque_ennemi():
    """ La fonction attaque_ennemi s'exécute 1000 ms après la fin de l'exécution de la fonction choix_case_tir
              - ne prend aucun paramètre en entrée
              - met à jour les zones de commentaires correspondant au début de l'attaque de l'ennemi
              - appelle la fonction continuer_attaque_ennemi 1000 ms après la fin de son exécution
    """
    global nombre_attaque_joueur
    nombre_attaque_joueur=nombre_attaque_joueur+1
    zone_texte_nombre_attaques_joueur['text']="Nombre d'attaque du joueur:",nombre_attaque_joueur # on actualise la variable nombre_attaque_joueur

    consigne['text']="L'ennemi attaque" # mise à jour des commentaires dans les zones de texte
    commentaire_tir['text']=''
    cadre1.after(1000,continuer_attaque_ennemi) # appel de la fonction continuer_attaque_ennemi après 1000 ms

def choix_case_tir(event):
    """ La fonction choix_case_tir est liée à la détection d'un click sur le bouton gauche de la souris  
              - prend pour paramètre un évènement souris
              - dessine l'attaque sur la case sélectionnée et met à jour les zones de commentaires 
              - met à jour les variables globales :
                    * grille_ordi : s'il y a un bateau sur la case sélectionnée, la case correspondante dans grille_ordi prend la valeur 6
                    * combat : passe à True dès que l'ennemi a fini de jouer afin de permettre au joueur de tirer
              - affiche "fin de la partie" si tous les bateaux de l'ennemi ont été coulés
              - appelle la fonction attaque_ennemi 1000 ms après la fin de son exécution sinon 
    """
    global grille_ordi,combat
    consigne_tir['text']=""
    if combat==True:
        x = event.x # on récupère les coordonnées de la souris
        y = event.y
        colonne=x//40 # puis la ligne et la colonne correspondantes dans le tableau
        ligne=y//40
        case=[ligne,colonne]
        num_bateau=num_bateau_attaque(grille_ordi,case) # numéro du bateau attaqué (None si aucun bateau)
        grille_ordi=attaque(grille_ordi,case) # mise à jour de la grille de jeu de l'ordinateur
                                                         # si il y a un bateau sur la case attaquée, elle prend la valeur 6
        dessine_attaque(grille_ordi,ligne,colonne,terrain_ordi,commentaire_tir,num_bateau) # affichage graphique de l'attaque
        combat=False # le joueur ne peut plus tirer, c'est au tour de l'ordinateur
        if a_perdu(grille_ordi): # cas où le joueur a gagné la partie
            commentaire_tir['text']=""
            issue['text']="Fin de la partie : vous avez gagné !"
        else: # cas où la partie continue
            cadre2.after(1000, attaque_ennemi) # appel de la fonction attaque_ennemi après 1000 ms

# Pour détecter un click sur le bouton gauche de la souris, on va relier (bind en anglais) cet évenement (<Button-1>) à la fonction choix_case_tir     
terrain_ordi.bind("<Button-1>", choix_case_tir)


fenetre.mainloop() 
# A partir de cette instruction, Tkinter est en alerte et réceptionne plusieurs fois par secondes les événements clavier et souris,
# il regarde tout ce qui se passe et vous avertit lorsqu'il détecte un des événements que vous lui aurez demandé de surveiller
# (pour l'instant on n'a encore rien demandé donc il observe simplement).
# C'est pourquoi on met cette instruction en dernier: on démarre la surveillance une fois que tous les objets ont étés correctement placés.

