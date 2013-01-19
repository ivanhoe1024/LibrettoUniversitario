# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow_Esami.ui'
#
# Created: Sun Dec 30 16:13:52 2012
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow_Esami(object):
    def setupUi(self, MainWindow_Esami):
        MainWindow_Esami.setObjectName(_fromUtf8("MainWindow_Esami"))
        MainWindow_Esami.setWindowModality(QtCore.Qt.ApplicationModal)

        MainWindow_Esami.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtGui.QWidget(MainWindow_Esami)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow_Esami.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow_Esami)
        self.menubar.setEnabled(True)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 495, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow_Esami.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow_Esami)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow_Esami.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow_Esami)
        self.toolBar.setToolTip(_fromUtf8(""))
        self.toolBar.setStatusTip(_fromUtf8(""))
        self.toolBar.setMovable(False)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow_Esami.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar)
        self.actionAggiungi_Esame = QtGui.QAction(MainWindow_Esami)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/dialog-more.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAggiungi_Esame.setIcon(icon)
        self.actionAggiungi_Esame.setObjectName(_fromUtf8("actionAggiungi_Esame"))
        self.actionRimuovi_Esame = QtGui.QAction(MainWindow_Esami)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/dialog-cancel-3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRimuovi_Esame.setIcon(icon1)
        self.actionRimuovi_Esame.setObjectName(_fromUtf8("actionRimuovi_Esame"))
        self.actionEsci = QtGui.QAction(MainWindow_Esami)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/Icons/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEsci.setIcon(icon2)
        self.actionEsci.setObjectName(_fromUtf8("actionEsci"))
        self.actionInformazioni = QtGui.QAction(MainWindow_Esami)
        self.actionInformazioni.setObjectName(_fromUtf8("actionInformazioni"))
        
        #pulsante modifica esame aggiunto a mano
        self.actionModifica_Esame=QtGui.QAction(QtGui.QIcon(':/Icons/mod1.png'),'Modifica esame', MainWindow_Esami)
        
        self.menuFile.addAction(self.actionAggiungi_Esame)
        self.menuFile.addAction(self.actionModifica_Esame)
        self.menuFile.addAction(self.actionRimuovi_Esame)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEsci)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionAggiungi_Esame)
        self.toolBar.addAction(self.actionModifica_Esame)
        self.toolBar.addAction(self.actionRimuovi_Esame)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionEsci)

        self.retranslateUi(MainWindow_Esami)
        QtCore.QObject.connect(self.actionEsci, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow_Esami.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Esami)

    def retranslateUi(self, MainWindow_Esami):
        MainWindow_Esami.setWindowTitle(QtGui.QApplication.translate("MainWindow_Esami", "Libretto Universitario -- Esami", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow_Esami", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow_Esami", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAggiungi_Esame.setText(QtGui.QApplication.translate("MainWindow_Esami", "Aggiungi Esame", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAggiungi_Esame.setStatusTip(QtGui.QApplication.translate("MainWindow_Esami", "Aggiungi un esame al database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAggiungi_Esame.setShortcut(QtGui.QApplication.translate("MainWindow_Esami", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRimuovi_Esame.setText(QtGui.QApplication.translate("MainWindow_Esami", "Rimuovi Esame", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRimuovi_Esame.setStatusTip(QtGui.QApplication.translate("MainWindow_Esami", "Rimuovi l\'esame selezionato dal database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRimuovi_Esame.setShortcut(QtGui.QApplication.translate("MainWindow_Esami", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEsci.setText(QtGui.QApplication.translate("MainWindow_Esami", "Esci", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEsci.setStatusTip(QtGui.QApplication.translate("MainWindow_Esami", "Esci e torna alla finestra principale", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEsci.setShortcut(QtGui.QApplication.translate("MainWindow_Esami", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInformazioni.setText(QtGui.QApplication.translate("MainWindow_Esami", "Informazioni", None, QtGui.QApplication.UnicodeUTF8))
        
        self.actionModifica_Esame.setStatusTip('Modifica un esame già inserito')
        self.actionModifica_Esame.setShortcut(QtGui.QApplication.translate("MainWindow_Esami", "Ctrl+M", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow_Esami = QtGui.QMainWindow()
    ui = Ui_MainWindow_Esami()
    ui.setupUi(MainWindow_Esami)
    MainWindow_Esami.show()
    sys.exit(app.exec_())

