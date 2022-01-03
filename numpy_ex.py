"""This module contains numpy operations"""
import numpy as np

print(np.__version__)

lsarr = np.array([1, 2, 3, 4])

print(lsarr)

print(type(lsarr))

tparr = np.array((1, 2, 3, 4, 5))
print("Accessing first element of 1-d array : ", tparr[0])

print(tparr)
print("Slicing on 1-d array : ", tparr[0:2])
print("\n Dimension of above array", tparr.ndim, "\n")


# Dimensions

# 2-D

tdarr = np.array([[1, 2, 3], [4, 5, 6]])
print(tdarr)
print("Accessing first element of 2-d array : ", tdarr[0, 0])
print("Slicing on 2-d array : ", tdarr[1, 0:2])
print("Slicing on 2-d array : ", tdarr[0:2, 2])
print("\n Dimension of above array", tdarr.ndim, "\n")


# 3-D

trdarr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(trdarr)
print("Accessing first element of 3-d array : ", trdarr[0, 0, 0])
print("\n Dimension of above array", trdarr.ndim, "\n")

# n-D

ndarr = np.array([1, 2, 3, 4, 5], ndmin=6)
print(ndarr)
print("\n Dimension of above array", ndarr.ndim, "\n")

# filter an array

arr = np.array([1, 2, 3, 4, 5, 6])

even = []
odd = []

for i in arr:
    if i % 2 == 0:
        even.append(True)
        odd.append(False)
    else:
        odd.append(True)
        even.append(False)

oarr = arr[odd]

earr = arr[even]

print("These are odd numbers :", oarr)
print()
print("These are even numbers :", earr)
