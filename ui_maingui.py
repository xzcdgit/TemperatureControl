# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Code\Python\TemperatureControl\maingui.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(639, 576)
        MainWindow.setTabletTracking(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("d:\\Code\\Python\\TemperatureControl\\1.jpeg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout.addWidget(self.lineEdit_16, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox_4)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_22.setObjectName("pushButton_22")
        self.gridLayout.addWidget(self.pushButton_22, 3, 0, 1, 2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_4)
        font = QtGui.QFont()
        font.setKerning(True)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_4)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 0, 1, 2)
        self.gridLayout_9.addWidget(self.groupBox_4, 1, 0, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_7)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox_7)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_7)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_3.addWidget(self.lineEdit, 1, 2, 1, 2)
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_28.setObjectName("pushButton_28")
        self.gridLayout_3.addWidget(self.pushButton_28, 2, 3, 1, 1)
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_30.setObjectName("pushButton_30")
        self.gridLayout_3.addWidget(self.pushButton_30, 2, 2, 1, 1)
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton_27.setObjectName("pushButton_27")
        self.gridLayout_3.addWidget(self.pushButton_27, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_7)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 1, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_7, 3, 0, 1, 2)
        self.groupBox_8 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_8)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_4.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_8, 4, 0, 1, 2)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab_3)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_29 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_29.setFont(font)
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_33.setFont(font)
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 0, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_34.setFont(font)
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.gridLayout_2.addWidget(self.label_34, 0, 2, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_35.setFont(font)
        self.label_35.setAlignment(QtCore.Qt.AlignCenter)
        self.label_35.setObjectName("label_35")
        self.gridLayout_2.addWidget(self.label_35, 0, 3, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_36.setFont(font)
        self.label_36.setAlignment(QtCore.Qt.AlignCenter)
        self.label_36.setObjectName("label_36")
        self.gridLayout_2.addWidget(self.label_36, 1, 0, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_37.setFont(font)
        self.label_37.setAlignment(QtCore.Qt.AlignCenter)
        self.label_37.setObjectName("label_37")
        self.gridLayout_2.addWidget(self.label_37, 1, 1, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.gridLayout_2.addWidget(self.label_38, 1, 2, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_39.setFont(font)
        self.label_39.setAlignment(QtCore.Qt.AlignCenter)
        self.label_39.setObjectName("label_39")
        self.gridLayout_2.addWidget(self.label_39, 1, 3, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_30.setFont(font)
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.gridLayout_2.addWidget(self.label_30, 2, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_31.setFont(font)
        self.label_31.setAlignment(QtCore.Qt.AlignCenter)
        self.label_31.setObjectName("label_31")
        self.gridLayout_2.addWidget(self.label_31, 2, 1, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_32.setFont(font)
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.gridLayout_2.addWidget(self.label_32, 2, 2, 1, 1)
        self.label_43 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_43.setFont(font)
        self.label_43.setAlignment(QtCore.Qt.AlignCenter)
        self.label_43.setObjectName("label_43")
        self.gridLayout_2.addWidget(self.label_43, 2, 3, 1, 1)
        self.label_40 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.gridLayout_2.addWidget(self.label_40, 3, 0, 1, 1)
        self.label_41 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.gridLayout_2.addWidget(self.label_41, 3, 1, 1, 1)
        self.label_42 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_42.setFont(font)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.gridLayout_2.addWidget(self.label_42, 3, 2, 1, 1)
        self.label_44 = QtWidgets.QLabel(self.groupBox_5)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_44.setObjectName("label_44")
        self.gridLayout_2.addWidget(self.label_44, 3, 3, 1, 1)
        self.gridLayout_9.addWidget(self.groupBox_5, 2, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 351, 191))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.doubleSpinBox_6 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_6.setDecimals(1)
        self.doubleSpinBox_6.setMinimum(-100.0)
        self.doubleSpinBox_6.setMaximum(100.0)
        self.doubleSpinBox_6.setObjectName("doubleSpinBox_6")
        self.gridLayout_5.addWidget(self.doubleSpinBox_6, 3, 1, 1, 1)
        self.doubleSpinBox_8 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_8.setDecimals(1)
        self.doubleSpinBox_8.setMinimum(-100.0)
        self.doubleSpinBox_8.setMaximum(100.0)
        self.doubleSpinBox_8.setObjectName("doubleSpinBox_8")
        self.gridLayout_5.addWidget(self.doubleSpinBox_8, 3, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.gridLayout_5.addWidget(self.label_8, 2, 0, 1, 1)
        self.doubleSpinBox_4 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_4.setDecimals(1)
        self.doubleSpinBox_4.setMinimum(-100.0)
        self.doubleSpinBox_4.setMaximum(100.0)
        self.doubleSpinBox_4.setObjectName("doubleSpinBox_4")
        self.gridLayout_5.addWidget(self.doubleSpinBox_4, 1, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.gridLayout_5.addWidget(self.label_6, 0, 2, 1, 1)
        self.doubleSpinBox_5 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setDecimals(1)
        self.doubleSpinBox_5.setMinimum(-100.0)
        self.doubleSpinBox_5.setMaximum(100.0)
        self.doubleSpinBox_5.setObjectName("doubleSpinBox_5")
        self.gridLayout_5.addWidget(self.doubleSpinBox_5, 3, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout_5.addWidget(self.label_11, 2, 3, 1, 1)
        self.doubleSpinBox_7 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_7.setDecimals(1)
        self.doubleSpinBox_7.setMinimum(-100.0)
        self.doubleSpinBox_7.setMaximum(100.0)
        self.doubleSpinBox_7.setObjectName("doubleSpinBox_7")
        self.gridLayout_5.addWidget(self.doubleSpinBox_7, 3, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout_5.addWidget(self.label_5, 0, 1, 1, 1)
        self.doubleSpinBox_3 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_3.setDecimals(1)
        self.doubleSpinBox_3.setMinimum(-100.0)
        self.doubleSpinBox_3.setMaximum(100.0)
        self.doubleSpinBox_3.setObjectName("doubleSpinBox_3")
        self.gridLayout_5.addWidget(self.doubleSpinBox_3, 1, 2, 1, 1)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setMinimum(-100.0)
        self.doubleSpinBox.setMaximum(100.0)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.gridLayout_5.addWidget(self.doubleSpinBox, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout_5.addWidget(self.label_3, 0, 0, 1, 1)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_2.setDecimals(1)
        self.doubleSpinBox_2.setMinimum(-100.0)
        self.doubleSpinBox_2.setMaximum(100.0)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.gridLayout_5.addWidget(self.doubleSpinBox_2, 1, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.gridLayout_5.addWidget(self.label_9, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.gridLayout_5.addWidget(self.label_10, 2, 2, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_5.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.gridLayout_10.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 639, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.menu_2.addAction(self.action)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "温度记录器"))
        self.tabWidget.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>形线分析器</p><p><br/></p></body></html>"))
        self.groupBox_4.setTitle(_translate("MainWindow", "串口连接"))
        self.lineEdit_16.setText(_translate("MainWindow", "38400"))
        self.label.setText(_translate("MainWindow", "串口号"))
        self.pushButton_22.setText(_translate("MainWindow", "连接"))
        self.lineEdit_2.setText(_translate("MainWindow", "COM3"))
        self.label_4.setText(_translate("MainWindow", "波特率"))
        self.pushButton_7.setText(_translate("MainWindow", "可用串口检测"))
        self.groupBox_7.setTitle(_translate("MainWindow", "操作选项"))
        self.label_2.setText(_translate("MainWindow", "保存目录"))
        self.pushButton_28.setText(_translate("MainWindow", "保存记录"))
        self.pushButton_30.setText(_translate("MainWindow", "打开保存文件夹"))
        self.pushButton_27.setText(_translate("MainWindow", "开始记录"))
        self.pushButton.setText(_translate("MainWindow", "启动动态绘图"))
        self.groupBox_8.setTitle(_translate("MainWindow", "提示"))
        self.groupBox_5.setTitle(_translate("MainWindow", "数据显示"))
        self.label_29.setText(_translate("MainWindow", "通道1"))
        self.label_33.setText(_translate("MainWindow", "通道2"))
        self.label_34.setText(_translate("MainWindow", "通道3"))
        self.label_35.setText(_translate("MainWindow", "通道4"))
        self.label_36.setText(_translate("MainWindow", "----"))
        self.label_37.setText(_translate("MainWindow", "----"))
        self.label_38.setText(_translate("MainWindow", "----"))
        self.label_39.setText(_translate("MainWindow", "----"))
        self.label_30.setText(_translate("MainWindow", "通道5"))
        self.label_31.setText(_translate("MainWindow", "通道6"))
        self.label_32.setText(_translate("MainWindow", "通道7"))
        self.label_43.setText(_translate("MainWindow", "通道8"))
        self.label_40.setText(_translate("MainWindow", "----"))
        self.label_41.setText(_translate("MainWindow", "----"))
        self.label_42.setText(_translate("MainWindow", "----"))
        self.label_44.setText(_translate("MainWindow", "----"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "数据读取"))
        self.groupBox.setTitle(_translate("MainWindow", "零点偏移"))
        self.label_8.setText(_translate("MainWindow", "通道5"))
        self.label_6.setText(_translate("MainWindow", "通道3"))
        self.label_11.setText(_translate("MainWindow", "通道8"))
        self.label_5.setText(_translate("MainWindow", "通道2"))
        self.label_3.setText(_translate("MainWindow", "通道1"))
        self.label_7.setText(_translate("MainWindow", "通道4"))
        self.label_9.setText(_translate("MainWindow", "通道6"))
        self.label_10.setText(_translate("MainWindow", "通道7"))
        self.pushButton_2.setText(_translate("MainWindow", "修改"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "配置"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.action.setText(_translate("MainWindow", "无"))
