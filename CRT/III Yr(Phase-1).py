'''
-------------------SLL--------------------------
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
def createLinkedList(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            temp.next=Node(val)
            temp=temp.next
    return head          #head=<__main__.Node object at 0x000002B453E8B0E0>   #head.data=1     #head.next=<__main__.Node object at 0x000001C302B43D90>
arr=list(map(int,input().split()))             #1 2 3 4    --1
print(createLinkedList(arr))          


-------------------DLL-------------------------
class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createDoublyLinkedList(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            newNode=Node(val)
            temp.next=newNode
            newNode.prev=temp
            temp=temp.next
arr=list(map(int,input().split()))
print(createDoublyLinkedList(arr))


---------------------SCLL----------------------------
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
def createSCLL(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            temp.next=Node(val)
            temp=temp.next
    temp.next=head
arr=list(map(int,input().split()))
print(createSCLL(arr))

--------------------DCLL-----------------------------
class Node:
    def __init__(self,val):
        self.prev=None
        self.data=val
        self.next=None
def createDCLL(arr):
    head=None
    for val in arr:
        if(head==None):
            head=Node(val)
            temp=head
        else:
            newNode=Node(val)
            temp.next=newNode
            newNode.prev=temp
            temp=temp.next
    temp.next=head
    head.prev=temp
arr=list(map(int,input().split()))   
print(createDCLL(arr))

-------------Recursion-------------------
def hello():
    print("hey python")
print("hey java")
hello()


def fun1():
    print("hi")
    fun1()
fun1()

def fun1(x):
   if(x==0):   #base condition
    return
   print(x)
   fun1(x-1)   #starts & ends at function call
x=4
fun1(x)

def fun1(x):
   if(x==0):   
    return
   fun1(x-1)
   print(x)
x=4
fun1(x)

---------pillars of oops:----------------
1.class-blueprint of a object
2.object-instance of a class
3.inheritance
4.polymorphism
5.encapsulation
6.abstraction


class Hello:
    def fun1(self):
        print("hi")
obj=Hello() #Object creation
obj.fun1() #object.methodName



----------importance of constructor __init__---------
class Hello:
    def __init__(self):
        self.a=10
        self.b=20
    def fun1(self):
        print(self.a)
    def fun2(self):
        print(self.b)
ob=Hello()
ob.fun1()
ob.fun2()

class Father():
    def fun1(self):
        print("I can do job")
class Son(Father):
    def fun2(self):
        print("I can play")
ob=Son()
ob.fun1()

--------------------------------------------------------------------------------BIT MANIPULATION------------------------------------------------------------------------------------------
------------decimal to binary-----------
n=int(input())
binaryResult=""
while(n!=0):
    rem=n%2
    binaryResult+=str(rem)
    n=n//2
print(binaryResult[::-1])


n=15
print(bin(n)[2::])

---------binary to decimal-------------------
binaryString="1111"   #15
p2=1
result=0
for i in binaryString[::-1]:
    if(i=="1"):
        result=result+p2
    p2=p2*2
print(result)


----------------check ith bit------------
def checkKthBit(n,k):
    if((n&(1<<k))==0):
        return False
    return True
n=int(input())
k=int(input())
print(checkKthBit(n,k))


--------------------set ith bit----------------
def setKthBit(n,k):
    n=n|(1<<k)
    return n
n=int(input())
k=int(input())
print(setKthBit(n,k))



-------------clearly ith bit-------------------
n=int(input())
k=int(input())
n=n&(~(1<<k))
print(n)


--------------Toggle-----------------------
n=int(input())
k=int(input())
n=n^(1<<k)
print(n)

---------Single number-------------------
def singleNum(nums):
    res=0
    for n in nums:
        res=n^res
    return res
nums=list(map(int,input().split()))
print(singleNum(nums))


-------Remove right most set bit-------------
n=int(input())
n=n&(n-1)
print(n)


---------Power of 2-----------------------
def isPowerOfTwo(n):
    if(n==0):
        return false
    return n&(n-1)==0
n=int(input())
print(isPowerOfTwo(n))


----------subsets/subsequence--------------------
def Subsets(nums):
    n=len(nums)
    total_subsets=1<<n
    ans=[]
    for val in range(total_subsets):
        lst=[]
        for i in range(n):
            if(val&(1<<i)):
                lst.append(nums[i])
        ans.append(lst)
    return ans
nums=list(map(int,input().split()))
print(Subsets(nums))


----------------subsequence with sum k------------------

def generateSubsets(nums,k):
    n=len(nums)
    total_subsets=1<<n
    ans=[]
    for val in range(total_subsets):
        lst=[]
        for i in range(n):
            if(val&(1<<i)):
                lst.append(nums[i])
        ans.append(lst)
   for array in ans:
        if(sum(array)==k):
            return
while(n!=0):
    n=n//2
    c=c+1
print(c)


n=int(input())
factorsCount=0
for i in range(1,n+1):
    if(n%i==0):
        factorsCount=factorsCount+1
if(factorsCount==2):
    print("Prime")
else:
    print("Not a prime")


def checkPrimeorNot(num):
    count=0
    for i in range(1,num+1):
        if(num%i==0):
            count+=1
        if(count==2):
            return True
        else:
            return False
n=int(input())
Sum=0
while(n!=0):
    rem=n%10
    if(checkPrimeorNot(rem)):
        Sum+=rem
    n=n//10
print(Sum)


n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range(i+1):
        print((j+1),end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()

'''
n=int(input())
for i in range(n):
    for j in range(n-i-1):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    print()
'''
                                          -----------------------------------------------DAY 3--------------------------------------------
1.------------Subsets using backtracking--------------
class Solution:
    def generate(self,ind,subset,ans,nums):
        if(ind==len(nums)):
            ans.append(subset.copy())
            return
        subset.append(nums[ind])
        self.generate(ind+1,subset,ans,nums)
        subset.pop()
        self.generate(ind+1,subset,ans,nums)
    def subsets(self,nums):
        ind=0
        subset=[]
        ans=[]
        self.generate(ind,subset,ans,nums)
        return ans
obj=Solution()
nums=list(map(int,input().split()))
print(obj.subsets(nums))


2.-------------combination sum using backtracking-----------------------
class Solution:
    def generate(self,ind,subset,ans,nums,target):
        if(target==0):
            ans.append(subset.copy())
            return
        if(target<0):
            return
        if(ind==len(nums)):
            return
        subset.append(nums[ind])
        self.generate(ind,subset,ans,nums,target-nums[ind])
        subset.pop()
        self.generate(ind+1,subset,ans,nums,target)
    def combinationSum(self,nums,target):
        ind=0
        subset=[]
        ans=[]
        self.generate(ind,subset,ans,nums,target)
        return ans
obj=Solution()
nums=list(map(int,input().split()))
target=int(input())
print(obj.combinationSum(nums,target))


3.-----------------generate parenthesis using backtracking-----------------
class Solution:
    def generate(self,curr_str,ans,Open,Close,n):
        if(Open+Close==2*n and Open==Close):
            ans.append(curr_str)
            return
        if(Open>n):
            return
        if(Close>Open):
            return
        self.generate(curr_str+"(",ans,Open+1,Close,n)
        self.generate(curr_str+")",ans,Open,Close+1,n)
    def generateParenthesis(self,n):
        curr_str=""
        ans=[]
        Open=0
        Close=0
        self.generate(curr_str,ans,Open,Close,n)
        return ans
obj=Solution()
n=int(input())
print(obj.generateParenthesis(n))


s={}
print(type(s))

s={0}
print(type(s))

ad=lambda a:b=a+b   #instead of fun def lambda is used
print(add(5,10))


---------------sort a dic-syntax ----------
sorted(iterable,key=lambda x:x[1])

d={5:10,2:9,0:1}
u_d=sorted(d.items(),key=lambda x:x[1])  #0-key,1-value in x:x[]     for largest x:-x[]
print(u_d)


4.---------sort characters by frequency-----------
class Solution:
    def frequencySort(self,s):
        d={}
        for char in s:
            if(char in d):
                d[char]=d[char]+1
            else:
                d[char]=1
        u_d=sorted(d.items(),key=lambda x:-x[1])
        resultString=""
        for key,value in u_d:
            for i in range(value):
                resultString=resultString+key
        return resultString
obj=Solution()
s=input()
print(obj.frequencySort(s))
    

5.--------sort array by increasing frequency------------
class Solution:
    def frequencySort(self,nums):
        d={}
        for num in nums:
            if(num in d):
                d[num]=d[num]+1
            else:
                d[num]=1
        u_d=sorted(d.items(),key=lambda x:(x[1],-x[0]))
        resultArray=[]
        for key,value in u_d:
            for i in range(value):
                resultArray.append(key)
        return resultArray
obj=Solution()
nums=list(map(int,input().split()))
print(obj.frequencySort(nums))
    
'''


