import numpy as np
import time
import random 
import threading 
import concurrent.futures 

class Peripherial:
    failed = False 
    occupied = False 
    def __init__(self, index, beta, time_job, reboot):
        self.index = index
        self.beta = beta
        self.time_job = time_job
        self.reboot = reboot
        self.p1 = threading.Thread(target=self.failing)
    
    def failing(self):
        while(True):
            time_to_fail = np.random.exponential(self.beta, None)
            time.sleep(time_to_fail)
            print(f"failing {self.index}")
            self.failed = True
            time.sleep(self.reboot)
            self.failed = False
            print(f"restarted {self.index}")
            

    def execute_job(self, job):
        if self.failed == False: 
            self.occupied = True
            A = np.random.randint(100, size=(10))
            B = np.random.randint(100, size=(10))
        
            if job == 1:
                self.sum_vec(A, B)
            elif job == 2:
                self.dot_product(A, B)
            elif job == 3:
                X = np.random.randint(100, size=(4,4))
                Y = np.random.randint(100, size=(4,4))
                self.multiply(X, Y)
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
                print(t.result())
        print("first")
        for a in first:
            print(a)
        print("second")
        for a in second:
            print(a)
        print("result")
        for a in result:
            print(a)

    def add(self, a, b):
        return (a + b)    
       
    def dot_product(self, first, second):
       result =  sum([x*y for x,y in zip(first,second)])
    
       
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
        for i in range(num_p):
            self.peripherial.append(Peripherial(i, 4, 2, 2))


    def fails(self):
        while(self.turned_on):
            time_to_fail = np.random.exponential(self.gamma, None)
            print(f"FAILING...failing before:)")
            time.sleep(time_to_fail)
            print(f"FAILING...failing central")
            self.failed = True
            print(f"restarted ")
            time.sleep(self.reboot)
            self.failed = False

    def intialize_job_generator(self):
        jobs = [1,2,3]
        while(self.turned_on):
            s = np.random.poisson(self.alpha)
            time.sleep(s)
            j = random.choice(jobs)
            print(f"INITIALIZING...append job {j} waited this amount of time {s}")
            self.do.append(j)
        


    def distribute_job(self):
        while(self.turned_on):
            if self.failed == False:
                time.sleep(self.delta)
                if self.do:
                    to_do = self.do.pop(0)
                    while self.peripherial[self.counter].occupied == True:
                        self.counter += 1 
                        if self.counter == self.num_p - 1:
                            self.counter = 0
                    if self.peripherial[self.counter].occupied == False:
                        print(f"DISTRIBUTING... this is the {to_do} job, executed by {self.counter} computer ")
                        self.peripherial[self.counter].execute_job(to_do)
                        self.counter += 1
                    if self.counter == self.num_p - 1:
                        self.counter = 0 
                else: 
                    print("NO JOB TO BE DONE")
                    
     
    
    def turn_on(self):
        self.p1.start()
        self.p2.start()
        self.p3.start()

          

    def turn_off(self):
        self.turned_on = False
        self.p1.join()
        self.p2.join()
        self.p3.join()


c = Central(5, 5, 5, 5, 4)
# c.intialize_job_generator()
# c.distribute_job()

p = Peripherial(0, 3, 3, 3)
p.execute_job(1)

