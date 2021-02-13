import _thread
import logging
import threading
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)     #定义日志打印级别为INFO

loops = [2,4]       #设置两个循环秒数，第一个读取的值为loop0,第二个为loop1

class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def loop(nloop,nsec):
    logging.info("start loop " + str(nloop) + " at " + ctime())     #ctime为time标准库中的当前时间方法
    sleep(nsec)
    logging.info("end loop" + str(nloop) + " at " + ctime())

def main():
    logging.info("start all at" +  ctime())
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = MyThread(loop, (i,loops[i]), loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()       #加锁步骤
    logging.info("end all at" + ctime())

if __name__=='__main__':
    main()


#原语
#锁，解决数据互斥访问
#信号量
