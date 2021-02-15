# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 422)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setBaseSize(QSize(680, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 9)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tabWidget.setAcceptDrops(False)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setTabPosition(QTabWidget.North)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideLeft)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.horizontalLayout_6 = QHBoxLayout(self.tab)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.edt_login = QLineEdit(self.tab)
        self.edt_login.setObjectName(u"edt_login")
        self.edt_login.setMinimumSize(QSize(100, 0))
        self.edt_login.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.edt_login)

        self.edt_pass = QLineEdit(self.tab)
        self.edt_pass.setObjectName(u"edt_pass")
        self.edt_pass.setMinimumSize(QSize(100, 0))
        self.edt_pass.setMaximumSize(QSize(100, 16777215))
        self.edt_pass.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.edt_pass.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_6.addWidget(self.edt_pass)

        self.btn_connection = QPushButton(self.tab)
        self.btn_connection.setObjectName(u"btn_connection")
        self.btn_connection.setMinimumSize(QSize(100, 0))
        self.btn_connection.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_6.addWidget(self.btn_connection)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.horizontalLayout = QHBoxLayout(self.tab_2)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 3)
        self.label_5 = QLabel(self.tab_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5)

        self.cb_ats = QComboBox(self.tab_2)
        self.cb_ats.addItem("")
        self.cb_ats.setObjectName(u"cb_ats")
        self.cb_ats.setMinimumSize(QSize(200, 0))

        self.verticalLayout_4.addWidget(self.cb_ats)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.tab_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_2.addWidget(self.label)

        self.de_start = QDateEdit(self.tab_2)
        self.de_start.setObjectName(u"de_start")
        self.de_start.setMinimumSize(QSize(85, 0))
        self.de_start.setCalendarPopup(True)

        self.horizontalLayout_2.addWidget(self.de_start)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(20, 0))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.de_stop = QDateEdit(self.tab_2)
        self.de_stop.setObjectName(u"de_stop")
        self.de_stop.setMinimumSize(QSize(85, 0))
        self.de_stop.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.de_stop)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.tab_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 0))
        self.label_3.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_4.addWidget(self.label_3)

        self.cb_whocalledtype = QComboBox(self.tab_2)
        self.cb_whocalledtype.addItem("")
        self.cb_whocalledtype.addItem("")
        self.cb_whocalledtype.addItem("")
        self.cb_whocalledtype.setObjectName(u"cb_whocalledtype")
        self.cb_whocalledtype.setMinimumSize(QSize(150, 0))
        self.cb_whocalledtype.setBaseSize(QSize(0, 0))

        self.horizontalLayout_4.addWidget(self.cb_whocalledtype)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_correction = QLabel(self.tab_2)
        self.lb_correction.setObjectName(u"lb_correction")
        self.lb_correction.setMinimumSize(QSize(60, 0))
        self.lb_correction.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_5.addWidget(self.lb_correction)

        self.ed_clientnumber = QLineEdit(self.tab_2)
        self.ed_clientnumber.setObjectName(u"ed_clientnumber")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.ed_clientnumber.sizePolicy().hasHeightForWidth())
        self.ed_clientnumber.setSizePolicy(sizePolicy2)

        self.horizontalLayout_5.addWidget(self.ed_clientnumber)

        self.cb_whocalled = QComboBox(self.tab_2)
        self.cb_whocalled.setObjectName(u"cb_whocalled")
        self.cb_whocalled.setEnabled(True)
        self.cb_whocalled.setEditable(False)

        self.horizontalLayout_5.addWidget(self.cb_whocalled)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_clear = QPushButton(self.tab_2)
        self.btn_clear.setObjectName(u"btn_clear")

        self.verticalLayout_3.addWidget(self.btn_clear)

        self.btn_download = QPushButton(self.tab_2)
        self.btn_download.setObjectName(u"btn_download")

        self.verticalLayout_3.addWidget(self.btn_download)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_5.addWidget(self.tabWidget)

        self.tbl_view_pandas = QTableView(self.centralwidget)
        self.tbl_view_pandas.setObjectName(u"tbl_view_pandas")
        self.tbl_view_pandas.setSortingEnabled(True)
        self.tbl_view_pandas.horizontalHeader().setMinimumSectionSize(100)
        self.tbl_view_pandas.horizontalHeader().setDefaultSectionSize(100)

        self.verticalLayout_5.addWidget(self.tbl_view_pandas)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.btn_report = QPushButton(self.centralwidget)
        self.btn_report.setObjectName(u"btn_report")

        self.horizontalLayout_7.addWidget(self.btn_report)


        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u0437\u0432\u043e\u043d\u043a\u043e\u0432 Mango-Office", None))
        self.edt_login.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.edt_pass.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btn_connection.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0435\u043d\u0438\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0430\u0442\u0438\u0441\u0442\u0438\u043a\u0430 \u043f\u043e \u0410\u0422\u0421:", None))
        self.cb_ats.setItemText(0, "")

        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0441 ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0442\u043e \u0437\u0432\u043e\u043d\u0438\u043b", None))
        self.cb_whocalledtype.setItemText(0, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442", None))
        self.cb_whocalledtype.setItemText(1, QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None))
        self.cb_whocalledtype.setItemText(2, QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0438\u0435\u043d\u0442 \u0438\u043b\u0438 \u0441\u043e\u0442\u0440\u0443\u0434\u043d\u0438\u043a", None))

        self.lb_correction.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0442\u043e\u0447\u043d\u0438\u0442\u044c", None))
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u0438\u0442\u044c", None))
        self.btn_download.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u0417\u0432\u043e\u043d\u043a\u0438", None))
        self.btn_report.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0447\u0435\u0442 \u0432 XLS", None))
    # retranslateUi

