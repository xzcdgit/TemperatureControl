import time
from yaml import emit
from PyQt5.QtCore import QThread, pyqtSignal
import time


class PID:

    def __init__(self, kp, ki, kd, set_point=0, sample_time=0.01):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.set_point = set_point
        self.sample_time = sample_time
        self.reset()

    def pset(self, set_point):
        self.set_point = set_point

    def reset(self):
        self.p_term = 0.0
        self.i_term = 0.0
        self.d_term = 0.0
        self.last_error = 0.0
        self.output = 0.0
        self.last_time = time.time()

    def update(self, feedback):
        t = time.time()
        dt = t - self.last_time
        if dt < self.sample_time:
            return
        error = self.set_point - feedback
        delta_error = error - self.last_error
        self.p_term = self.kp * error
        self.i_term += self.ki * error * dt
        self.d_term = self.kd * delta_error / dt
        self.output = self.p_term + self.i_term + self.d_term
        self.last_error = error
        self.last_time = t

        #self.output特殊设置
        if self.output < 0:
            self.output = 0
        elif self.output > 100:
            self.output = 100


class TemperaturController(QThread):
    '''
  多线程类 继承自qt多线程类 主要用于在gui运行的同时 
  循环和串口进行通信并实时发送回gui线程以更新界面数据
  '''
    thread_sts_signal = pyqtSignal(int)  #线程状态信号
    current_temperature_signal = pyqtSignal(int)  #请求实时温度信号

    def __init__(self):
        '''
    构造函数

    '''
        super(TemperaturController, self).__init__()
        self.P = 3.25
        self.I = 0.04
        self.D = 120
        self.FRESH_TIME = 4

        self.current_point = 0
        self.quit_flag = False

    def set_params(self, p=0.6, i=0.04, d=0, fresh_time=4):
        self.P = p
        self.I = i
        self.D = d
        self.FRESH_TIME = fresh_time

    def judge_error(self):
        if self.current_point == 0:
            raise ValueError("当前温度异常")
        if self.quit_flag:
            self.quit_flag = False
            raise SystemError("手动终止")

    def set_quit(self):
        '''
    线程结束 标识符设定 线程结束后会自动反馈信号 改变主线程的ui显示
    '''
        self.quit_flag = True

    def clearflagSet(self, num: str):
        '''
    数据清零标识符设定
    '''
        self.clear_flag = num

    def set_current_point(self, current_point):
        self.current_point = current_point

    def get_current_point(self):
        self.current_temperature_signal.emit(1)
        return self.current_point

    def linear_heating(self, st_point: int, tar_point: int, tar_time: int):
        self.judge_error()
        current_point = self.get_current_point()
        if current_point > st_point:
            st_point = current_point
            print("起始温度小于当前温度，直接将起始温度设置为当前温度")

        pid = PID(self.P, self.I, self.D, set_point=st_point)
        #预热
        while current_point < st_point:
            self.judge_error()
            current_point = self.get_current_point()
            pid.update(current_point)
            print("预热阶段  目标温度{} 当前温度{} 设定功率{}".format(st_point, current_point,
                                                      pid.output))
            time.sleep(self.FRESH_TIME)

        print("到达起始温度，开始线性升温")

        #微分目标温度

        for part_time in range(tar_time):
            self.judge_error()
            sttime = time.time()
            increase_point = (tar_point - st_point) / tar_time
            part_point = st_point + increase_point * (part_time + 1)
            if tar_point <= part_point:
                part_point = tar_point
            pid.pset(part_point)
            while True:
                self.judge_error()
                current_point = self.get_current_point()
                pid.update(current_point)
                print("线性升温阶段  目标温度{} 阶段目标{} 当前温度{} 设定功率{}".format(
                    tar_point, part_point, current_point, pid.output))
                time.sleep(self.FRESH_TIME)
                
                current_time = time.time()
                if current_time - sttime >= 60:
                    break
        print("升温结束")

    def run(self):
        '''
    多线程 run方法重构
    '''
        try:
            self.thread_sts_signal.emit(1)
            self.linear_heating(10, 40, 2)
            self.linear_heating(40, 40, 2)
            self.linear_heating(40, 80, 2)
            self.thread_sts_signal.emit(-1)
        except Exception as e:
            print(e)
            self.thread_sts_signal.emit(-2)


if __name__ == '__main__':
    current_temperature = 0
    st_point = 0
    tar_point = 130
    tar_time = 50
    my_controler = TemperaturController()
    my_controler.set_current_point(10)
    my_controler.start()
    for i in range(10000000):
        my_controler.set_current_point(10+i*0.1)
        time.sleep(1)
