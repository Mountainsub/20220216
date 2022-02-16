import subprocess
import asyncio
import multiprocessing
import threading
import pandas as pd
import numpy as np
import time 
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from request5.rakuten_rss import rss , rss2 
from lib.ddeclient import DDEClient


if __name__ == "__main__":
    s = 0
    args = sys.argv 
    num = int(args[1])
    count, temp = num, num
    """
    if args[1] == "T":
        count = 0
        temp = 0
    else:
        count = 100
        temp=100
    """
    while count <= temp + 16: 
        try:
            with open('file_'+ str(count) + '.txt', 'r') as f:                           
                try:
                    """
                    for line in f:
                        pass
                    a = float(line)
                    """
                    a = f.readline()
                    count += 1
                    s += float(a)
                except:
                    continue
        except:
            pass
    print(s)

