# -*- coding: utf-8 -*-

from qt import *

class JanelaBuscaRegistros(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("JanelaBuscaRegistros")



        self.listView = QListView(self,"listView")
        self.listView.addColumn(self.__tr("Registro"))
        self.listView.addColumn(self.__tr("Nome"))
        self.listView.addColumn(self.__tr("Curso"))
        self.listView.addColumn(self.__tr("Status"))
        self.listView.setGeometry(QRect(20,75,500,270))

        self.textLabel1 = QLabel(self,"textLabel1")
        self.textLabel1.setGeometry(QRect(20,15,297,20))

        self.textLabel2 = QLabel(self,"textLabel2")
        self.textLabel2.setGeometry(QRect(20,352,376,20))

        self.lineEdit2 = QLineEdit(self,"lineEdit2")
        self.lineEdit2.setGeometry(QRect(20,40,300,24))

        self.botao_editar = QPushButton(self,"botao_editar")
        self.botao_editar.setGeometry(QRect(430,350,90,24))

        self.botao_listar = QPushButton(self,"botao_listar")
        self.botao_listar.setGeometry(QRect(430,40,90,24))

        self.botao_buscar = QPushButton(self,"botao_buscar")
        self.botao_buscar.setGeometry(QRect(330,40,90,24))

        self.languageChange()

        self.resize(QSize(544,387).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)


    def buscar(self):
        pass
    def listar(self):
        pass
    def editar(self):
        pass

    def languageChange(self):
        self.setCaption(self.__tr("Busca de registros"))
        self.listView.header().setLabel(0,self.__tr("Registro"))
        self.listView.header().setLabel(1,self.__tr("Nome"))
        self.listView.header().setLabel(2,self.__tr("Curso"))
        self.listView.header().setLabel(3,self.__tr("Status"))
        self.listView.clear()
        item = QListViewItem(self.listView,None)
        item.setText(0,self.__tr("Item 1"))

        item = QListViewItem(self.listView,item)
        item.setText(0,self.__tr("Item 2"))

        self.textLabel1.setText(self.__trUtf8("\x44\x69\x67\x69\x74\x65\x20\x6f\x20\x6e\x6f\x6d\x65\x20\x64\x6f\x20\x61\x6c\x75\x6e\x6f\x20\x65\x20\x63\x6c\x69\x71\x75\x65\x20\x6e\x6f\x20\x62\x6f\x74\xc3\xa3\x6f\x20\x62\x75\x73\x63\x61\x72"))
        self.textLabel2.setText(self.__trUtf8("\x50\x61\x72\x61\x20\x65\x64\x69\x74\x61\x72\x2c\x20\x73\x65\x6c\x65\x63\x69\x6f\x6e\x65\x20\x6f\x20\x69\x74\x65\x6d\x20\x6e\x61\x20\x6c\x69\x73\x74\x61\x20\x65\x20\x63\x6c\x69\x71\x75\x65\x20\x6e\x6f\x20\x62\x6f\x74\xc3\xa3\x6f\x20\x61\x6f\x20\x6c\x61\x64\x6f"))
        self.botao_editar.setText(self.__tr("Editar"))
        self.botao_listar.setText(self.__tr("Listar todos"))
        self.botao_buscar.setText(self.__tr("Buscar"))


    def __tr(self,s,c = None):
        return qApp.translate("JanelaBuscaRegistros",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("JanelaBuscaRegistros",s,c,QApplication.UnicodeUTF8)
