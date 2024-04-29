# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'BriefingsUi.ui'
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
from PySide6.QtWidgets import (QApplication, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_BriefingsWindow(object):
    def setupUi(self, BriefingsWindow):
        if not BriefingsWindow.objectName():
            BriefingsWindow.setObjectName(u"BriefingsWindow")
        BriefingsWindow.resize(956, 599)
        font = QFont()
        font.setPointSize(9)
        BriefingsWindow.setFont(font)
        self.centralwidget = QWidget(BriefingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(10, 10, 941, 551))
        self.employees_tab = QWidget()
        self.employees_tab.setObjectName(u"employees_tab")
        self.employees_tw = QTableWidget(self.employees_tab)
        self.employees_tw.setObjectName(u"employees_tw")
        self.employees_tw.setGeometry(QRect(10, 10, 391, 501))
        self.briefings_tw = QTableWidget(self.employees_tab)
        self.briefings_tw.setObjectName(u"briefings_tw")
        self.briefings_tw.setGeometry(QRect(510, 10, 421, 501))
        self.instruct_pb = QPushButton(self.employees_tab)
        self.instruct_pb.setObjectName(u"instruct_pb")
        self.instruct_pb.setGeometry(QRect(410, 50, 93, 81))
        self.tabWidget.addTab(self.employees_tab, "")
        self.departments_tab = QWidget()
        self.departments_tab.setObjectName(u"departments_tab")
        self.tabWidget.addTab(self.departments_tab, "")
        BriefingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BriefingsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 956, 26))
        BriefingsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BriefingsWindow)
        self.statusbar.setObjectName(u"statusbar")
        BriefingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BriefingsWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(BriefingsWindow)
    # setupUi

    def retranslateUi(self, BriefingsWindow):
        BriefingsWindow.setWindowTitle(QCoreApplication.translate("BriefingsWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0430\u0436\u0438", None))
        self.instruct_pb.setText(QCoreApplication.translate("BriefingsWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438\n"
"\u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0430\u0436", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.employees_tab), QCoreApplication.translate("BriefingsWindow", u"\u0412\u0441\u0435 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.departments_tab), QCoreApplication.translate("BriefingsWindow", u"\u0414\u0435\u043f\u0430\u0440\u0442\u0430\u043c\u0435\u043d\u0442\u044b", None))
    # retranslateUi

