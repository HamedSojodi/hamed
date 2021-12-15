#lass range:
#   def __init__(self, start:int , end:int=None, step:int=1 ):

#       self.start=start
#       self.end=end
#       self.step=step



#   def __iter__(self):
#       self.start=self.start
#       return self


#   def __next__(self):
#       self.start +=self.step
#       if self.start > self.end:
#           raise StopIteration()
#       return self.start




#_iter=range(3, 10, 1)
#or x in m_iter:
#   print(x)

#mport datetime
#rom time import sleep
#mport logging

#ogging.basicConfig(level=logging.ERROR)

#lass ProcessTime:

#   @property
#   def elapsed_time(self):
#       return datetime.datetime.now()-self.now

#   def __enter__(self):
#       self.now=datetime.datetime.now()
#       return self.now

#   def __exit__(self, exc_type, exc_val, exc_tb):
#       if exc_type:
#           logging.error(exc_type,exc_val)

#       else:
#           return  self.elapsed_time
#       return True


#_timer=ProcessTime()
import datetime
from time import sleep

def process_timer(func):
    def wraaper_func():
        res=func(datetime.datetime.now()-datetime.datetime.now())
        return res

    return wraaper_func




@process_timer
def primals(n:int):
    for num in range(n +1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)

print(primals())





