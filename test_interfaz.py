from datetime import datetime

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import mariadb


class UiFrame(object):
    def setupUi(self, Frame):
        if Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(900, 600)
        self.stackedWidget = QStackedWidget(Frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QRect(-1, 0, 900, 600))
        self.pageLog = QWidget()
        self.pageLog.setObjectName(u"pageLog")
        self.pageLog.setEnabled(True)
        self.buttonLog_2 = QPushButton(self.pageLog)
        self.buttonLog_2.setObjectName(u"buttonLog_2")
        self.buttonLog_2.setGeometry(QRect(540, 350, 183, 54))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.buttonLog_2.setFont(font)
        self.buttonLog_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonLog_2.setStyleSheet(u"QPushButton{\n"
                                       "border-radius: 25px;\n"
                                       "border: 2px solid  rgb(25, 225, 175);\n"
                                       "padding: 20px;\n"
                                       " width: 10px;\n"
                                       " height: 10px;\n"
                                       "}\n"
                                       "\n"
                                       ".QPushButton:hover {\n"
                                       "    background-color: rgb(25, 225, 175);\n"
                                       "    color: black;\n"
                                       "}")
        self.buttonLog_2.setAutoDefault(False)
        self.buttonLog_2.setFlat(False)
        self.passText_2 = QLineEdit(self.pageLog)
        self.passText_2.setObjectName(u"passText_2")
        self.passText_2.setGeometry(QRect(540, 310, 183, 25))
        font1 = QFont()
        font1.setPointSize(12)
        self.passText_2.setFont(font1)
        self.passText_2.setStyleSheet(u"QLineEdit{\n"
                                      "border: 2px solid  rgb(25, 225, 175);\n"
                                      "border-radius: 4px;\n"
                                      "}")
        self.passText_2.setEchoMode(QLineEdit.Password)
        self.label_6 = QLabel(self.pageLog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(540, 290, 183, 16))
        self.label_6.setFont(font)
        self.label_7 = QLabel(self.pageLog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(540, 240, 183, 16))
        self.label_7.setFont(font)
        self.userText_2 = QLineEdit(self.pageLog)
        self.userText_2.setObjectName(u"userText_2")
        self.userText_2.setGeometry(QRect(540, 260, 183, 25))
        self.userText_2.setFont(font1)
        self.userText_2.setStyleSheet(u"QLineEdit{\n"
                                      "border: 2px solid rgb(25, 225, 175);\n"
                                      "border-radius: 4px;\n"
                                      "}")
        self.label_8 = QLabel(self.pageLog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(540, 200, 183, 23))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)
        self.frameLog = QFrame(self.pageLog)
        self.frameLog.setObjectName(u"frameLog")
        self.frameLog.setEnabled(True)
        self.frameLog.setGeometry(QRect(-20, 0, 341, 601))
        self.frameLog.setAutoFillBackground(False)
        self.frameLog.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(25, 225, 175);\n"
                                    "border-radius: 25px;\n"
                                    "}")
        self.frameLog.setFrameShape(QFrame.StyledPanel)
        self.frameLog.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frameLog)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.label_2 = QLabel(self.frameLog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 4, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 5, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.label = QLabel(self.frameLog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap("icons_rc/sistem_inventary.png"))
        self.label.setScaledContents(True)

        self.gridLayout_3.addWidget(self.label, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageLog)
        self.pageOptions = QWidget()
        self.pageOptions.setGeometry(QRect(0, 0, 900, 600))
        self.pageOptions.setObjectName(u"pageOptions")
        self.frame = QFrame(self.pageOptions)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 121, 600))
        self.frame.setStyleSheet(u"QFrame{\n"
                                 "Background: rgb(42, 53, 66)\n"
                                 "}\n"
                                 "")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAutoFillBackground(False)
        self.label_9.setPixmap(QPixmap("icons_rc/User.png"))
        self.label_9.setScaledContents(False)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.accessBut = QPushButton(self.frame)
        self.accessBut.setObjectName(u"accessBut")
        font3 = QFont()
        font3.setFamily(u"Segoe WP Semibold")
        font3.setBold(True)
        font3.setWeight(75)
        self.accessBut.setFont(font3)
        self.accessBut.setStyleSheet(u"QPushButton{\n"
                                     "color: rgb(245, 245, 245);\n"
                                     "border-radius: 25px;\n"
                                     "border: 2px solid  rgb(25, 225, 175);\n"
                                     "padding: 20px;\n"
                                     " width: 10px;\n"
                                     " height: 10px;\n"
                                     "}\n"
                                     "\n"
                                     ".QPushButton:hover {\n"
                                     "    background-color: rgb(25, 225, 175);\n"
                                     "    color: black;\n"
                                     "}")

        self.verticalLayout.addWidget(self.accessBut)

        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setPixmap(QPixmap("icons_rc/Compras.png"))
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.comprasBut = QPushButton(self.frame)
        self.comprasBut.setObjectName(u"comprasBut")
        self.comprasBut.setFont(font3)
        self.comprasBut.setStyleSheet(u"QPushButton{\n"
                                      "color: rgb(245, 245, 245);\n"
                                      "border-radius: 25px;\n"
                                      "border: 2px solid  rgb(25, 225, 175);\n"
                                      "padding: 20px;\n"
                                      " width: 10px;\n"
                                      " height: 10px;\n"
                                      "}\n"
                                      "\n"
                                      ".QPushButton:hover {\n"
                                      "    background-color: rgb(25, 225, 175);\n"
                                      "    color: black;\n"
                                      "}")

        self.verticalLayout.addWidget(self.comprasBut)

        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap("icons_rc/Ventas.png"))
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.ventasBut = QPushButton(self.frame)
        self.ventasBut.setObjectName(u"ventasBut")
        self.ventasBut.setStyleSheet(u"QPushButton{\n"
                                     "color: rgb(245, 245, 245);\n"
                                     "border-radius: 25px;\n"
                                     "border: 2px solid  rgb(25, 225, 175);\n"
                                     "padding: 20px;\n"
                                     " width: 10px;\n"
                                     " height: 10px;\n"
                                     "}\n"
                                     "\n"
                                     ".QPushButton:hover {\n"
                                     "    background-color: rgb(25, 225, 175);\n"
                                     "    color: black;\n"
                                     "}")

        self.verticalLayout.addWidget(self.ventasBut)

        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setPixmap(QPixmap("icons_rc/Productos.png"))
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.productsBut = QPushButton(self.frame)
        self.productsBut.setObjectName(u"productsBut")
        self.productsBut.setStyleSheet(u"QPushButton{\n"
                                       "color: rgb(245, 245, 245);\n"
                                       "border-radius: 25px;\n"
                                       "border: 2px solid  rgb(25, 225, 175);\n"
                                       "padding: 20px;\n"
                                       " width: 10px;\n"
                                       " height: 10px;\n"
                                       "}\n"
                                       "\n"
                                       ".QPushButton:hover {\n"
                                       "    background-color: rgb(25, 225, 175);\n"
                                       "    color: black;\n"
                                       "}")

        self.verticalLayout.addWidget(self.productsBut)

        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setPixmap(QPixmap("icons_rc/Proveedor.png"))
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.provBut = QPushButton(self.frame)
        self.provBut.setObjectName(u"provBut")
        self.provBut.setStyleSheet(u"QPushButton{\n"
                                   "color: rgb(245, 245, 245);\n"
                                   "border-radius: 25px;\n"
                                   "border: 2px solid  rgb(25, 225, 175);\n"
                                   "padding: 20px;\n"
                                   " width: 10px;\n"
                                   " height: 10px;\n"
                                   "}\n"
                                   "\n"
                                   ".QPushButton:hover {\n"
                                   "    background-color: rgb(25, 225, 175);\n"
                                   "    color: black;\n"
                                   "}")

        self.verticalLayout.addWidget(self.provBut)

        self.stackedWidget.addWidget(self.pageOptions)
        self.pageAccesos = QWidget()
        self.pageAccesos.setObjectName(u"pageAccesos")
        self.rolesU = QComboBox(self.pageAccesos)
        self.rolesU.setObjectName(u"rolesU")
        self.rolesU.setGeometry(QRect(250, 130, 91, 22))
        self.nameU = QLineEdit(self.pageAccesos)
        self.nameU.setObjectName(u"nameU")
        self.nameU.setGeometry(QRect(100, 110, 113, 20))
        self.apellidoU = QLineEdit(self.pageAccesos)
        self.apellidoU.setObjectName(u"apellidoU")
        self.apellidoU.setGeometry(QRect(100, 160, 113, 20))
        self.verticalLayoutWidget = QWidget(self.pageAccesos)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(380, 100, 81, 111))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.crearP = QCheckBox(self.verticalLayoutWidget)
        self.crearP.setObjectName(u"crearP")

        self.verticalLayout_2.addWidget(self.crearP)

        self.leerP = QCheckBox(self.verticalLayoutWidget)
        self.leerP.setObjectName(u"leerP")

        self.verticalLayout_2.addWidget(self.leerP)

        self.modificarP = QCheckBox(self.verticalLayoutWidget)
        self.modificarP.setObjectName(u"modificarP")

        self.verticalLayout_2.addWidget(self.modificarP)

        self.eliminarP = QCheckBox(self.verticalLayoutWidget)
        self.eliminarP.setObjectName(u"eliminarP")

        self.verticalLayout_2.addWidget(self.eliminarP)

        self.crearU = QPushButton(self.pageAccesos)
        self.crearU.setObjectName(u"crearU")
        self.crearU.setGeometry(QRect(120, 210, 75, 23))
        self.nombreR = QLineEdit(self.pageAccesos)
        self.nombreR.setObjectName(u"nombreR")
        self.nombreR.setGeometry(QRect(500, 130, 113, 20))
        self.crearRol = QPushButton(self.pageAccesos)
        self.crearRol.setObjectName(u"crearRol")
        self.crearRol.setGeometry(QRect(520, 180, 75, 23))
        self.label_14 = QLabel(self.pageAccesos)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(100, 90, 47, 13))
        self.label_15 = QLabel(self.pageAccesos)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(100, 140, 47, 13))
        self.label_16 = QLabel(self.pageAccesos)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(250, 110, 47, 13))
        self.label_17 = QLabel(self.pageAccesos)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(380, 80, 51, 20))
        self.stackedWidget.addWidget(self.pageAccesos)
        self.pageCompras = QWidget()
        self.pageCompras.setObjectName(u"pageCompras")
        self.stackedWidget.addWidget(self.pageCompras)
        self.pageVentas = QWidget()
        self.pageVentas.setObjectName(u"pageVentas")
        self.stackedWidget.addWidget(self.pageVentas)
        self.pageProductos = QWidget()
        self.pageProductos.setObjectName(u"pageProductos")
        self.gridLayoutWidget = QWidget(self.pageProductos)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(70, 110, 451, 201))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cantMinProd = QLineEdit(self.gridLayoutWidget)
        self.cantMinProd.setObjectName(u"cantMinProd")

        self.gridLayout.addWidget(self.cantMinProd, 3, 1, 1, 1)

        self.cantMaxProd = QLineEdit(self.gridLayoutWidget)
        self.cantMaxProd.setObjectName(u"cantMaxProd")

        self.gridLayout.addWidget(self.cantMaxProd, 5, 1, 1, 1)

        self.label_22 = QLabel(self.gridLayoutWidget)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 4, 0, 1, 1)

        self.precioProd = QLineEdit(self.gridLayoutWidget)
        self.precioProd.setObjectName(u"precioProd")

        self.gridLayout.addWidget(self.precioProd, 1, 1, 1, 1)

        self.label_23 = QLabel(self.gridLayoutWidget)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout.addWidget(self.label_23, 4, 1, 1, 1)

        self.costoProd = QLineEdit(self.gridLayoutWidget)
        self.costoProd.setObjectName(u"costoProd")

        self.gridLayout.addWidget(self.costoProd, 3, 0, 1, 1)

        self.label_21 = QLabel(self.gridLayoutWidget)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout.addWidget(self.label_21, 2, 1, 1, 1)

        self.addProdBut = QPushButton(self.gridLayoutWidget)
        self.addProdBut.setObjectName(u"addProdBut")

        self.gridLayout.addWidget(self.addProdBut, 7, 1, 1, 1)

        self.label_19 = QLabel(self.gridLayoutWidget)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout.addWidget(self.label_19, 0, 1, 1, 1)

        self.marcaProd = QLineEdit(self.gridLayoutWidget)
        self.marcaProd.setObjectName(u"marcaProd")

        self.gridLayout.addWidget(self.marcaProd, 7, 0, 1, 1)

        self.label_20 = QLabel(self.gridLayoutWidget)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout.addWidget(self.label_20, 2, 0, 1, 1)

        self.nombreProd = QLineEdit(self.gridLayoutWidget)
        self.nombreProd.setObjectName(u"nombreProd")

        self.gridLayout.addWidget(self.nombreProd, 1, 0, 1, 1)

        self.label_18 = QLabel(self.gridLayoutWidget)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_24 = QLabel(self.gridLayoutWidget)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout.addWidget(self.label_24, 6, 0, 1, 1)

        self.categoriaProd = QLineEdit(self.gridLayoutWidget)
        self.categoriaProd.setObjectName(u"categoriaProd")

        self.gridLayout.addWidget(self.categoriaProd, 5, 0, 1, 1)

        self.stackedWidget.addWidget(self.pageProductos)

        self.retranslateUi(Frame)

        self.stackedWidget.setCurrentIndex(0)
        self.buttonLog_2.setDefault(False)

        QMetaObject.connectSlotsByName(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Sistema De Inventario", None))
        self.buttonLog_2.setText(QCoreApplication.translate("Frame", u"Iniciar sesi\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("Frame", u"Password:", None))
        self.label_7.setText(QCoreApplication.translate("Frame", u"User:", None))
        self.label_8.setText(QCoreApplication.translate("Frame", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"Inventory System", None))
        self.label.setText("")
        self.label_9.setText("")
        self.accessBut.setText(QCoreApplication.translate("Frame", u"Accesos", None))
        self.label_10.setText("")
        self.comprasBut.setText(QCoreApplication.translate("Frame", u"Compras", None))
        self.label_11.setText("")
        self.ventasBut.setText(QCoreApplication.translate("Frame", u"Ventas", None))
        self.label_12.setText("")
        self.productsBut.setText(QCoreApplication.translate("Frame", u"Productos", None))
        self.label_13.setText("")
        self.provBut.setText(QCoreApplication.translate("Frame", u"Proveedor", None))
        self.nameU.setText("")
        self.crearP.setText(QCoreApplication.translate("Frame", u"Crear", None))
        self.leerP.setText(QCoreApplication.translate("Frame", u"Leer", None))
        self.modificarP.setText(QCoreApplication.translate("Frame", u"Modificar", None))
        self.eliminarP.setText(QCoreApplication.translate("Frame", u"Eliminar", None))
        self.crearU.setText(QCoreApplication.translate("Frame", u"Crear Usuario", None))
        self.crearRol.setText(QCoreApplication.translate("Frame", u"Crear Rol", None))
        self.label_14.setText(QCoreApplication.translate("Frame", u"Nombre:", None))
        self.label_15.setText(QCoreApplication.translate("Frame", u"Apellido:", None))
        self.label_16.setText(QCoreApplication.translate("Frame", u"Rol:", None))
        self.label_17.setText(QCoreApplication.translate("Frame", u"Privilegios:", None))
        self.label_22.setText(QCoreApplication.translate("Frame", u"Categor\u00eda", None))
        self.label_23.setText(QCoreApplication.translate("Frame", u"Existencia_Max:", None))
        self.label_21.setText(QCoreApplication.translate("Frame", u"Existencia_Min:", None))
        self.addProdBut.setText(QCoreApplication.translate("Frame", u"A\u00f1adir Producto", None))
        self.label_19.setText(QCoreApplication.translate("Frame", u"Precio:", None))
        self.label_20.setText(QCoreApplication.translate("Frame", u"Costo:", None))
        self.label_18.setText(QCoreApplication.translate("Frame", u"Nombre:", None))
        self.label_24.setText(QCoreApplication.translate("Frame", u"Marca:", None))
    # retranslateUi


class MainWindow(QMainWindow, UiFrame):
    global user
    global password
    global userCreate
    global userChange
    global dateCreate
    global dateChange

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonLog_2.clicked.connect(self.login)

    def login(self):
        print("Login")
        print(self.userText_2.text())
        print(self.passText_2.text())

        user = self.userText_2.text()
        password = self.passText_2.text()

        try:
            conn = mariadb.connect(
                user=user,
                password=password,
                host="localhost",
                port=3306,
                database="project"
            )
            print("Conectado")
            cur = conn.cursor()
            # Imprimir las tablas
            cur.execute("SHOW TABLES")
            print(cur.fetchall())
            cur.execute("SELECT User FROM mysql.user")
            print(cur.fetchall())
            self.pageLog.hide()
            self.pageOptions.show()

            cur.close()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            print("Error al conectar")

    def access(self):
        self.pageOptions.hide()
        self.pageAccesos.show()

    def createRol(self):
        global privilegios
        global idR
        nombre = self.nombreR.text()
        if self.crearP.isChecked() and self.leerP.isChecked() and self.modificarP.isChecked() and \
                self.eliminarP.isChecked():
            privilegios = "Admin"
        elif self.crearP.isChecked() and self.leerP.isChecked() and self.modificarP.isChecked():
            privilegios = "Supervisor"
        elif self.crearP.isChecked() and self.leerP.isChecked():
            privilegios = "Usuario"
        elif self.leerP.isChecked():
            privilegios = "Lector"

        try:
            conn = mariadb.connect(
                user=user,
                password=password,
                host="localhost",
                port=3306,
                database="project"
            )
            cur = conn.cursor()
            idR = 0
            cur.callproc('sp_insetarPrivilegio', (idR, nombre, privilegios, user, datetime.now().strftime("%Y-%m-%d")))
            idR = idR + 1

        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            print("Error al conectar")


if __name__ == "__main__":
    import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
