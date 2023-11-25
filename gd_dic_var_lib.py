"""Module dictionnaire d'initialisation de variables pour les exemples"""


def deponderer(dp):

    # construi le graphe non_pondere
    N=len(dp)
    d=[[None for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if dp[i][j] is not None:
                d[i][j]={"poid":1}
            else:
                d[i][j]=dp[i][j]
    return d

def affiche_madj_bool(dadj):

    ma=dadj["ma"]
    etq=dadj["etq"]

    NX=len(ma)
    NY=NX
    mb = [[0] * NY for i in range(NX)]

    ls=[etq[n]["id"] for n in range(len(ma))]
    s = '  '.join([str(e) for e in ls ])

    print("")
    print("Matrice d'adjacence booleene")
    #print("   {0}".format(s))
    print("")
    for x in range(len(ma)):
        for y in range(len(ma[0])):
            if ma[x][y] is not None:
                mb[x][y]=1
            else:
                mb[x][y]=0

        print("{0:3s} {1}".format(etq[x]["id"],mb[x]))
    print("")

#===================================================================================
# Dico d'adjacence de definition de Graphes divers
#===================================================================================

#################################
### Graphe sans cycle oriente (si true)

NS=7
#del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][5]={"poid":5}
ma[1][0]={"poid":3}
ma[1][3]={"poid":10}
ma[1][4]={"poid":3}
ma[1][5]={"poid":11}
ma[2][1]={"poid":1}
ma[2][3]={"poid":7}
ma[4][3]={"poid":4}
ma[5][0]={"poid":1}
ma[6][0]={"poid":5}
ma[6][4]={"poid":4}


etq=[{"id":"1"}, # Etq.du Sommet 0
     {"id":"2"}, # Etq.du Sommet 1
     {"id":"3"}, # Etq.du Sommet 2
     {"id":"4"}, # Etq.du Sommet 3
     {"id":"5"}, # Etq.du Sommet 4
     {"id":"6"}, # Etq.du Sommet 5
     {"id":"7"}  # Etq.du Sommet 6
    ]

g_or_nocycle_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
# Graphe non_pondere
g_or_nocycle={"ma":deponderer(ma),"etq":etq}

#################################
### Graphe avec 2 cycle oriente (si true)
NS=7
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][5]={"poid":5}
ma[1][0]={"poid":13}
ma[1][3]={"poid":10}
ma[1][4]={"poid":3}
ma[2][1]={"poid":1}
ma[3][2]={"poid":7}
ma[4][3]={"poid":4}
ma[5][0]={"poid":1}
ma[5][1]={"poid":11}
ma[6][0]={"poid":5}
ma[6][4]={"poid":4}


etq=[{"id":"1"}, # Etq.du Sommet 0
     {"id":"2"}, # Etq.du Sommet 1
     {"id":"3"}, # Etq.du Sommet 2
     {"id":"4"}, # Etq.du Sommet 3
     {"id":"5"}, # Etq.du Sommet 4
     {"id":"6"}, # Etq.du Sommet 5
     {"id":"7"}  # Etq.du Sommet 6
    ]

g_or_cycle_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente

# Graphe non_pondere
g_or_cycle={"ma":deponderer(ma),"etq":etq}
#################################
### Graphe non-oriente : https://www.maths-cours.fr/methode/algorithme-de-dijkstra-etape-par-etape/ ###

NS=6
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][1]={"poid":8}
ma[0][2]={"poid":10}
ma[0][4]={"poid":10}
ma[0][5]={"poid":4}
ma[1][2]={"poid":7}
ma[1][3]={"poid":3}
ma[1][4]={"poid":5}
ma[2][3]={"poid":4}
ma[3][4]={"poid":8}
ma[4][5]={"poid":8}


etq=[{"id":"E"}, # Etq.du Sommet 0
     {"id":"L"}, # Etq.du Sommet 1
     {"id":"M"}, # Etq.du Sommet 2
     {"id":"N"}, # Etq.du Sommet 3
     {"id":"S"}, # Etq.du Sommet 4
     {"id":"T"}  # Etq.du Sommet 5
    ]

g_dijkstra_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
# Graphe non_pondere
g_dijkstra={"ma":deponderer(ma),"etq":etq}

#################################
### Graphe arborescence
NS=15
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][1]={"poid":5}
ma[0][2]={"poid":3}
ma[1][3]={"poid":10}
ma[1][4]={"poid":3}
ma[2][5]={"poid":1}
ma[2][6]={"poid":7}
ma[3][7]={"poid":4}
ma[3][8]={"poid":1}
ma[4][9]={"poid":11}
ma[4][10]={"poid":5}
ma[5][11]={"poid":20}
ma[5][12]={"poid":5}
ma[6][13]={"poid":2}
ma[6][14]={"poid":5}

etq=[{"id":"A1"}, # Etq.du Sommet 0
     {"id":"B1"}, # Etq.du Sommet 1
     {"id":"B2"}, # Etq.du Sommet 2
     {"id":"C1"}, # Etq.du Sommet 3
     {"id":"C2"}, # Etq.du Sommet 4
     {"id":"C3"}, # Etq.du Sommet 5
     {"id":"C4"},  # Etq.du Sommet 6
     {"id":"D1"},  # Etq.du Sommet 7
     {"id":"D2"},
     {"id":"D3"},
     {"id":"D4"},
     {"id":"D5"},
     {"id":"D6"},
     {"id":"D7"},
     {"id":"D8"}
    ]

g_arbo_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
# Graphe non_pondere
g_arbo={"ma":deponderer(ma),"etq":etq}
#################################
### Graphe Test + 1 cycle oriente + 2 cycle non roriente

NS=11
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][1]={"poid":5}
ma[0][2]={"poid":3}
ma[1][3]={"poid":10}
ma[1][4]={"poid":3}
ma[2][5]={"poid":4}
ma[3][7]={"poid":1}
ma[4][7]={"poid":1}
ma[5][8]={"poid":5}
ma[6][2]={"poid":20}
ma[7][9]={"poid":7}
ma[8][6]={"poid":15}
ma[8][10]={"poid":15} # on laisse un sommet isolé


etq=[{"id":"S"}, # Etq.du Sommet 0
     {"id":"A1"}, # Etq.du Sommet 1
     {"id":"B1"}, # Etq.du Sommet 2
     {"id":"A2"}, # Etq.du Sommet 3
     {"id":"A3"}, # Etq.du Sommet 4
     {"id":"B2"}, # Etq.du Sommet 5
     {"id":"B3"},  # Etq.du Sommet 6
     {"id":"A4"},  # Etq.du Sommet 7
     {"id":"B4"},
     {"id":"A5"},
     {"id":"B5"}
    ]
g_test_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
# Graphe non_pondere
g_test={"ma":deponderer(ma),"etq":etq}

#################################
### Graphe arborescence
NS=15
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][1]={"poid":5}
ma[0][2]={"poid":3}
ma[1][3]={"poid":10}
ma[1][4]={"poid":3}
ma[2][5]={"poid":1}
ma[2][6]={"poid":7}
ma[3][7]={"poid":4}
ma[3][8]={"poid":1}
ma[4][9]={"poid":11}
ma[4][10]={"poid":5}
ma[5][11]={"poid":20}
ma[5][12]={"poid":5}
ma[6][13]={"poid":2}
ma[6][14]={"poid":5}

etq=[{"id":"A1"}, # Etq.du Sommet 0
     {"id":"B1"}, # Etq.du Sommet 1
     {"id":"B2"}, # Etq.du Sommet 2
     {"id":"C1"}, # Etq.du Sommet 3
     {"id":"C2"}, # Etq.du Sommet 4
     {"id":"C3"}, # Etq.du Sommet 5
     {"id":"C4"},  # Etq.du Sommet 6
     {"id":"D1"},  # Etq.du Sommet 7
     {"id":"D2"},
     {"id":"D3"},
     {"id":"D4"},
     {"id":"D5"},
     {"id":"D6"},
     {"id":"D7"},
     {"id":"D8"}
    ]

g_arbo_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
# Graphe non_pondere
g_arbo={"ma":deponderer(ma),"etq":etq}
#################################
### Graphe Test Grille
def graphe_grillage():
    # Size grid = NX * NY
    NX=5
    NY=NX

    NS=NX*NY
    ma=[[None for _ in range(NS)] for _ in range(NS)]
    etq=[None]*NS

    n=0
    for j in range(NY):
        for i in range(NX):

            #print("")
            #print("n=",n,"i=",i,"j=",j)
            # Contruction de etq
            x,d,b=None,None,None
            cx,cg,cd,ch,cb="","","","",""

            x=str(j)+str(i)
            g=str(j)+str(i-1)
            d=str(j)+str(i+1)
            b=str(j-1)+str(i)
            h=str(j+1)+str(i)


            #print("x=",x,"g=",g,"d=",d,"h=",h,"b=",b)
            etq[n]={"id":x}

            cx=n

            if i != 0:
                cg=n-1
            if i != NX-1:
                cd=n+1
            if j != 0:
                cb=n-NX
            if j != NY-1:
                ch=n+NX


            #print("cx=",cx,"cg=",cg,"cd=",cd,"ch=",ch,"cb=",cb)

            if (i%2 == 0) and (ch != "") :
                ma[cx][ch]={"poid":1}
                #print('i')
            elif (i%2 ==1) and (cb != ""):
                ma[cx][cb]={"poid":1}
                #print("v")

            if (j%2 == 0) and (cd != "") :
                ma[cx][cd]={"poid":1}
            #    print(">")
            elif (j%2 == 1) and (cg != ""):
                ma[cx][cg]={"poid":1}
            #    print("<")

            n+=1

    return {"ma":ma,"etq":etq}  # dictionnaire d'adjacente


g_grid_p=graphe_grillage()
# Graphe non_pondere
g_grid={"ma":deponderer(g_grid_p["ma"]),"etq":g_grid_p["etq"]}

#################################
### Graphe pentagrammme

NS=5
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][1]={"poid":1}
ma[0][2]={"poid":2}
ma[0][3]={"poid":3}
ma[0][4]={"poid":4}
ma[1][0]={"poid":10}
ma[1][2]={"poid":12}
ma[1][3]={"poid":13}
ma[1][4]={"poid":14}
ma[2][0]={"poid":20}
ma[2][1]={"poid":21}
ma[2][3]={"poid":23}
ma[2][4]={"poid":24}
ma[3][0]={"poid":30}
ma[3][1]={"poid":31}
ma[3][2]={"poid":32}
ma[3][4]={"poid":34}
ma[4][0]={"poid":40}
ma[4][1]={"poid":41}
ma[4][2]={"poid":42}
ma[4][3]={"poid":43}



etq=[{"id":"A"}, # Etq.du Sommet 0
     {"id":"B"}, # Etq.du Sommet 1
     {"id":"C"}, # Etq.du Sommet 2
     {"id":"D"}, # Etq.du Sommet 3
     {"id":"E"} # Etq.du Sommet 4
    ]

g_penta_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
g_penta={"ma":deponderer(ma),"etq":etq}

#################################
### Graphe eulerien

NS=7
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][1]={"poid":1}
ma[0][2]={"poid":7}
ma[0][6]={"poid":3}
ma[1][2]={"poid":10}
ma[1][3]={"poid":4}
ma[1][4]={"poid":8}
ma[2][3]={"poid":1}
ma[2][5]={"poid":10}
ma[3][4]={"poid":12}
ma[3][5]={"poid":2}
ma[4][5]={"poid":3}
ma[5][6]={"poid":5}
#ma[6][4]={"poid":1}


etq=[{"id":"A"}, # Etq.du Sommet 0
     {"id":"B"}, # Etq.du Sommet 1
     {"id":"C"}, # Etq.du Sommet 2
     {"id":"D"}, # Etq.du Sommet 3
     {"id":"E"}, # Etq.du Sommet 4
     {"id":"F"}, # Etq.du Sommet 5
     {"id":"T"} # Etq.du Sommet 6
    ]

g_euler_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
g_euler={"ma":deponderer(ma),"etq":etq}

#################################
### Graphe eulerien oriente

NS=7
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][1]={"poid":7}
ma[0][6]={"poid":7}
ma[1][3]={"poid":7}
ma[2][0]={"poid":7}
ma[3][2]={"poid":7}
ma[3][4]={"poid":7}
ma[3][5]={"poid":7}
ma[4][2]={"poid":7}
ma[4][0]={"poid":7}
ma[5][4]={"poid":7}
ma[6][2]={"poid":7}


etq=[{"id":"0"}, # Etq.du Sommet 0
     {"id":"1"}, # Etq.du Sommet 1
     {"id":"2"}, # Etq.du Sommet 2
     {"id":"3"}, # Etq.du Sommet 3
     {"id":"4"}, # Etq.du Sommet 4
     {"id":"5"}, # Etq.du Sommet 5
     {"id":"6"} # Etq.du Sommet 6
    ]

g_eulero_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
g_eulero={"ma":deponderer(ma),"etq":etq}

#################################
### Graphe eulerien

NS=7
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[0][1]={"poid":1}
ma[0][2]={"poid":7}
ma[0][6]={"poid":3}
ma[1][2]={"poid":10}
ma[1][3]={"poid":4}
ma[1][4]={"poid":8}
ma[2][3]={"poid":1}
ma[2][5]={"poid":10}
ma[3][4]={"poid":12}
ma[3][5]={"poid":2}
ma[4][5]={"poid":3}
ma[5][6]={"poid":5}
#ma[6][4]={"poid":1}


etq=[{"id":"A"}, # Etq.du Sommet 0
     {"id":"B"}, # Etq.du Sommet 1
     {"id":"C"}, # Etq.du Sommet 2
     {"id":"D"}, # Etq.du Sommet 3
     {"id":"E"}, # Etq.du Sommet 4
     {"id":"F"}, # Etq.du Sommet 5
     {"id":"T"} # Etq.du Sommet 6
    ]

g_euler_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
g_euler={"ma":deponderer(ma),"etq":etq}

#################################
### Graphe topologie oriente

NS=6
del ma,etq
ma=[[None for _ in range(NS)] for _ in range(NS)]

ma[1][2]={"poid":15}
ma[1][3]={"poid":1}
ma[1][4]={"poid":11}
ma[2][3]={"poid":16}
ma[3][0]={"poid":-1}
ma[3][4]={"poid":2}
ma[4][0]={"poid":0}
ma[5][0]={"poid":3}
ma[5][1]={"poid":9}
ma[5][2]={"poid":11}
ma[5][4]={"poid":19}



etq=[{"id":"1"}, # Etq.du Sommet 0
     {"id":"2"}, # Etq.du Sommet 1
     {"id":"3"}, # Etq.du Sommet 2
     {"id":"4"}, # Etq.du Sommet 3
     {"id":"5"}, # Etq.du Sommet 4
     {"id":"6"}, # Etq.du Sommet 5
    ]

g_topo_p={"ma":ma,"etq":etq} # dictionnaire d'adjacente
g_topo={"ma":deponderer(ma),"etq":etq}
#===================================================================================
# Diverses Listes
#===================================================================================
