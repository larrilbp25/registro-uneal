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

class SolicitacaoDAO:
    ''' métodos para inserção, seleção, modificação e deleção de
        itens da tabela Solicitacao
        
        REVER isso aqui, tá uma bosta!
    '''
    
    def __init__(self):
        self.create()
    
    def create(self):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            create = u'''create table Solicitacao 
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
            '''
            cursor.execute(create)
            banco.commit()
            return True
        except:
            pass
                
    def insert(self, objeto):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            insert = u'''insert into Solicitacao (id, nome, curso, data, certidao, declaracao, diploma, historico, outros, urgencia, observacoes)
                         values ( %d, "%s", "%s", "%s", %b, %b, %b, %b, %b, %b, "%s" );''' % (
                         objeto['id'], objeto['nome'], objeto['curso'], objeto['data'], objeto['certidao'], objeto['declaracao'],
                         objeto['diploma'], objeto['historico'], objeto['outros'], objeto['urgencia'], objeto['observacoes'],)
            cursor.execute(insert)
            banco.commit()
            return True
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", u"Erro de inserção no banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning
    
    def update(self, objeto):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            update = u'''update Solicitacao set ( "id"=%d, "nome"="%s", "curso"="%s", "data"="%s", "certidao"=%b, "declaracao"=%b, 
                        "diploma"=%b, "historico"=%b, "outros"=%b, "urgencia"=%b, "observacoes"="%s" ) where (registro = %d);''' % (
                        objeto['id'], objeto['nome'], objeto['curso'], objeto['data'], objeto['certidao'], objeto['declaracao'], 
                        objeto['diploma'], objeto['historico'], objeto['outros'], objeto['urgencia'], objeto['observacoes'],)
            cursor.execute(update)
            banco.commit()
            return True
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", "Erro de atualização no banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning
    
    def delete(self, objeto):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            delete = u'''delete from Solicitacao 
                         where ("registro" = %d);''' % objeto['id']
            cursor.execute(delete)
            banco.commit()
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", "Erro ao remover do banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning
        
    def select(self, objeto):
        try:
            banco = sqlite3.connect('banco.db')
            cursor = banco.cursor()
            delete = u'''select * from Solicitacao where ("registro" = %d);''' % objeto['id']
            cursor.execute(delete)
            return cursos.fetchall()
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", "Erro da consulta no banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning

    def selectAll(self):
        try:
            banco = sqlite.connect('banco.db')
            cursor = banco.cursor()
            selectAll = u'''select * from Solicitacao;'''
            cursor.execute(selectAll)
            return cursor.fetchall()
        except Exception, e:
            warning = QMessageBox.warning(None, "Database error", "Erro da consulta no banco de dados. O erro foi:\n\n%s" % e, QMessageBox.Ok)
            return ~warning

    def getNewID(self):
        return len(self.selectAll()) + 1
