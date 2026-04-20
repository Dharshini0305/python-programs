//You are given a polynomial  of a single indeterminate (or variable), .
//You are also given the values of x and y. Your task is to verify if P(x)=k.

//Constraints
//All coefficients of polynomial  are integers.
//x and y are also integers.
//Input Format
//The first line contains the space separated values of x and y.
//The second line contains the polynomial .
//Print True if P(x)=k. Otherwise, print False.
//Program
x, k = map(int, input().split())
polynomial = input()
print(eval(polynomial) == k)
