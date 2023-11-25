"""Module Liste chainee, FIFO, LIFO, Heap, Graphes"""

import random
from gd_guiLib import *
from gd_listLib import *
from gd_dicVarLib import *

#
# GRAPHES
#

#===================================================================================
# Classe pour Graphes
#===================================================================================
class Sommet:
    def __init__(self, i, diconf):
        self.id = i
        if diconf is not None:
            self.val = diconf  # ex: {"id":"S","pere":"T","couleur":bleu}
        else:
            self.val = {}
        self.voisin = {}  # un dico d'element de type Arc (keys=id sommets voisins) ex: {"poid":10,"couleur"=bleu}

class Arc:
    def __init__(self, diconf):
        # self.dest=s
        if diconf is not None:
            self.val = diconf  # ex: {"poid":"4","couleur":vert}
        else:
            self.val = {"poid": "1"}

class Graph:
    """Un graphe defini par dic. adjacence"""

    def __init__(self, b):
        self.sommets = {}  # un dico d'objet Sommet
        self.oriente = b  # graphe oriente vrai, faux

    def ajoute_sommet(self, s, diconf):
        s = str(s)
        if s not in self.sommets:
            self.sommets[s] = Sommet(s, diconf)

    def supprime_sommet(self, s):
        del self.sommets[s]
        for c, a in self.sommets.items():
            if s in a.voisin:
                del a.voisin[s]

    def existe_sommet(self, s):
        return s in self.sommets

    def config_sommet(self, s, diconf):
        s = str(s)
        if s not in self.sommets:
            self.sommets[s] = Sommet(s, diconf)
        else:
            for c, a in diconf.items():
                self.sommets[s].val[c] = a

    def ajoute_arc(self, s1, s2, diconf):
        s1 = str(s1)
        s2 = str(s2)
        self.ajoute_sommet(s1, None)
        self.ajoute_sommet(s2, None)
        self.sommets[s1].voisin[s2] = Arc(diconf)
        if not self.oriente:
            self.sommets[s2].voisin[s1] = Arc(diconf)

    def supprime_arc(self, s1, s2):
        del self.sommets[s1].voisin[s2]
        if not self.oriente:
            del self.sommets[s2].voisin[s1]

    def liste_sommets(self):
        return list(self.sommets)

    def degres(self, s):
        s = str(s)
        dp = len(self.sommets[s].voisin)
        dm = None
        if self.oriente:
            dm = 0
            for cle, attribut in sorted(self.sommets.items()):
                print(cle, attribut)
                for i in self.sommets[cle].voisin:
                    if i == s:
                        dm += 1
        return len(self.sommets[s].voisin), dm

    def affiche_graphe(self):
        print("")
        for cle, attribut in sorted(self.sommets.items()):
            print("({0}) :: {1}".format(cle, attribut.val))
            for cle2, attribut2 in sorted(attribut.voisin.items()):
                print("       .--> ({0}) : {1}".format(cle2, attribut2.val))
        print("")

#===================================================================================
# Fonction pour Graphes
#===================================================================================
def creer_matrice_adj(g):
    """Format Matrice d'adjacence à partir d'un graphe"""
    NS = len(g.sommets.keys())
    ma = [[None for _ in range(NS)] for _ in range(NS)]
    etq_s = [None] * NS

    s_list = sorted((g.sommets.keys()))

    for n in range(len(s_list)):
        etq_s[n] = g.sommets[s_list[n]].val

    for s, s_val in g.sommets.items():
        for v, v_val in s_val.voisin.items():
            ma[s_list.index(s)][s_list.index(v)] = v_val
    # ma=matrice d'adj., etq=decodage indice matrice/id sommet
    return {"ma": ma, "etq": etq_s}

def creer_graphe(da, oriente):
    """ Cree un graphe a partir d'un format matrice d'adj."""
    ma = da["ma"]
    etq = da["etq"]

    g = Graph(oriente)
    for i in range(len(ma)):
        for j in range(len(ma)):
            if ma[i][j] is not None:
                g.ajoute_arc(etq[i]["id"], etq[j]["id"], ma[i][j])
                g.config_sommet(etq[j]["id"], etq[j])
        g.config_sommet(etq[i]["id"], etq[i])
    return g
#===================================================================================
# Parcours en profondeur Pile optimise
#===================================================================================
def dfs_lifo(g, s):

    l = creer_lifo()
    l.empiler(s)

    marque = [s]

    ac = Graph(g.oriente)
    ac.config_sommet(s, g.sommets[s].val)
    ac.config_sommet(s, {"pere": None})

    while not l.est_vide():
        print("Lifo:")
        l.afficher()

        x = l.depiler()

        print(">> Traitement de",x)
        print("marque=",marque)
        p = ac.sommets[x].val["pere"]


        if p is not None:
            pd = g.sommets[p].voisin[x].val["poid"]
            ac.ajoute_arc(p, x, {"poid": pd})
            printDebug(" {0}. Ajout arc ({1}) --> ({2})".format("", p, x))
            ac.config_sommet(x, g.sommets[x].val)
        for v in g.sommets[x].voisin:
            if v not in marque:
                print("empile ", v)
                l.empiler(v)
                ac.config_sommet(v, {"pere": x})
                ac.affiche_graphe()

                marque.append(v)



    return ac
#===================================================================================
# Parcours en profondeur optimise
#===================================================================================
def dfs_explorer(g, s, ac, ot):
    if s not in ac.liste_sommets():
        printDebug("{0}. Ajout de ({1}) dans ac".format("", s))
        ac.config_sommet(s, g.sommets[s].val)
        ac.config_sommet(s, {"pere": None})
    for v in g.sommets[s].voisin:
        printDebug("{0}. ({1}) --> ({2}) dans ac".format("", s, v))

        if v not in ac.liste_sommets():
            printDebug(" {0}. ({1}) Pas encore traité".format("", v))
            ac.config_sommet(v, {"pere": s})
            p = g.sommets[s].voisin[v].val["poid"]
            ac.ajoute_arc(s, v, {"poid": p})
            printDebug(" {0}. ajout arc ({1})--> ({2})".format("", s, v))
            ac.affiche_graphe()
            dfs_explorer(g, v, ac, ot)
    ot.insert(0, s)
    #ac.config_sommet(s, {"ot":ot})


def dfs(g, s, ac):
    """Parcours en Profondeur DFS de g a partir de s"""

    printDebug("{0}> Parcours en Profondeur DFS a partir de ({1})".format("", s))

    if not g.existe_sommet(s):
        raise IndexError("Le graphe {0} n'a pas de sommet {1}".format(g, s))

    for i in s:
        printDebug("{0}# Sommet ({1})".format("", i))

        if i not in ac.liste_sommets():
            printDebug("{0}. ({1}) Pas encore traité".format("", i))
            dfs_explorer(g, i, ac)

        ac.config_sommet(s, {"pere": None})



        """
        explorer(graphe G, sommet s)
              marquer le sommet s
              afficher(s)
              pour tout sommet t voisin du sommet s
                    si t n'est pas marqué alors
                           explorer(G, t);
        Le parcours en profondeur d'un graphe G est alors :

        parcoursProfondeur(graphe G)
              pour tout sommet s du graphe G
                    si s n'est pas marqué alors
                           explorer(G, s)

        """


#===================================================================================
# Parcours en profondeur
#===================================================================================
def dfs_0(g, s, n_rec):
    """Parcours en Profondeur DFS de g a partir de s"""
    # n_rec sert pour les tabulations
    # g de type Graph = le grph dont on fait le DFS
    # s le sommet de type Sommet dont on part
    # ac l'arbre couvrant retourne
    # n_rec un compteur de recurence = 0 pour initialisation

    s = str(s)

    # Style
    ntabu = ""
    for i in range(n_rec):
        ntabu = ntabu + " "

    printDebug(
        "{0}> Parcours en Profondeur DFS a partir de ({1})".format(ntabu, s))

    if s not in g.sommets:
        raise IndexError("Le graphe {0} n'a pas de sommet {1}".format(g, s))

    if n_rec == 0:  # Initialisation
        printDebug("{0} . Initialisation graphe: Oriente={1}".format(ntabu, g.oriente))
        global nb_cycle
        nb_cycle = 0
        global ac
        ac = Graph(g.oriente)
        # ac.config_sommet(s,{"pere":None})
        for i in g.sommets:
            g.config_sommet(i, {"pere": None, "couleur": "blanc"})
            ac.config_sommet(i, g.sommets[i].val)

    n_rec += 1

    # Style
    ntabu = ""
    for i in range(n_rec):
        ntabu = ntabu + " "

    g.config_sommet(s, {"couleur": "gris"})

    printDebug("{0}. ({1}): blanc --> gris".format(ntabu, s))
    for v in g.sommets[s].voisin:
        printDebug("{0}. ({1}) --> ({2})".format(ntabu, s, v))
        if g.sommets[v].val["couleur"] == "blanc":
            g.config_sommet(v, {"pere": s})
            p = g.sommets[s].voisin[v].val["poid"]
            ac.ajoute_arc(s, v, {"poid": p})
            printDebug(
                "{0}. ({2}) est blanc: ajout arc ({1})--> ({2})".format(ntabu, s, v))
            ac = dfs(g, v, n_rec)

        elif (g.sommets[v].val["couleur"] == "gris"):
            printDebug("{0}. ({1})=gris".format(ntabu, v))

            if (g.sommets[s].val["pere"] != v):
                nb_cycle += 1
                tx = "cycle" + str(nb_cycle)
                printDebug("{0}. {1} car ({2}) ne vient pas de {3}".format(ntabu, tx, s, v))

                g.config_sommet(v, {tx: s})
                c = s
                while c != v:
                    g.config_sommet(c, {tx: s})
                    c = g.sommets[c].val["pere"]

        elif g.sommets[v].val["couleur"] == "noir":
            printDebug("{0}. ({1}) est noir ...".format(ntabu, v))
        else:
            printDebug("Warning:couleur inconnue")

    g.config_sommet(s, {"couleur": "noir"})
    ac.config_sommet(s, g.sommets[s].val)

    printDebug("{0}. ({1}): gris --> noir".format(ntabu, s))
    return ac

#===================================================================================
# Detection de cycle: Parcours en profondeur
#===================================================================================
def cycle_present(g, s, init):
    """Detection de cycle dans un graphe à partir de s (pour algo de Kruskal)"""
    # g de type Graph = le grph dont on fait le DFS
    # s le sommet de type Sommet dont on part
    # ac l'arbre couvrant retourne
    # n_rec un compteur de recurence = 0 pour initialisation

    s = str(s)
    ntabu = ""

    printDebug("{0}  + Recheche de cycles a partir de ({1})".format(ntabu, s))

    if s not in g.sommets:
        raise IndexError("Le graphe {0} n'a pas de sommet {1}".format(g, s))

    if init is None:  # Initialisation
        printDebug("{0}  . Initialisation graphe: Oriente={1}".format(
            ntabu, g.oriente))
        couleur = {}
        pere = {}
        for i in g.sommets:
            couleur[i] = "blanc"
            pere[i] = None
    else:
        couleur = init[0]
        pere = init[1]

    couleur[s] = "gris"
    printDebug("{0}  . ({1}): blanc --> gris".format(ntabu, s))
    for v in g.sommets[s].voisin:
        printDebug("{0}    . ({1}) --> ({2})".format(ntabu, s, v))
        if couleur[v] == "blanc":
            printDebug("{0}    . ({1}) = blanc".format(ntabu, v))
            pere[v] = s
            cycle_present(g, v, [couleur, pere])

        elif couleur[v] == "gris":
            printDebug("{0}    . ({1}) = gris".format(ntabu, v))
            printDebug("{0}    . Cycle trouve !!!".format(ntabu, v))

            if pere[s] != v:
                return True

        elif couleur[v] == "noir":
            printDebug("{0}    . ({1}) = noir ...".format(ntabu, v))
        else:
            printDebug("Warning:couleur inconnue")

    couleur[s] = "noir"
    printDebug("{0}. ({1}): gris --> noir".format(ntabu, s))
    return False


#===================================================================================
# Parcours en largeur
#===================================================================================
def bfs(g, s):
    # g de type Graph = le grph dont on fait le BFS
    # s le sommet de type Sommet dont on part
    # retourne ac l'arbre couvrant

    # Initialisation
    ntabu = ""
    n_cycle = 0
    n_rec = 0
    s = str(s)

    printDebug(
        "{0}> Parcours en Largeur BFS a partir de ({1})".format(ntabu, s))

    if s not in g.sommets:
        raise IndexError("Le graphe {0} n'a pas de sommet {1}".format(g, s))

    # Style
    n_rec += 1
    for i in range(n_rec):
        ntabu = ntabu + " "

    printDebug("{0}. Initialisation graphe: Oriente={1}".format(ntabu, g.oriente))

    if not g.existe_sommet(s):
        raise IndexError("Le Sommet", s, "n'existe pas")

    ac = Graph(g.oriente)

    for i in g.sommets:
        ac.config_sommet(i, {"couleur": "blanc", "dist": "Inf", "pere": None})

    procList = creer_fifo()
    procList.enfiler(s)

    ac.config_sommet(s, {"couleur": "gris", "dist": 0, "pere": None})
    printDebug("{0}. ({1}) blanc --> gris".format(ntabu, s))

    # Traitement
    while not procList.est_vide():
        u = procList.defiler()

        # Style
        ntabu = ""
        n_rec = procList.taille()
        for i in range(int(n_rec)):
            ntabu = ntabu + " "

        printDebug(
            "{0}+ ({1}) defile pour traitement: niveau {2}".format(ntabu, u, n_rec - 1))

        for v in g.sommets[u].voisin:
            printDebug("{0}- ({1}) --> ({2})".format(ntabu, u, v))
            if ac.sommets[v].val["couleur"] == "blanc":

                printDebug("{0}| ({1}) est blanc".format(ntabu, v))
                dist = ac.sommets[u].val["dist"] + g.sommets[u].voisin[v].val["poid"]
                ac.config_sommet(v, {"couleur": "gris", "pere": u, "dist": dist})
                p = g.sommets[u].voisin[v].val["poid"]
                ac.ajoute_arc(u, v, {"poid": p})
                printDebug("{0}| ajoute arc ({1}) --> ({2})".format(ntabu, u, v))
                printDebug("{0}| ({1}): blanc --> gris , dist={2} ".format(ntabu, v, dist))
                procList.enfiler(v)

                # Style
                ntabu = ""
                n_rec = procList.taille()
                for i in range(int(n_rec)):
                    ntabu = ntabu + " "
            else:
                printDebug(
                    "{0}| ({1}) n'est pas blanc (dèja vu)".format(ntabu, v))

        ac.config_sommet(u, {"couleur": "noir"})

        printDebug("{0}| ({1}): gris --> noir".format(ntabu, u))
        n_rec += 1
    return ac

#===================================================================================
# Algo de Dijkstra
#===================================================================================
def dijkstra(g, s):
    # g de type Graph = le grph dont on fait le dijkstra
    # s le sommet de type Sommet dont on part
    # retourne ac l'arbre couvrant retourne ?

    # Initialisation
    s = str(s)
    ntabu = ""
    n_rec = 0
    printDebug("{0}> Algo. de Dijskra a partir de ({1})".format(ntabu, s))

    # Style
    n_rec += 1
    ntabu = ""
    for i in range(n_rec):
        ntabu = ntabu + " "

    printDebug("{0}. Initialisation graphe: Oriente={1}".format(ntabu, g.oriente))

    if not g.existe_sommet(s):
        raise IndexError("Le Sommet", s, "n'existe pas")

    NS = len(g.liste_sommets())

    ac = Graph(g.oriente)
    ac.config_sommet(s, {"dist": 0, "pere": None})

    mdl = creer_heap(False)  # pourquoi pas avec creer_queue() ???
    for i in g.sommets:

        mdl.enfiler(i, float('inf'))
        g.config_sommet(i, {"dist": float('inf'), "pere": None})

    mdl.modifier(s, 0)
    ac.config_sommet(s, {"dist": 0})
    g.config_sommet(s, {"dist": 0})

    # Traitement
    while not mdl.est_vide():

        # Style
        ntabu = ""
        n_rec = mdl.taille()
        for i in range(int(n_rec)):
            ntabu = ntabu + " "

        e = mdl.defiler()

        u = e["id"]
        vu = e["val"]
        printDebug("{0}+ Traitement de ({1})".format(ntabu, u))

        for v in g.sommets[u].voisin:
            printDebug("{0}. ({1}) --> ({2})".format(ntabu, u, v))
            curDist = mdl.valeur(v)
            curDist1 = g.sommets[v].val["dist"]  # TDD fonction mdl.valeur(id)

            if curDist is not None:
                printDebug(
                    "{0}. dist. courante de ({1}) à ({2}) = {3} / {4}".format(ntabu, s, v, curDist, curDist1))
                printDebug(
                    "{0}  dist. de ({1}) à ({2}) = {3}".format(ntabu, s, u, vu))
                printDebug("{0}    + Longeur arc ({1}) --> ({2}) = {3}".format(
                    ntabu, u, v, g.sommets[u].voisin[v].val["poid"]))
                newDist = e["val"] + g.sommets[u].voisin[v].val["poid"]

                if newDist < curDist:
                    mdl.modifier(v, newDist)
                    g.config_sommet(v, {"pere": u, "dist": newDist})
                    ac.ajoute_arc(u, v, g.sommets[u].voisin[v].val)
                    printDebug("{0}. Nouvelle dist. de ({1}) à ({2}) = {3}".format(
                        ntabu, s, v, newDist))
            else:
                printDebug(
                    "{0}. pas de plus court chemin possible".format(ntabu, v))
        ac.config_sommet(u, g.sommets[u].val)
    return ac

#===================================================================================
# Arbre couvrant de poid minimal:PRIM:recursif
#===================================================================================
def acpm_prim(g, ac, n_rec):
    """Methode Prim"""

    ntabu = ""
    printDebug("{0}> Algo. de Prim: {1}".format(ntabu, n_rec))

    if g.sommets is None:
        printDebug("{0}. Pas de sommets a traiter".format(ntabu))
        return None

    if n_rec == 0:
        n_rec = 1
        printDebug("{0}. Initialisation graphe: Oriente={1}".format(
            ntabu, g.oriente))

        #global ac
        # ac=Graph(g.oriente)
        for i in g.sommets:
            g.config_sommet(i, {"pere": None, "couleur": "blanc"})
            # ac.config_sommet(i,g.sommets[i].val)
            s = g.sommets[i].val["id"]  # peut mieux faire

        g.config_sommet(s, {"couleur": "noir"})
        ac.config_sommet(s, g.sommets[s].val)

    # Fontion qui retourne l'arc de poid min dont un seul sommet appartient à l'arbre en construction
    ns = None
    sp = None
    pmin = float('inf')
    for i in g.sommets:
        printDebug("{0}. ({1}) est {2}".format(
            ntabu, i, g.sommets[i].val["couleur"]))
        if g.sommets[i].val["couleur"] == "noir":

            printDebug(
                "{0}  . Recherche d'arc sortant de ({1})".format(ntabu, i))

            for a in g.sommets[i].voisin:
                printDebug("{0}    . traitement de ({1}) {2}".format(
                    ntabu, a, g.sommets[a].val["couleur"]))
                if g.sommets[a].val["couleur"] == "blanc":
                    printDebug(
                        "{0}    . ({1}) --> ({2}) {3}".format(ntabu, i, a, g.sommets[a].val["couleur"]))
                    printDebug("{0}    . ({1}):{2} < ({3}):{4} ?".format(
                        ntabu, a, g.sommets[i].voisin[a].val["poid"], ns, pmin))

                    if (g.sommets[i].voisin[a].val["poid"] < pmin) and (g.sommets[a].val["couleur"] != "noir"):
                        printDebug(
                            "{0}    . ({1}) est le sommet avec l'arc de poid min".format(ntabu, a))
                        pmin = g.sommets[i].voisin[a].val["poid"]
                        ns = a
                        sp = i

    if ns is not None:
        printDebug(
            "{0}  . on agrandi l'arbre de poid min avec ({1})".format(ntabu, ns))
        g.config_sommet(ns, {"pere": sp, "couleur": "noir"})
        # g.sommets[sp].voisin[ns].["poid"]
        ac.ajoute_arc(sp, ns, {"poid": pmin})
        ac.config_sommet(ns, g.sommets[ns].val)
        ac.affiche_graphe()
        acpm_prim(g, ac, 1)

    else:

        printDebug(
            "{0}. Pas de voisin de nouveaux sommets a traiter".format(ntabu))
        ac.affiche_graphe()
        print("ac=", ac)
        # return ac

#===================================================================================
# Arbre couvrant de poid minimal:PRIM:File de priorite
#===================================================================================
def acpm_prim_heap(g, s):
    """Methode Prim avec file de priorite"""
    s = str(s)
    ntabu = ""
    printDebug("{0}> Algo. de Prim (heap)".format(ntabu))

    if not g.existe_sommet(s):
        raise IndexError("Le Sommet", s, "n'existe pas")

    ac = Graph(g.oriente)
    mdl = HeapQueue(False)  # pourquoi pas avec creer_queue() ???
    for i in g.sommets:
        mdl.enfiler(i, float('inf'))
        g.config_sommet(
            i, {"pere": None, "couleur": "blanc", "dist": float('inf')})
        #printDebug("{0}. configuration du sommets ({1})".format(ntabu,i))

    mdl.modifier(s, 0)

    e = mdl.defiler()

    u = e["id"]
    vu = e["val"]
    pere = u  # g.sommets[u].val["pere"]
    g.config_sommet(u, {"couleur": "noir", "dist": vu})
    ac.config_sommet(u, g.sommets[u].val)
    while not mdl.est_vide():

        printDebug(
            "{0}+ Traitement de ({1}) / rest {2}".format(ntabu, u, mdl.taille()))

        for v in g.sommets[u].voisin:
            printDebug("{0}|- ({1}) --> ({2}):{3}".format(ntabu,
                                                          u, v, g.sommets[v].val["couleur"]))
            if g.sommets[v].val["couleur"] != "noir":
                parc = g.sommets[u].voisin[v].val["poid"]

                printDebug("{0}|  . c ({1})--{2}-->({3})".format(ntabu,
                                                                 g.sommets[v].val["pere"], mdl.valeur(v), v))
                printDebug(
                    "{0}|  . n ({1})--{2}-->({3})".format(ntabu, u, parc, v))

                if parc < mdl.valeur(v):
                    printDebug(
                        "{0}|  . maj heap avec nouvel arc min vers ({1})".format(ntabu, v))
                    mdl.modifier(v, parc)
                    ds = g.sommets[u].val["dist"] + parc
                    g.config_sommet(v, {"dist": ds, "pere": u})

        c = u
        e = mdl.defiler()
        u = e["id"]
        vu = e["val"]
        pere = g.sommets[u].val["pere"]
        print("pere=", pere)

        ac.ajoute_arc(pere, u, g.sommets[pere].voisin[u].val)
        printDebug("{0}. Ajout d'un arc ({1})--> ({2})".format(ntabu, pere, u))
        g.config_sommet(u, {"couleur": "noir"})
        ac.config_sommet(u, g.sommets[u].val)

    return ac

#===================================================================================
# Arbre couvrant de poid minimal: Kruskal
#===================================================================================
def acpm_kruskal(g,ac):
    """Methode Krushkal"""

    ntabu = ""
    printDebug("{0}> Algo. de Krushkal".format(ntabu))

    mdl = HeapQueue(False)
    dicArc = {}
    # On recupere tous les arcs (non-orientes) pour les trier et
    for i in g.sommets:
        print("i=", i)
        ac.config_sommet(i, {"pere": None})
        for v in g.sommets[i].voisin:
            # trie pour n'en garder q'un E<-->T = T<-->E
            a = tuple(sorted([i, v]))
            dicArc[a] = g.sommets[i].voisin[v].val["poid"]

    # On met les arc dans la fiel de priorite pour les trier
    for k, v in dicArc.items():
        mdl.enfiler(k, v)
    affiche_tab(mdl.root, "HeapQueue")

    while not mdl.est_vide():

        a = mdl.defiler()
        u = a["id"]
        vu = a["val"]
        s1 = u[0]
        s2 = u[1]
        #printDebug("{0}+ Traitement de l'arc {1} de poid {2}".format(ntabu,u,vu))
        printDebug(
            "{0}> Test de l'ajoute de l'arc ({1}) --> ({2})".format(ntabu, s1, s2))
        ac.ajoute_arc(s1, s2, {"poid": vu})

        ac.affiche_graphe()
        # Est-ce que ce nouvel arc cree un cycle? <=> est-ce que les 2 extremité
        if cycle_present(ac, s1, None):

            printDebug(
                "{0}. suppression du nouvel arc car il cree un cycle".format(ntabu))
            ac.supprime_arc(s1, s2)

        else:
            printDebug("{0}. on conserve le nouvel arc".format(ntabu))

#===================================================================================
# Recherche de circuit Eulerien dans un graphe
#===================================================================================
def gph_circuit_euler(g, sd):
    """
    Recherche de circuit eulerien dans le graphe g avec la méthode d'Euler
    s: le sommet de depart si g Eulérien (sinon circuit a partir des sommets impairs)
    """
    printDebug("> gph_circuit_euler".format())
    # Compte le nombre de sommets a degres impairs
    nbi = 0
    circuit = []
    gr = Graph(g.oriente)
    for s in g.sommets: # Recherche sommets impaires + init. graphe de controle gr
        deg = len(g.sommets[s].voisin)
        if (deg % 2) == 1:
            circuit.append(s)
            nbi += 1

        # On essaie de ne pas modifier le graph en entree (a faire si possible pour les autres algo)
        gr.config_sommet(s, {"pere": None, "couleur": "blanc"})
        for v in g.sommets[s].voisin:
            gr.ajoute_arc(s, v, {"poid": g.sommets[s].voisin[v].val["poid"], "couleur": "blanc"})

    print("  . Nb. de degres impair={0}".format(nbi))

    if (nbi != 0) and (nbi != 2):
        return None
    if (nbi == 2):
        # contruis un chemin entre les 2 sommets
        circuit, d, bo = chemin_vers(bfs(gr, circuit[0]), circuit[1])
        for i in range(1, len(circuit)):
            gr.sommets[circuit[i - 1]].voisin[circuit[i]].val["couleur"] = "noir"
            gr.sommets[circuit[i]].voisin[circuit[i - 1]].val["couleur"] = "noir"
    else:
        circuit.append(sd)

    ac = Graph(g.oriente)

    se = set(circuit)
    print("se=",se)
    noMoreArc = True
    while noMoreArc :
        print("### se=", se)
        for s in se:
            print(" ")
            print(se)
            print(circuit)
            print("> Traitement du sommet ({0})".format(s))

            ch, cy=gph_exist_cycle(gr, s)
            if cy:
                i = circuit.index(s) + 1
                circuit[i:i] = ch
        se=set(circuit)


        noMoreArc=False
        for s in gr.sommets:
            for v in gr.sommets[s].voisin:
                if gr.sommets[s].voisin[v].val["couleur"] == "blanc":
                    noMoreArc = True

    return circuit

def gph_exist_cycle(g,s):
    """
    Recherche dans le graphe g la presence d'un cycle a partir d'un sommet s
    g: graphe avec cycle codé
    s: sommet de début/fin du cycle
    Retourne si cycle:
        - Modification du graphe g par marquage en noir des arrete du cycle
        - la liste des sommets du cycle code dans le graphe g
        - booleen a True
    Sinon:
        - le graphe g non modifie
        - None
        - booleen a False
    """

    c = None
    d = None
    cy = False
    ac = Graph(g.oriente)
    ac = gph_cherche_cycle(g,ac,s,None,0)

    c, d, cy = chemin_vers(ac, s)

    if cy:
        for i in range(1, len(c)):
            g.sommets[c[i - 1]].voisin[c[i]].val["couleur"] = "noir"
            g.sommets[c[i]].voisin[c[i - 1]].val["couleur"] = "noir"
        g.sommets[c[0]].voisin[c[-1]].val["couleur"] = "noir"
        g.sommets[c[-1]].voisin[c[0]].val["couleur"] = "noir"
    else:
        c=None
        printDebug(". Pas de cycle a partir de {0}".format(s))

    return c, cy

def gph_cherche_cycle(g, ac, s, init, n_rec):
    """
    Recherche un cycle dans le graphe g à partir du sommet s
    ac un graph couvrant de controle
    init=None lors de l'initialisation ()
    Retourne:
        - l'arbre couvrant avec le codage du cycle
        - g si pas de cycle
    """

    # Style
    ntabu = ""
    for i in range(n_rec):
        ntabu = ntabu + " "

    s = str(s)
    if init == None:
        for i in g.sommets: # Recherche sommets impaires + init. graphe de controle gr
            # On essaie de ne pas modifier le graph en entree (a faire si possible pour les autres algo)
            ac.config_sommet(i, {"pere": None, "couleur": "blanc"})
            for v in g.sommets[i].voisin:
                ac.ajoute_arc(i, v, g.sommets[i].voisin[v].val)
        ac.config_sommet(s, {"couleur": "rouge"}) # Sommet initiateur de la recursion
        print("")
        print("* Graphe Initialise:")
        ac.affiche_graphe()
    else:
        ac.config_sommet(s, {"couleur": "gris"})

    print("{0}> DFS a partir de ({1})".format(ntabu, s))
    printDebug("{0}. ({1}): blanc --> gris".format(ntabu, s))
    n_rec += 1
    for v in ac.sommets[s].voisin:
        printDebug("{0}. ({1}) --> ({2})".format(ntabu, s, v))
        if ac.sommets[s].voisin[v].val["couleur"] == "blanc":
            if ac.sommets[v].val["couleur"] == "blanc":
                # On relance recursivement le DFS
                printDebug("{0}. ({1}) est blanc".format(ntabu, v))
                ac.config_sommet(v, {"pere": s})
                printDebug("{0}. pere de ({1}) = ({2})".format(ntabu, v, s))

                n_rec += 1
                ac = gph_cherche_cycle(g, ac, v, s, n_rec)

            elif ac.sommets[v].val["couleur"] == "rouge":
                # On a découvert un cycles
                printDebug("{0}. ({1}) est gris (cycle)".format(ntabu, v))
                print("{0}. ({1}) vient de ({2}) ?".format(ntabu, s, v))

                # Le sommet v n'est pas le pere de s et il est le sommet de depart
                if (ac.sommets[s].val["pere"] != v): #(ac.sommets[v].val["pere"] == "start"):
                    printDebug("{0}. non, presence de cycle on doit stopper".format(ntabu))
                    ac.config_sommet(v, {"pere": s})

                    for i in ac.sommets: # Tout a noir pour stopper la recursion
                        ac.config_sommet(i, {"couleur": "noir"})

                    ac.config_sommet(v, {"couleur": "vert"})
                else:
                    printDebug("{0}. ({1}) est le pere de ({2})...".format(ntabu, v, s))

    ac.config_sommet(s, {"couleur": "noir"})

    return ac
#===================================================================================
# Coloration des sommets ...
#===================================================================================
def coloration_sommets(g):
    """
    Colorie les sommets du graphe g (méthode algo. glouton)

    """
    couleur_dic = ('ROUGE','VERT','JAUNE','BLEU','ORANGE','VIOLET','ROSE')

    # Duplication du graphe d'entree
    gr=Graph(g.oriente)
    for s in g.sommets:
        gr.config_sommet(s, {"couleur": "BLANC"})

        for v in g.sommets[s].voisin:
            gr.ajoute_arc(s, v, {"poid": g.sommets[s].voisin[v].val["poid"]})


    for s in gr.sommets:
        couleur_dispo = list(couleur_dic)
        printDebug(". Traitement sommet {0}".format(s))
        for v in gr.sommets[s].voisin:
             if gr.sommets[v].val["couleur"] != "BLANC":

                printDebug("Supprime {0} de la liste: {1}".format(gr.sommets[v].val["couleur"], couleur_dispo))
                if gr.sommets[v].val["couleur"] in couleur_dispo:
                    couleur_dispo.remove(gr.sommets[v].val["couleur"])
                print("# Graphe couleur:")
                gr.affiche_graphe()
        gr.config_sommet(s, {"couleur":couleur_dispo[0]})


    return gr


#===================================================================================
# Chemin entre 2 sommets a partir d'un arbre couvrant
#===================================================================================
def chemin_vers(g, sf):

    c = []
    s = sf
    cy = False
    dist = None
    if not g.existe_sommet(str(sf)):
        raise IndexError("Le Sommet {0} n'existe pas".format(sf))
    c.append(sf)
    f = s
    s = g.sommets[s].val["pere"]
    while s is not None:
        c.append(s)
        f = s
        s = g.sommets[s].val["pere"]


        if s == sf:
            cy = True
            s = None

    c.reverse()

    if "dist" in g.sommets[sf].val:
        dist = g.sommets[sf].val["dist"]

    if len(c) > 1:
        s = c[0]
        str(s)
        s = "( " + s + " )"
        d = 0
        for i in range(1, len(c)):
            d = g.sommets[c[i - 1]].voisin[c[i]].val["poid"]
            s = s + " --" + str(d) + "--> ( " + str(c[i]) + " )"

        printDebug(s)
        printDebug("Distance de {0} à {1} = {2}".format(c[0], c[-1], dist))

    return c, dist, cy

#===================================================================================
# Manipulation de graphe (exemple)
#===================================================================================
def ex_manipule_graphe(da):

    printDebug(">> manipule_graphe():")
    """
    g_or_nocycle_p
    g_or_cycle
    g_dijkstra_p
    g_arbo_p
    g_test_p
    g_grid_p
    """
    SO, SF, ori = "T", "M", False

    affiche_madj_bool(da)
    g = creer_graphe(da,ori)

    print("")
    print("> Graphe Original:")
    g.affiche_graphe()
    ab = Graph(ori)
    ###
    # ac=dfs(g,SO,0) # parcours en profondeur
    # ac=bfs(g,SO) # parcours en largeur
    ac = dijkstra(g, SO)
    acpm_kruskal(g, ab)

    # par passage de parametre (pas reussi a faire comme bfs())
    ab = Graph(ori)
    acpm_prim(g, ab, 0)
    ac = acpm_prim_heap(g, SO)
    ####

    print("")
    print("> Graphe Final:")
    g.affiche_graphe()

    print("")
    print("> Arbre Couvrant:")
    ac.affiche_graphe()

    ch, d = chemin_vers(ac, SF)

    print("chemin: {0}".format(ch))
    print("Distance de {0} à {1} = {2}".format(SO, SF, d))

    # print("")
    #print("> dico couvrant:")
    # da=creer_matrice_adj(ac)
    #affiche_tab(da["ma"],"matrice d'adjacence:")
    # affiche_tab(da["etq"],"Etiquette:")


##################################################################################
#  MAIN
##################################################################################

### LISTE ###
# ex_manipule_liste()

### TAS ###
# ex_manipule_tas()

### GRAPHES ###
# ex_manipule_graphe()
