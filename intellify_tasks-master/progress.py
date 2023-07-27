import PySimpleGUI as sg
import time
mylist = [1,2,3,4,5,6,7,8]
for i, item in enumerate(mylist):
    sg.one_line_progress_meter('This is my progress meter!', i+1, len(mylist), '-key-')
    time.sleep(1)
    print(i)
    

import time
from tqdm import tqdm
mylist = [1,2,3,4,5,6,7,8]
s = input("Begin Download: Y/N? ")
if s=='Y':
    print("Downloading")
    for i in tqdm(mylist):
        time.sleep(1)
    print("Downloaded")
else :
    exit()
    

import time
import sys
from tqdm import trange


def do_something():
    time.sleep(1)

def do_another_something():
    time.sleep(1)


for i in trange(10, file=sys.stdout, desc='outer loop'):
    do_something()

    for j in trange(100,file=sys.stdout, leave=False, unit_scale=True, desc='inner loop'):
        do_another_something()
        
        
import time

from random import randrange
from multiprocessing.pool import ThreadPool

from tqdm import tqdm


def func_call(position, total):
    text = 'progressbar #{position}'.format(position=position)
    with  tqdm(total=total, position=position, desc=text) as progress:
        for _ in range(0, total, 5):
            progress.update(5)
            time.sleep(randrange(3))


pool = ThreadPool(10)
tasks = range(5)
for i, url in enumerate(tasks, 1):
    pool.apply_async(func_call, args=(i, 100))
pool.close()
pool.join()