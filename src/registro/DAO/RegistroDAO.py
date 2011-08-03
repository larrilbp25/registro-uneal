# -*- coding:utf-8 -*-

import sqlite
from qt import QMessageBox

class RegistroDAO:
    
    def __init__(self):
        self.create()
    
    def create(self):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            create = u'''create table Registro 
                    ( id INTEGER,
                      registro INTEGER,
                      tipo INTEGER,
                      nome VARCHAR (100),
                      curso VARCHAR (50),
                      data_registro VARCHAR (10),
                      data_saida VARCHAR (10),
                      status INTEGER,
                      observacoes VARCHAR (1000),
                      PRIMARY KEY (id)
                    );
            '''
            cursor.execute(create)
            banco.commit()
            return True
        except Exception, e:
            return e
                
    def insert(self, objeto):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            insert = u'''insert into Registro (id, registro, tipo, nome, curso, data_registro, data_saida, status, observacoes) values (%d,%d,%d,"%s","%s","%s","%s",%d,"%s");''' % (objeto['id'], objeto['registro'], objeto['tipo'], objeto['nome'], objeto['curso'], objeto['data_registro'], objeto['data_saida'], objeto['status'], objeto['observacoes'],)
            cursor.execute(insert)
            banco.commit()
            return True
        except Exception, e:
            return e
    
    def update(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            update = u'''update Registro set ( "tipo"=%d, "nome"=%s, "curso"=%s, "data_registro"=%s, "status"=%d, "observacoes"=%s ) where (registro = %d);''' % (
                  object['tipo'], object['nome'], object['curso'], object['data_registro'], object['data_saida'], object['status'], object['observacoes'], object['registro'])
            cursor.execute(update)
            banco.commit()
            return True
        except Exception, e:
            return e
    
    def delete(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            delete = u'''delete from Registro where ("registro" = %d);''' % object['registro']
            cursor.execute(delete)
            banco.commit()
        except Exception, e:
            return e
        
    def select(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            select = u'''select * from Registro where ("registro" = %d);''' % object['registro']
            cursor.execute(select)
            banco.commit()
            return cursor
        except Exception, e:
            return e
        
    def selectAll(self):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            selectAll = u"select * from Registro"
            cursor.execute(selectAll)
            resultados = cursor.fetchall()
            return resultados
        except Exception, e:
            return e
