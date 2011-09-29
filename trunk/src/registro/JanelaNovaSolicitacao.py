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
from DAO.SolicitacaoDAO import SolicitacaoDAO
from JanelaNovoRegistro import LISTA_GRADUACAO

class JanelaNovaSolicitacao(QWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("JanelaNovaSolicitacao")


        self.lineEdit_nome = QLineEdit(self,"lineEdit_nome")
        self.lineEdit_nome.setGeometry(QRect(110,20,410,22))

        self.label_nome = QLabel(self,"label_nome")
        self.label_nome.setGeometry(QRect(20,20,68,20))

        self.comboBox_curso = QComboBox(0,self,"comboBox_curso")
        self.comboBox_curso.setGeometry(QRect(110,60,410,22))

        self.label_curso = QLabel(self,"label_curso")
        self.label_curso.setGeometry(QRect(20,60,68,20))

        self.label_data = QLabel(self,"label_data")
        self.label_data.setGeometry(QRect(20,100,86,20))

        self.checkBox_certidao = QCheckBox(self,"checkBox_certidao")
        self.checkBox_certidao.setGeometry(QRect(110,140,210,20))

        self.checkBox_declaracao = QCheckBox(self,"checkBox_declaracao")
        self.checkBox_declaracao.setGeometry(QRect(110,160,210,20))

        self.checkBox_diploma = QCheckBox(self,"checkBox_diploma")
        self.checkBox_diploma.setGeometry(QRect(110,180,210,20))

        self.checkBox_historico = QCheckBox(self,"checkBox_historico")
        self.checkBox_historico.setGeometry(QRect(110,200,93,20))

        self.label_solicitacao = QLabel(self,"label_solicitacao")
        self.label_solicitacao.setGeometry(QRect(20,140,86,20))

        self.checkBox_outros = QCheckBox(self,"checkBox_outros")
        self.checkBox_outros.setGeometry(QRect(110,220,250,20))

        self.checkBox_urgencia = QCheckBox(self,"checkBox_urgencia")
        self.checkBox_urgencia.setGeometry(QRect(110,250,410,40))

        self.textEdit_observacoes = QTextEdit(self,"textEdit_observacoes")
        self.textEdit_observacoes.setGeometry(QRect(110,300,410,70))

        self.label_observacoes = QLabel(self,"label_observacoes")
        self.label_observacoes.setGeometry(QRect(20,300,86,20))

        self.dateEdit_data = QDateEdit(self,"dateEdit_data")
        self.dateEdit_data.setEnabled(1)
        self.dateEdit_data.setGeometry(QRect(110,100,100,22))
        self.dateEdit_data.setDate(QDate(2000,1,1))
        self.dateEdit_data.setAutoAdvance(1)

        self.botao_salvar = QPushButton(self,"botao_salvar")
        self.botao_salvar.setGeometry(QRect(240,380,90,24))

        self.botao_limpar = QPushButton(self,"botao_limpar")
        self.botao_limpar.setGeometry(QRect(340,380,90,24))

        self.botao_cancelar = QPushButton(self,"botao_cancelar")
        self.botao_cancelar.setGeometry(QRect(440,380,90,24))

        self.languageChange()

        self.resize(QSize(544,415).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)
        
        self.connect(self.botao_salvar, SIGNAL("clicked()"), self.salvar)
        self.connect(self.botao_limpar, SIGNAL("clicked()"), self.limpar_campos)
        self.connect(self.botao_cancelar, SIGNAL("clicked()"), self.close)


    def salvar(self):
        dict = {}
        
        registro_dao = SolicitacaoDAO()
        
        dict['id'] = registro_dao.getNewID()
        
        if len(self.lineEdit_nome.text()) != 0:
            dict['nome'] = str(self.lineEdit_nome.text())
        else:
            return QMessageBox.warning(None, "Oops", u"Você esqueceu de digitar o nome do aluno.")
        
        dict['curso'] = LISTA_GRADUACAO[self.comboBox_curso.currentItem()]
        
        date = self.dateEdit_data.date()
        dict['data'] = str(date.year()) + '-' + str(date.month()) + '-' + str(date.day())

        if self.checkBox_certidao.isChecked(): dict['certidao'] = 1
        else: dict['certidao'] = 0

        if self.checkBox_declaracao.isChecked(): dict['declaracao'] = 1
        else: dict['declaracao'] = 0

        if self.checkBox_diploma.isChecked(): dict['diploma'] = 1
        else: dict['diploma'] = 0

        if self.checkBox_historico.isChecked(): dict['historico'] = 1
        else: dict['historico'] = 0

        if self.checkBox_outros.isChecked(): dict['outros'] = 1
        else: dict['outros'] = 0

        if self.checkBox_urgencia.isChecked(): dict['urgencia'] = 1
        else: dict['urgencia'] = 0
        
        dict['observacoes'] = self.textEdit_observacoes.text()
        
        if registro_dao.insert(dict) == True:
            QMessageBox.information(None, "Salvo", "Dados salvos com sucesso.")
            return self.close()
        
        print "JanelaNovaSolicitacao.salvar(): Not implemented yet"
    
    def limpar_campos(self):
        for item in self.lineEdit_nome, self.textEdit_observacoes:
            item.clear()
        for item in self.checkBox_certidao, self.checkBox_declaracao, self.checkBox_diploma, self.checkBox_historico, self.checkBox_outros, self.checkBox_urgencia:
            item.setChecked(False)
        for item in self.dateEdit_data:
            pass
        print "JanelaNovaSolicitacao.limpar(): Not implemented yet"

    def languageChange(self):
        self.setCaption(self.__trUtf8("Nova solicitação"))
        self.label_nome.setText(self.__tr("Nome"))
        self.comboBox_curso.clear()
        for item in LISTA_GRADUACAO:
            self.comboBox_curso.insertItem(self.__trUtf8(item))
        self.label_curso.setText(self.__tr("Curso"))
        self.label_data.setText(self.__tr("Data"))
        self.label_solicitacao.setText(self.__trUtf8("Solicitação"))
        self.checkBox_certidao.setText(self.__trUtf8("Certidão de conclusão de curso"))
        self.checkBox_declaracao.setText(self.__trUtf8("Declaração"))
        self.checkBox_diploma.setText(self.__tr("Diploma"))
        self.checkBox_historico.setText(self.__trUtf8("Histórico"))
        self.checkBox_outros.setText(self.__trUtf8("Outros (especificar nas observações)"))
        self.checkBox_urgencia.setText(self.__trUtf8("Marque aqui caso seja uma solicitação de urgência comprovada\n(especificar nas observações)"))
        self.label_observacoes.setText(self.__trUtf8("Observações"))
        self.botao_salvar.setText(self.__tr("Salvar"))
        self.botao_limpar.setText(self.__tr("Limpar"))
        self.botao_cancelar.setText(self.__tr("Cancelar"))


    def __tr(self,s,c = None):
        return qApp.translate("JanelaNovaSolicitacao",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("JanelaNovaSolicitacao",s,c,QApplication.UnicodeUTF8)
