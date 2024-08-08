arr=[]
n=int(input("Enter the no.of elements:"))
for i in range (n):
    arr.append(int(input(f"Enter elements {i+1}:")))
print(f"Array: {arr}" )
for i in range(n):
    for j in range(i+1,n):
        if arr[i]>arr[j]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
print("Sorted array:",arr)


   OUTPUT
===========

C:\Users\mlm\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\mlm\PycharmProjects\pythonProject\gcd.py 
Enter 1st number:60
Enter 2nd number:48
The gcd of 60 and 48 is :  12

Process finished with exit code 0
