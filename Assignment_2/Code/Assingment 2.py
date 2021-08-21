import numpy as np
import matplotlib.pyplot as plt
# assigning the vectors
A = np.array([1,2])
A.resize((2,1))
B = np.array([7,0])
B.resize((2,1))
#finding the direction vector
m=B-A
m.resize((2,1))
#finding other point with collinearity parameter "k"
for k in range(5):
  X=A+((k+1)*m)
  plt.scatter(A[0],A[1],marker="o")
  plt.scatter(B[0],B[1],marker="o")
  plt.scatter(X[0],X[1],marker="o")
  plt.text(A[0],A[1], "A", color='black')
  plt.text(B[0],B[1], "B", color='black')
  #plt.text(X[0],X[1], "X", color='black')
p=[A[0],X[0]]
q=[A[1],X[1]]
plt.plot(p,q,label="AB")
plt.xlabel('$X$')
plt.ylabel('$Y$')
plt.title('Collinear Line')
plt.legend(bbox_to_anchor=(1, 1), loc='lower center')
plt.grid()
plt.show()



