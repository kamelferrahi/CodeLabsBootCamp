import numpy as np
from PIL import Image
from numpy.linalg import norm

def isTriangulairUpper(arr):
    nrow = arr.shape[0]
    ncol = arr.shape[1]
    for i in range(nrow): #for all numbers of the matrix that are below the diagonal check if they are equal to 0
        for j in range(i):
            if (arr[i,j]!=0): return False
    return True


def isTriangulairLower(arr):
    nrow = arr.shape[0]
    ncol = arr.shape[1]
    for j in range(ncol):  #for all numbers of the matrix that are above the diagonal check if they are equal to 0
        for i in range(j):
            if (arr[i,j]!=0): return False
    return True

img = Image.open("2d-gradient-3.png")
arr = np.array(img)
arr = arr.reshape(arr.shape[0],arr.shape[1]*arr.shape[2]) #reshape the 3d array into a 2d array
arrt = np.transpose(arr)
isUpper = isTriangulairUpper(arr)
isLower = isTriangulairLower(arr)
print("The matrix: ",arr)
print("\nThe transpose of the matrix: ",arrt)
print("\nIs the image Triangulair Upper: ",isUpper)
print("\nIs the image Triangulair Lower: ",isLower)
print("\nIs the matrix diagonal: ",isLower and isUpper) #a matrix is diagonal if and only if is Triangulair lower and upper

n = int(input("\nChoose a vector number between 0 and "+str(arr.shape[0])+": "))

vector = arr[n,:]

print("\nNorme 1 of the vector: ",norm(vector,1))
print("\nNorme 2 of the vector: ",norm(vector))
