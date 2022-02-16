from ctypes import wintypes
import subprocess

import pandas as pd
import numpy as np
import time 
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from request5.rakuten_rss import rss , rss2 
from lib.ddeclient import DDEClient
import datetime


#並列処理
def get_lines(cmd):
    '''
    :param cmd: str 実行するコマンド.
    :rtype: generator
    :return: 標準出力 (行毎).
    '''
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    while True:
        line = proc.stdout.readline()
        if line:
            yield line

        if not line and proc.poll() is not None:
            break
    return





#dde_ware = []

def Main(k):
        
    calc = 0
        #dde_ware, calc = rss("現在値",k)[0], rss("現在値",k)[1]
    #print(k)
    return rss("現在値",k)    
        
    



def calculation(dde_ware, indexes_weight):
        #t1 = time.time()
    calc = rss2("現在値",0, dde_ware, indexes_weight)
            
        #t2 = time.time()
    return calc

if __name__ == '__main__':  
    args = sys.argv
    count = int(args[2])*126 
    num = args[1]
    temp = 0
    #t1 = time.time()
    if int(num) == 0:
        if count <= 2142:
            for line in get_lines(cmd='python main2.py ' + str(count)+ ' T'): # ファイル読み込み　第一引数はスタートナンバー                
                string = "file_"+ str(int(num) + int(args[2])) + ".txt"
                f = open(string, 'w')
                temp = line.decode('sjis')
                print(temp)
                f.write(temp.rstrip('\n'))
                f.close() 
                    #print(count)
                    #time.sleep(0.1)
                #firstLoop = False
                firststep = True
            #count += 126
            if False:
                proc = subprocess.Popen('python main3.py '+ str(count), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                #count = 0
                
            #break
        #while True
                result = proc.communicate()[0].decode('sjis')
                #break
                #print(result)
                #temp += 1
        #t2 = time.time()
        #print("present time:"+ str(t2),float(result)+61.18* 0.01)
        #count = 0
    else:
        a = 0
        while a <= 10**5:
            proc = subprocess.Popen('python main3.py '+ str(0), shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            result = proc.communicate()[0].decode('sjis')
            dt = datetime.datetime.today()
            with open("fileX.txt", "a") as f:
                f.write(str(float(result)+61.18* 0.01))
            print("present time:"+ str(dt),float(result)+61.18* 0.01)
            time.sleep(1.5)
            a += 1
    



