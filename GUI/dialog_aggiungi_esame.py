# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog_aggiungi_esame.ui'
#
# Created: Wed Jan  2 01:59:01 2013
#      by: PyQt4 UI code generator 4.9.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog_aggiunta(object):
    def setupUi(self, Dialog_aggiunta):
        Dialog_aggiunta.setObjectName(_fromUtf8("Dialog_aggiunta"))
        Dialog_aggiunta.resize(411, 291)
        Dialog_aggiunta.setStyleSheet(_fromUtf8("QLineEdit:focus {\n"
"\n"
"background-color: yellow;\n"
"\n"
"}"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_aggiunta)
        self.buttonBox.setGeometry(QtCore.QRect(50, 250, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.widget = QtGui.QWidget(Dialog_aggiunta)
        self.widget.setGeometry(QtCore.QRect(10, 10, 391, 231))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 0, 1, 1)
        self.checkBox_inmedia = QtGui.QCheckBox(self.widget)
        self.checkBox_inmedia.setObjectName(_fromUtf8("checkBox_inmedia"))
        self.gridLayout.addWidget(self.checkBox_inmedia, 8, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)
        self.lineEdit_2_docente = QtGui.QLineEdit(self.widget)
        self.lineEdit_2_docente.setObjectName(_fromUtf8("lineEdit_2_docente"))
        self.gridLayout.addWidget(self.lineEdit_2_docente, 6, 0, 1, 1)
        self.lineEdit_nome_esame = QtGui.QLineEdit(self.widget)
        self.lineEdit_nome_esame.setObjectName(_fromUtf8("lineEdit_nome_esame"))
        self.gridLayout.addWidget(self.lineEdit_nome_esame, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 5, 1, 1, 1)
        self.dateEdit = QtGui.QDateEdit(self.widget)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(0, 0, 0)))
        self.dateEdit.setCurrentSection(QtGui.QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.gridLayout.addWidget(self.dateEdit, 6, 1, 1, 1)
        self.comboBox_voto = QtGui.QComboBox(self.widget)
        self.comboBox_voto.setObjectName(_fromUtf8("comboBox_voto"))
        self.gridLayout.addWidget(self.comboBox_voto, 1, 1, 1, 1)
        self.lineEdit_crediti = QtGui.QLineEdit(self.widget)
        self.lineEdit_crediti.setObjectName(_fromUtf8("lineEdit_crediti"))
        self.gridLayout.addWidget(self.lineEdit_crediti, 3, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.widget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.retranslateUi(Dialog_aggiunta)
        #QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_aggiunta.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_aggiunta.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_aggiunta)
        Dialog_aggiunta.setTabOrder(self.lineEdit_nome_esame, self.comboBox_voto)
        Dialog_aggiunta.setTabOrder(self.comboBox_voto, self.lineEdit_crediti)
        Dialog_aggiunta.setTabOrder(self.lineEdit_crediti, self.lineEdit_2_docente)
        Dialog_aggiunta.setTabOrder(self.lineEdit_2_docente, self.dateEdit)
        Dialog_aggiunta.setTabOrder(self.dateEdit, self.checkBox_inmedia)
        Dialog_aggiunta.setTabOrder(self.checkBox_inmedia, self.buttonBox)

    def retranslateUi(self, Dialog_aggiunta):
        Dialog_aggiunta.setWindowTitle(QtGui.QApplication.translate("Dialog_aggiunta", "Aggiungi esame", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_inmedia.setText(QtGui.QApplication.translate("Dialog_aggiunta", "Includi nella Media", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog_aggiunta", "Docente:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog_aggiunta", "Esame:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog_aggiunta", "Voto:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_2_docente.setPlaceholderText(QtGui.QApplication.translate("Dialog_aggiunta", "Inserisci il nome del docente...", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_nome_esame.setPlaceholderText(QtGui.QApplication.translate("Dialog_aggiunta", "Inserisci il nome dell\'esame...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog_aggiunta", "Data:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_crediti.setPlaceholderText(QtGui.QApplication.translate("Dialog_aggiunta", "Inserisci il numero di crediti...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog_aggiunta", "Crediti:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog_aggiunta = QtGui.QDialog()
    ui = Ui_Dialog_aggiunta()
    ui.setupUi(Dialog_aggiunta)
    Dialog_aggiunta.show()
    sys.exit(app.exec_())

