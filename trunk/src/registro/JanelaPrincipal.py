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
from imagens import *
from JanelaNovoRegistro import JanelaNovoRegistro
from JanelaNovaSolicitacao import JanelaNovaSolicitacao
from JanelaSobre import JanelaSobre
from JanelaCadastroUsuario import JanelaCadastroUsuario

class JanelaPrincipal(QMainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        QMainWindow.__init__(self,parent,name,fl)
        self.statusBar()

        self.arquivoNovoIcone = QPixmap()
        self.arquivoNovoIcone.loadFromData(icone_novo,"PNG")
        self.image4 = QPixmap()
        self.image4.loadFromData(icone_desfazer,"PNG")
        self.image5 = QPixmap()
        self.image5.loadFromData(icone_refazer,"PNG")
        self.image6 = QPixmap()
        self.image6.loadFromData(icone_recortar,"PNG")
        self.image7 = QPixmap()
        self.image7.loadFromData(icone_copiar,"PNG")
        self.image8 = QPixmap()
        self.image8.loadFromData(icone_colar,"PNG")
        self.buscar_icone = QPixmap()
        self.buscar_icone.loadFromData(icone_buscar,"PNG")
        if not name:
            self.setName("JanelaPrincipal")



        self.arquivoNovoAction = QAction(self,"arquivoNovoAction")
        self.arquivoNovoAction.setIconSet(QIconSet(self.arquivoNovoIcone))
        self.arquivoNovoRegistroAction = QAction(self,"arquivoNovoRegistroAction")
        self.arquivoNovoSolicitacaoAction = QAction(self,"arquivoNovoSolicitacaoAction")
        self.arquivoNovoUsuarioAction = QAction(self, "arquivoNovaContaAction")
        self.arquivoSairAction = QAction(self,"arquivoSairAction")
        self.editarDesfazerAction = QAction(self,"editarDesfazerAction")
        self.editarDesfazerAction.setIconSet(QIconSet(self.image4))
        self.editarRefazerAction = QAction(self,"editarRefazerAction")
        self.editarRefazerAction.setIconSet(QIconSet(self.image5))
        self.editarRecortarAction = QAction(self,"editarRecortarAction")
        self.editarRecortarAction.setIconSet(QIconSet(self.image6))
        self.editarCopiarAction = QAction(self,"editarCopiarAction")
        self.editarCopiarAction.setIconSet(QIconSet(self.image7))
        self.editarColarAction = QAction(self,"editarColarAction")
        self.editarColarAction.setIconSet(QIconSet(self.image8))
        self.ajudaSobreAction = QAction(self,"ajudaSobreAction")
        self.buscaAction = QAction(self,"buscaDiplomaAction")
        self.buscaAction.setIconSet(QIconSet(self.buscar_icone))
        self.buscaDiplomaAction = QAction(self,"buscaDiplomaAction")
        self.buscaCertificadoAction = QAction(self,"buscaCertificado_de_Ps_GraduaoAction")




        self.MenuBar = QMenuBar(self,"MenuBar")

        self.Arquivo = QPopupMenu(self)
        self.arquivoNovo = QPopupMenu(self)
        self.Arquivo.setAccel(QString.null,self.Arquivo.insertItem(self.arquivoNovoAction.iconSet(),self.__tr("Novo registro..."),self.arquivoNovo))
        self.arquivoNovoRegistroAction.addTo(self.arquivoNovo)
        self.arquivoNovoSolicitacaoAction.addTo(self.arquivoNovo)
        self.arquivoNovoUsuarioAction.addTo(self.Arquivo)
        self.Arquivo.insertSeparator()
        self.arquivoSairAction.addTo(self.Arquivo)
        self.MenuBar.insertItem(QString(""),self.Arquivo,1)

        self.Editar = QPopupMenu(self)
        self.editarDesfazerAction.addTo(self.Editar)
        self.editarRefazerAction.addTo(self.Editar)
        self.Editar.insertSeparator()
        self.editarRecortarAction.addTo(self.Editar)
        self.editarCopiarAction.addTo(self.Editar)
        self.editarColarAction.addTo(self.Editar)
        self.Editar.insertSeparator()
        self.MenuBar.insertItem(QString(""),self.Editar,2)

        self.Registros = QPopupMenu(self)
        self.buscar = QPopupMenu(self)
        self.Registros.setAccel(QString.null,self.Registros.insertItem(self.buscaAction.iconSet(),self.__tr("Buscar"),self.buscar))
        self.buscaDiplomaAction.addTo(self.buscar)
        self.buscaCertificadoAction.addTo(self.buscar)
        self.MenuBar.insertItem(QString(""),self.Registros,3)

        self.Ajuda = QPopupMenu(self)
        self.ajudaSobreAction.addTo(self.Ajuda)
        self.MenuBar.insertItem(QString(""),self.Ajuda,4)


        self.languageChange()

        self.resize(QSize(558,445).expandedTo(self.minimumSizeHint()))
        self.clearWState(Qt.WState_Polished)

        self.connect(self.arquivoNovoRegistroAction,SIGNAL("activated()"),self.arquivoNovoRegistro)
        self.connect(self.arquivoNovoSolicitacaoAction,SIGNAL("activated()"),self.arquivoNovoSolicitacao)
        self.connect(self.arquivoNovoUsuarioAction,SIGNAL("activated()"),self.arquivoNovoUsuario)
        self.connect(self.arquivoSairAction,SIGNAL("activated()"),self.close)
        self.connect(self.editarDesfazerAction,SIGNAL("activated()"),self.editarDesfazer)
        self.connect(self.editarRefazerAction,SIGNAL("activated()"),self.editarRefazer)
        self.connect(self.editarRecortarAction,SIGNAL("activated()"),self.editarRecortar)
        self.connect(self.editarCopiarAction,SIGNAL("activated()"),self.editarCopiar)
        self.connect(self.editarColarAction,SIGNAL("activated()"),self.editarColar)
        self.connect(self.ajudaSobreAction,SIGNAL("activated()"),self.ajudaSobre)
        self.connect(self.buscaDiplomaAction,SIGNAL("activated()"),self.buscarDiploma)
        self.connect(self.buscaCertificadoAction,SIGNAL("activated()"),self.buscarCertificado)


    def languageChange(self):
        self.setCaption(self.__trUtf8("Registro Acadêmico - Campus III"))
        self.arquivoNovoAction.setText(self.__tr("Novo"))
        self.arquivoNovoAction.setMenuText(self.__tr("Novo"))
        self.arquivoNovoRegistroAction.setText(self.__tr("Registro de diploma ou certificado"))
        self.arquivoNovoRegistroAction.setMenuText(self.__tr("Registro de diploma ou certificado"))
        self.arquivoNovoSolicitacaoAction.setText(self.__trUtf8("Solicitação"))
        self.arquivoNovoSolicitacaoAction.setMenuText(self.__trUtf8("Solicitação"))
        self.arquivoNovoUsuarioAction.setText(self.__trUtf8("Nova usuário"))
        self.arquivoNovoUsuarioAction.setMenuText(self.__trUtf8("Novo usuário"))
        self.arquivoSairAction.setText(self.__tr("Sair"))
        self.arquivoSairAction.setMenuText(self.__tr("Sair"))
        self.arquivoSairAction.setAccel(QString.null)
        self.editarDesfazerAction.setText(self.__tr("Desfazer"))
        self.editarDesfazerAction.setMenuText(self.__tr("Desfazer"))
        self.editarDesfazerAction.setAccel(self.__tr("Ctrl+Z"))
        self.editarRefazerAction.setText(self.__tr("Refazer"))
        self.editarRefazerAction.setMenuText(self.__tr("Refazer"))
        self.editarRefazerAction.setAccel(self.__tr("Ctrl+Y"))
        self.editarRecortarAction.setText(self.__tr("Recortar"))
        self.editarRecortarAction.setMenuText(self.__tr("Recortar"))
        self.editarRecortarAction.setAccel(self.__tr("Ctrl+X"))
        self.editarCopiarAction.setText(self.__tr("Copiar"))
        self.editarCopiarAction.setMenuText(self.__tr("Copiar"))
        self.editarCopiarAction.setAccel(self.__tr("Ctrl+C"))
        self.editarColarAction.setText(self.__tr("Colar"))
        self.editarColarAction.setMenuText(self.__tr("Colar"))
        self.editarColarAction.setAccel(self.__tr("Ctrl+V"))
        self.ajudaSobreAction.setText(self.__tr("Sobre"))
        self.ajudaSobreAction.setMenuText(self.__tr("Sobre"))
        self.buscaAction.setText(self.__tr("Buscar"))
        self.buscaAction.setMenuText(self.__tr("Buscar"))
        self.buscaDiplomaAction.setText(self.__tr("Diploma"))
        self.buscaDiplomaAction.setMenuText(self.__tr("Diploma"))
        self.buscaCertificadoAction.setText(self.__trUtf8("Certificado de Pós-Graduação"))
        self.buscaCertificadoAction.setMenuText(self.__trUtf8("Certificado de Pós-Graduação"))
        if self.MenuBar.findItem(1):
            self.MenuBar.findItem(1).setText(self.__tr("Arquivo"))
        if self.MenuBar.findItem(2):
            self.MenuBar.findItem(2).setText(self.__tr("Editar"))
        self.Registros.changeItem(self.Registros.idAt(0),self.__tr("Buscar"))
        if self.MenuBar.findItem(3):
            self.MenuBar.findItem(3).setText(self.__tr("Registros"))
        if self.MenuBar.findItem(4):
            self.MenuBar.findItem(4).setText(self.__tr("Ajuda"))


    def arquivoNovoRegistro(self):
        self.novo = JanelaNovoRegistro()
        self.novo.show()
        
    def arquivoNovoSolicitacao(self):
        self.novo = JanelaNovaSolicitacao()
        self.novo.show()

    def arquivoNovoUsuario(self):
        self.novo = JanelaCadastroUsuario()
        self.novo.show()

    def editarDesfazer(self):
        print "JanelaPrincipal.editarDesfazer(): Not implemented yet"

    def editarRefazer(self):
        print "JanelaPrincipal.editarRefazer(): Not implemented yet"

    def editarRecortar(self):
        print "JanelaPrincipal.editarRecortar(): Not implemented yet"

    def editarCopiar(self):
        print "JanelaPrincipal.editarCopiar(): Not implemented yet"

    def editarColar(self):
        print "JanelaPrincipal.editarColar(): Not implemented yet"

    def ajudaSobre(self):
        self.sobre = JanelaSobre()
        self.sobre.show()

    def buscarDiploma(self):
        print "JanelaPrincipal.buscarDiploma(): Not implemented yet"

    def buscarCertificado(self):
        print "JanelaPrincipal.buscarCertificado(): Not implemented yet"

    def __tr(self,s,c = None):
        return qApp.translate("JanelaPrincipal",s,c)

    def __trUtf8(self,s,c = None):
        return qApp.translate("JanelaPrincipal",s,c,QApplication.UnicodeUTF8)