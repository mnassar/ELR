
#!/usr/bin/env python 
import numpy as np  
import random 
m=100
X= np.array ( [ [1, x/10.] for x in range(m+1) ] ) 
y = np.array ( [ [2*x[1] + 1] for x in X] )  


theta = np.array ( [ [random.random()],[random.random()] ] ) 
print theta
alpha = 0.01
A=np.dot(X.T, X)
B=np.dot(X.T, y)
for it in range (10000): 
	theta = theta - (alpha / m) * (np.dot(A, theta) - B )
	print theta   


