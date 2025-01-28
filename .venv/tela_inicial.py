from PyQt5.QtWidgets import QLabel, QBoxLayout, QVBoxLayout, QHBoxLayout,QApplication, QLineEdit, QPushButton, QWidget
import sys
from Patrimonio import Patrimonio
from localizacao import localizacao
from atualizacao import atualizacao
class telainicial (QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerenciar")
        self.setGeometry(300,200,200,150)
        self.layout_v = QVBoxLayout()

        self.label_titulo = QLabel ("Clique para abrir a janela")
        self.button = QPushButton ("Abrir cadastro")
        self.button2 = QPushButton("Abrir localização")
        self.button3 = QPushButton("Abrir Atualização")

        self.layout_v.addWidget(self.label_titulo)
        self.layout_v.addWidget(self.button)
        self.layout_v.addWidget(self.button2)
        self.layout_v.addWidget(self.button3)

        self.button.clicked.connect(self.abrir_cadastro)
        self.button2.clicked.connect(self.abrir_localizacao)
        self.button3.clicked.connect(self.abrir_atualizacao)

        self.setLayout(self.layout_v)
    def abrir_localizacao(self):
        self.loc = localizacao()
        self.loc.show()

    def abrir_cadastro(self):
        self.pat = Patrimonio()
        self.pat.show()
    def abrir_atualizacao(self):
        self.atua = atualizacao()
        self.atua.show()
        
app = QApplication(sys.argv)
tela = telainicial ()
tela.show ()
app.exec()
