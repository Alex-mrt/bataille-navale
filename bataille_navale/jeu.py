from random import randint
grille_joueur = [[0 for i in range(10)] for j in range(10)]
liste_bateaux=[["porte-avion",1,5],["croiseur",2,4],["sous-marin 1",3,3],["sous-marin 2",4,3],["torpilleur",5,2]]
grille_coup_ordi = [[None for i in range(10)] for j in range(10)] # grille dans laquelle on mémorisera les coups joués par l'ennemi
                                                                  # None : la case n'a pas été jouée
def numero(bateau):
    
    """
    La fonction numero(bateau) permet de avoir le numéro du bateau grâce au paramètre (bateau)
    """
    
    return bateau[1]

def longueur(bateau):
    
    """
    La fonction longueur(bateau) permet de avoir la longueur du bateau grâce au paramètre (bateau)
    """

    return bateau[-1]

def nom_bateau(num_bateau):
    
    """
    La fonction nom_bateau(num_bateau) qui prend pour paramètre un numéro de bateau num_bateau et renvoie le nom du bateau
    """
    
    return liste_bateaux[num_bateau-1][0]
    
def choix_premiere_case_valide(grille,case):
    
    """
    la fonction choix_premiere_case_valide(grille,case) qui prend pour paramètre une grille de jeu grille
    et une case case et renvoie True si le choix de la case est valide pour commencer à placer un bateau dans la grille de
    jeu et False sinon.
    """
    
    return grille[case[0]][case[1]]==0 and case!=[9,9] 

def verifie_consecutives(case_1,case_2):
    
    """
    la fonction verifie_consecutives(case_1,case_2) qui prend pour paramètres deux cases case_1 et
    case_2 d'une grille de jeu, et renvoie True si la case_2 est consécutives à la case_1 et False sinon.
    """
    
    return (case_2[0]==case_1[0]+1 and case_2[1]==case_1[1]) or (case_2[0]==case_1[0] and case_2[1]==case_1[1]+1)

def orientation_bateau(case_1,case_2):
    
    """
    la fonction orientation_bateau(case_1,case_2) qui prend pour paramètres deux cases consécutives
    case_1 et case_2 d'une grille de jeu, et renvoie l'orientation ("h" pour horizontal et "v" pour vertical) du
    bateau dénie par ces deux cases consécutives.
    """
    
    if case_2[0]==case_1[0]+1:
        return "v"
    else:
        return "h"
    
def est_dans_grille(grille, bateau, case,sens):
    
    """
    la fonction est_dans_grille(grille, bateau, case,sens) qui :
    prend pour paramètres une grille de jeu grille, une liste bateau, une case case et une orientation sens
    renvoie True si on peut placer le bateau à partir de la case donnée et dans le sens donné sans sortir de la
    grille et False sinon.
    """
    
    if sens=='v':
        return case[0]+bateau[-1]<=10
    elif sens=='h':
        return case[1]+bateau[-1]<=10
            
def verifie_chevauchement(grille, bateau, case,sens):
   
    """
    la fonction verifie_chevauchement(grille, bateau, case,sens) qui :
    prend pour paramètres une grille de jeu grille, une liste bateau, une case case et une orientation sens
    renvoie True si on peut placer le bateau à partir de la case donnée et dans le sens donné sans chevaucher un
    autre bateau et False sinon.
    """
   
    if sens=='v':
        for i in range(bateau[-1]):
            if grille[case[0]+i][case[1]]!=0:
                return False
    elif sens=='h':
        for i in range(bateau[-1]):
            if grille[case[0]][case[1]+i]!=0:
                return False
    return True
    
def verifie_placement_possible(grille, bateau, case,sens):
     
    """
    la fonction verifie_placement_possible(grille, bateau, case,sens) qui :
    prend pour paramètres une grille de jeu grille, une liste bateau, une case case et une orientation sens
    renvoie True si on peut placer le bateau à partir de la case donnée et dans le sens donné et False sinon.
    On peut placer le bateau s'il ne sort pas de la grille et s'il ne chevauche pas d'autres bateaux.
    """
     
    return est_dans_grille(grille,bateau,case,sens) and verifie_chevauchement(grille,bateau,case,sens)

def choix_deuxieme_case_valide(grille,bateau,case_1,case_2):
     
    """
    la fonction choix_deuxieme_case_valide(grille,bateau,case_1,case_2) qui :
    prend pour paramètres une grille de jeu grille, une liste bateau, la première case choisie par le joueur
    case_1, la deuxième case choisie par le joueur case_2
    renvoie True si le choix de la deuxième case est valide et False sinon.
    """
     
    return verifie_consecutives(case_1,case_2) and verifie_placement_possible(grille,bateau,case_1,orientation_bateau(case_1,case_2))

def positionne_bateau(grille, bateau, case,sens):
    
    """
    la fonction positionne_bateau(grille, bateau, case,sens) qui :
    prend pour paramètres une grille de jeu grille, une liste bateau, une case case et une orientation sens
    modie la grille de jeu pour indiquer le numéro du bateau dans les cases qui correspondent à sa position
    renvoie la grille modifiée.
    """
    
    if sens=='v':
        for i in range(bateau[-1]):
                grille[case[0]+i][case[1]]=numero(bateau)
    elif sens=='h':
        for i in range(bateau[-1]):
                grille[case[0]][case[1]+i]=numero(bateau)
    return grille

def init_grille_hasard():
     
    """
    la fonction init_grille_hasard() qui génère et renvoie la grille de jeu de l'ordinateur dans laquelle la flotte
    de bateaux a été placée aléatoirement.
    """
     
    grille_ordi = [[0 for i in range(10)] for j in range(10)]
    for bateau in liste_bateaux:
        sens=randint(0,1)
        case=[randint(0,9),randint(0,9)]
        if sens==0:
            sens='v'
        else:
            sens='h'
        while verifie_placement_possible(grille_ordi,bateau,case,sens)==False:
            case=[randint(0,9),randint(0,9)]
            sens=randint(0,1)
            if sens==0:
                sens='v'
            else:
                sens='h'
        positionne_bateau(grille_ordi, bateau, case,sens)
    return grille_ordi

    
def coup_aleatoire_ordi():
    
    """
    la fonction coup_aleatoire_ordi() qui renvoie une case ( liste [ligne,colonne] ) choisie aléatoirement dans la grille
    l'ordinateur ne doit pas tirer deux fois au même endroit
    fait en sorte de jouer en croix c'est à dire une case sur 2 sadiminue par 2 le nombre de cases à explorer.Car en effet, le plus petit bateau comporte
    2 cases, donc pour être sûr de le détecter, il suffit de laisser une case entre chaque tir.
    """
     
    ligne=randint(0, 9)
    if ligne%2==1:
        colonne=randint(0, 9)
        while colonne%2==0:
            colonne=randint(0, 9)
    else:
        colonne=randint(0, 9)
        while colonne%2==1:
            colonne=randint(0, 9)
    coup=[ligne,colonne]
    if grille_coup_ordi[coup[0]][coup[1]]==None:
        return coup
    
    while grille_coup_ordi[coup[0]][coup[1]]!=None:
        ligne = randint(0, 9)
        if ligne % 2 == 1:
            colonne = randint(0, 9)
            while colonne % 2 == 0:
                colonne = randint(0, 9)
        else:
            colonne = randint(0, 9)
            while colonne % 2 == 1:
                colonne = randint(0, 9)

        coup = [ligne, colonne]
        if grille_coup_ordi[coup[0]][coup[1]]==None:
            return coup

def est_touche(grille,case):
     
    """
    la fonction est_touche(grille,case) qui :
    prend pour paramètres une grille de jeu grille et une case case
    renvoie True s'il y a un bateau sur la case et False sinon.
    """
     
    return grille[case[0]][case[1]]!=0

def num_bateau_attaque(grille,case):
    
    """
    la fonction num_bateau_attaque(grille,case) qui :
    prend pour paramètres une grille de jeu grille et une case case
    renvoie, s'il y a un bateau sur la case, le numéro du bateau attaqué 
    """
    
    if grille[case[0]][case[1]]!=0:
        return grille[case[0]][case[1]]
 
def attaque(grille,case):
     
    """
    la fonction attaque(grille, case) qui :
    prend pour paramètres une grille de jeu grille et une case case
    met à jour la grille de jeu en fonction du résultat du tir ( 6 dans la case si un bateau est touché), et la renvoie
    """
     
    if grille[case[0]][case[1]]!=0:
        grille[case[0]][case[1]]=6
    return grille

def est_coule(num_bateau,grille):
    
    """
    la fonction est_coule(num_bateau,grille) qui :
    prend pour paramètres un numéro de bateau num_bateau et une grille de jeu grille
    renvoie True si le bateau est coulé (c'est-à-dire que son numéro n'apparait plus dans la grille) et False sinon
    """
    
    for colonne in grille:
        for case in colonne:
            if case==num_bateau:
                return False
    return True
                
def a_perdu(grille):
    
    """
    la fonction a_perdu(grille) qui :
    prend pour paramètres une grille de jeu grille
    renvoie True si le joueur possédant la grille a perdu et False sinon
    """
    
    for colonne in grille:
        for case in colonne:
            if case!=0 and case!=6:
                return False
    return True

def coup_ordi():
        
    """
    La fonction coup_ordi() fait en sorte que l'ordinateur imite au mieux le comportement humain :
    S'il y a dans la grille des coups joués une case touchée non verrouillée (cela signie qu'on a touché un bateau et
    qu'il n'est pas encore coulé) :
    s'il y a une case déjà touchée dans les cases voisines, on continue à tirer dans cette direction
    sinon, on tire sur une case libre dans les cases voisines (c'est à dire une case sur laquelle on n'a pas déjà
    tiré) : il y en a forcément une car les bateaux font au minimum deux cases
    Sinon, on joue un coup aléatoire
    """
    
    for ligne in range(len(grille_coup_ordi)):
        
        for colonne in range(len(grille_coup_ordi[ligne])):
            
            if grille_coup_ordi[ligne][colonne]== 6:
                
                if ligne+2<len(grille_coup_ordi) and grille_coup_ordi[ligne+1][colonne]==6 and grille_coup_ordi[ligne+2][colonne]==None: #si une ligne après est rouge et la deuxième non, on tire sur la deuxième
                    return [ligne+2,colonne] 
                if ligne+2<len(grille_coup_ordi) and grille_coup_ordi[ligne+1][colonne]==6 and (grille_coup_ordi[ligne+2][colonne]==6 or grille_coup_ordi[ligne+2][colonne]==0) and grille_coup_ordi[ligne-1][colonne]==None: #si une ligne après est rouge et la deuxième aussi, on tire sur celle avant la première
                    return [ligne-1,colonne]
                if ligne+2<len(grille_coup_ordi) and grille_coup_ordi[ligne+1][colonne]==None and grille_coup_ordi[ligne+2][colonne]==6: 
                    return [ligne+1,colonne]
                
                if ligne-2>=0 and grille_coup_ordi[ligne-1][colonne]==6 and grille_coup_ordi[ligne-2][colonne]==None:
                    return [ligne-2,colonne]
                if ligne-2>=0 and grille_coup_ordi[ligne-1][colonne]==6 and (grille_coup_ordi[ligne-2][colonne]==6 or grille_coup_ordi[ligne-2][colonne]==0) and grille_coup_ordi[ligne+1][colonne]==None:
                    return [ligne+1,colonne]
                if ligne-2>=0 and grille_coup_ordi[ligne-1][colonne]==None and grille_coup_ordi[ligne-2][colonne]==6: 
                    return [ligne-1,colonne]


                if colonne+2<len(grille_coup_ordi) and grille_coup_ordi[ligne][colonne+1]==6 and grille_coup_ordi[ligne][colonne+2]==None:
                    return [ligne,colonne+2]
                if colonne+2<len(grille_coup_ordi) and grille_coup_ordi[ligne][colonne+1]==6 and (grille_coup_ordi[ligne][colonne+2]==6 or grille_coup_ordi[ligne][colonne+2]==0) and grille_coup_ordi[ligne][colonne-1]==None:
                    return [ligne,colonne-1]
                if colonne+2<len(grille_coup_ordi) and grille_coup_ordi[ligne][colonne+1]==None and grille_coup_ordi[ligne][colonne+2]==6:
                    return [ligne,colonne+1]
            
                if colonne-2>=0 and grille_coup_ordi[ligne][colonne-1]==6 and grille_coup_ordi[ligne][colonne-2]==None:
                    return [ligne,colonne-2]
                if colonne-2>=0 and grille_coup_ordi[ligne][colonne-1]==6 and (grille_coup_ordi[ligne][colonne-2]==6 or grille_coup_ordi[ligne][colonne-2]==0) and grille_coup_ordi[ligne][colonne+1]==None:
                    return [ligne,colonne+1]
                if colonne-2>=0 and grille_coup_ordi[ligne][colonne-1]==None and grille_coup_ordi[ligne][colonne-2]==6:
                    return [ligne,colonne-1]
                
                #si aucune case autour est valide on essaye toute les cases autour si elles n'ont jamais était essayées.
                
                if ligne+1<len(grille_coup_ordi) and grille_coup_ordi[ligne+1][colonne]==None:
                    return [ligne+1,colonne]
                if ligne-1>=0 and grille_coup_ordi[ligne-1][colonne]==None:
                    return [ligne-1,colonne]
                
                if colonne+1<len(grille_coup_ordi) and grille_coup_ordi[ligne][colonne+1]==None:
                    return [ligne,colonne+1]
                
                if colonne-1>=0 and grille_coup_ordi[ligne][colonne-1]==None:
                    return [ligne,colonne-1]
        
    return coup_aleatoire_ordi() #si aucune case est intéressante à verifier, on effectue alors un tir aléatoire


if __name__ == "__main__":
    import tests