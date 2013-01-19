from PyQt4 import QtGui, QtCore
from MainWindow_Esami import Ui_MainWindow_Esami
from engine import *
from dialog_aggiungi_esame import *

import sys, datetime

import icone

class Dialog_aggiunta_esami(Ui_Dialog_aggiunta):
    def __init__(self):
        super(Dialog_aggiunta_esami, self).__init__()
    def setupUi(self, Dialog_aggiunta):
        super(Dialog_aggiunta_esami, self).setupUi(Dialog_aggiunta)

        self.Dialog_Parent=Dialog_aggiunta
        
        

        #proprietà dateEdit
        self.dateEdit.setMinimumDate(QtCore.QDate(1980,1,1))
        self.dateEdit.setMaximumDate(QtCore.QDate(2050,1,1))
        curr_date=datetime.datetime.now()
        self.dateEdit.setDate(QtCore.QDate(curr_date.year, curr_date.month, curr_date.day))
        self.dateEdit.setDisplayFormat('dd/MM/yyyy')
        

        #proprietà comboBox_voto
        for i in voti_disponibili:
            self.comboBox_voto.addItem(str(i))

        #CONNESSIONE combobox_voto con InMedia
        self.checkBox_inmedia.setTristate(False)
        self.comboBox_voto.currentIndexChanged.connect(self.voto_media)

        #CONNESSIONE PULSANTE OK GENERALE!!
        self.buttonBox.accepted.connect(self.OK)


    def voto_media(self, index):
        if index!=0:
            self.checkBox_inmedia.setCheckState(QtCore.Qt.Checked)
        else:
            self.checkBox_inmedia.setCheckState(QtCore.Qt.Unchecked)

    def OK(self):

        try:
            nome_esame=self.lineEdit_nome_esame.text()
            docente=self.lineEdit_2_docente.text()
            voto=voti_disponibili[self.comboBox_voto.currentIndex()]
            inmedia=self.checkBox_inmedia.isChecked()
            data= self.dateEdit.date().toString('dd/MM/yyyy')
            crediti=int(self.lineEdit_crediti.text())

        #CREA OGGETTO ESAME E NE TESTA LA VALIDITÀ; AGGIUNGE L'ESAME AL DATABASE


            esame_instance=esame(nome_esame,voto, crediti, data, docente, inmedia)


            #AGGIUNGO AL DATABASE L'ESAME CREATO
            db=connetti_database()

            aggiungi_al_database(esame_instance, db)
            chiudi_database(db)

            self.Dialog_Parent.accept()

        except ExamError:
            QtGui.QMessageBox.warning(self.Dialog_Parent, 'ERRORE', "Attenzione: i dati dell'esame non sono validi!\n\nControlla di averli inseriti tutti in modo corretto.\n\nNB: una IDONEITÀ non può essere inserita nella media!!")
        except ValueError:
            QtGui.QMessageBox.warning(self.Dialog_Parent, 'ERRORE', 'Attenzione: il numero di crediti deve essere espresso da un numero!')
        except DatabasePresentError:
            QtGui.QMessageBox.warning(self.Dialog_Parent, 'ERRORE', 'Attenzione: Nel database è già presente un esame con questo nome!\nNon possono esistere esami con lo stesso nome!')

class Dialog_Rimozione_Esame(QtGui.QDialog):
    def __init__(self, modello, lista_esami_modello, parent=None):
        super(Dialog_Rimozione_Esame, self).__init__(parent)

        self.modello=modello

        self.lista_esami_modello=lista_esami_modello

        self.Genitore=parent
        
        self.setWindowTitle('Rimozione esame')
        
        self.setWindowIcon(QtGui.QIcon(':/Icons/application.png'))

        self.label=QtGui.QLabel("Seleziona l'esame che vuoi rimuovere e premi OK")


        self.buttons=QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        self.listview=QtGui.QListView()
        self.listview.setModel(self.modello)

        vboxlayout=QtGui.QVBoxLayout()
        vboxlayout.addWidget(self.label)

        vboxlayout.addWidget(self.listview)
        vboxlayout.addWidget(self.buttons)

        self.setLayout(vboxlayout)

        #self.buttons.accepted.connect(self.Elimina_Esame)
        QtCore.QObject.connect(self.buttons, QtCore.SIGNAL("accepted()"), self.Elimina_Esame)
        self.buttons.rejected.connect(self.reject)

    def Elimina_Esame(self):


        temp=self.listview.selectedIndexes()
        try:

            index=temp[0].row()
            nome_esame=self.lista_esami_modello[index].nome

            db=connetti_database()

            elimina_dal_database(nome_esame, db)
            chiudi_database(db)

            self.accept()
        except DatabaseAbsentError:
            pass


class Dialog_Modifica_Esame_Parametri(Dialog_aggiunta_esami):
    def __init__(self, esame_da_modificare):
        super(Dialog_Modifica_Esame_Parametri, self).__init__()
        self.esame_da_modificare=esame_da_modificare
        
    def setupUi(self, Dialog_aggiunta):
        super(Dialog_Modifica_Esame_Parametri, self).setupUi(Dialog_aggiunta)
        
        
        Dialog_aggiunta.setWindowTitle(QtGui.QApplication.translate("Dialog_aggiunta", "Modifica Esame", None, QtGui.QApplication.UnicodeUTF8))
        
        self.lineEdit_nome_esame.setText(self.esame_da_modificare.nome)
        self.lineEdit_2_docente.setText(self.esame_da_modificare.docente)
        self.lineEdit_crediti.setText(str(self.esame_da_modificare.crediti))
        self.dateEdit.setDate(QtCore.QDate.fromString(self.esame_da_modificare.data, 'dd/MM/yyyy'))
        
        if self.esame_da_modificare.isidoneita==True:
            self.comboBox_voto.setCurrentIndex(0)
        elif self.esame_da_modificare.lode==True:
            self.comboBox_voto.setCurrentIndex(14)
        
        else:
            self.comboBox_voto.setCurrentIndex(voti_disponibili.index(self.esame_da_modificare.voto))
        
        if self.esame_da_modificare.inmedia==True:
            self.checkBox_inmedia.setCheckState(QtCore.Qt.Checked)
        else:
            self.checkBox_inmedia.setCheckState(QtCore.Qt.Unchecked)
            
    def OK(self):
        db=connetti_database()

        elimina_dal_database(self.esame_da_modificare.nome, db)
        chiudi_database(db)
        
        super(Dialog_Modifica_Esame_Parametri, self).OK()


class Dialog_Modifica_Esame (Dialog_Rimozione_Esame):
    def __init__(self, modello, lista_esami_modello, parent=None):
        super(Dialog_Modifica_Esame, self).__init__(modello, lista_esami_modello, parent)
        
        self.setWindowTitle('Modifica esame')
        
        self.label.setText("Seleziona l'esame che vuoi modificare")
        
        #QtCore.QObject.connect(self.buttons, QtCore.SIGNAL("accepted()"), self.Modifica_Esame)
        self.buttons.rejected.connect(self.reject)
        
    def Elimina_Esame(self):
        '''Reimplementazione di Elimina_Esame, in realta' modifica l'esame'''
        temp=self.listview.selectedIndexes()
        try:

            index=temp[0].row()
            nome_esame=self.lista_esami_modello[index].nome

            db=connetti_database()
            
            self.esame_da_modificare=db[nome_esame] #da passare come argomento insieme al dialog a setupUI
            
            chiudi_database(db)
            
            Dialog_modifica = QtGui.QDialog()
            ui_dialog_modifica = Dialog_Modifica_Esame_Parametri(self.esame_da_modificare)
            ui_dialog_modifica.setupUi(Dialog_modifica)
            if Dialog_modifica.exec_():

                self.accept()

            
            

            
        except DatabaseAbsentError:
            pass
        
    