import os
import time

import numpy as np
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog, QApplication
#matplot绘图库
import matplotlib.pyplot as plt
#自定义库
from ui_maingui import Ui_MainWindow
import function_dataanalysis
import communicate_threadset
import serialset
import initial_params
import pid_control


#ui界面设置类
class MyMainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):  #初始函数
        super(MyMainWindow, self).__init__(parent)  #继承父类函数
        self.setupUi(self)  #继承窗口函数MyMainWindow.setupUi的所有变量 以便修改界面函数显示
        self.toolSet()  #设置界面槽函数
        self.paramsSet()  #设置预参数

    def paramsSet(self):

        self.temperature_shows = [
            self.label_36, self.label_37, self.label_38, self.label_39,
            self.label_40, self.label_41, self.label_42, self.label_44
        ]

        #保存目录初始化
        files_save_path = os.getcwd() + r"\data"
        self.lineEdit.setText(files_save_path)

        #串口号初始化
        serial_str = serialset.serialsearch()
        self.textBrowser.setText(serial_str)
        serials = serial_str.split("\n")
        for serial in serials:
            if 'USB-SERIAL CH340' in serial:
                tmps = serial.split(" ")
                self.lineEdit_2.setText(tmps[0])
                break

        self.is_recording = False  #记录标识符
        self.record_data_num = 0  #记录数据量统计
        self.is_showed = False  #绘图线程创建标识符
        self.record_data_list = []
        self.sttime = time.time()

        #零点校准配置文件读取
        self.init_path = 'initset.ini'
        self.zero_param_shows = [
            self.doubleSpinBox, self.doubleSpinBox_2, self.doubleSpinBox_3,
            self.doubleSpinBox_4, self.doubleSpinBox_5, self.doubleSpinBox_6,
            self.doubleSpinBox_7, self.doubleSpinBox_8
        ]
        self.init_params_opter = initial_params.IniSetUp()
        self.zero_params = self.init_params_opter.configRead(self.init_path)
        for i in range(8):
            self.zero_param_shows[i].setValue(self.zero_params[i])

        #自动加热线程
        self.main_temperature = 0
        self.controler = pid_control.TemperaturController()
        self.controler.thread_sts_signal.connect(
            self.recall_auto_process_sts)  #连接线程状态信号
        self.controler.current_temperature_signal.connect(
            self.return_temperature)  #连接实时温度信号

    def return_temperature(self, sign_type: int):
        self.controler.set_current_point(self.main_temperature)

    def auto_process(self):
        self.controler.start()  #启动线程

    def recall_auto_process_sts(self, run_sts: int):
        print(run_sts)

    def toolSet(self):
        self.pushButton_22.clicked.connect(self.sercomSet)  #串口连接
        self.pushButton_7.clicked.connect(self.sersearch)  #可用串口查询
        self.pushButton_27.clicked.connect(self.recordOpt)  #开始记录
        self.pushButton_28.clicked.connect(self.csvfileSave)  #保存记录
        self.pushButton_30.clicked.connect(self.opend_folder)  #打开保存文件夹
        self.pushButton.clicked.connect(self.dynamic_drawing)  #动态绘图
        self.pushButton_3.clicked.connect(self.handle_drawing)  #手动绘图
        self.pushButton_2.clicked.connect(self.zero_params_set)  #修改零点偏移参数
        self.pushButton_4.clicked.connect(self.auto_process)  #自动温控 启动
        self.pushButton_5.clicked.connect(
            lambda x: self.controler.set_quit())  #自动温控 终止

    def threadsts(self, finish_way: int):
        '''
    串口通信线程 结束时将返回结束状态并自动调用一次该函数
    @参数
    finish_way: 1表示线程正常结束   2表示线程运行异常（创建串口通信对象失败 可能是连接的串口名错误）结束
    '''
        if finish_way == 1:
            self.statusBar.showMessage('成功关闭串口', 5000)
            self.pushButton_22.setText('连接')
        else:
            self.statusBar.showMessage('串口连接失败', 5000)
            self.pushButton_22.setText('连接')

    def opend_folder(self):
        folder_path = self.lineEdit.text()
        if os.path.exists(folder_path):
            os.startfile(folder_path)
        else:
            self.statusBar.showMessage('目标路径不存在', 5000)

    def handle_drawing(self):
        file_path = QFileDialog.getOpenFileName(self, "选择文件", "",
                                                "CSV文件(*.csv)")[0]
        if file_path:
            with open(file_path, 'r') as f:
                text = f.read()
            try:
                lines = text.split('\n')
                if len(lines) > 3:
                    lines.pop(0)  #去除标题
                    lines.pop()  #去除结尾的换行符
                    for index, line in enumerate(lines):
                        lines[index] = list(map(float, line.split(',')))
                    lines_arr = np.array(lines)
                    colors = ['r', 'g', 'b', 'y', 'm', 'c', 'orange', 'yellow']
                    linestyles = ['-', '-', '-', '-', '-', '-', '-', '-']
                    #markers = ['.', '.', '.', '.', '.', '.', '.', '.']
                    sttime = lines[0][0]
                    timeArray = time.localtime(int(sttime))
                    show_date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                    for i in range(1, len(lines[0])):
                        if lines_arr[0, i] == 0:
                            continue
                        plt.plot(lines_arr[:, 0] - sttime,
                                 lines_arr[:, i],
                                 color=colors[i - 1],
                                 linestyle=linestyles[i - 1],
                                 label='input' + str(i))
                    plt.title("handle_drawing")  #设置标题
                    plt.legend()
                    plt.xlabel('time(s) stTime: ' + show_date)
                    plt.ylabel('temperature(°)')
                    plt.show()
            except Exception as e:
                self.statusBar.showMessage('目标数据非法', 5000)

    def dynamic_drawing(self):
        if self.is_showed == False:
            self.is_showed = True
            self.pushButton.setText('关闭动态绘图')
            colors = ['r', 'g', 'b', 'y', 'm', 'c', 'orange', 'yellow']
            linestyles = ['-', '-', '-', '-', '-', '-', '-', '-']
            #markers = ['.', '.', '.', '.', '.', '.', '.', '.']
            #如果动态绘图有效则发送数据
            timeArray = time.localtime(int(self.sttime))
            show_date = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            while True:
                if self.record_data_num > 0:
                    all_data = np.array(self.record_data_list)
                    x = all_data[:, 0] - self.sttime
                    for i in range(1, len(all_data[0])):
                        if all_data[0][i] == 0:
                            continue
                        plt.plot(x,
                                 all_data[:, i],
                                 color=colors[i - 1],
                                 linestyle=linestyles[i - 1],
                                 label='input' + str(i))
                    plt.title("dynamic_drawing")  #设置标题
                    plt.legend()
                    plt.xlabel('time(s) stTime: ' + show_date)
                    plt.ylabel('temperature(°)')
                    plt.pause(2)
                    plt.cla()
                    if self.is_showed == False:
                        self.pushButton.setText('启动动态绘图')
                        plt.close()
                        break
                else:
                    self.is_showed = False
                    self.pushButton.setText('启动动态绘图')
                    break
        else:
            self.is_showed = False
            self.pushButton.setText('启动动态绘图')

    def sercomSet(self):
        '''
    连接串口 并创建串口的循环通信线程
    '''
        if self.pushButton_22.text() == '连接':
            self.serthread = communicate_threadset.MyThread(
                self.lineEdit_2.text(), int(self.lineEdit_16.text()))  #创建线程类对象
            self.serthread.data_signal.connect(self.callBack)  #连接信号
            self.serthread.finish_signal.connect(self.threadsts)  #连接信号
            self.serthread.start()  #启动线程
            self.statusBar.showMessage('打开串口成功', 5000)
            self.pushButton_22.setText('断开')
        else:
            self.serthread.threadFinish()  #线程退出标识符置位
            self.serthread.wait()  #等待线程退出

    def closeLink(self, current_index):
        '''
    当页面切换时 如果串口处于连接状态 关闭串口线程
    @参数
    current_index: 当前的页面序号
    '''
        if current_index != 0:
            if self.pushButton_22.text() == '断开':
                self.serthread.threadFinish()  #线程退出标识符置位
                self.serthread.wait()  #等待线程退出

    def zero_params_set(self):
        params = []
        for i in range(8):
            params.append(self.zero_param_shows[i].value())
        res = self.init_params_opter.configWrite(self.init_path, params)
        #重新读取参数
        self.zero_params = self.init_params_opter.configRead(self.init_path)
        for i in range(8):
            self.zero_param_shows[i].setValue(self.zero_params[i])

        if res:
            self.statusBar.showMessage('参数修改成功', 5000)
        else:
            self.statusBar.showMessage('参数修改失败', 5000)

    def sersearch(self):
        '''
    用于查询可用的串口名称 查询结果为字符串的形式
    '''
        serial_str = serialset.serialsearch()
        self.textBrowser.setText(serial_str)

    #数据回调函数
    def callBack(self, data: list):
        '''
    串口通信线程 每当串口通信线程内的数据获得更新时 
    将会发送信号调用该函数刷新gui界面
    '''
        #第一个数据为时间戳
        for i in range(8):
            if data[i + 1] != 0:
                data[i + 1] = data[i + 1] + self.zero_params[i]
                self.temperature_shows[i].setText(str(data[i + 1]))
            else:
                self.temperature_shows[i].setText('----')

        #设置当前主温度
        self.main_temperature = data[1]

        #如果记录标识符为True
        if self.is_recording == True:
            self.record_data_list.append(data)
            self.record_data_num += 1
            #自动记录（每5分钟保存一次）
            if (self.record_data_num + 1) % 300 == 0:
                csv_save_fullpath = function_dataanalysis.csvAutoSave(
                    self.lineEdit.text(), self.record_data_list)

            if self.record_data_num > 200000:
                self.recordOpt()  #调用数据记录函数，自动结束记录
                self.statusBar.showMessage('记录数据量超过200000组,自动结束记录', 5000)

    def reset_record_data(self):
        self.record_data_num = 0
        self.record_data_list = []  #重置记录的数据

    def recordOpt(self):
        '''
    数据记录槽函数
    根据按键文件 调用该函数后 改变 数据记录标识符 
    '''
        if self.is_recording == False:
            self.reset_record_data()  #重新记录 重置已经记录的数据
            self.is_recording = True
            self.pushButton_27.setText('完成记录')
            self.statusBar.showMessage('正在记录...', 5000)
            self.sttime = time.time()
        else:
            self.is_recording = False
            self.pushButton_27.setText('开始记录')
            self.statusBar.showMessage('完成记录', 5000)
            self.csvfileSave()  #自动进行一次提示保存的操作

    def savefolderOpen(self):
        '''
    测量数据界面的打开文件保存文件夹按钮
    '''
        try:
            if self.lineEdit_15.text() != '':
                folder_path = os.path.split(self.lineEdit_15.text())
                os.startfile(folder_path[0])
                self.statusBar.showMessage('打开保存目录', 5000)
        except Exception as e:
            self.statusBar.showMessage('路径有误,打开文件夹失败', 5000)

    def csvfileSave(self):
        '''
    保存csv文件
    '''
        # 保存确定框
        reply = QMessageBox.question(self, '保存', '确定保存？',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.Yes)
        if reply == QMessageBox.Yes:
            csv_save_fullpath = function_dataanalysis.csvSave(
                self.lineEdit.text(), self.record_data_list)
            self.statusBar.showMessage('已保存 路径名: ' + csv_save_fullpath, 5000)
        else:
            self.statusBar.showMessage('取消保存，在新的记录开始之前可以使用保存记录按钮保存本次数据 ', 5000)

    #程序退出提示
    def closeEvent(self, event):
        reply = QMessageBox.question(self, '信息', '确认退出吗？',
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            plt.close('all')
            event.accept()
        else:
            event.ignore()
