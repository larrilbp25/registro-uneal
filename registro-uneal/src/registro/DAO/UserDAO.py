# -*- coding:utf-8 -*-

import sqlite3
from qt import QMessageBox

class UserDAO:
    
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
