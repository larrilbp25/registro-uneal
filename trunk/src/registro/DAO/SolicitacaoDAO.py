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

import sqlite3
from qt import QMessageBox

class SolicitacaoDAO:
    ''' métodos para inserção, seleção, modificação e deleção de
        itens da tabela Solicitacao
        
        REVER isso aqui, tá uma bosta!
    '''
    
    def __init__(self):
        self.create()
    
    def create(self):
        try:
            banco = sqlite3.connect('database/banco.db')
            cursor = banco.cursor()
            create = '''create table Solicitacao 
                    ( id INTEGER PRIMARY KEY,
                      nome VARCHAR (100),
                      curso VARCHAR (50),
                      data VARCHAR (10),
                      certidao BOOLEAN,
                      declaracao BOOLEAN,
                      diploma BOOLEAN,
                      historico BOOLEAN,
                      outros BOOLEAN,
                      urgencia BOOLEAN,
                      observacoes VARCHAR (1000)
                    );
            '''
            cursor.execute(create)
            banco.commit()
            return True
        except:
            warning = QMessageBox.warning(None, "Database error", "Erro na criação da tabela Solicitação, talvez ela já tenha sido criada.", QMessageBox.Yes)
            return warning
                
    def insert(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            insert = '''insert into Solicitacao values ( %d, %s, %s, %s, %b, %b, %b, %b, %b, %b, %s );''' % (
                 object['id'], object['nome'], object['curso'], object['data'], object['certidao'], object['declaracao'],
                 object['diploma'], object['historico'], object['outros'], object['urgencia'], object['observacoes'])
            cursor.execute(insert)
            banco.commit()
            return True
        except:
            warning = QMessageBox.warning(None, "Database error", "Erro de inserção no banco de dados.", QMessageBox.Yes)
            return warning
    
    def update(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            update = '''update Solicitacao set ( "id"=%d, "nome"=%s, "curso"=%s, "data"=%s, "certidao"=%b, "declaracao"=%b, 
                        "diploma"=%b, "historico"=%b, "outros"=%b, "urgencia"=%b, "observacoes"=%s ) where (registro = %d);''' % (
                    object['id'], object['nome'], object['curso'], object['data'], object['certidao'], object['declaracao'], 
                    object['diploma'], object['historico'], object['outros'], object['urgencia'], object['observacoes'])
            cursor.execute(update)
            banco.commit()
            return True
        except:
            warning = QMessageBox.warning(None, "Database error", "Erro de atualização no banco de dados.", QMessageBox.Yes)
            return warning
    
    def delete(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            delete = '''delete from Solicitacao where ("registro" = %d);''' % object['id']
            cursor.execute(delete)
            banco.commit()
        except:
            warning = QMessageBox.warning(None, "Database error", "Erro ao remover do banco de dados.", QMessageBox.Yes)
            return warning
        
    def select(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            delete = '''select * from Solicitacao where ("registro" = %d)''' % object['id']
            cursor.execute(delete)
            banco.commit()
            return True
        except:
            warning = QMessageBox.warning(None, "Database error", "Erro da consulta no banco de dados.", QMessageBox.Yes)
            return warning
