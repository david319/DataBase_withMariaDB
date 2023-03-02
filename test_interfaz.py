from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import mariadb


class UiFrame(object):
    def setupUi(self, Frame):
        if Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.setWindowModality(Qt.NonModal)
        Frame.setEnabled(True)
        Frame.resize(900, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Frame.sizePolicy().hasHeightForWidth())
        Frame.setSizePolicy(sizePolicy)
        Frame.setMinimumSize(QSize(900, 600))
        Frame.setMaximumSize(QSize(900, 600))
        self.frameLog = QFrame(Frame)
        self.frameLog.setObjectName(u"frameLog")
        self.frameLog.setGeometry(QRect(-20, 0, 341, 601))
        self.frameLog.setAutoFillBackground(False)
        self.frameLog.setStyleSheet(u"QFrame{\n"
                                    "background-color:rgb(25, 225, 175);\n"
                                    "border-radius: 25px;\n"
                                    "}")
        self.frameLog.setFrameShape(QFrame.StyledPanel)
        self.frameLog.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frameLog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_5, 5, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_6, 1, 1, 1, 1)

        self.label = QLabel(self.frameLog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"")
        self.label.setPixmap(QPixmap(u":/icono/sistem_inventary.png"))
        self.label.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label, 2, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.label_2 = QLabel(self.frameLog)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.gridLayoutWidget = QWidget(Frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(339, -1, 561, 601))
        self.gridLog = QGridLayout(self.gridLayoutWidget)
        self.gridLog.setObjectName(u"gridLog")
        self.gridLog.setContentsMargins(0, 0, 0, 0)
        self.passText = QLineEdit(self.gridLayoutWidget)
        self.passText.setObjectName(u"passText")
        font1 = QFont()
        font1.setPointSize(12)
        self.passText.setFont(font1)
        self.passText.setStyleSheet(u"QLineEdit{\n"
                                    "border: 2px solid  rgb(25, 225, 175);\n"
                                    "border-radius: 4px;\n"
                                    "}")
        self.passText.setEchoMode(QLineEdit.Password)

        self.gridLog.addWidget(self.passText, 5, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLog.addItem(self.verticalSpacer, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLog.addWidget(self.label_3, 1, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_4.setFont(font2)

        self.gridLog.addWidget(self.label_4, 2, 1, 1, 1)

        self.buttonLog = QPushButton(self.gridLayoutWidget)
        self.buttonLog.setObjectName(u"buttonLog")
        self.buttonLog.setFont(font2)
        self.buttonLog.setCursor(QCursor(Qt.PointingHandCursor))
        self.buttonLog.setStyleSheet(u"QPushButton{\n"
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
        self.buttonLog.setAutoDefault(False)
        self.buttonLog.setFlat(False)

        self.gridLog.addWidget(self.buttonLog, 6, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLog.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.userText = QLineEdit(self.gridLayoutWidget)
        self.userText.setObjectName(u"userText")
        self.userText.setFont(font1)
        self.userText.setStyleSheet(u"QLineEdit{\n"
                                    "border: 2px solid rgb(25, 225, 175);\n"
                                    "border-radius: 4px;\n"
                                    "}")

        self.gridLog.addWidget(self.userText, 3, 1, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)

        self.gridLog.addWidget(self.label_5, 4, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLog.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLog.addItem(self.verticalSpacer_2, 7, 1, 1, 1)

        self.frameOptions = QFrame(Frame)
        self.frameOptions.setObjectName(u"frameOptions")
        self.frameOptions.setEnabled(False)
        self.frameOptions.setGeometry(QRect(1, -1, 880, 610))
        self.frameOptions.setFrameShape(QFrame.StyledPanel)
        self.frameOptions.setFrameShadow(QFrame.Raised)
        self.frameOptions.raise_()
        self.frameLog.raise_()
        self.gridLayoutWidget.raise_()

        self.retranslateUi(Frame)

        self.buttonLog.setDefault(False)

        QMetaObject.connectSlotsByName(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"DataBase", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Frame", u"Inventory System", None))
        self.label_3.setText(QCoreApplication.translate("Frame", u"Login", None))
        self.label_4.setText(QCoreApplication.translate("Frame", u"User:", None))
        self.buttonLog.setText(QCoreApplication.translate("Frame", u"Iniciar sesi\u00f3n", None))
        self.label_5.setText(QCoreApplication.translate("Frame", u"Password:", None))
    # retranslateUi


class MainWindow(QMainWindow, UiFrame):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.buttonLog.clicked.connect(self.login)

    def login(self):
        print("Login")
        print(self.userText.text())
        print(self.passText.text())

        user = self.userText.text()
        password = self.passText.text()

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
            self.frameLog.hide()
            self.gridLog.hide()
            self.frameOptions.show()

            cur.close()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            print("Error al conectar")


if __name__ == "__main__":
    import sys

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
