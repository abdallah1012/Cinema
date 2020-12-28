# -*- coding: utf-8 -*-


import sys

from PyQt5.QtWidgets import QApplication
from WelcomeWidget import WelcomeWidget

#Initiator
def run():
    app = QApplication(sys.argv)
    welcome_widget = WelcomeWidget()
    welcome_widget.show()
    sys.exit(app.exec_())
   
	
if __name__ == '__main__':
   run()