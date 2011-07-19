# -*- coding:utf-8 -*-

import sqlite3
from qt import QMessageBox

class SolicitacaoDAO:
    
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
