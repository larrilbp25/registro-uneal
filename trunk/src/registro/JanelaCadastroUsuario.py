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


class JanelaCadastroUsuario(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("JanelaCadastroUsuario")

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
        self.lineEdit_senha.setEchoMode(2)

        self.botao_salvar = QPushButton(self,"botao_salvar")
        self.botao_salvar.setGeometry(QRect(180,260,90,24))

        self.botao_cancelar = QPushButton(self,"botao_cancelar")
        self.botao_cancelar.setGeometry(QRect(380,260,90,24))

        self.botao_limpar = QPushButton(self,"botao_limpar")
        self.botao_limpar.setGeometry(QRect(280,260,90,24))

        self.lineEdit_nome = QLineEdit(self,"lineEdit_nome")
        self.lineEdit_nome.setGeometry(QRect(180,60,290,22))

        self.lineEdit_repetir_senha = QLineEdit(self,"lineEdit_repetir_senha")
        self.lineEdit_repetir_senha.setGeometry(QRect(180,220,290,22))
        self.lineEdit_repetir_senha.setEchoMode(2)
        
        self.languageChange()

        self.resize(QSize(492,298).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.botao_salvar,SIGNAL("clicked()"),self.salvar)
        self.connect(self.botao_cancelar,SIGNAL("clicked()"),self.close)
        self.connect(self.botao_limpar,SIGNAL("clicked()"),self.limpar_campos)


    def languageChange(self):
        self.setCaption(self.__trUtf8(u"Cadastro de Usuário"))
        self.label_cpf.setText(self.__trUtf8("CPF (somente números)"))
        self.label_nome.setText(self.__tr("Nome"))
        self.label_email.setText(self.__tr("Email"))
        self.label_login.setText(self.__tr("Login"))
        self.label_senha.setText(self.__tr("Senha"))
        self.label_repetir_senha.setText(self.__tr("Repetir a senha"))
        self.botao_salvar.setText(self.__tr("Salvar"))
        self.botao_cancelar.setText(self.__tr("Cancelar"))
        self.botao_limpar.setText(self.__tr("Limpar"))
        self.lineEdit_repetir_senha.setText(QString.null)

    def salvar(self):
        for item in self.lineEdit_cpf, self.lineEdit_email, self.lineEdit_login, self.lineEdit_nome, self.lineEdit_repetir_senha, self.lineEdit_senha:
            if len(item.text())==0:
                print item.text(), u' não preenchido' # pegar o nome de batismo da variavel ?????????????????????????
                return

    def limpar_campos(self):
        for item in self.lineEdit_cpf, self.lineEdit_email, self.lineEdit_login, self.lineEdit_nome, self.lineEdit_repetir_senha, self.lineEdit_senha:
            item.clear()

    def __tr(self,s,c = None):
        return qApp.translate("JanelaCadastroUsuario",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("JanelaCadastroUsuario",s,c,QApplication.UnicodeUTF8)
