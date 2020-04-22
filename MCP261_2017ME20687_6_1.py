import numpy as np
import math
import random
from scipy.stats import ttest_1samp



def Failure():
    global Clock              #simulation clock
    global NextFailure      # time of next failure event
    global NextRepair       #time of next repair event
    global S                #system state
    global Slast            #previous value of the system state
    global Tlast            #time of previous state change
    global Area 
    global Sinit            # area under S(t) curve
    
    S = S - 1
    b=np.argmax(NextRepair)
    c=np.argmin(NextRepair)
    if (S<Sinit and S>0):
        NextFailure = Clock + 2*math.ceil(5 *random.random())
        NextRepair[c] = NextRepair[b] + 3.5
    Area = Area + Slast * (Clock - Tlast)
    Tlast = Clock
    Slast = S
    #return {S, NextFailure, NextRepair}
def Repair():
    
    global Clock             # simulation clock
    global NextFailure      #Time of next failure event
    global NextRepair       # time of next repair event
    global S                # system state
    global Slast            # previous value of the system state
    global Tlast            #time of previous state change
    global Area             # area under S(t) curve# Repair event
#Update state and schedule future events
    S = S + 1
    if (S == 1):
        NextRepair = Clock + 3.5
        NextFailure = Clock + 2*math.ceil(5 * random.random())
        
            
            #Update area under the S(t) curve
        Area = Area + Slast * (Clock - Tlast)
        Tlast = Clock
        Slast = S
# Schedule the initial failure event
def Timer():
    
    Infinity = 1000000;
    global Clock             # simulation clock
    global NextFailure      #Time of next failure event
    global NextRepair 
    repair=np.zeros(Sinit) 
    i=0
    while(i<Sinit):
        repair[i]=abs(NextRepair[i])
        i=i+1
    a= np.argmin(repair)   # time of next repair event
    
#Determine the next event and advance time
    
    if (NextFailure < abs(NextRepair[a])):
        y = 'Failure'
        Clock = NextFailure
        NextFailure = Infinity
    else:
        y = 'Repair'
        Clock = NextRepair[a]
        NextRepair[a] = -Infinity;
    return y;


    

Infinity = 1000000;
random.seed(1235)
SumS = 0
SumY = 0
n=5
i=1
time=[]
while i<101:
    S = n
    Slast = n
    Sinit=n
    Clock = 0.0
    Tlast = 0.0
    Area = 0.0
    NextFailure = 2*math.ceil(5 * random.random())
    NextRepair = np.full(n,((-1)*Infinity),dtype=float)
    NextRepair[0]=NextFailure+3.5
    Clock=NextFailure
    S=S-1
    NextFailure =Clock+ 2*math.ceil(5 * random.random())
    

    

    while S > 0:
        NextEvent = Timer()
        if NextEvent == "Failure":
            Failure()
        else:
            Repair()
    SumS = SumS + Area / Clock
   
    #print(time)
    SumY = SumY + Clock
    time.append(Clock)
    i=i+1
print("Average failure at time:",SumY/100)
