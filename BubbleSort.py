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
