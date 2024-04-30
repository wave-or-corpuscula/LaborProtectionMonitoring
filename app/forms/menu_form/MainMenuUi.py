# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainMenuUi.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        if not MenuWindow.objectName():
            MenuWindow.setObjectName(u"MenuWindow")
        MenuWindow.resize(357, 478)
        self.centralwidget = QWidget(MenuWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logout_pb = QPushButton(self.centralwidget)
        self.logout_pb.setObjectName(u"logout_pb")
        self.logout_pb.setGeometry(QRect(270, 10, 71, 31))
        font = QFont()
        font.setPointSize(10)
        self.logout_pb.setFont(font)
        self.username_lb = QLabel(self.centralwidget)
        self.username_lb.setObjectName(u"username_lb")
        self.username_lb.setGeometry(QRect(110, 10, 151, 31))
        self.username_lb.setFont(font)
        self.username_lb.setStyleSheet(u"border: 1px solid black;")
        self.changeData_pb = QPushButton(self.centralwidget)
        self.changeData_pb.setObjectName(u"changeData_pb")
        self.changeData_pb.setGeometry(QRect(70, 80, 221, 51))
        font1 = QFont()
        font1.setPointSize(12)
        self.changeData_pb.setFont(font1)
        self.briefingCheck_pb = QPushButton(self.centralwidget)
        self.briefingCheck_pb.setObjectName(u"briefingCheck_pb")
        self.briefingCheck_pb.setGeometry(QRect(70, 160, 221, 51))
        self.briefingCheck_pb.setFont(font1)
        self.exit_pb = QPushButton(self.centralwidget)
        self.exit_pb.setObjectName(u"exit_pb")
        self.exit_pb.setGeometry(QRect(70, 340, 221, 51))
        self.exit_pb.setFont(font1)
        MenuWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MenuWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 357, 26))
        MenuWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MenuWindow)
        self.statusbar.setObjectName(u"statusbar")
        MenuWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MenuWindow)

        QMetaObject.connectSlotsByName(MenuWindow)
    # setupUi

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(QCoreApplication.translate("MenuWindow", u"\u0413\u043b\u0430\u0432\u043d\u043e\u0435 \u043c\u0435\u043d\u044e", None))
        self.logout_pb.setText(QCoreApplication.translate("MenuWindow", u"\u0412\u044b\u0439\u0442\u0438", None))
        self.username_lb.setText(QCoreApplication.translate("MenuWindow", u"username", None))
        self.changeData_pb.setText(QCoreApplication.translate("MenuWindow", u"\u0414\u0430\u043d\u043d\u044b\u0435 \u043e\u0445\u0440\u0430\u043d\u044b \u0442\u0440\u0443\u0434\u0430", None))
        self.briefingCheck_pb.setText(QCoreApplication.translate("MenuWindow", u"\u041f\u0440\u043e\u0445\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u041e\u0422", None))
        self.exit_pb.setText(QCoreApplication.translate("MenuWindow", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

