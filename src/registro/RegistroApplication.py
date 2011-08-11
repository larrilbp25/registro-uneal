#!/usr/bin/python
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

from utils import erroGtk
    
try:
    from qt import QApplication
except:
    mensagem_erro = u'''Um erro de importação ocorreu, é provável que você não tenha o Qt ou o PyQt instalado. Para instalar, execute o seguinte comando:
    
    sudo apt-get install qt3-dev-tools pyqt-tools python-qt3'''
    erroGtk(mensagem_erro)
try:
    import sqlite
except:
    mensagem_erro = u'''Um erro de importação ocorreu, é provável que você não tenha o sqlite instalado. Para instalar, execute o seguinte comando:
    
    sudo apt-get install sqlite'''
    erroGtk(mensagem_erro)
    
import sys
from JanelaPrincipal import JanelaPrincipal

if __name__ == "__main__":
    app = QApplication(sys.argv)
    a = JanelaPrincipal()
    a.show()
    app.exec_loop()