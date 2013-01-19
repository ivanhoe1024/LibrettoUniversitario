__author__ = 'ivanhoe1024'

from PyQt4 import QtGui, QtCore

import shelve

voti_disponibili=['IDONEITÀ', 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, '30 e LODE']

COLUMN=('Esame', 'Voto', 'Crediti', 'Data', 'Docente', 'Includi in Media')



class Modello_Tabella(QtCore.QAbstractTableModel):
    def __init__(self, lista_esami):
        super(Modello_Tabella, self).__init__()
        self.lista_esami=lista_esami

    def rowCount(self, QModelIndex_parent=None):
        return len(self.lista_esami)
    def columnCount(self, QModelIndex_parent=None):
        return len(COLUMN)
    def headerData(self, section, orientation, role):
        if role==QtCore.Qt.DisplayRole:
            if orientation==QtCore.Qt.Horizontal:
                return COLUMN[section]
            elif orientation==QtCore.Qt.Vertical:
                return section + 1

    def data(self, index, role):

        if role==QtCore.Qt.DisplayRole:
            row=index.row()
            col=index.column()

            lista_valori=[self.lista_esami[row].nome,self.lista_esami[row].voto,self.lista_esami[row].crediti,self.lista_esami[row].data,self.lista_esami[row].docente]
            
            #CORREGGI TRUE/FALSE IN VIEW PER LA MEDIA
            if self.lista_esami[row].inmedia == True:
                lista_valori.append('SI')
            elif self.lista_esami[row].inmedia == False:
                lista_valori.append('NO')
                
            #CORREGGI VISUALIZZAZIONE DI VOTI TESTUALI
            if self.lista_esami[row].voto==0:
                lista_valori[1]="IDONEITA'"
            elif self.lista_esami[row].lode==True and self.lista_esami[row].voto==30:
                lista_valori[1]='30 e LODE'

            value=lista_valori[col]

            return value

class ExamError(Exception):
    pass

class DatabasePresentError(Exception):
    pass

class DatabaseAbsentError(Exception):
    pass

class esame:
    def __init__(self, nome, voto, crediti, data, docente='', inmedia=False):
        self.nome=nome

        if voto==voti_disponibili[0]:
            self.voto=0
            self.isidoneita=True
            self.inmedia=inmedia
            self.lode=False
        elif voto==voti_disponibili[-1]:
            self.voto=30
            self.inmedia=inmedia
            self.isidoneita=False
            self.lode=True
        else:
            self.voto=voto
            self.lode=False
            self.inmedia=inmedia
            self.isidoneita=False


        self.crediti=crediti
        self.data=data
        self.docente=docente


        if not self.isvalid():
            raise ExamError
        


    def isvalid(self):
        if (self.voto>=18 and self.voto<=30 and self.lode==False and self.isidoneita==False):
            return True
        elif (self.lode==True and self.voto==30 and self.isidoneita==False):
            return True
        elif (self.isidoneita==True and self.inmedia==False and self.voto==0):
            return True
        else:
            return False

    #PROBABILMENTE INUTILE, FORSE LA ELIMINO

    def media(self):
        if self.inmedia==True and self.isvalid()==True:
            return (self.voto*self.crediti, self.crediti)
        else:
            return 0

def connetti_database():
    db=shelve.open('database_esami', writeback=False)
    return db

def crea_lista_esami():
    lista_esami=[]
    db=connetti_database()
    for i in db.values():
        lista_esami.append(i)
    db.close()
    return lista_esami

def aggiungi_al_database(esame, db):
    nome=esame.nome
    if nome in db.keys():
        raise DatabasePresentError
    else:
        db[nome]=esame
        return True

def elimina_dal_database(esame, db):
    if esame in db.keys():
        del db[esame]
        return True
    else:
        raise DatabaseAbsentError

def chiudi_database(db):
    db.close()
    return True
