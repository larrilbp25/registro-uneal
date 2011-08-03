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

class UserDAO:
    ''' métodos para inserção, seleção, modificação e deleção de
        itens da tabela User
        
        REVER isso aqui, tá uma bosta!
    '''
    
    def __init__(self):
        self.create()
    
    def create(self):
        try:
            banco = sqlite3.connect('database/banco.db')
            cursor = banco.cursor()
            create = '''create table User 
                    ( cpf INTEGER NOT NULL PRIMARY KEY,
                      nome VARCHAR (100),
                      email VARCHAR (50),
                      login VARCHAR (30),
                      senha VARCHAR (30),
                      autenticacao BOOLEAN,
                      admin BOOLEAN,
                    );
            '''
            cursor.execute(create)
            banco.commit()
            return True
        except:
            warning = QMessageBox.warning(None, "Database error", "Erro na criação da tabela Registro, talvez ela já tenha sido criada.", QMessageBox.Yes)
            return warning
                
    def insert(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            insert = '''insert into User values ( %d, %s, %s, %s, %s, %b, %b );''' % (
                  object['cpf'], object['nome'], object['email'], object['login'], object['senha'], object['autenticacao'], object['admin'])
            cursor.execute(insert)
            banco.commit()
            return True
        except:
            return False
    
    def update(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            update = '''update User set ( "nome"=%s, "email"=%s, "login"=%s, "senha"=%s, "autenticacao"=%b, "admin"=%b ) where (cpf = %d);''' % (
                  object['cpf'], object['nome'], object['email'], object['login'], object['senha'], object['autenticacao'], object['admin'])
            cursor.execute(update)
            banco.commit()
            return True
        except:
            return False
    
    def delete(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            delete = '''delete from User where ("cpf" = %d);''' % object['cpf']
            cursor.execute(delete)
            banco.commit()
        except:
            return False
        
    def select(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            delete = '''select * from User where ("cpf" = %d)''' % object['cpf']
            cursor.execute(delete)
            banco.commit()
            return True
        except:
            return False
