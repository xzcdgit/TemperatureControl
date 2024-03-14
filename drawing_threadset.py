from yaml import emit
from PyQt5.QtCore import QThread, pyqtSignal
import time
import numpy as np
import matplotlib.pyplot as plt


class MyThread(QThread):
    '''
  多线程类 继承自qt多线程类 主要用于在gui运行的同时 
  循环和串口进行通信并实时发送回gui线程以更新界面数据
  '''
    data_signal = pyqtSignal(list)  #串口获得的数据反馈给主线程的信号
    finish_signal = pyqtSignal(int)  #线程结束信号

    def __init__(self, parent=None):
        '''
    构造函数
    @参数
    portname: 端口号
    baudrate: 波特率
    '''
        super(MyThread, self).__init__(parent)
        self.run_flag = True
        self.clear_flag = 0
        self.points = np.array([])

    def threadFinish(self):
        '''
    线程结束 标识符设定 线程结束后会自动反馈信号 改变主线程的ui显示
    '''
        self.run_flag = False
    def pointInfo(self, points:list):
        #points结构[[时间戳，值1，值2...值4],...]
        self.points = np.array(points)

    def clearflagSet(self, num: str):
        '''
    数据清零标识符设定
    '''
        self.clear_flag = num

    def run(self):
        '''
    多线程 run方法重构
    '''
        print("drawing start")
        #创建画布
        sttime = time.time()
        
        while True:
            if self.run_flag == False:
                break
            try:
                if len(self.points[0]) > 0:
                    x = self.points[:, 0] - sttime
                    y1 = self.points[:, 0]
                    y2 = self.points[:, 1]
                    y3 = self.points[:, 2]
                    plt.plot(x,y1,x,y2,x,y3)
                    plt.show()
                else:
                    time.sleep(2)
            except Exception as e:
                time.sleep(2)
            
            
            
            #time.sleep(2)  #每秒刷新一次数据
            #print(time.time()-st)
        #self.serialopt.serialClose()
        #self.finish_signal.emit(1)
        self.run_flag == True
        print("drawing quit")
