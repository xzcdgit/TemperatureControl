from cProfile import label
import time
from turtle import width
import numpy as np
import matplotlib.pyplot as plt
from subprocess import PIPE, Popen, DEVNULL

from numpy import append


def run(cmd, retype="r"):
    '''run System Command and Return Command Stdout Object'''
    try:
        with Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE, encoding="utf-8") as f:
            Ret_Type = {"r": f.stdout.read, "rl": f.stdout.readline, "rls" : f.stdout.readlines, "rc": f.wait}
            if retype == 're':
                return f.stdout.read() + f.stderr.read()
            return Ret_Type[retype]()
    except Exception as e:
        print("\033[31mExecute Err:%s\033[0m"%e)


class DeltaPid(object):
    '''
        PID calculate
        pwm = pre_pwm + kp*(err-pre_ee) + ki*err + kd*(err-2*pre_err+pre_pre_ee)
    '''
    def __init__(self, target_temp, max_pwm, min_pwm, p, i, d):
        self.max_pwm = max_pwm
        self.min_pwm = min_pwm
        self.k_p = p
        self.k_i = i
        self.k_d = d
        self.target_temp = target_temp
        self._pre_temp = target_temp
        self._pre_pre_temp = target_temp - 1

    def calculate(self, cur_temp, pwm_in):
        # pwm = pre_pwm + kp*(err-pre_ee) + ki*err + kd*(err-2*pre_err+pre_pre_ee)
        pwm_out = 0
        p_change = self.k_p * (cur_temp - self._pre_temp)
        i_change = self.k_i * (cur_temp - self.target_temp)
        d_change = self.k_d * (cur_temp - 2 * self._pre_temp + self._pre_pre_temp)
        print(f"p:{p_change} i:{i_change} d:{d_change}")

        delta_output = p_change + i_change + d_change
        print(f"p+i+d output={delta_output}")

        pwm_out = delta_output + pwm_in
        print(f"calculate pwm={pwm_out}")
        self._pre_pre_temp = self._pre_temp
        self._pre_temp = cur_temp

        pwm_out = self.max_pwm if pwm_out > self.max_pwm else (self.min_pwm if pwm_out < self.min_pwm else pwm_out )
        print(f"actual output pwm={pwm_out}")

        return pwm_out


class Pwm(object):
    '''
        function1: set and get fan and heater pwm
        function2: get socket temp
    '''
    def __init__(self, path):
        self.path = f"{path}"
        self.fan_en = []
        self.heater_en = []
        self.fan_pwm = []
        self.heater_pwm = []
        self.temp = []
        for i in range(1, 5):
            self.fan_en.append(f"{self.path}fan{i}_en")
            self.heater_en.append(f"{self.path}heater{i}_en")
            self.fan_pwm.append(f"{self.path}fan{i}_pwm")
            self.heater_pwm.append(f"{self.path}heater{i}_pwm")
            self.temp.append(f"{self.path}temp{i}")

    def en_fan(self, index):
        cmd = f"echo 100 > {self.fan_en[index - 1]}"
        run(cmd)

    def en_heater(self, index):
        cmd = f"echo 100 > {self.heater_en[index - 1]}"
        run(cmd)

    def get_temp(self, index):
        return 0
        cmd = f"cat {self.temp[index - 1]}"
        return run(cmd).replace('\n', '')

    def get_fan_pwm(self, index):
        cmd = f"cat {self.fan_pwm[index - 1]}"
        return run(cmd).replace('\n', '')

    def set_fan_pwm(self, pwm, index):
        cmd = f"echo {pwm} > {self.fan_pwm[index - 1]}"
        run(cmd)

    def get_heater_pwm(self, index):
        cmd = f"cat {self.heater_pwm[index - 1]}"
        return run(cmd).replace('\n', '')

    def set_heater_pwm(self, pwm, index):
        cmd = f"echo {pwm} > {self.heater_pwm[index - 1]}"
        run(cmd)


def filter(index, limit):
    usb_path = "/sys/dev/char/USB0/USB/"
    pwm = Pwm(usb_path)
    temp = []
    for i in range(0, 7):
        temp_old = int(pwm.get_temp(index))
        temp_new = int(pwm.get_temp(index))
        print(temp_old, temp_new)
        if abs(temp_old - temp_new) < limit: 
            temp.append(temp_old)
            temp.append(temp_new)
    print(temp)
    if not temp:
        return int(pwm.get_temp(index))
    return int(sum(temp)/len(temp))


def test(count=5000, target_temp = 105):
    usb_path = "/sys/dev/char/USB0/USB/"
    pwm = Pwm(usb_path)
    counts = np.arange(count)
    outputs = []
    pwms = []
    # enable fan and heater
    pwm.en_fan(1)
    pwm.en_heater(1)

    # initial fan and heater pwm
    pwm.set_fan_pwm(0, 1)
    pwm.set_heater_pwm(100, 1)

    pid = DeltaPid(target_temp, 45, 5, 10, 0.7, 0.3)
    print(f"Now temp is {pwm.get_temp(1)}")
    print("start test ...")
    print(f"set heater pwm to 100, target temp is {target_temp} ...")

    # set temp to (target) and keep heater in 80 pwm
    print(f"time: {time.ctime()}")
    while True:
        temp1 = filter(1, 20)
        print(f"Now temp is {temp1}")
        time.sleep(1)
        if temp1 / 10 >= (target_temp):
            print("keep heater pwm to 80 ...")
            pwm.set_fan_pwm(35, 1)
            pwm.set_heater_pwm(80, 1)
            break
            # draw
    print(f"time: {time.ctime()}")

    for i in counts:
        print(f"No.{i} pid adjust")
        temp1 = filter(1, 20)
        now_fan_pwm = int(pwm.get_fan_pwm(1))
        pwms.append(now_fan_pwm)
        print(f"temp={temp1}C , fan pwm={now_fan_pwm}")
        now_pwm = pid.calculate(int(temp1) / 10, now_fan_pwm)
        pwm.set_fan_pwm(int(now_pwm), 1)
        time.sleep(1)
        outputs.append(int(temp1) / 10)

    print('Done')

    # draw
    plt.figure()
    plt.axhline(target_temp, c='red', label = "target_temp")
    plt.axhline(target_temp-3, c='yellow', label = "target_temp_min")
    plt.axhline(target_temp+3, c='red', label = "target_temp_max")
    plt.plot(counts, np.array(outputs), 'b.')
    plt.ylim(0, 130)
    plt.plot(counts, outputs, label = "temp")
    plt.plot(counts, pwms, label = "pwm")
    plt.title("PID")
    plt.xlabel('count')
    plt.ylabel('temperature')
    plt.legend()
    plt.tick_params(axis='both', width=1, length=5)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    plt.show()


if __name__ == "__main__":
    test()