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
from CreateDB import CreateDB

class RegistroDAO:
    ''' métodos para inserção, seleção, modificação e deleção de
        itens da tabela Registro
    '''
    
    def __init__(self):
        create = CreateDB()
    
#    def create(self):
#        try:
#            banco = sqlite.connect('banco.db')
#            cursor = banco.cursor()
#            create = u'''create table Registro 
#                    ( id INTEGER,
#                      registro INTEGER,
#                      tipo INTEGER,
#                      nome VARCHAR (100),
#                      curso VARCHAR (50),
#                      data_registro DATE,
#                      data_saida DATE,
#                      status INTEGER,
#                      observacoes VARCHAR (1000),
#                      PRIMARY KEY (id)
#                    );
#            '''
#            cursor.execute(create)
#            banco.commit()
#            return True
#        except:
#            pass
                
    def insert(self, objeto):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            insert = u'''insert into Registro (id, registro, tipo, nome, curso, data_registro, data_saida, status, observacoes) 
                         values (%d,%d,%d,"%s","%s","%s","%s",%d,"%s");''' % ( objeto['id'], objeto['registro'], objeto['tipo'], 
                                                                               objeto['nome'], objeto['curso'], objeto['data_registro'], 
                                                                               objeto['data_saida'], objeto['status'], objeto['observacoes'],)
            cursor.execute(insert)
            banco.commit()
            return True
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", u"Erro de inserção no banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning
    
    def update(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            update = u'''update Registro 
                         set ( "tipo"=%d, "nome"=%s, "curso"=%s, "data_registro"=%s, "status"=%d, "observacoes"=%s ) where (registro = %d);''' % (
                         object['tipo'], object['nome'], object['curso'], object['data_registro'], object['data_saida'], object['status'], 
                         object['observacoes'], object['registro'])
            cursor.execute(update)
            banco.commit()
            return True
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", u"Erro na atualização do banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning
    
    def delete(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            delete = u'''delete from Registro where ("registro" = %d);''' % object['registro']
            cursor.execute(delete)
            banco.commit()
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", u"Erro de deleção no banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning
        
    def select(self, object):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            select = u'''select * from Registro where ("registro" = %d);''' % object['registro']
            cursor.execute(select)
            return cursor.fetchall()
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", u"Erro de seleção no banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning
        
    def selectAll(self):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            selectAll = u"select * from Registro;"
            cursor.execute(selectAll)
            return cursor.fetchall()
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", u"Erro de seleção no banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning

    def getNewID(self):
        return len(self.selectAll()) + 1
