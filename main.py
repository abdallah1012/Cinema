# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:35:13 2020

@author: ojaro
"""

import sys

from PyQt5.QtWidgets import QApplication
from WelcomeWidget import WelcomeWidget


def run():
    app = QApplication(sys.argv)
    welcome_widget = WelcomeWidget()
    welcome_widget.show()
    sys.exit(app.exec_())
   
	
if __name__ == '__main__':
   run()