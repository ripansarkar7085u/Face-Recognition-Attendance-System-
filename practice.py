# from collections import Counter
# s=input("enter any string: ")
# c=Counter(s)
# print("Longest possible palindrome :",sum(v-v%2 for v in c.values())+any(v%2 for v in c.values()))
def left_rotate(arr,d):
    n=len(arr)
    d=d%n
    return arr[d:]+arr[:d]
arr=[1,2,3,4,5,6]
d=int(input("Enter no. of Rotatons: "))
rotated=left_rotate(arr,d)
print(rotated)
