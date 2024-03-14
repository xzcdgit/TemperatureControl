#from matplotlib import lines
#from numpy.lib.function_base import angle
import pandas as pd
import time
import os
import shutil
def txtSave(filepath:str,txtstring:str):
    '''
    保存txt文件
    @param
    filepath: 保存路径
    txtstring: 需要保存的字符串
    '''
    fw = open(filepath,'w')
    fw.write(txtstring) #字符串写入文件
    print(filepath)
    fw.close()
def readCsv(pathname:str):
    '''
    函数功能: 读取csv文件的内容
    pathname: csv文件的路径地址
    return: 以dataframe的格式返回csv文件的内容
    '''
    data = pd.read_csv(pathname)
    return data
def fileSave(ori_filepath:str, save_filepath:str):
    '''
    函数功能: 保存（复制）文件
    ori_filepath: 源文件路径地址
    save_filepath: 目标路径地址
    '''
    shutil.copy(ori_filepath,save_filepath)
def listTofile(data_list:list,pathname:str):
    '''
    函数功能: 将list数据保存为csv文件
    data_list: 需要保存的数据
    pathname: 文件保存路径
    '''
    datalist = transList(data_list)
    datalist.to_csv(pathname,index=False)
##########################################################################
def csvSave(pathname:str,data_list:list):
    '''
    函数功能: 将数据列保存为文件（专用特殊）
    data_list: 需要保存的数据
    pathname: 文件保存路径（文件夹路径）
    return: 完整的文件路径名
    '''
    crename = time.strftime("%Y%m%d", time.localtime()) #文件夹名（日期）
    mkDir(pathname+'\\'+crename)   #创建文件夹
    foldername = pathname+'\\'+crename        #完整文件夹路径名
    filename = fileName(foldername)                    #新文件名
    filepath = pathname+'\\'+crename+'\\'+filename #完整文件路径名
    datalist = transList(data_list) #数据转换
    datalist.to_csv(filepath,index=False) #保存数据
    return filepath

def csvAutoSave(pathname:str,data_list:list):
    '''
    函数功能: 将数据列保存为文件（专用特殊）
    data_list: 需要保存的数据
    pathname: 文件保存路径（文件夹路径）
    return: 完整的文件路径名
    '''
    crename = time.strftime("%Y%m%d", time.localtime()) #文件夹名（日期）
    mkDir(pathname+'\\'+crename)   #创建文件夹
    foldername = pathname+'\\'+crename        #完整文件夹路径名
    filename = autoFileName(foldername)                    #新文件名
    filepath = pathname+'\\'+crename+'\\'+filename #完整文件路径名
    datalist = transList(data_list) #数据转换
    datalist.to_csv(filepath,index=False) #保存数据
    return filepath

def transList(datalist:list)->pd.DataFrame:
    '''
    list列表转换为panda.DataFrame
    @param 
    datalist: 输入的list数据
    @return
    dataframe: 增加列名并返回dataframe格式的数据
    '''
    
    name=['timestamp'] + ['input'+str(i+1) for i in range(len(datalist[0])-1)]
    datalist = pd.DataFrame(columns=name,data=datalist)
    return datalist
def mkDir(fullpath:str): 
    '''
    创建文件夹
    @param
    fullpath: 需要创建的文件夹地址
    ''' 
    import os
    path = fullpath
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
    # 判断结果
    if not isExists:
      # 如果不存在则创建目录
      # 创建目录操作函数
      os.makedirs(path) 
      return 1,fullpath
    else:
      # 如果目录存在则不创建，并提示目录已存在
      return 0,fullpath
  
def fileName(file_dir:str):
    '''
    文件重命名函数（如果已有同名文件则文件名+1）专用
    @参数
    file_dir: 文件夹路径
    ''' 
    for root, dirs, files in os.walk(file_dir): 
        pass
    i = 1
    savename = '1.csv'
    while True:
        samename_flag = False
        for j in files:
            if j == savename:
                i =i+1
                savename = str(i)+'.csv'
                samename_flag = True
                break
        if samename_flag == False:
            return savename
        
        
def autoFileName(file_dir:str):
    '''
    文件重命名函数（如果已有同名文件则文件名+1）专用
    @参数
    file_dir: 文件夹路径
    ''' 
    for root, dirs, files in os.walk(file_dir): 
        pass
    i = 1
    savename = 'auto_1.csv'
    while True:
        samename_flag = False
        for j in files:
            if j == savename:
                i =i+1
                savename = 'auto_'+str(i)+'.csv'
                samename_flag = True
                break
        if samename_flag == False:
            return savename