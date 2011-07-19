#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

from qt import QApplication
from JanelaPrincipal import JanelaPrincipal

app = QApplication(sys.argv)
a = JanelaPrincipal()
a.show()
app.exec_loop()