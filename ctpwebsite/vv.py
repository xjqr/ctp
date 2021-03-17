from .md import *
from multiprocessing import process
#import threading
# class datarun(threading.Thread):

#     def __init__(self,threadID,threadname):
#         threading.Thread.__init__(self)
#         self.threadid=threadID
#         self.threadname=threadname

#     def run(self):
#         main()
#         return super().run()
    
class datarun(process):

    def __init__(self):
        super().__init__()

    def run(self):
        print('7')
        for i in range(900):
            pass
        print('9')


        