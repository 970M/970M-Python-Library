"""Module Lecture/Ecriture fichiers"""



def tab_ligne_fichier(cf):
    fe = open(cf, "r")
    lignes = fe.readlines()
    fe.close()
    return lignes

#
# OUVERTURE FICHIER CSV
#
#==========================================================================
# Remplissage du dictionnaire de donnÃ©e par ouverture classique de fichier
#==========================================================================
def TableDataFromClassicalOpenFile(csvFile):

    """ Remplissage du dictionnaire de donnÃ©e par ouverture classique de fichier """

    csvFileOut=csvFile+'.done1'
    dictKeys=[]
    tableData=[]

    with open(csvFileOut, "w") as filout:
        with open(csvFile, "r") as filin:

            ligne = filin.readline() # type str

            while ligne != "":
                ligne=ligne.rstrip("\n").split(";") # type list
                if not dictKeys:
                    dictKeys=ligne

                else:
                    ligneData={}
                    for k in range(len(dictKeys)):

                        ligneData[dictKeys[k]]=ligne[k] # type dict

                    tableData.append(ligneData)

                newLigne=list(ligne)
                #printDebug(newLigne)
                newLigne.append(str(datetime.date.today())+"\n")
                filout.write(";".join(newLigne))
                ligne = filin.readline()

    #printDebug("tableData=",tableData)
    #printDebug("type=",type(tableData))

    return(tableData) # Liste de dictionnaires

#===================================================================================
#  Remplissage du dictionnaire de donnÃ©e par ouverture via DictReader de biblio CSV
#===================================================================================
def TableDataFromCsvDictReader(csvFile):

    import csv

    csvFileOut=csvFile+'.done2'

    filin=open(csvFile, "r")
    tableData=list(csv.DictReader(filin,delimiter=";"))

    #printDebug("table=",tableData)
    #printDebug("type=",type(tableData))

    filout=open(csvFileOut, "w")
    tableDataDone=[]
    for i in range(len(tableData)):
        myDico=tableData[i].copy()
        myDico["DONE_ON"]=str(datetime.date.today())
        tableDataDone.append(myDico)

    w=csv.DictWriter(filout, tableDataDone[0].keys(),delimiter=";")
    w.writeheader()
    w.writerows(tableDataDone)

    filin.close()
    filout.close()

    return(tableData) # Liste de disctionnaires

#===================================================================================
# Remplissage du dictionnaire de donnÃ©e par ouverture via Reader de biblio CSV
#===================================================================================
def TableDataFromCsvReader(csvFile):

    import csv
    csvFileOut=csvFile+'.done3'
    filin=open(csvFile, "r")
    tableData=list(csv.reader(filin,delimiter=";"))
    filout=open(csvFileOut, "w")
    w=csv.writer(filout,delimiter=";")
    newLine=list(tableData[0])
    newLine.append("DONE_ON")
    w.writerow(newLine)
    for i in range(1,len(tableData)):
        newLine=list(tableData[i])
        newLine.append(str(datetime.date.today()))
        w.writerow(newLine)

    filin.close()
    filout.close()

    return(tableData) # Liste de listes

#===================================================================================
# Remplissage du dictionnaire de donnÃ©e par ouverture via panda_read de biblio pands: TBC car gestion de dataframe
#===================================================================================
def TableDataFromPandaRead(csvFile):

    import pandas
    return pandas.read_csv(csvFile)
    #printDebug(df)
    #printDebug("type=",type(df))
