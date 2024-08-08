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

C:\Users\mlm\PycharmProjects\pythonProject\venv\Scripts\python.exe C:\Users\mlm\PycharmProjects\pythonProject\bubblesort.py 
Enter the no.of elements:5
Enter element 1:10
Enter element 2:6
Enter element 3:36
Enter element 4:32
Enter element 5:2
Array: [10, 6, 36, 32, 2]
Sorted array: [2, 6, 10, 32, 36]

Process finished with exit code 0
