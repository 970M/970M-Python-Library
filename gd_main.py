#!/usr/bin/python3

#from gd_dataProcessingLib import *


import math
import scipy
import random

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mimg
import PIL

# Modules Perso.
from gd_listLib import *
from gd_graphLib import *
from gd_dicVarLib import *
from gd_ioFilesLib import *

### TO DO ###
"""
def circuit_eurlerien() # Methode de Fleury
def coloration_arretes() # par algo glouton idem sommets (a verifier)
def circuit_hamiltonien() # NP difficile
def bellman()
def Boyer_Moore()

"""
#===================================================================================
# Algo. de Bellman-Ford-Kalaba:
#===================================================================================
"""
proc relacher(s i , s j )
si d[s j ] > d[s i ] + cout(s i , s j ) alors
/* il vaut mieux passer par s i pour aller à s j */
d[s j ] ← d[s i ] + cout(s i , s j )
π[s j ] ← s i
finsi
fin relacher


fonc Bellman-Ford(G = (S, A), cout : S → R, s 0 ∈ S)
retourne une arborescence des plus courts chemins d’origine s 0
pour chaque sommet s i ∈ S faire
d[s i ] ← +∞
π[s i ] ← nil
fin pour
d[s 0 ] ← 0
pour k variant de 1 a | S | −1 faire
pour chaque arc (s i , s j ) ∈ A faire relacher(s i , s j ) fin pour
fin pour
pour chaque arc (s i , s j ) ∈ A faire
si d[s j ] > d[s i ] + cout(s i , s j ) alors afficher(“circuit absorbant”) finsi
fin pour
retourner(π)
fin Bellman-ford
"""
def relacher(ac,si,sj):
    if ac.sommets[sj].val["dist"] > ac.sommets[si].val["dist"] + ac.sommets[si].voisin[sj].val["poid"]:
        # Il vaut mieux passer pas si pour aller a sj
        ac.sommets[sj].val["dist"]=ac.sommets[si].val["dist"] + ac.sommets[si].voisin[sj].val["poid"]

        if ac.sommets[sj].val["pere"] is not None:
            ac.supprime_arc(ac.sommets[sj].val["pere"],sj)
        ac.config_sommet(sj, {"dist": ac.sommets[si].val["dist"] + ac.sommets[si].voisin[sj].val["poid"], "pere": si})
        ac.ajoute_arc(si,sj,ac.sommets[si].voisin[sj].val)



#===================================================================================
# Algo. de Bellman-Ford-Kalaba:
#===================================================================================
def bellman(g, s):

    ac=Graph(g.oriente)
    for i in g.sommets:
        ac.config_sommet(i, {"dist": float('inf'), "pere": None})

    ac.config_sommet(s, {"dist": 0, "pere": None})

    mod = True
    k = 1
    while (k <= len(g.sommets)) and mod:
        print("k=", k)
        mod = False
        for x in g.sommets:
            print("x=", x)
            for v in g.sommets[x].voisin:
                print("  v=", v)
                dist = ac.sommets[x].val["dist"] + g.sommets[x].voisin[v].val["poid"]

                if dist < ac.sommets[v].val["dist"]:
                    mod = True
                    print("nouvelle dist=", dist)
                    if ac.sommets[v].val["pere"] is not None:
                        ac.supprime_arc(ac.sommets[v].val["pere"], v)
                    ac.config_sommet(v, {"dist": dist, "pere": x})
                    ac.ajoute_arc(x, v, g.sommets[x].voisin[v].val)

        k = k + 1
        print("k=", k, "mod=", mod)
    return ac
#===================================================================================
# Classe pour arbres ...
#===================================================================================
class Noeud:
    def __init__(self, g, liste, d):
        self.data = liste
        self.left = g
        self.right = d
    """
    def __str__(self):
        return str(self.data.afficherData())
    """

    def afficher(self):
        print(self.data)

    def est_feuille(self):
        return (self.left is None) and (self.right is None)

class ABR:
    def __init__(self):
        self.root = None
    def inserer(self, liste):
        self.root = abr_inserer(self.root, liste)

def abr_prefixe(a):
    if a is None:
        return None
    print(a.data)
    abr_infixe(a.left)
    abr_infixe(a.right)

def abr_infixe(a):
    if a is None:
        return None
    abr_infixe(a.left)
    print(a.data)
    abr_infixe(a.right)

def abr_postfixe(a):
    if a is None:
        return None
    abr_infixe(a.left)
    abr_infixe(a.right)
    print(a.data)

def abr_inserer(a, liste):
    ind = 0
    if a is None:
        return Noeud(None, liste, None)

    if liste[ind] < a.data[ind]:
        return Noeud(abr_inserer(a.left, liste), a.data, a.right)
    else:
        return Noeud(a.left, a.data, abr_inserer(a.right, liste))

#===================================================================================
# Manipulation d'arbre
#===================================================================================
def ex_manipule_arbre():

    df = TableDataFromPandaRead("/home/gyom/CraftSpace/database/villes.csv")
    df = df.values
    #print("df=",df)

    #d1=Noeud(None,df[25],None)
    #d1.afficher()

    a=ABR()

    for i in range(len(df)):
        a.inserer(df[i])

    abr_infixe(a.root)




#===================================================================================
# Manipulation de graphe (exemple)
#===================================================================================
def ex_manipule_graphe(da):

    SO, SF, ori = "T", "M", True
    g = creer_graphe(da,ori)

    print("# Graphe Original:")
    g.affiche_graphe()

    ac = Graph(g.oriente)
    ch = []
    print(g.degres("3"))
    #ch=gph_circuit_euler(g,"0"); print(" "); print("Chemin Eulerien=",ch)
    #ac=bfs(g,"A"); ch=chemin_vers(ac,"E")
    #ac=dijkstra(g,"A"); ch=chemin_vers(ac,"E")
    ot=[]

    #dfs_explorer(g,"6",ac,ot) ; print("Arbre Couvrant") ; ac.affiche_graphe(); ch=chemin_vers(ac,"5"); print("ot=",ot)
    ac=bellman(g, 6); print("Arbre Couvrant"); ac.affiche_graphe()
    #ac=dfs_lifo(g,"6");print("Arbre Couvrant") ; ac.affiche_graphe()
    #ac=coloration_sommets(g); print(" "); print("# Graphe Final:"); ac.affiche_graphe()


##################################################################################
##  MAINs
##################################################################################

"""
g_or_nocycle_p
g_or_cycle
g_dijkstra_p
g_arbo_p
g_test_p
g_grid_p
"""


#ex_manipule_liste(10)
#ex_manipule_graphe(g_dijkstra_p)

#ex_manipule_graphe(g_penta)
#ex_manipule_arbre()
ex_manipule_graphe(g_topo_p)
