from jeu import*

grille1=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 1, 1, 1, 1, 1],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


grille2=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 3, 0, 0, 4, 4, 4, 0, 0, 0],\
          [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 2, 2, 2, 2, 0, 0, 0, 5, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille3=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 6, 6, 6, 6, 6, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 3, 0, 0, 4, 4, 4, 0, 0, 0],\
          [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 2, 6, 6, 2, 0, 0, 0, 6, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

grille4=[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 6, 6, 6, 6, 6, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 6, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 6, 0, 0, 6, 6, 6, 0, 0, 0],\
          [0, 6, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
          [0, 6, 6, 6, 6, 0, 0, 0, 6, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 6, 0],\
          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

############### Tests de la fonction numero ###############

assert numero(["porte-avion",1,5])==1
assert numero(["sous-marin 2",4,3])==4

############### Tests de la fonction longueur ###############

assert longueur(["porte-avion",1,5])==5
assert longueur(["croiseur",2,4])==4

############### Tests de la fonction nom_bateau ###############

assert nom_bateau(1)=='porte-avion'
assert nom_bateau(2)=='croiseur'

############### Tests de la fonction choix_premiere_case_valide ###############

assert choix_premiere_case_valide(grille1,[9,9])==False
assert choix_premiere_case_valide(grille1,[2,8])==False
assert choix_premiere_case_valide(grille1,[8,2])==True
assert choix_premiere_case_valide(grille1,[9,0])==True

############### Tests de la fonction verifie_consecutives ###############

assert verifie_consecutives([4,5],[4,7])==False
assert verifie_consecutives([4,5],[5,6])==False
assert verifie_consecutives([4,5],[4,4])==False
assert verifie_consecutives([4,5],[3,5])==False
assert verifie_consecutives([4,5],[4,6])==True
assert verifie_consecutives([4,5],[5,5])==True

############### Tests de la fonction orientation_bateau ###############

assert orientation_bateau([4,5],[4,6])== "h"
assert orientation_bateau([4,5],[5,5])== "v"

############### Tests de la fonction est_dans_grille ###############

assert est_dans_grille(grille1,["croiseur",2,4],[4,7],"h")==False
assert est_dans_grille(grille1,["croiseur",2,4],[8,6],"v")==False
assert est_dans_grille(grille1,["croiseur",2,4],[6,9],"v")==True
assert est_dans_grille(grille1,["croiseur",2,4],[6,9],"h")==False
assert est_dans_grille(grille1,["croiseur",2,4],[9,6],"h")==True
assert est_dans_grille(grille1,["croiseur",2,4],[9,6],"v")==False

############### Tests de la fonction verifie_chevauchement ###############

assert verifie_chevauchement(grille1,["croiseur",2,4],[2,2],"h")==False
assert verifie_chevauchement(grille1,["croiseur",2,4],[2,1],"h")==True
assert verifie_chevauchement(grille1,["croiseur",2,4],[1,2],"v")==True
assert verifie_chevauchement(grille1,["croiseur",2,4],[1,6],"v")==False

############### Tests de la fonction verifie_placement_possible ###############

assert verifie_placement_possible(grille1,["croiseur",2,4],[4,7],"h")==False
assert verifie_placement_possible(grille1,["croiseur",2,4],[6,9],"v")==True
assert verifie_placement_possible(grille1,["croiseur",2,4],[9,6],"v")==False
assert verifie_placement_possible(grille1,["croiseur",2,4],[2,1],"h")==True

############### Tests de la fonction choix_deuxieme_case_valide ###############

assert choix_deuxieme_case_valide(grille1,["croiseur",2,4],[2,2],[2,4])==False
assert choix_deuxieme_case_valide(grille1,["croiseur",2,4],[2,2],[2,3])==False
assert choix_deuxieme_case_valide(grille1,["croiseur",2,4],[3,1],[3,2])==True
assert choix_deuxieme_case_valide(grille1,["croiseur",2,4],[8,4],[9,4])==False
assert choix_deuxieme_case_valide(grille1,["croiseur",2,4],[1,6],[2,6])==False
assert choix_deuxieme_case_valide(grille1,["croiseur",2,4],[6,9],[7,9])==True

############### Tests de la fonction positionne_bateau ###############

assert positionne_bateau(grille1,["torpilleur",5,2],[1,1],"v")== [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                                  [0, 5, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                                  [0, 5, 0, 0, 0, 1, 1, 1, 1, 1],\
                                                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                                  [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\
                                                                  [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\
                                                                  [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\
                                                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

assert positionne_bateau(grille1,["croiseur",2,4],[7,4],"h")==[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                               [0, 5, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                               [0, 5, 0, 0, 0, 1, 1, 1, 1, 1],\
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                               [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\
                                                               [0, 0, 3, 0, 0, 0, 0, 0, 0, 0],\
                                                               [0, 0, 3, 0, 2, 2, 2, 2, 0, 0],\
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                                               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

############### Tests de la fonction est_touche ###############

assert est_touche(grille2,[3,2])==False
assert est_touche(grille2,[3,1])==True

############### Tests de la fonction num_bateau_attaque ###############

assert num_bateau_attaque(grille2,[3,1])==3
assert num_bateau_attaque(grille2,[1,6])==1
assert num_bateau_attaque(grille2,[8,8])==5

############### Tests de la fonction attaque###############

assert attaque(grille2,[4,6])==[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],\
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 3, 0, 0, 4, 4, 6, 0, 0, 0],\
                                [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 2, 2, 2, 2, 0, 0, 0, 5, 0],\
                                [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],\
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

assert attaque(grille2,[2,2])==[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 0, 0, 0, 1, 1, 1, 1, 1, 0],\
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 3, 0, 0, 4, 4, 6, 0, 0, 0],\
                                [0, 3, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],\
                                [0, 2, 2, 2, 2, 0, 0, 0, 5, 0],\
                                [0, 0, 0, 0, 0, 0, 0, 0, 5, 0],\
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

############### Tests de la fonction est_coule###############

assert est_coule(1,grille3)==True
assert est_coule(3,grille3)==False
assert est_coule(5,grille3)==False

############### Tests de la fonction est_coule###############

assert a_perdu(grille3)==False
assert a_perdu(grille4)==True