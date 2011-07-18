# -*- coding:utf-8 -*-

import sqlite3
from qt import QMessageBox

class RegistroDAO:
    
    def __init__(self):
        self.create()
    
    def create(self):
        try:
            banco = sqlite3.connect('database/banco.db')
            cursor = banco.cursor()
            create = '''create table Registro 
                    ( registro INTEGER,
                      tipo INTEGER,
                      nome VARCHAR (100),
                      curso VARCHAR (50),
                      data_registro VARCHAR (10),
                      data_saida VARCHAR (10),
                      status INTEGER,
                      observacoes VARCHAR (1000)
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
            insert = '''insert into Registro values ( %d, %s, %s, %s, %s, %d, %s );''' % (
                  object['tipo'], object['nome'], object['curso'], object['data_registro'], object['data_saida'], object['status'], object['observacoes'])
            cursor.execute(insert)
            banco.commit()
            return True
        except:
            return False
    
    def update(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            update = '''update Registro set ( "tipo"=%d, "nome"=%s, "curso"=%s, "data_registro"=%s, "status"=%d, "observacoes"=%s ) where (registro = %d);''' % (
                  object['tipo'], object['nome'], object['curso'], object['data_registro'], object['data_saida'], object['status'], object['observacoes'], object['registro'])
            cursor.execute(update)
            banco.commit()
            return True
        except:
            return False
    
    def delete(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            delete = '''delete from Registro where ("registro" = %d);''' % object['registro']
            cursor.execute(delete)
            banco.commit()
        except:
            return False
        
    def select(self, object):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            delete = '''select * from Registro where ("registro" = %d)''' % object['registro']
            cursor.execute(delete)
            banco.commit()
            return True
        except:
            return False
