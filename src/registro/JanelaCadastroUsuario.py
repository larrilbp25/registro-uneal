# -*- coding:utf-8 -*-

'''
    @author: alezy oliveira lima
    @contact: alezyoliveira[@]msn[.]com
    @license: GNU GPL v3.0

    
    Database tool for request registration management
    ( Núcleo Setorial de Registro e Controle Acadêmico - UNEAL Campus III
        Palmeira dos Índios - Alagoas - Brazil )
    Copyright (C) 2011  Alezy Oliveira Lima
    
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

from qt import *


class JanelaNovaSolicitacao(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("JanelaNovaSolicitacao")

        self.setEnabled(1)
        self.setMouseTracking(0)
        self.setAcceptDrops(0)


        self.label_cpf = QLabel(self,"label_cpf")
        self.label_cpf.setGeometry(QRect(20,20,149,20))

        self.label_nome = QLabel(self,"label_nome")
        self.label_nome.setGeometry(QRect(20,60,149,20))

        self.label_email = QLabel(self,"label_email")
        self.label_email.setGeometry(QRect(20,100,149,20))

        self.label_login = QLabel(self,"label_login")
        self.label_login.setGeometry(QRect(20,140,149,20))

        self.label_senha = QLabel(self,"label_senha")
        self.label_senha.setGeometry(QRect(20,180,149,20))

        self.label_repetir_senha = QLabel(self,"label_repetir_senha")
        self.label_repetir_senha.setGeometry(QRect(20,220,149,20))

        self.lineEdit_cpf = QLineEdit(self,"lineEdit_cpf")
        self.lineEdit_cpf.setGeometry(QRect(180,20,290,22))

        self.lineEdit_email = QLineEdit(self,"lineEdit_email")
        self.lineEdit_email.setGeometry(QRect(180,100,290,22))

        self.lineEdit_login = QLineEdit(self,"lineEdit_login")
        self.lineEdit_login.setGeometry(QRect(180,140,290,22))

        self.lineEdit_senha = QLineEdit(self,"lineEdit_senha")
        self.lineEdit_senha.setGeometry(QRect(180,180,290,22))

        self.botao_salvar = QPushButton(self,"botao_salvar")
        self.botao_salvar.setGeometry(QRect(180,260,90,24))

        self.botao_cancelar = QPushButton(self,"botao_cancelar")
        self.botao_cancelar.setGeometry(QRect(380,260,90,24))

        self.botao_limpar = QPushButton(self,"botao_limpar")
        self.botao_limpar.setGeometry(QRect(280,260,90,24))

        self.lineEdit_nome = QLineEdit(self,"lineEdit_nome")
        self.lineEdit_nome.setGeometry(QRect(180,60,290,22))

        self.lineEdit_repetir_senha = QLineEdit(self,"lineEdit_repetir_senha")
        self.lineEdit_repetir_senha.setEnabled(1)
        self.lineEdit_repetir_senha.setGeometry(QRect(180,220,290,22))
        lineEdit_repetir_senha_font = QFont(self.lineEdit_repetir_senha.font())
        self.lineEdit_repetir_senha.setFont(lineEdit_repetir_senha_font)

        self.languageChange()

        self.resize(QSize(492,298).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.botao_cancelar,SIGNAL("clicked()"),self.close)
        self.connect(self.botao_limpar,SIGNAL("clicked()"),self.lineEdit_cpf.clear)
        self.connect(self.botao_limpar,SIGNAL("clicked()"),self.lineEdit_email.clear)
        self.connect(self.botao_limpar,SIGNAL("clicked()"),self.lineEdit_login.clear)
        self.connect(self.botao_limpar,SIGNAL("clicked()"),self.lineEdit_nome.clear)
        self.connect(self.botao_limpar,SIGNAL("clicked()"),self.lineEdit_repetir_senha.clear)
        self.connect(self.botao_limpar,SIGNAL("clicked()"),self.lineEdit_senha.clear)


    def languageChange(self):
        self.setCaption(self.__trUtf8("\x43\x61\x64\x61\x73\x74\x72\x6f\x20\x64\x65\x20\x55\x73\x75\xc3\xa1\x72\x69\x6f"))
        self.label_cpf.setText(self.__tr("CPF (somente numeros)"))
        self.label_nome.setText(self.__tr("Nome"))
        self.label_email.setText(self.__tr("Email"))
        self.label_login.setText(self.__tr("Login"))
        self.label_senha.setText(self.__tr("Senha"))
        self.label_repetir_senha.setText(self.__tr("Repetir a senha"))
        self.botao_salvar.setText(self.__tr("Salvar"))
        self.botao_cancelar.setText(self.__tr("Cancelar"))
        self.botao_limpar.setText(self.__tr("Limpar"))
        self.lineEdit_repetir_senha.setText(QString.null)


    def __tr(self,s,c = None):
        return qApp.translate("JanelaNovaSolicitacao",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("JanelaNovaSolicitacao",s,c,QApplication.UnicodeUTF8)
