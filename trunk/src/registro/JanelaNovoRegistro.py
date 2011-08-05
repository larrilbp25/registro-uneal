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
from DAO.RegistroDAO import RegistroDAO

LISTA_GRADUACAO = [u"Ciências",
                   u"Ciências Biológicas",
                   u"Geografia",
                   u"História",
                   u"Letras",
                   u"Matemática",
                   u"Pedagogia",
                   u"Química",
                   u"Outro (especificar nas observações)"]

LISTA_POS_GRADUACAO = [u"História do Nordeste Brasileiro",
                       u"Língua Portuguesa e Literatura Brasileira",
                       u"Outro (especificar nas observações)"]

class JanelaNovoRegistro(QWidget):
    def __init__(self,parent = None,name = None,fl = 0, *args):
        QWidget.__init__(self,parent,name,fl)

        if not name:
            self.setName("JanelaNovo")

        # assinatura QRect: (x, y, width, height)
        self.label_registro = QLabel(self, "label_registro")
        self.label_registro.setGeometry(QRect(20,20,100,20))
        
        self.spinbox_registro = QSpinBox(self, "spinbox_registro")
        self.spinbox_registro.setGeometry(QRect(110,20,70,20))
        self.spinbox_registro.setMinValue(1)
        self.spinbox_registro.setEnabled(False)

        self.label_tipo = QLabel(self,"label_tipo")
        self.label_tipo.setGeometry(QRect(200,20,68,20))

        self.radio_diploma = QRadioButton(self,"radio_diploma")
        self.radio_diploma.setGeometry(QRect(240,20,70,20))

        self.radio_certificado = QRadioButton(self,"radio_certificado")
        self.radio_certificado.setGeometry(QRect(320,20,200,20))

        self.label_nome = QLabel(self,"label_nome")
        self.label_nome.setGeometry(QRect(20,60,68,20))

        self.lineEdit_nome = QLineEdit(self,"lineEdit_nome")
        self.lineEdit_nome.setGeometry(QRect(110,60,410,22))

        self.label_curso = QLabel(self,"label_curso")
        self.label_curso.setGeometry(QRect(20,100,68,20))
        
        self.comboBox_curso = QComboBox(0,self,"comboBox_curso")
        self.comboBox_curso.setGeometry(QRect(110,100,410,22))

        self.label_data_registro = QLabel(self,"label_data_registro")
        self.label_data_registro.setGeometry(QRect(20,140,100,20))

        self.dateEdit_data_registro = QDateEdit(self,"dateEdit_data_registro")
        self.dateEdit_data_registro.setGeometry(QRect(130,140,100,22))

        self.label_data_saida = QLabel(self,"label_data_saida")
        self.label_data_saida.setGeometry(QRect(250,140,86,20))

        self.dateEdit_data_saida = QDateEdit(self,"dateEdit_data_saida")
        self.dateEdit_data_saida.setGeometry(QRect(340,140,100,22))

        self.label_status = QLabel(self,"label_status")
        self.label_status.setGeometry(QRect(20,180,86,20))

        self.radio_status1 = QRadioButton(self,"radio_status1")
        self.radio_status1.setGeometry(QRect(110,180,300,20))

        self.radio_status2 = QRadioButton(self,"radio_status2")
        self.radio_status2.setGeometry(QRect(110,200,300,20))

        self.radio_status3 = QRadioButton(self,"radio_status3")
        self.radio_status3.setGeometry(QRect(110,220,300,20))

        self.radio_status4 = QRadioButton(self,"radio_status4")
        self.radio_status4.setGeometry(QRect(110,240,300,20))

        self.label_observacoes = QLabel(self,"label_observacoes")
        self.label_observacoes.setGeometry(QRect(20,270,86,20))

        self.textEdit_observacoes = QTextEdit(self,"textEdit_observacoes")
        self.textEdit_observacoes.setGeometry(QRect(110,270,410,70))

        self.botao_salvar = QPushButton(self,"botao_salvar")
        self.botao_salvar.setGeometry(QRect(240,350,90,24))

        self.botao_limpar = QPushButton(self,"botao_limpar")
        self.botao_limpar.setGeometry(QRect(340,350,90,24))

        self.botao_cancelar = QPushButton(self,"botao_cancelar")
        self.botao_cancelar.setGeometry(QRect(440,350,90,24))

        self.languageChange()

        self.connect(self.radio_diploma, SIGNAL("clicked()"), self.alterarTipoDocumento)
        self.connect(self.radio_certificado, SIGNAL("clicked()"), self.alterarTipoDocumento)
        self.connect(self.radio_status1, SIGNAL("clicked()"), self.alterarStatus)
        self.connect(self.radio_status2, SIGNAL("clicked()"), self.alterarStatus)
        self.connect(self.radio_status3, SIGNAL("clicked()"), self.alterarStatus)
        self.connect(self.radio_status4, SIGNAL("clicked()"), self.alterarStatus)
        self.connect(self.botao_salvar, SIGNAL("clicked()"), self.salvar)
        self.connect(self.botao_limpar, SIGNAL("clicked()"), self.limpar_campos)
        self.connect(self.botao_cancelar, SIGNAL("clicked()"), self.close)

        self.resize(QSize(544,387).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)
        
        # se houver argumentos (usar no formulário de edição)
        if args:
            self.editar_form(*args)


    def languageChange(self):
        self.setCaption(self.__tr("Novo diploma/certificado"))
        self.comboBox_curso.clear()
        self.label_registro.setText(self.__trUtf8("Nº de registro"))
        self.label_tipo.setText(self.__tr("Tipo"))
        self.label_status.setText(self.__tr("Status"))
        self.radio_status1.setText(self.__tr("Processo montado encontra-se no Campus III"))
        self.radio_status2.setText(self.__tr("Processo enviado ao RCA/Arapiraca"))
        self.radio_status3.setText(self.__trUtf8("O Diploma já chegou ao Campus III"))
        self.radio_status4.setText(self.__tr("Diploma entregue ao aluno"))
        self.botao_salvar.setText(self.__tr("Salvar"))
        self.radio_diploma.setText(self.__tr("Diploma"))
        self.botao_limpar.setText(self.__tr("Limpar"))
        self.label_nome.setText(self.__tr("Nome"))
        self.label_data_saida.setText(self.__trUtf8("Data de saída"))
        self.label_data_registro.setText(self.__trUtf8("Data de registro"))
        self.label_curso.setText(self.__tr("Curso"))
        self.botao_cancelar.setText(self.__tr("Cancelar"))
        self.label_observacoes.setText(self.__trUtf8("Observações"))
        self.radio_certificado.setText(self.__trUtf8("Certificado de Pós-graduação"))

    def alterarTipoDocumento(self):
        self.disparador = self.sender()
        if self.disparador==self.radio_diploma:
            self.radio_diploma.setChecked(True)
            self.radio_certificado.setChecked(False)
            self.alterarListadeCursos(1)
        elif self.disparador==self.radio_certificado:
            self.radio_diploma.setChecked(False)
            self.radio_certificado.setChecked(True)
            self.alterarListadeCursos(2)
        
    def alterarListadeCursos(self, disparador):
        self.comboBox_curso.clear()
        if disparador==1:
            lista = LISTA_GRADUACAO
        elif disparador==2:
            lista = LISTA_POS_GRADUACAO
        for item in lista:
            self.comboBox_curso.insertItem(self.__trUtf8(item))

    def alterarStatus(self):
        self.disparador = self.sender()
        for item in self.radio_status1, self.radio_status2, self.radio_status3, self.radio_status4:
            if item == self.disparador:
                item.setChecked(True)
                self.spinbox_registro.setEnabled(True) if (item == self.radio_status3 or item == self.radio_status4) else self.spinbox_registro.setEnabled(False)
            else:
                item.setChecked(False)
        
    def limpar_campos(self):
        for item in self.radio_diploma, self.radio_certificado, self.radio_status1, self.radio_status2, self.radio_status3, self.radio_status4:
            item.setChecked(False)
        self.lineEdit_nome.setText("")
        self.textEdit_observacoes.setText("")
        self.comboBox_curso.clear()
        for item in self.dateEdit_data_registro, self.dateEdit_data_saida:
            pass
    
    def editar_form(self, *args):
        self.lineEdit_nome.setText(self.__trUtf8(args[0]['nome']))
        if args[0]['tipo']==1:
            self.radio_diploma.setChecked()
        elif args[0]['tipo']==2:
            self.radio_certificado.setChecked()
        #self.comboBox_curso.setCurrentItem("?????????????????????????????")
        #self.dateEdit_data_registro.setDate("????????????????????????????")
        #self.dateEdit_data_saida.setDate("???????????????????????????????")
        if args[0]['status']==1:
            self.radio_status1.setChecked()
        elif args[0]['status']==2:
            self.radio_status2.setChecked()
        elif args[0]['status']==3:
            self.radio_status3.setChecked()
        elif args[0]['status']==4:
            self.radio_status4.setChecked()
        self.textEdit_observacoes.setText(self.__trUtf8(args[0]['observacoes']))
        self.connect(self.botao_salvar, SIGNAL('clicked()'), self.update)
        
    def salvar(self):
        dict = {}
        
        registro_dao = RegistroDAO()
        
        dict['id'] = registro_dao.getNewID()
        
        dict['registro'] = self.spinbox_registro.value()
        
        if self.radio_diploma.isChecked():
            dict['tipo'] = 1
            dict['curso'] = LISTA_GRADUACAO[self.comboBox_curso.currentItem()]
        elif self.radio_certificado.isChecked():
            dict['tipo'] = 2
            dict['curso'] = LISTA_POS_GRADUACAO[self.comboBox_curso.currentItem()]
        else:
            return QMessageBox.warning(None, "Oops", u"Você esqueceu de marcar o tipo de registro (diploma ou certificado.")

        if len(self.lineEdit_nome.text()) != 0:
            dict['nome'] = str(self.lineEdit_nome.text())
        else:
            return QMessageBox.warning(None, "Oops", u"Você esqueceu de digitar o nome do aluno.")
        
        data_registro = self.dateEdit_data_registro.date()
        dict['data_registro'] = str(data_registro.year()) + '-' + str(data_registro.month()) + '-' + str(data_registro.day())
        data_saida = self.dateEdit_data_saida.date()
        dict['data_saida'] = str(data_saida.year()) + '-' + str(data_saida.month()) + '-' + str(data_saida.day())
        
        if self.radio_status1.isChecked() or self.radio_status2.isChecked() or self.radio_status3.isChecked() or self.radio_status4.isChecked():
            if self.radio_status1.isChecked():
                dict['status'] = 1
            elif self.radio_status2.isChecked():
                dict['status'] = 2
            elif self.radio_status3.isChecked():
                dict['status'] = 3
            else:
                dict['status'] = 4
        else:
            return QMessageBox.warning(None, "Oops", u"Você esqueceu de marcar o status da solicitação de registro de diploma.")
        
        dict['observacoes'] = str(self.textEdit_observacoes.text())
        
        if registro_dao.insert(dict) == True:
            QMessageBox.information(None, "Salvo", "Dados salvos com sucesso.")
            return self.close()
        
    def update(self):
        print "JanelaNovoRegistro.salvar(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("JanelaNovo",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("JanelaNovo",s,c,QApplication.UnicodeUTF8)
