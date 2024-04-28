# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DataManagingUi.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_DataManagingWindow(object):
    def setupUi(self, DataManagingWindow):
        if not DataManagingWindow.objectName():
            DataManagingWindow.setObjectName(u"DataManagingWindow")
        DataManagingWindow.resize(800, 594)
        self.centralwidget = QWidget(DataManagingWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.dataDisplay_tw = QTableWidget(self.centralwidget)
        self.dataDisplay_tw.setObjectName(u"dataDisplay_tw")
        self.dataDisplay_tw.setGeometry(QRect(10, 10, 611, 451))
        self.dataDisplay_tw.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dataDisplay_tw.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.managingTools_gb = QGroupBox(self.centralwidget)
        self.managingTools_gb.setObjectName(u"managingTools_gb")
        self.managingTools_gb.setGeometry(QRect(630, 140, 161, 201))
        self.addRecord_pb = QPushButton(self.managingTools_gb)
        self.addRecord_pb.setObjectName(u"addRecord_pb")
        self.addRecord_pb.setGeometry(QRect(10, 30, 141, 41))
        self.changeRecord_pb = QPushButton(self.managingTools_gb)
        self.changeRecord_pb.setObjectName(u"changeRecord_pb")
        self.changeRecord_pb.setGeometry(QRect(10, 80, 141, 41))
        self.deleteRecord_pb = QPushButton(self.managingTools_gb)
        self.deleteRecord_pb.setObjectName(u"deleteRecord_pb")
        self.deleteRecord_pb.setGeometry(QRect(10, 130, 141, 41))
        self.backToMenu_pb = QPushButton(self.centralwidget)
        self.backToMenu_pb.setObjectName(u"backToMenu_pb")
        self.backToMenu_pb.setGeometry(QRect(640, 420, 141, 41))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 469, 611, 61))
        self.inputs_hbl = QHBoxLayout(self.horizontalLayoutWidget)
        self.inputs_hbl.setObjectName(u"inputs_hbl")
        self.inputs_hbl.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(630, 20, 151, 21))
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.currentTable_cb = QComboBox(self.centralwidget)
        self.currentTable_cb.setObjectName(u"currentTable_cb")
        self.currentTable_cb.setGeometry(QRect(630, 50, 151, 31))
        self.currentTable_cb.setFont(font)
        DataManagingWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DataManagingWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        DataManagingWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DataManagingWindow)
        self.statusbar.setObjectName(u"statusbar")
        DataManagingWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DataManagingWindow)

        QMetaObject.connectSlotsByName(DataManagingWindow)
    # setupUi

    def retranslateUi(self, DataManagingWindow):
        DataManagingWindow.setWindowTitle(QCoreApplication.translate("DataManagingWindow", u"\u0423\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u0434\u0430\u043d\u043d\u044b\u043c\u0438", None))
        self.managingTools_gb.setTitle(QCoreApplication.translate("DataManagingWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043c\u0435\u043d\u0442\u044b", None))
        self.addRecord_pb.setText(QCoreApplication.translate("DataManagingWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.changeRecord_pb.setText(QCoreApplication.translate("DataManagingWindow", u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c", None))
        self.deleteRecord_pb.setText(QCoreApplication.translate("DataManagingWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.backToMenu_pb.setText(QCoreApplication.translate("DataManagingWindow", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.label.setText(QCoreApplication.translate("DataManagingWindow", u"\u0412\u044b\u0431\u043e\u0440 \u0442\u0430\u0431\u043b\u0438\u0446\u044b:", None))
    # retranslateUi

