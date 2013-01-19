__author__ = 'ivanhoe1024'
__version__='0.95-beta'
import sys
from PyQt4 import QtCore, QtGui
from engine import *
#from css import *
from MainWindow_Esami_child import *
import icone


class widget_princ (QtGui.QWidget):
    def __init__(self):
        super(widget_princ, self).__init__()


        #PULSANTE ESCI
        self.exit_button=QtGui.QToolButton(self)
        self.exit_button.setIcon(QtGui.QIcon(':/Icons/application-exit.png'))
        self.exit_button.setIconSize(QtCore.QSize(48, 48))
        self.exit_button.setText('Esci')
        self.exit_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        #self.exit_button.setToolTip('Esci dall'applicazione')
        self.exit_button.setStatusTip("Esci dall'applicazione")


        #PULSANTE ESAMI
        self.esami_button=QtGui.QToolButton(self)
        self.esami_button.setIcon(QtGui.QIcon(':/Icons/applications-education.png'))
        self.esami_button.setIconSize(QtCore.QSize(48, 48))
        self.esami_button.setText('Esami')
        self.esami_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        #self.esami_button.setToolTip('Vedi la lista degli esami')
        self.esami_button.setStatusTip('Vedi la lista degli esami')

        #PULSANTE STATISTICHE
        self.stat_button=QtGui.QToolButton(self)
        self.stat_button.setIcon(QtGui.QIcon(':/Icons/statistiche.png'))
        self.stat_button.setIconSize(QtCore.QSize(48, 48))
        self.stat_button.setText('Statistiche')
        self.stat_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        #self.stat_button.setToolTip('Vedi le statistiche')
        self.stat_button.setStatusTip('Vedi le statistiche')

        #PULSANTE INFO
        self.info_button=QtGui.QToolButton(self)
        self.info_button.setIcon(QtGui.QIcon(':/Icons/information.png'))
        self.info_button.setIconSize(QtCore.QSize(48, 48))
        self.info_button.setText('Informazioni')
        self.info_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        #self.info_button.setToolTip('Vedi le informazioni')
        self.info_button.setStatusTip('Vedi le informazioni')



        #LAYOUT ORIZZONTALE
        hlayout=QtGui.QHBoxLayout()
        hlayout.addWidget(self.esami_button)
        hlayout.addWidget(self.stat_button)
        hlayout.addWidget(self.info_button)
        hlayout.addWidget(self.exit_button)
        hlayout.setSpacing(15)
        hlayout.setMargin(10)
        self.setLayout(hlayout)

        #CSS
        #self.setStyleSheet(css_finestra_principale)

        

class Finestra(QtGui.QMainWindow):
    def __init__(self, MainWindow_Esami_instance):
        super(Finestra, self).__init__()
        self.MainWindow_Esami_instance=MainWindow_Esami_instance

        self.setWindowTitle('Libretto Universitario')
        self.setWindowIcon(QtGui.QIcon(':/Icons/application.png'))

        self.statusbar=self.statusBar().showMessage('Benvenuto!')


        self.widgetprinc=widget_princ()

        self.setCentralWidget(self.widgetprinc)
        
        #SIGNAL AND SLOTS
        QtCore.QObject.connect(self.widgetprinc.exit_button, QtCore.SIGNAL('clicked()'), self.close)
        QtCore.QObject.connect(self.widgetprinc.stat_button, QtCore.SIGNAL('clicked()'), self.stat)
        QtCore.QObject.connect(self.widgetprinc.esami_button, QtCore.SIGNAL('clicked()'), self.pulsante_esami)
        QtCore.QObject.connect(self.widgetprinc.info_button, QtCore.SIGNAL('clicked()'), self.info)

    def stat(self):
        dialog_stat=Dialog_statistica()
        if dialog_stat.exec_():
            pass

    def info(self):
        QtGui.QMessageBox.information(self,'Informazioni','Programma scritto in Python 3 con librerie grafiche Qt. \n\nScritto da Francesco Orofino (ivanhoe1024@gmail.com)\n\nVersione: %s' %(__version__))

    def pulsante_esami(self):
        
        self.MainWindow_Esami_instance.show()


class Dialog_statistica(QtGui.QDialog):
    def __init__(self):
        super(Dialog_statistica, self).__init__()

        #CALCOLO STATISTICHE


        lista_esami=crea_lista_esami()
        #NUMERO DI ESAMI
        num_esami=len(lista_esami)

        num_tot_crediti=0
        num_crediti_media=0
        num_lodi=0
        media_aritm_numeratore=0
        media_ponderata_numeratore=0
        
        esami_in_media=0
        
        for i in lista_esami:
            num_tot_crediti=num_tot_crediti + i.crediti
            if i.inmedia==True:
                num_crediti_media=num_crediti_media + i.crediti
                media_ponderata_numeratore=media_ponderata_numeratore + int(i.crediti * i.voto)
                media_aritm_numeratore=media_aritm_numeratore + i.voto
                esami_in_media+=1
            if i.lode==True:
                num_lodi=num_lodi + 1

        try:
            media_aritm=media_aritm_numeratore/esami_in_media
        except ZeroDivisionError:
            media_aritm=0
        try:
            media_ponderata=media_ponderata_numeratore/num_crediti_media
        except ZeroDivisionError:
            media_ponderata=0
            
        voto_laurea_base=media_ponderata*11/3
            
        self.setWindowTitle('Statistiche')
        
        self.testo_principale='''Numero Totale esami:   %d

Totale Crediti:         %d
di cui utilizzati per la media:    %d

Numero di Lodi:    %d

Media Aritmetica:    %g
Media Ponderata:    %g

Voto base di Laurea:    %g''' %(num_esami,num_tot_crediti, num_crediti_media, num_lodi, media_aritm, media_ponderata, voto_laurea_base)
        
        self.mainLabel=QtGui.QLabel()
        self.mainLabel.setText(self.testo_principale)
        
        self.button=QtGui.QPushButton('Chiudi')
        self.button.clicked.connect(self.close)
        
        layout=QtGui.QVBoxLayout()
        layout.addWidget(self.mainLabel)
        layout.addWidget(self.button)
        self.setLayout(layout)






def main():
    #Creo applicazione
    app=QtGui.QApplication(sys.argv)
    #Creo un oggetto di tipo Finestra
    #w=Finestra()


    #Creo finestra ESAMI
    MainWindow_Esami_instance = QtGui.QMainWindow()
    ui_esami = Finestra_Principale_Esami()
    ui_esami.setupUi(MainWindow_Esami_instance)

    #Creo finestra iniziale del programma passandogli il riferimento della finestra esami
    w=Finestra(MainWindow_Esami_instance)

    w.show()

    #Loop dell'applicazione
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()