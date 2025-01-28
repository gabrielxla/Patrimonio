from PyQt5.QtWidgets import QLabel, QBoxLayout, QVBoxLayout, QHBoxLayout,QApplication, QLineEdit, QPushButton, QWidget
import sys

class atualizacao (QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(350,350,1000,300)
        
        self.setWindowTitle("Atualização")

        ##LAYOUT VERTICAL!
        self.layout_v = QVBoxLayout ()

        self.label_equipamento = QLabel ("ID:")
        self.label_equipamento.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_equipamento = QLineEdit()
        self.edit_equipamento.setStyleSheet("QLineEdit{font-size:12pt}")

        self.label_ID = QLabel ("Numero de Série: ")
        self.label_ID.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_ID = QLineEdit ()
        self.edit_ID.setStyleSheet("QLineEdit{font-size:12pt}")

        self.label_nome = QLabel ("Data da ultima verificação")
        self.label_nome.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_nome = QLineEdit ()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")

        self.label_Local = QLabel ("Observação")
        self.label_Local.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_local = QLineEdit()
        self.edit_local.setStyleSheet("QLineEdit{font-size:12pt}")

       
        ##BUTAO
        self.button = QPushButton("Registrar")
        self.button.setStyleSheet("QPushButton{Background-color:red;color:white;font-size:12pt;font-weight:bold}")

        self.button.clicked.connect(self.registrar)

        #Adição do layout vertical
        self.layout_v.addWidget(self.label_equipamento)
        self.layout_v.addWidget(self.edit_equipamento)
        
        self.layout_v.addWidget(self.label_ID)
        self.layout_v.addWidget(self.edit_ID)

        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)
        
        self.layout_v.addWidget(self.label_Local)
        self.layout_v.addWidget(self.edit_local)

        self.layout_v.addWidget(self.button)

        ##!!
        self.setLayout(self.layout_v)
    
    def registrar(self):
        arquivo = open ("localizacao.txt","+a", encoding="utf8")
        arquivo.write(f"ID: {self.edit_equipamento.text()}\n")
        arquivo.write(f"Número de Série: {self.edit_ID.text()}\n")
        arquivo.write(f"Data da Ultima verificação: {self.edit_nome.text()}\n")
        arquivo.write(f"Observação: {self.edit_local.text()}\n")
       
        arquivo.write("_______________________________\n")
        arquivo.close ()

#app = QApplication(sys.argv)

#tela = atualizacao ()
#tela.show()
#app.exec()