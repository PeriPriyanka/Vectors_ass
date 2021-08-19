import numpy as np
import matplotlib.pyplot as plt
#3D axes plot
fig = plt.figure()
dim = plt.axes(projection ='3d')
#vertices
A=np.array([3,6,9])
A.resize(3,1)
B=np.array([10,20,30])
B.resize(3,1)
C=np.array([25,-41,5])
C.resize(3,1)
#checking the right angle
if ((A-C).T@(B-C)==0):
	print("ABC is a right triangle and right angle at c")
elif ((A-B).T@(C-B)==0):
	print("ABC is a right triangle and right angle at B")
elif ((B-A).T@(C-A)==0):
	print("ABC is a right triangle and right angle at A")
else:
	print("ABC is a not right triangle")
#plot of points
dim.scatter(A[0],A[1],A[2],marker="x")
dim.scatter(B[0],B[1],B[2],marker="x")
dim.scatter(C[0],C[1],C[2],marker="x")
dim.text(3,6,9, "A", color='black')
dim.text(10,20,30, "B", color='black')
dim.text(25,-41,5, "C", color='black')
#joing points A,B
x1 = np.linspace(3, 10, 10)
y1 = np.linspace(6, 20, 10)
z1 = np.linspace(9, 30, 10)
dim.plot3D(x1, y1, z1, 'blue',label="AB")
#joing points B,C
x2 = np.linspace(10, 25, 10)
y2 = np.linspace(20, -41, 10)
z2 = np.linspace(30, 5, 10)
dim.plot3D(x2, y2, z2, 'red',label="BC")
#joing points A,C
x3 = np.linspace(3, 25, 10)
y3 = np.linspace(6, -41, 10)
z3 = np.linspace(9, 5, 10)
dim.plot3D(x3, y3, z3, 'green',label="AC")
#plotting
dim.set_xlabel('$X$')
dim.set_ylabel('$Y$')
dim.set_zlabel('$Z$')
plt.title('Triangle')
plt.legend(bbox_to_anchor=(1, 1), loc='lower center')
plt.show()

