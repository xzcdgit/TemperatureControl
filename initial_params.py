#专用配置文件读取写入文件
import configparser
import os


class IniSetUp(object):
    '''
  配置文件操作类 用于读取或者写入配置文件的内容 内容固定 专用于相关程序
  '''

    def __init__(self):
        '''
    构造函数
    @参数
    config_path: ini配置文件的完整地址路径
    '''
        pass
        #self.config_path = config_path  #ini文件的地址
        #self.configRead()  #实例化时即执行读取ini文件参数内容
        
    def configInit(self, config_path:str):
        with open(config_path, 'w') as f:
            f.write('[ZeroTrim]\ninput1 = 0\ninput2 = 0\ninput3 = 0\ninput4 = 0\ninput5 = 0\ninput6 = 0\ninput7 = 0\ninput8 = 0\n')
        

    def configRead(self, config_path) -> list[float]:
        '''
    读取特定ini配置文件的内容
    '''
        if os.path.exists(config_path) == False:
            self.configInit(config_path)
            
        config = configparser.RawConfigParser()
        config.read(config_path, encoding="utf-8")
        res = []
        for i in range(8):
            res.append(float(config["ZeroTrim"]["input"+str(i+1)]))
        return res

    def configWrite(self, config_path, values:list[float]):
        '''
    将修改后的配置文件内容覆盖掉原来的内容
    原本不存在的内容将被新建
    '''
        if len(values) == 8:
            with open(config_path, 'w') as f:
                f.write('[ZeroTrim]\ninput1 = {}\ninput2 = {}\ninput3 = {}\ninput4 = {}\ninput5 = {}\ninput6 = {}\ninput7 = {}\ninput8 = {}\n'.format(*values))
            return 1
        else:
            return 0

if __name__ == '__main__':
    my_test = IniSetUp()
    res = my_test.configRead('initset.ini')
    print(res)
    my_test.configWrite('initset.ini',[1,2,3,4,5,6,7,8])