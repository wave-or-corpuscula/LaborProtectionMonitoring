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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDateEdit, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_BriefingsWindow(object):
    def setupUi(self, BriefingsWindow):
        if not BriefingsWindow.objectName():
            BriefingsWindow.setObjectName(u"BriefingsWindow")
        BriefingsWindow.resize(939, 712)
        font = QFont()
        font.setPointSize(9)
        BriefingsWindow.setFont(font)
        self.centralwidget = QWidget(BriefingsWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.briefings_tw = QTableWidget(self.centralwidget)
        self.briefings_tw.setObjectName(u"briefings_tw")
        self.briefings_tw.setGeometry(QRect(10, 420, 911, 211))
        self.briefings_tw.setSelectionMode(QAbstractItemView.SingleSelection)
        self.briefings_tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.briefings_tw.setSortingEnabled(True)
        self.selectedBriefing_le = QLineEdit(self.centralwidget)
        self.selectedBriefing_le.setObjectName(u"selectedBriefing_le")
        self.selectedBriefing_le.setGeometry(QRect(420, 290, 191, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.selectedBriefing_le.setFont(font1)
        self.back_pb = QPushButton(self.centralwidget)
        self.back_pb.setObjectName(u"back_pb")
        self.back_pb.setGeometry(QRect(830, 290, 93, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 290, 111, 41))
        self.label.setFont(font1)
        self.employees_tw = QTableWidget(self.centralwidget)
        self.employees_tw.setObjectName(u"employees_tw")
        self.employees_tw.setGeometry(QRect(10, 50, 911, 231))
        self.employees_tw.setSelectionMode(QAbstractItemView.SingleSelection)
        self.employees_tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.employees_tw.setSortingEnabled(True)
        self.selectedEmployee_le = QLineEdit(self.centralwidget)
        self.selectedEmployee_le.setObjectName(u"selectedEmployee_le")
        self.selectedEmployee_le.setGeometry(QRect(130, 290, 161, 41))
        self.selectedEmployee_le.setFont(font1)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 290, 121, 41))
        self.label_2.setFont(font1)
        self.instruct_pb = QPushButton(self.centralwidget)
        self.instruct_pb.setObjectName(u"instruct_pb")
        self.instruct_pb.setGeometry(QRect(620, 290, 201, 41))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 121, 41))
        self.label_3.setFont(font1)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 360, 141, 41))
        self.label_4.setFont(font1)
        self.employeesSearch_le = QLineEdit(self.centralwidget)
        self.employeesSearch_le.setObjectName(u"employeesSearch_le")
        self.employeesSearch_le.setGeometry(QRect(210, 11, 711, 31))
        self.briefingsStart_de = QDateEdit(self.centralwidget)
        self.briefingsStart_de.setObjectName(u"briefingsStart_de")
        self.briefingsStart_de.setGeometry(QRect(298, 370, 141, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(268, 360, 31, 41))
        font2 = QFont()
        font2.setPointSize(15)
        self.label_5.setFont(font2)
        self.briefingEnd_de = QDateEdit(self.centralwidget)
        self.briefingEnd_de.setObjectName(u"briefingEnd_de")
        self.briefingEnd_de.setGeometry(QRect(488, 370, 141, 31))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(448, 360, 31, 41))
        font3 = QFont()
        font3.setPointSize(16)
        self.label_6.setFont(font3)
        self.filterBriefings_pb = QPushButton(self.centralwidget)
        self.filterBriefings_pb.setObjectName(u"filterBriefings_pb")
        self.filterBriefings_pb.setGeometry(QRect(640, 370, 131, 31))
        self.briefingsToExcel_pb = QPushButton(self.centralwidget)
        self.briefingsToExcel_pb.setObjectName(u"briefingsToExcel_pb")
        self.briefingsToExcel_pb.setGeometry(QRect(150, 370, 31, 31))
        icon = QIcon()
        icon.addFile(u"../../icons/excel.JPG", QSize(), QIcon.Normal, QIcon.Off)
        self.briefingsToExcel_pb.setIcon(icon)
        self.employeesToExcel_pb = QPushButton(self.centralwidget)
        self.employeesToExcel_pb.setObjectName(u"employeesToExcel_pb")
        self.employeesToExcel_pb.setGeometry(QRect(170, 10, 31, 31))
        self.employeesToExcel_pb.setIcon(icon)
        self.cancelFilterBriefings_pb = QPushButton(self.centralwidget)
        self.cancelFilterBriefings_pb.setObjectName(u"cancelFilterBriefings_pb")
        self.cancelFilterBriefings_pb.setGeometry(QRect(790, 370, 131, 31))
        BriefingsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(BriefingsWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 939, 26))
        BriefingsWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(BriefingsWindow)
        self.statusbar.setObjectName(u"statusbar")
        BriefingsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BriefingsWindow)

        QMetaObject.connectSlotsByName(BriefingsWindow)
    # setupUi

    def retranslateUi(self, BriefingsWindow):
        BriefingsWindow.setWindowTitle(QCoreApplication.translate("BriefingsWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0430\u0436\u0438", None))
        self.back_pb.setText(QCoreApplication.translate("BriefingsWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label.setText(QCoreApplication.translate("BriefingsWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a:", None))
        self.label_2.setText(QCoreApplication.translate("BriefingsWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0430\u0436:", None))
        self.instruct_pb.setText(QCoreApplication.translate("BriefingsWindow", u"\u041f\u0440\u043e\u0432\u0435\u0441\u0442\u0438 \u0438\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0430\u0436", None))
        self.label_3.setText(QCoreApplication.translate("BriefingsWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a\u0438:", None))
        self.label_4.setText(QCoreApplication.translate("BriefingsWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u0430\u0436\u0438:", None))
        self.employeesSearch_le.setPlaceholderText(QCoreApplication.translate("BriefingsWindow", u"\u041f\u043e\u0438\u0441\u043a...", None))
        self.label_5.setText(QCoreApplication.translate("BriefingsWindow", u"C", None))
        self.label_6.setText(QCoreApplication.translate("BriefingsWindow", u"\u043f\u043e", None))
        self.filterBriefings_pb.setText(QCoreApplication.translate("BriefingsWindow", u"\u041e\u0442\u043e\u0431\u0440\u0430\u0437\u0438\u0442\u044c", None))
        self.briefingsToExcel_pb.setText("")
        self.employeesToExcel_pb.setText("")
        self.cancelFilterBriefings_pb.setText(QCoreApplication.translate("BriefingsWindow", u"\u041e\u0442\u043c\u0435\u043d\u0438\u0442\u044c", None))
    # retranslateUi

