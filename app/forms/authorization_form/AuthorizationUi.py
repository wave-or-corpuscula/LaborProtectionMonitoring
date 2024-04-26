# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AuthorizationFormUi.ui'
##
## Created by: Qt User Interface Compiler version 6.6.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_AuthorizationWindow(object):
    def setupUi(self, AuthorizationWindow):
        if not AuthorizationWindow.objectName():
            AuthorizationWindow.setObjectName(u"AuthorizationWindow")
        AuthorizationWindow.resize(606, 455)
        self.centralwidget = QWidget(AuthorizationWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 60, 191, 41))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.username_le = QLineEdit(self.centralwidget)
        self.username_le.setObjectName(u"username_le")
        self.username_le.setGeometry(QRect(70, 120, 391, 41))
        self.username_le.setFont(font)
        self.password_le = QLineEdit(self.centralwidget)
        self.password_le.setObjectName(u"password_le")
        self.password_le.setGeometry(QRect(70, 180, 391, 41))
        self.password_le.setFont(font)
        self.signIn_pb = QPushButton(self.centralwidget)
        self.signIn_pb.setObjectName(u"signIn_pb")
        self.signIn_pb.setGeometry(QRect(150, 260, 231, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.signIn_pb.setFont(font1)
        AuthorizationWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AuthorizationWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 606, 26))
        AuthorizationWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AuthorizationWindow)
        self.statusbar.setObjectName(u"statusbar")
        AuthorizationWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AuthorizationWindow)

        QMetaObject.connectSlotsByName(AuthorizationWindow)
    # setupUi

    def retranslateUi(self, AuthorizationWindow):
        AuthorizationWindow.setWindowTitle(QCoreApplication.translate("AuthorizationWindow", u"\u0410\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.label.setText(QCoreApplication.translate("AuthorizationWindow", u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f", None))
        self.username_le.setPlaceholderText(QCoreApplication.translate("AuthorizationWindow", u"\u0418\u043c\u044f \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f", None))
        self.password_le.setPlaceholderText(QCoreApplication.translate("AuthorizationWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.signIn_pb.setText(QCoreApplication.translate("AuthorizationWindow", u"\u0412\u043e\u0439\u0442\u0438", None))
    # retranslateUi

