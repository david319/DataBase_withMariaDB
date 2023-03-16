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
        self.stackedWidget.setGeometry(QRect(0, 0, 900, 600))
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
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Frame)

        self.buttonLog_2.setDefault(False)


        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.buttonLog_2.setText(QCoreApplication.translate("Frame", u"Iniciar sesi\u00f3n", None))
        self.label_6.setText(QCoreApplication.translate("Frame", u"Password:", None))
        self.label_7.setText(QCoreApplication.translate("Frame", u"User:", None))
        self.label_8.setText(QCoreApplication.translate("Frame", u"Login", None))
        self.label_2.setText(QCoreApplication.translate("Frame", u"Inventory System", None))
        self.label.setText("")
# retranslateUi


class MainWindow(QMainWindow, UiFrame):
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
            self.page_2.show()

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
