# Discrete-Event-Simulation
System with multiple machines – one is an active machine and the other is an inactive spare. The spare machine becomes active when the (currently) active machine fails, while the failed machine immediately starts repair. The failed machine becomes the spare when its repair is completed. Only one component at a time can be repaired, so the system as a whole fails if both components have failed, and it is operational as long as at least one of the components is working.
The time to failure of a machine can with equal probability be 2, 4, 6, 8 or 10 days, while repair takes exactly 3.5 days. A repaired machine is as good as new.
Average time to failure is calculated with 5 machines (100 replications) 

Done in python.
So we had to make the spare machines functional whenever a working machine failed. We were simultaneously adding up the total time.
And there occurred a time where all the working machines had failed and by then none of the failed machines had been repaired. So that was the average failure time Also, I had calculated the averge no. of machine that entire time duration. 
This was implemented using different functions for repair and failure and functions that would call the respective functions, i.e. failure and events according to the demand of the situation
