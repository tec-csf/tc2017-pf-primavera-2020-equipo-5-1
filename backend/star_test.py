import numpy as np
import time
import random 
import threading 
import concurrent.futures 
import multiprocessing as mp
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
        self.status = []
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
            self.status.append(0) 
            self.failed = True
            self.current_job = 0
            time.sleep(self.reboot)
            self.failed = False
            self.status.append(1) 
            
    def assign_job(self, job):
        self.status.append(2)
        self.current_job = job

    def execute_job(self):
        while(True):
            if self.failed == False and self.occupied == False and self.current_job != 0: 
                self.occupied = True
                A = np.random.randint(100, size=(3))
                B = np.random.randint(100, size=(3))
        
                if self.current_job == 1:
                    self.sum_vec(A, B)
                    self.status.append(3) 
                    self.current_job = 0
                elif self.current_job == 2:
                    self.dot_product(A, B)
                    self.status.append(4)
                    self.current_job = 0
                elif self.current_job == 3:
                    global X, Y
                    X = np.random.randint(100, size=(4,4))
                    Y = np.random.randint(100, size=(4,4))
                    self.multiply(X,Y)
                    self.status.append(5)
                    self.current_job = 0
                else: 
                    self.status.append(6)
                self.occupied = False 

    def multiply(self, A, B):
        result = [[0 for x in range(len(A))] for y in range(len(B[0]))] 
        with concurrent.futures.ThreadPoolExecutor(max_workers = len(A)) as executor:
             for i in range(len(A)):
                t = executor.submit(self.row_multiply, i, A, B)
                result[i] = t.result()

    def row_multiply(self, row, A, B):
        result_row = [0 for y in range(len(B[0]))] 
        for j in range(len(B[0])):
            for k in range(len(B)):
                result_row[j] += A[row][k] * B[k][j]
        return result_row


    
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
    def __init__(self, num_p, alpha, delta, reboot, gamma, beta):
        #number of computers in star topology 
        self.num_p = num_p
        #initialize jobs every alpha 
        self.alpha = alpha
        #failing every gamma
        self.gamma = gamma
        #distribute jobs every delta 
        self.delta = delta
        #constant time of failure 
        self.reboot = reboot

        self.status = []
        
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
            self.peripherial.append(Peripherial(i, beta, 2, reboot))

    def connect_peripherals(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers = self.num_p) as executor:
            for i in range(self.num_p):
                executor.submit(self.peripherial[i].turned_on)

    def fails(self):
        while(self.turned_on):
            time_to_fail = np.random.exponential(self.gamma, None)
            time.sleep(time_to_fail)
            self.status.append(0)
            self.failed = True
            self.status.append(1)
            time.sleep(self.reboot)
            self.failed = False

    def intialize_job_generator(self):
        jobs = [1,2,3]
        while(self.turned_on):
            s = np.random.poisson(self.alpha)
            time.sleep(s)
            j = random.choice(jobs)
            self.status.append(2)
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
                        self.status.append(3)
                        self.peripherial[self.counter].assign_job(to_do)
                        self.counter += 1
                    if self.counter == self.num_p:
                        self.counter = 0 
                else: 
                    self.status.append(4)
                    
     
    
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




