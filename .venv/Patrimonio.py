from PyQt5.QtWidgets import QLabel, QBoxLayout, QVBoxLayout, QHBoxLayout,QApplication, QLineEdit, QPushButton, QWidget, QMessageBox
import sys

class Patrimonio (QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(350,350,1000,300)
        
        self.setWindowTitle("Patrimonio Material")

        ##LAYOUT VERTICAL!
        self.layout_v = QVBoxLayout ()

        self.label_equipamento = QLabel ("Qual é o equipamento?:")
        self.label_equipamento.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_equipamento = QLineEdit()
        self.edit_equipamento.setStyleSheet("QLineEdit{font-size:12pt}")

        self.label_ID = QLabel ("Identificador ou ID: ")
        self.label_ID.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_ID = QLineEdit ()
        self.edit_ID.setStyleSheet("QLineEdit{font-size:12pt}")

        self.label_nome = QLabel ("Nome ou Marca do equipamento")
        self.label_nome.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_nome = QLineEdit ()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")

        self.label_Local = QLabel ("Localização")
        self.label_Local.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_local = QLineEdit()
        self.edit_local.setStyleSheet("QLineEdit{font-size:12pt}")

        self.label_Aquisicao = QLabel ("Quando foi adquirido")
        self.label_Aquisicao.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_aquisicao = QLineEdit ()
        self.edit_aquisicao.setStyleSheet("QLineEdit{font-size:12pt}")

        self.label_fabricacao = QLabel ("Quando foi fabricado:")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_fabricacao = QLineEdit()
        self.edit_fabricacao.setStyleSheet("QLineEdit{font-size:12pt}")
        
        self.label_descricao = QLabel("Descrição")
        self.label_descricao.setStyleSheet("QLabel{font-size:18pt}")

        self.edit_descricao = QLineEdit ()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:25pt}")



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

        self.layout_v.addWidget(self.label_fabricacao)
        self.layout_v.addWidget(self.edit_fabricacao)
        
        self.layout_v.addWidget(self.label_Aquisicao)
        self.layout_v.addWidget(self.edit_aquisicao)

        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        self.layout_v.addWidget(self.button)

        ##!!
        self.setLayout(self.layout_v)
    
    def registrar(self):
        if (self.edit_ID.text()=="" or self.edit_nome.text()=="" or self.edit_local.text()=="" or self.edit_descricao.text()==""):QMessageBox.critical(self,"ERRO","PREENCHA TUDO")
        else:
            arquivo = open ("Patrimonio.csv","+a", encoding="utf8")
            arquivo.write(f"{self.edit_equipamento.text()};")
            arquivo.write(f"{self.edit_ID.text()};")
            arquivo.write(f"{self.edit_nome.text()};")
            arquivo.write(f"{self.edit_local.text()};")
            arquivo.write(f"{self.edit_fabricacao.text()};")
            arquivo.write(f"{self.edit_aquisicao.text()};")
            
            arquivo.write(f"{self.edit_descricao.text()};\n")
        
            
            arquivo.close ()
            QMessageBox.information(self,"SALVEEE","TA SALVO RLX")
#app = QApplication(sys.argv)

#tela = Patrimonio ()
#tela.show()
#app.exec()