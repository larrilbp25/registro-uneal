# -*- coding: utf-8 -*-

from qt import *
from imagens import logo_uneal

texto_sobre = '''
Este software é um banco de dados de acompanhamento
e controle de processos de expedição de Diploma do
Campus III (Palmeira dos Índios) da Universidade
Estadual de Alagoas e é disponibilizado sob os
termos da licença GNU GPL versão 3, sendo assim
Software Livre.
    
Versão: 0.1 alfa
Desenvolvedor: Alezy Oliveira Lima
Email: alezy.oliveira@uneal.edu.br
'''

class JanelaSobre(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        self.image0 = QPixmap()
        self.image0.loadFromData(logo_uneal,"PNG")
        if not name:
            self.setName("JanelaSobre")



        self.label_logo_uneal = QLabel(self,"label_logo_uneal")
        self.label_logo_uneal.setGeometry(QRect(130,10,50,70))
        self.label_logo_uneal.setPixmap(self.image0)
        self.label_logo_uneal.setScaledContents(1)

        self.label_sobre = QLabel(self,"label_sobre")
        self.label_sobre.setGeometry(QRect(10,90,297,191))

        self.botao_fechar = QPushButton(self,"botao_fechar")
        self.botao_fechar.setGeometry(QRect(100,290,112,24))

        self.languageChange()

        self.resize(QSize(315,326).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.botao_fechar,SIGNAL("clicked()"),self.close)


    def languageChange(self):
        self.setCaption(self.__tr("Sobre o software"))
        self.label_sobre.setText(self.__trUtf8(texto_sobre))
        self.botao_fechar.setText(self.__tr("Fechar"))


    def __tr(self,s,c = None):
        return qApp.translate("JanelaSobre",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("JanelaSobre",s,c,QApplication.UnicodeUTF8)
