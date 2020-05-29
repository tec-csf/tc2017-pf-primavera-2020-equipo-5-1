import numpy as np
import time
import random 
import threading 
import concurrent.futures 
import multiprocessing
import ctypes

class Peripherial:
    failed = False 
    occupied = False 
    part = 0
    threadNumber = 0
    def __init__(self, index, beta, time_job, reboot):
        self.index = index
        self.beta = beta
        self.time_job = time_job
        self.current_job = 0
        self.reboot = reboot
        self.fail = threading.Thread(target=self.failing)
        self.executing = threading.Thread(target=self.execute_job)
        
  
    def turned_on(self):
        self.fail.start()
        self.executing.start()
    
    def turn_off(self):
        self.fail.join()
        self.executing.join()

    def failing(self):
        while(True):
            time_to_fail = np.random.exponential(self.beta, None)
            time.sleep(time_to_fail)
            print(f"COMPUTER  {self.index} failing after {time_to_fail} interrupted {self.current_job}")
            self.failed = True
            self.current_job = 0
            time.sleep(self.reboot)
            self.failed = False
            print(f"COMPUTER  {self.index}  restarted")
            
    def assign_job(self, job):
        print(f"COMPUTER  {self.index}  job assigned {job}")
        self.current_job = job

    def execute_job(self):
        while(True):
            if self.failed == False and self.occupied == False and self.current_job != 0: 
                self.occupied = True
                A = np.random.randint(100, size=(3))
                B = np.random.randint(100, size=(3))
        
                if self.current_job == 1:
                    self.sum_vec(A, B)
                    print(f"COMPUTER  {self.index}  sum vectors 1")
                    self.current_job = 0
                elif self.current_job == 2:
                    self.dot_product(A, B)
                    print(f"COMPUTER  {self.index}  dot product 2")
                    self.current_job = 0
                elif self.current_job == 3:
                    X = np.random.randint(100, size=(4,4))
                    Y = np.random.randint(100, size=(4,4))
                    self.multiply(X,Y)
                    print(f"COMPUTER  {self.index}  multiply matrix 3")
                    self.current_job = 0
                else: 
                    print("none of the above")
                self.occupied = False 

    def multiply(self, A, B):
        result = [[0 for x in range(len(A))] for y in range(len(B[0]))] 
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    result[i][j] += A[i][k] * B[k][j] 


    
    def sum_vec(self, first, second):
        result = [0  for row in range(len(first))]
        
        with concurrent.futures.ThreadPoolExecutor(max_workers = len(first)) as executor:
            for i in range(len(first)):
                t = executor.submit(self.add, first[i], second[i])
                result[i] = t.result()

    def add(self, a, b):
        return (a + b)    
       
    def dot_product(self, first, second):
        result = 0
        with concurrent.futures.ThreadPoolExecutor(max_workers = len(first)) as executor:
             for i in range(len(first)):
                t = executor.submit(self.acum_sum, first[i], second[i], result)
                result = t.result()
    
    def acum_sum(self, a, b, result):
        return result+(a*b)
    
       
class Central: 
    def __init__(self, num_p, alpha, delta, reboot, gamma):
        self.num_p = num_p
        self.alpha = alpha
        self.gamma = gamma
        self.delta = delta
        self.reboot = reboot
        self.turned_on = True
        self.failed = False
        self.counter = 0
        self.do = []
        self.failing = False
        self.peripherial = []
        self.p1 = threading.Thread(target=self.fails)
        self.p2 = threading.Thread(target=self.intialize_job_generator)
        self.p3 = threading.Thread(target=self.distribute_job)
        self.p4 = threading.Thread(target=self.connect_peripherals)
        for i in range(num_p):
            self.peripherial.append(Peripherial(i, 100, 2, 20))

    def connect_peripherals(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers = self.num_p) as executor:
            for i in range(self.num_p):
                executor.submit(self.peripherial[i].turned_on)

    def fails(self):
        while(self.turned_on):
            time_to_fail = np.random.exponential(self.gamma, None)
            time.sleep(time_to_fail)
            print(f"CENTRAL FAILING...failing central")
            self.failed = True
            print(f"CENTRAL FAILING...restarted ")
            time.sleep(self.reboot)
            self.failed = False

    def intialize_job_generator(self):
        jobs = [1,2,3]
        while(self.turned_on):
            s = np.random.poisson(self.alpha)
            time.sleep(s)
            j = random.choice(jobs)
            print(f"CENTRAL INITIALIZING...append job {j} waited this amount of time {s}")
            self.do.append(j)
        


    def distribute_job(self):
        while(self.turned_on):
            if self.failed == False:
                time.sleep(self.delta)
                if self.do:
                    to_do = self.do.pop(0)
                    while self.peripherial[self.counter].occupied == True:
                        self.counter += 1 
                        if self.counter == self.num_p:
                            self.counter = 0
                    if self.peripherial[self.counter].occupied == False:
                        print(f"CENTRAL DISTRIBUTING... this is the {to_do} job, executed by {self.counter} computer ")
                        self.peripherial[self.counter].assign_job(to_do)
                        self.counter += 1
                    if self.counter == self.num_p:
                        self.counter = 0 
                else: 
                    print("CENTRAL DISTRIBUTING... NO JOB TO BE DONE")
                    
     
    
    def turn_on(self):
        self.p1.start()
        self.p2.start()
        self.p3.start()
        self.p4.start()

    def turn_off(self):
        self.turned_on = False
        self.p1.join()
        self.p2.join()
        self.p3.join()
        self.p4.join()
        with concurrent.futures.ThreadPoolExecutor(max_workers = self.num_p) as executor:
            for i in range(self.num_p):
                executor.submit(self.peripherial[i].turn_off)




c = Central(4, 3, 3, 3, 50)
c.turn_on()
time.sleep(100)
c.turn_off()

