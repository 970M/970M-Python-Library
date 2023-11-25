"""Module Liste chainee, FIFO, LIFO, Heap"""

import random
from gd_guiLib import *
from gd_dicVarLib import *

#
# LISTE CHAINEE
#

#===================================================================================
# CLASS
#===================================================================================
class Cell:
    """Une cellule d'une liste chainee"""

    def __init__(self, v, s):
        self.value = v  # type pas precise donc a tester avec une classe
        self.next = s  # idem

class List:
    """Une liste chainee"""

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_cell(self, v):
        self.head = Cell(v, self.head)

    def length(self):
        return lst_length(self.head)

    def sorted(self):
        self.head = lst_tri_select(self.head)

    def get_cell(self, n):
        """Renvoi le n ieme element d'une liste chainee, numerote a partir de 0"""
        return lst_get_cell(self.head, n)

    def switch(self, i, j):
        self.head = lst_exchange(self.head, i, j)

    def insert(self, i, v):
        self.head = lst_insert(self.head, i, v)

    def delete(self, i):
        self.head = lst_delete(self.head, i)

    def reverse(self):
        self.head = lst_reverse(self.head)

    def add(self, lsth):
        self.head = lst_concatenate_rec(self.head, lsth.head)

#===================================================================================
# Fonction sur pointeur de cellule (.head)
#===================================================================================
def lst_length(lsth):
    """Longeur d'une liste"""
    len = 0
    c = lsth
    # print("c=",c.next.value)
    while c is not None:
        c = c.next
        len += 1
    return len

def lst_split(lsth, i):
    """Sépare une liste en 2 à l'indice i"""
    n = 0
    h1 = None
    h2 = lsth
    while (h2 is not None) and (n <= i): # On met dans h1 tout ce qu'il y a avant i
        h1 = Cell(h2.value, h1)
        h2 = h2.next
        n += 1
    return lst_reverse(h1), h2

def lst_concatenate_rec(lsth1, lsth2):
    """Concatene ltsh2 apres lsth1 et retourne le tout"""
    h = None
    c = lsth1
    if c is None:
        return lsth2
    else:
        # Ajoute une cellule dans .next recursivement
        h = Cell(c.value, lst_concatenate_rec(c.next, lsth2))
    return h

def lst_concatenate_ite(lsth1, lsth2):
    """Concatene ltsh2 apres lsth1 et retourne le tout"""
    if lsth1 is None:
        return lsth2
    else:
        h = lsth2
        c = lst_reverse(lsth1)
        while c is not None:
            h = Cell(c.value, h)
            c = c.next
        return h

def lst_insert(lsth, i, v):
    """Insere la valeur v a la position i"""
    h = None
    c = lsth
    n = 0
    # On parcours la liste et en i on place
    # la nouvelle cellule avant la cellule i existante
    while c is not None:
        if n == i:
            h = Cell(v, h)
            h = Cell(c.value, h)
        else:
            h = Cell(c.value, h)
        c = c.next
        n += 1
    return lst_reverse(h)

def lst_delete(lsth, i):
    """Supprime la cellule i"""
    h = None
    c = lsth
    n = 0
    while c is not None:
        if n != i:
            h = Cell(c.value, h)
        c = c.next
        n += 1
    return lst_reverse(h)

def lst_get_cell(lsth, i):
    """Renvoi la valeur de la cellule i"""
    n = 0
    c = lsth
    if i < 0:
        raise IndexError("indice invalide")
    while (c is not None) and (n < i):
        # print("ind=",ind)
        c = c.next
        n += 1
    return c.value

def lst_reverse(lsth):
    """Inverse l'ordre des element d'un liste"""
    r = None
    c = lsth
    n = 0
    while c is not None:
        r = Cell(c.value, r)
        c = c.next
    return r

def lst_exchange(lsth, i, j):
    """ Echange la position de la cellule i avec celle de j"""
    if i != j:
        r = None
        c = lsth
        n = 0
        while c is not None:
            if n == i: # On recherche la valeur de la cellule j pour la placer en i
                r = Cell(lst_get_cell(lsth, j), r)
            elif n == j: # On recherche la valeur de la cellule i pour la placer en j
                r = Cell(lst_get_cell(lsth, i), r)
            else: # On laisse tel quel
                r = Cell(c.value, r)
            c = c.next
            n += 1
        return lst_reverse(r)
    else:
        return lsth

def lst_disp(lst, h):
    """ Affiche une liste horizontalement (h=1) ou verticalement (h=0)"""
    if h == 0:
        # print(lst.length())
        for n in range(lst.length()):
            try:
                v = lst.get_cell(n)
                print("{0:4d}:[{1:4d}]".format(n, lst.get_cell(n)))
            except:
                print("Element", n, ":ERROR")
    else:
        i = ""
        r = ""
        for n in range(lst.length()):
            try:
                i = i + "{0:>5d} ".format(n)
                r = r + "[{0:>4d}]".format(lst.get_cell(n))
            except:
                r = r + "[{0:4s}]".format("ERROR")
        print("{0}".format(r))
        print("{0}".format(i))

#===================================================================================
# Tri Selection
#===================================================================================
def lst_tri_select(lst):
    """Tri par selection d'une liste"""
    if lst.is_empty():
        return None
    imin = 0
    vmin = lst.get_cell(0)
    for i in range(lst.length()): # Pour chaque element de la liste
        vmin = lst.get_cell(i)
        imin = i
        for j in range(i + 1, lst.length(), 1): # et pour chaque element suivant
            vj = lst.get_cell(j)
            if vj < vmin: # On les compare
                vmin = vj
                imin = j

        lst.switch(i, imin) # On met le plus petit à l'indice le plus bas (switch gere si i=imin)

#===================================================================================
# Tri Insersion
#===================================================================================
def lst_tri_inser(lst):
    """Tir par insersion (jeu de carte)"""
    for i in range(1, lst.length()): # Pour toute la liste
        j = i
        v = lst.get_cell(i)

        # Tant que la valeur v de l'element courant i est plus petite que celle de son précésseur j-1, on descend l'indice j
        while (j > 0) and (v < lst.get_cell(j - 1)):
            j -= 1

        if j != i: # Si i n'est pas deja a sa place, on le descend en j
            lst.insert(j, v)
            lst.delete(i + 1)
#===================================================================================
# Tri Fusion
#===================================================================================
def lst_alternate_split(lsth):
    """Cree 2 listes en alternant les elements: pour tri fusion"""
    h1 = None
    h2 = None
    #printDebug(". lst_alternate_split({0})".format(lsth.value))
    while (lsth is not None):
        h1, h2 = Cell(lsth.value, h2), h1 # On cree des cellule en h1 que h2 recupere le tour d'apres
        lsth = lsth.next
    return h1, h2


def lst_merge_sorted(lsth1, lsth2):
    """Fusionne 2 listes triée s"""
    h = None

    if lsth1 is None:
        #printDebug(". lst_merge_sorted(None,{0})".format(lsth2.value))
        return lsth2
    if lsth2 is None:
        #printDebug(". lst_merge_sorted({0},None)".format(lsth1.value))
        return lsth1
    #printDebug(". lst_merge_sorted({0},{1})".format(lsth1.value, lsth2.value))


    if lsth1.value < lsth2.value:
        """On met la premiere cellule de la plus petite en premier puis on tri le reste recursivement"""
        #printDebug("v1={0} < v2={1}".format(lsth1.value,lsth2.value))

        return Cell(lsth1.value, lst_merge_sorted(lsth1.next, lsth2))
    else:
        #printDebug("v1={0} > v2={1}".format(lsth1.value,lsth2.value))
        return Cell(lsth2.value, lst_merge_sorted(lsth1, lsth2.next))


def lst_tri_fusion(lsth):
    """ Tri fusion d'un liste"""
    #printDebug("> debut lst_tri_fusion({0})".format(lsth.value))
    h = 1
    lst = List()
    lst1 = List()
    lst2 = List()
    lst.head = lsth
    printDebug("tri fusion de:")
    lst_disp(lst, h)

    if (lsth is None) or (lsth.next is None):
        return lsth

    # On decoupe la liste en 2
    lst1.head, lst2.head = lst_alternate_split(lsth)
    #print("Liste 1:")
    #lst_disp(lst1, h)
    #print("Liste 2:")
    #lst_disp(lst2, h)

    # On relance le tri recursivement sur les 2 listes puis on fusionne les resultats tries
    lsth = lst_merge_sorted(lst_tri_fusion(lst1.head),
                            lst_tri_fusion(lst2.head))
    printDebug(". fin lst_tri_fusion({0})".format(lsth.value))
    return lsth

#===================================================================================
# LIFO: Pile
#===================================================================================
class Lifo:
    """Une pile avec 1 liste chainee"""

    def __init__(self):
        self.head = None

    def est_vide(self):
        return self.head is None

    def empiler(self, v):
        self.head = Cell(v, self.head)

    def depiler(self):
        if self.est_vide():
            raise IndexError("Impossible de depiler une pile vide")
        v = self.head.value
        self.head = self.head.next
        return v

    def afficher(self):
        c = self.head
        s = []
        while c is not None:
            s.append(c.value)

            c = c.next
        printDebug(s)

    def taille(self):
        len = 0
        curCell = self.head
        while (curCell is not None):
            # printDebug(curCell.value)
            curCell = curCell.next
            len += 1
        return (len)

def creer_lifo():
    return Lifo()

#===================================================================================
# FIFO: File
#===================================================================================
class Fifo:
    """Une file avec 2 piles"""

    def __init__(self):
        self.entree = Lifo()
        self.sortie = Lifo()

    def est_vide(self):
        return self.entree.est_vide() and self.sortie.est_vide()

    def enfiler(self, v):
        self.entree.empiler(v)

    def defiler(self):
        if self.sortie.est_vide():
            while not self.entree.est_vide():
                self.sortie.empiler(self.entree.depiler())
        if self.sortie.est_vide():
            raise IndexError("Impossible de depiler une pile vide")

        return self.sortie.depiler()

    def taille(self):
        te = self.entree.taille()
        ts = self.sortie.taille()
        #printDebug("te={0}, ts={1}".format(te,ts))
        return int(te + ts)


def creer_fifo():
    return Fifo()

#===================================================================================
# Tas : File de priorite
#===================================================================================
class HeapQueue:
    """File de priorite: Un arbre binaire de recherche tasse gere par un tableau """

    def __init__(self, m):
        self.root = None
        self.maxheap = m  # True maxheap, False Minheap

        # racine : sommet 0
        # parent du sommet i : sommet (i − 1)/2
        # fils gauche du sommet i : sommet 2i + 1
        # fils droit du sommet i : sommet 2i + 2
        # sommet i est une feuille : 2i + 1 > n
        # sommet i a un fils droit : 2i + 2 < n

    def est_vide(self):
        return self.root is None

    def cmp(self, v1, v2): # Fonction de comparaison pour gestion HeapMax /heapMin
        if self.maxheap is True:
            #printDebug("    {0} > {1} ?".format(v1,v2))
            return v1 > v2
        else:
            #printDebug("    {0} < {1} ?".format(v1,v2))
            return v1 < v2

    def percolate_up(self, i):
        #printDebug("  . percolate_up de {0} {1}".format(i,self.root[i]))
        ip = (i - 1) // 2

        if (i == 0):
            #printDebug("  . {0} est deja prioritaire ...".format(i))
            return None

        #printDebug("  . {0} {1} est-il prioritaire sur {2} {3} ?".format(i,self.root[i],ip,self.root[ip]))
        if self.cmp(self.root[i]["val"], self.root[ip]["val"]):
            #printDebug("  . oui {0} {1} <--> {2} {3}".format(i,self.root[i],ip,self.root[ip]))
            t = self.root[i]
            self.root[i] = self.root[ip]
            self.root[ip] = t
            #affiche_tab(self.root,"Permute ")
            if ip > 0:
                self.percolate_up(ip)
            # else:
                #printDebug("    ip=",ip)
        # else:
            #printDebug("  . priorite de {1} {0} atteinte en position {1}".format(self.root[i],i))
            # printDebug("")

    def percolate_down(self, i):
        #printDebug("  . percolate_down de {0} {1}".format(i,self.root[i]))
        ifg = (2 * i + 1)
        ifd = (2 * i + 2)

        if not (ifd > len(self.root)):
            #printDebug("  . {0} {1} a au moins un fils gauche: {2} {3}".format(i,self.root[i],ifg,self.root[ifg]))
            ifx = ifg

            if ifd < len(self.root):
                #printDebug("  . {0} {1} a 2 fils: g {2} {3} | d {4} {5}".format(i,self.root[i],ifg,self.root[ifg],ifd,self.root[ifd]))

                if not self.cmp(self.root[ifg]["val"], self.root[ifd]["val"]):
                    ifx = ifd
                    #printDebug("  . le fils droit {0} {1} est prioritaire".format(i,self.root[i],ifg,self.root[ifg]))

                #printDebug("  . {0} {1} est-il prioritaire sur {2} {3} ?".format(i,self.root[i],ifx,self.root[ifx]))
            # if self.root[i]["val"] > self.root[ifx]["val"]:
            if self.cmp(self.root[ifx]["val"], self.root[i]["val"]):

                #printDebug("  . non, on permute {0} {1} avec {2} {3}".format(i,self.root[i],ifx,self.root[ifx]))
                t = self.root[i]
                self.root[i] = self.root[ifx]
                self.root[ifx] = t
                #affiche_tab(self.root,"Permute ")

                # Si ifx a au moins un fils:
                if (2 * ifx + 1) < (len(self.root)):
                    self.percolate_down(ifx)
                # else:
                    #printDebug("    ifx={0} n'a pas de fils".format(ifx))

    def enfiler(self, id, v):
        if not self.est_vide():
            self.root = self.root + [{"id": id, "val": v}]
            #printDebug("> Ajout {0} en position {1}".format(self.root[len(self.root)-1],len(self.root)-1))
            #affiche_tab(self.root,"Nouvel élément en queue")
            self.percolate_up(len(self.root) - 1)
        else:
            self.root = [{"id": id, "val": v}]
            #printDebug("> Ajout {0} en position {1}".format(self.root[len(self.root)-1],len(self.root)-1))
            # affiche_tab(self.root,"s")

    def defiler(self):

        if not self.est_vide():
            m = self.root[0]
            # printDebug("")
            #printDebug("> Defile element {0}".format(m))
            #affiche_tab(self.root,"Etat avant suppression")
            #printDebug(". {0} {1} <--> {2} {3}".format(0,self.root[0],len(self.root)-1,self.root[len(self.root)-1]))
            self.root[0] = self.root[-1]
            del self.root[-1]
            #affiche_tab(self.root,"Etat apres suppression")

            if len(self.root) == 0:
                self.root = None
                # printDebug("")
            else:
                self.percolate_down(0)
        else:
            # printDebug("vide")
            m = None
        return m

    def modifier(self, id, v):
        # printDebug("")
        #printDebug("> modifie la valeur de l'element {0}".format(id))
        #affiche_tab(self.root,"Etat avant modification")

        for i in range(len(self.root)):
            if self.root[i]["id"] == id:
                #printDebug(" id=",id,"val=",self.root[i]["val"],"-->",v)
                #printDebug("  . valeur de {0} {1} passe de {2} à {3}".format(i,self.root[i],self.root[i]["val"],v))
                if self.cmp(v, self.root[i]["val"]):
                    self.root[i]["val"] = v
                    self.percolate_up(i)
                else:
                    self.root[i]["val"] = v
                    self.percolate_down(i)

                #affiche_tab(self.root,"Etat apres modification")
                return None

    def taille(self): # Nombre d'element dans le tas
        return len(self.root)

    def valeur(self, id):
        if not self.est_vide():
            for i in range(len(self.root)):
                if self.root[i]["id"] == id:
                    return self.root[i]["val"]
        else:
            return None

def creer_heap(max):
    return HeapQueue(max)

def afficher_heap(h):
    printDebug(h.root)

#
# Exemples d'utilisation
#

#===================================================================================
# Manipulation de liste (exemple)
#===================================================================================
def ex_manipule_liste(N):

    h = 1
    lst = List()
    lst1 = List()
    lst2 = List()
    # Ajout d'elements dans la liste chainee
    # Attention la liste sera d'ordre inverse
    val = [random.randint(0, 100) for i in range(N)]

    for n in val:
        lst.add_cell(n)
        # lst2.add_cell(n//3)
    """
    for n in range(N):
        lst.add_cell(n)
    """
    #print(" "); print("Liste initiale 1"); print(""); lst_disp(lst1,h)
    print(" ")
    print("Liste initiale")
    print("")
    lst_disp(lst, h)

    # lst_tri_select(lst)
    # lst_tri_inser(lst)
    # lst.head=lst_tri_fusion(lst.head)
    # lst.reverse()
    # lst.head=lst_exchange(lst.head,2,4)
    lst1.head, lst2.head = lst_split(lst.head, 6)
    lst2.reverse()
    lst.head = lst_concatenate_rec(lst1.head, lst2.head)
    print(" ")
    print(" ")
    print("Liste traitee:")
    print("")
    lst_disp(lst, h)
    print(" ")
    print("Liste 1 apres:")
    print("")
    lst_disp(lst1, h)
    print(" ")
    print("Liste 2 apres:")
    print("")
    lst_disp(lst2, h)

#===================================================================================
# Manipulation de tas (exemple)
#===================================================================================
def ex_manipule_tas():

    tas = s(False)

    d = [["A", 40],
         ["D", 13],
         ["B", 38],
         ["F", 34],
         ["T", 11],
         ["G", 35],
         ["K", 40],
         ["P", 5],
         ["S", 2]
         ]

    for i in d:
        tas.enfiler(i[0], i[1])

    print("")
    print(">> Modifier")
    m = [["T", 37],
         ["P", 12],
         ["P", 52]
         ]

    for i in m:
        tas.modifier(i[0], i[1])

    """
    i=0
    mr=[]
    imax=10
    while (not tas.est_vide()) and (i<imax):
        mr=mr+[tas.defiler()]
        i+=1
    affiche_tab(mr, "Tas")
    """
