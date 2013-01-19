__author__ = 'ivanhoe1024'

from PyQt4 import QtGui, QtCore
from MainWindow_Esami import Ui_MainWindow_Esami
from engine import *
from dialog_aggiungi_esame import *
from dialogs import *

import icone




import sys, datetime




try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Finestra_Principale_Esami(Ui_MainWindow_Esami):
    def __init__(self):
        super(Finestra_Principale_Esami, self).__init__()

    def setupUi(self, MainWindow_Esami):
        super(Finestra_Principale_Esami, self).setupUi(MainWindow_Esami)
        self.tableview=QtGui.QTableView()

        self.MainWindow_Parent=MainWindow_Esami

        self.MainWindow_Parent.setCentralWidget(self.tableview)
        self.lista_esami_modello=crea_lista_esami()
        self.modello=Modello_Tabella(self.lista_esami_modello)
        self.tableview.setModel(self.modello)
        self.tableview.setCornerButtonEnabled(False)
        self.MainWindow_Parent.resize(720, 300)
        self.MainWindow_Parent.setWindowIcon(QtGui.QIcon(':/Icons/application.png'))
        
        


        QtCore.QObject.connect(self.actionAggiungi_Esame, QtCore.SIGNAL("triggered()"), self.aggiungi_esame)
        QtCore.QObject.connect(self.actionRimuovi_Esame, QtCore.SIGNAL("triggered()"), self.rimuovi_esame)
        QtCore.QObject.connect(self.actionModifica_Esame, QtCore.SIGNAL("triggered()"),self.modifica_esame)

    def aggiorna_modello(self):
        
        self.lista_esami_modello=crea_lista_esami()
        self.modello=Modello_Tabella(self.lista_esami_modello)
        self.tableview.setModel(self.modello)
        
    def aggiungi_esame(self):
        Dialog_aggiunta = QtGui.QDialog()
        ui_dialog = Dialog_aggiunta_esami()
        ui_dialog.setupUi(Dialog_aggiunta)
        if Dialog_aggiunta.exec_():

            self.aggiorna_modello()



    def rimuovi_esame(self):
        dialog_rimozione=Dialog_Rimozione_Esame(self.modello, self.lista_esami_modello, parent=self.MainWindow_Parent)

        if dialog_rimozione.exec_():
            self.aggiorna_modello()
            
    def modifica_esame(self):
        dialog_modifica=Dialog_Modifica_Esame(self.modello, self.lista_esami_modello, parent=self.MainWindow_Parent)
        
        if dialog_modifica.exec_():
            self.aggiorna_modello()


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow_Esami = QtGui.QMainWindow()
    ui = Finestra_Principale_Esami()
    ui.setupUi(MainWindow_Esami)
    MainWindow_Esami.show()
    sys.exit(app.exec_())

