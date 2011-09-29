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

import sqlite
from qt import QMessageBox

class CreateDB:
    ''' métodos para criação das tabelas do banco ("banco.db")
        
        @todo: REVER isso aqui!
    '''
    
    def __init__(self):
        self.createDB()
        
    def createDB(self):
        try:
            self.banco = sqlite.connect('banco.db')
            self.cursor = banco.cursor()
            self.tabelas = u'''
                create table Solicitacao 
                    ( id INTEGER PRIMARY KEY,
                      nome VARCHAR (100),
                      curso VARCHAR (50),
                      data DATE,
                      certidao BOOLEAN,
                      declaracao BOOLEAN,
                      diploma BOOLEAN,
                      historico BOOLEAN,
                      outros BOOLEAN,
                      urgencia BOOLEAN,
                      observacoes VARCHAR (1000)
                    );
                    
                create table User 
                    ( cpf INTEGER NOT NULL PRIMARY KEY,
                      nome VARCHAR (100),
                      email VARCHAR (50),
                      login VARCHAR (30),
                      senha VARCHAR (30),
                      autenticacao BOOLEAN,
                      admin BOOLEAN
                    );
                    
                create table Registro 
                    ( id INTEGER,
                      registro INTEGER,
                      tipo INTEGER,
                      nome VARCHAR (100),
                      curso VARCHAR (50),
                      data_registro DATE,
                      data_saida DATE,
                      status INTEGER,
                      observacoes VARCHAR (1000),
                      PRIMARY KEY (id)
                    );
            '''
            self.cursor.execute(self.tabelas)
            
            self.banco.commit()
            
            return True
        except:
            return False
        