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
            print 'a tabela ja foi criada'
                
    def insert(self, objeto):
        try:
            print "objeto: ", objeto
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            insert = u'''insert into Registro values ( %d, %d, %s, %s, %s, %s, %d, %s );''' % objeto['registro'], objeto['tipo'], objeto['nome'], objeto['curso'], objeto['data_registro'], objeto['data_saida'], objeto['status'], objeto['observacoes']
            print "vou executar o Insert..."
            cursor.execute(insert)
            print "insert executado, vou commitar"
            banco.commit()
            print "commit!"
            return True
        except Exception, e:
            print e
            return False
    
    def update(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            update = u'''update Registro set ( "tipo"=%d, "nome"=%s, "curso"=%s, "data_registro"=%s, "status"=%d, "observacoes"=%s ) where (registro = %d);''' % (
                  object['tipo'], object['nome'], object['curso'], object['data_registro'], object['data_saida'], object['status'], object['observacoes'], object['registro'])
            cursor.execute(update)
            banco.commit()
            return True
        except:
            return False
    
    def delete(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            delete = u'''delete from Registro where ("registro" = %d);''' % object['registro']
            cursor.execute(delete)
            banco.commit()
        except:
            return False
        
    def select(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            select = u'''select * from Registro where ("registro" = %d);''' % object['registro']
            cursor.execute(select)
            banco.commit()
            return cursor
        except:
            return False
        
    def selectAll(self):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            selectAll = u"select * from Registro"
            cursor.execute(selectAll)
            resultados = cursor.fetchall()
            return resultados
        except:
            return False
