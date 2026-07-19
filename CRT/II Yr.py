
'''

DAY-1
          -----------------------Factors-----------------------
n=int(input())
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        print(i)
        if(i!=n//i):
            print(n//i)

n=int(input())
c=0
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        c+=1
        if(i!=n//i):
            c+=1
print(c)

         ------------------------Primes-----------------------'''
n=int(input())
c=0
for i in range(1,int(n**0.5)+1):
    if(n%i==0):
        c+=1
        if(i!=n//i):
            c+=1
if(c==2):
    print("Prime")
else:
    print("Not Prime")
'''
    ------------------------Function--------------------------
def Varsha(a,b):#can change parameters in fun def
    print(a)#10
    return b#go back to fun call it does not print i.e,.20
    print(a)
a=10
b=20
print(Varsha(a,b))#cannot change parameters in fun call
#funs into 2 :-1.fun def 2.fun call


    ---------------------Sieve of eratosthenes-----------------
n=int(input())#30
isPrime=[1]*n
for i in range(2,int(n**0.5)+1):#optimize (2,n)
    if(isPrime[i]==1):
        for j in range(i*i,n,i):#optimize (2*i,n,i)
            isPrime[j]=0
count=0
for i in range(2,len(isPrime)):
    if(isPrime[i]==1):
        count+=1
print(count)
#T.C:-O(N*log(log N))

           -------------------------Patterns-------------------------
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=" ")
    print()




n=int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()


n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(0,2*i-1):
        print("*",end=" ")
    print()


n=int(input())
for i in range(1,n+1):
    for j in range(n-i):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()

       --------------------------Add lists-------------------------------
nums1=list(map(int,input().split()))
nums2=list(map(int,input().split()))
i=0
j=0
result=[]
while(i<len(nums1) and j<len(nums2)):
    if(nums1[i]<=nums2[j]):
        result.append(nums1[i])
        i+=1
    elif(nums2[j]<nums1[i]):
        result.append(nums2[j])
        j+=1    
while(i<len(nums1)):
    result.append(nums1[i])
    i+=1
while(j<len(nums2)):
    result.append(nums2[j])
    j+=1            
print(result)

         --------------------Sort list----------------------
nums=list(map(int,input().split()))
i=0
for j in range(1,len(nums)):
    if(nums[i]!=nums[j]):
        nums[i+1]=nums[j]
        i+=1
print(nums[0:i+1])




DAY-2
        -----------------------Two Sum-1----------------

nums=list(map(int,input().split()))
target=int(input())
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j]==target):
            print(i,j)

        --------------------Two Sum-2------------------------
nums=list(map(int,input().split()))
target=int(input())
d={}
for a in range(0,len(nums)):
    b=target-nums[a]
    if(b in d):
        print(a,d[b])
    else:
        d[nums[a]]=a
        
        -------------------Two Sum-3-------------------------

def twoSum(nums,target):
    low=0
    high=len(nums)-1
    while(low<high):
        Sum=nums[low]+nums[high]
        if(Sum==target):
            return "Yes"
        elif(Sum>target):
            high-=1
        elif(Sum<target):
            low+=1
    return "No"
nums=list(map(int,input().split()))


        ------------------------Three Sum-1-----------------
n=len(nums)
triplet_sum=set()
for i in range(0,n-2):
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            if(nums[i]+nums[j]+nums[k]==0):
                temp=[nums[i],nums[j],nums[k]]
                temp.sort()
                triplet_sum.add(tuple(temp))
                ans=[]
                for triplet in triplet_sum:
                    ans.append(list(triplet))
                print(ans)

       ---------------------Three Sum-2----------------------'''
'''nums = list(map(int, input().split()))
triplet_sum = set()
n = len(nums)

for i in range(n - 1):
    d = {}
    for j in range(i + 1, n):
        k = -(nums[i] + nums[j])
        if k in d:
            temp = tuple(sorted((nums[i], nums[j], k)))
            triplet_sum.add(temp)
        d[nums[j]] = j

ans = [list(triplet) for triplet in triplet_sum]  # Moving this outside the loop
print(ans)



     ------------------------Three Sum-3------------------------

ans=[]
nums=list(map(int,input().split()))
nums.sort()
for i in range(0,len(nums)):
    if(i>0 and nums[i]==nums[i-1]):
        continue
    j=i+1
    k=len(nums)-1
    while(j<k):
        Sum=nums[i]+nums[j]+nums[k]
        if(Sum<0):
            j+=1
        elif(Sum>0):
            k-=1
        else:
            temp=[nums[i],nums[j],nums[k]]
            ans.append(temp)
            j+=1
            k-=1
            while(j<k and nums[j]==nums[j-1]):
                j+=1
            while(j<k and nums[k]==nums[k+1]):
                k-=1
print(ans)

                   ---------------4SUM-1-------------
num=list(map(int,input().split()))
n=len(num)
four=set()
for i in range(0,n-2):
    d={}
    for j in range(i+1,n-1):
        for k in range(j+1,n):
            l=-(num[i]+num[j]+num[k])
            if(l in d):
                temp=[num[i],num[j],num[k],l]
                temp.sort()
                four.add(tuple(temp))
            d[num[k]]=k
ans=[]
for quadra in four:
    ans.append(list(quadra))
print(ans)
--------------------------4Sum-2------------------------
num=list(map(int,input().split()))
four=set()
n=len(num)
for i in range (0,n-3):
    for j in range (i+1,n-2):
        for k in range (j+1,n-1):
            for l in range (k+1,n):
                if(num[i]+num[j]+num[k]+num[l]==0):
                    temp=[num[i],num[j],num[k],num[l]]
                    temp.sort()
                    four.add(tuple(temp))
ans=[]
for quadra in four:
    ans.append(list(quadra))
print(ans)

------------------
nums=list(map(int,input().split()))
target=int(input())
d={}
for a in range(0,len(nums)):
    b=target-nums[a]
    if(b in d):
        print(a,d[b])
    else:
        d[nums[a]]=a



DAY-3
-----------Rotate Image----------------
matrix=[[1,2,3],[4,5,6],[7,8,9]]
r=len(matrix)
c=len(matrix[0])
dup=[]
for i in range(r):
    temp=[0]*r
    dup.append(temp)
for i in range(0,r):
    for j in range(0,c):
        dup[j][r-1-i]=matrix[i][j]
for i in range(0,r):
    for j in range(0,c):
        matrix[i][j]=dup[i][j]   
print(matrix)

----------Matrix Diagonal Sum-------------
nums=[[1,2,3],[4,5,6],[7,8,9]]
r=len(nums)
Sum=0
for i in range(0,len(nums)):
    Sum+=nums[i][i]
    if(i!=r-1-i):
        Sum+=nums[i][r-1-i]
print(Sum)

-----------Secondary Diagonal Sum-------------
Sum=0
nums=[[1,2,3],[4,5,6],[7,8,9]]
r=len(nums)
for i in range(0,len(nums)):
    Sum+=nums[i][r-1-i]
print(Sum)

--------------Primary Diagonal Sum-----------
Sum=0
nums=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(0,len(nums)):
    Sum+=nums[i][i]
print(Sum)

------------Matrix Sum-------------------
nums=[[1,2,3],[4,5,6],[7,8,9]]
Sum=0
for i in range(0,len(nums)):
    for j in range(0,len(nums[0])):
        if(i==j):
            Sum+=nums[i][j]
print(Sum)

-----------Rotate Image 4D-------------
matrix=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
r=len(matrix)
c=len(matrix[0])
for i in range(0,r-1):
    for j in range(i+1,c):
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
for i in range(0,r):
    matrix[i]=matrix[i][ : :  -1]
print(matrix)

----------------Spiral Traversal Matrix------------
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
ans=[]
sr=0
er=len(mat)-1
sc=0
ec=len(mat[0])-1
while(sr<=er and sc<=ec):
    for i in range(sc,ec+1):
        ans.append(mat[sr][i])
    sr+=1
    for i in range(sr,er+1):
        ans.append(mat[i][ec])
    ec-=1
    if(sr<=er):
        for i in range(ec,sc-1,-1):
             ans.append(mat[er][i])
        er-=1
    if(sc<=ec):     
        for i in range(er,sr-1,-1):
               ans.append(mat[i][sc])
        sc+=1
print(ans)

----------------Search In Sorted Matrix-----------
def searchInSortedMatrix(mat,target,c):
    r=0
    while(c>=0 and r<len(mat)):
        if(mat[r][c-1]==target):
            return True
        elif(mat[r][c-1]<target):
            r+=1
        elif(mat[r][c-1]>target):
            c-=1    
    return False
r,c=map(int,input().split())
mat=[]
for i in range(r):
    lst=list(map(int,input().split()))
    mat.append(lst)
target=int(input())
print(searchInSortedMatrix(mat,target,c))

-------------Move Zeros To End--------------
nums=list(map(int,input().split()))
zero=[]
nonzero=[]
for i in nums:
    if(i==0):
       zero.append(i)
    else:
       nonzero.append(i)
print(nonzero+zero)

------------

nums=list(map(int,input().split()))
i=-1
for ind in range(0,len(nums)):
    if(nums[ind]==0):
        i=ind
        break
if(i!=1):
    for j in range(i+1,len(nums)):
        if(nums[j]!=0):
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
print(nums)




  
DAY-4
         ----------------------1.Selection Sort----------------------
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    Min=i
    for j in range(i+1,len(arr)):
       if(arr[j]<arr[Min]):
         Min=j
    arr[i],arr[Min]=arr[Min],arr[i]
print(arr)

           ------------------------2.Bubble Sort------------------------
arr=list(map(int,input().split()))
for i in range(len(arr)-1,-1,-1):
    for j in range(0,i):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)


           --------------------3.Insertion Sort----------------------------
arr=list(map(int,input().split()))
for i in range(0,len(arr)):
    j=i
    while(j>0 and arr[j-1]>arr[j]):
        arr[j-1],arr[j]=arr[j],arr[j-1]
        j-=1
print(arr)

         --------------------Function------------------------
def Varsha(a,b):
    print(a)
a=10
b=20
Varsha(a,b)

      ---------------------4.Quick Sort------------------------------
def qs(nums,low,high):
    if(low<high):
        pIndex=partition(nums,low,high)
        qs(nums,low,pIndex-1)
        qs(nums,pIndex+1,high)
def partition(nums,low,high):
    i=low
    j=high
    pivot=nums[low]
    while(i<j):
        while(nums[i]<=pivot and i<=high-1):
            i+=1
        while(nums[i]>pivot and j>=low+1):
            j-=1
            if(i<j):
                nums[i],nums[j]=nums[j],nums[i]
        nums[low],nums[j]=nums[j],nums[low]
        return j
nums=list(map(int,input().split()))
qs(nums,0,len(nums)-1)
print(nums)

        ----------------------5.Merge Sort--------------------------
def merge(nums,low,high):
    if low>=high:
        return
    mid=(low+high)//2
    merge(nums,low,mid)
    merge(nums,mid+1,high)
    sort(nums,low,mid,high)
def sort(nums,low,mid,high):
    i=low
    j=mid+1
    k=[]
    while i<=mid and j<=high:  
        if nums[i] <= nums[j]:
            k.append(nums[i])
            i+=1
        else:
            k.append(nums[j])  
            j+=1
    while i<=mid:
        k.append(nums[i])
        i += 1
    while j<=high:
        k.append(nums[j])
        j+=1
    for ind, val in enumerate(k):
        nums[ind+low]=val 
nums = list(map(int, input().split()))
merge(nums, 0, len(nums) - 1)
.print(nums)


          --------------------Left rotate-------------------
arr=list(map(int,input().split()))
n=int(input())
temp=arr[0]
for i in range(1,n):
    arr[i-1]=arr[i]
arr[n-1]=temp
print(arr)

         -----------------------Missing number-------------
def num(arr):
    n=len(arr)+1  
    total_sum=(n*(n+1))//2 
    array_sum=sum(arr)  
    return total_sum-array_sum  
arr=[1,2,4,5,6]
print(num(arr))

DAY-5
         -----------------------Sub array------------------------
nums=[1,2,3]
for i in range(0,len(nums)):
    for j in range(i,len(nums)):
        print(nums[i:j+1])
        ------------------Valid paranthesis-----------------
stack=[]
for i in s:
    if(i in"({["):
        stack.append(i)
    else:
        if(len(stack)==0):
            return False
        x.stack.pop()
        if(x=="{" and i=="{" or x=="[" and i=="]" or x=="(" and i==")"):
            continue
        else:
            return False
        print(len(stack)==0)
        



arr=[1,3,4]
k=int(input)
Max=0
for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        s_a=arr[i:j+1]
        if(sum(s_a)==k):
            Max=max(Max,len(s_a))
print(Max)
                    ------------lower bound---------------
arr=list(map(int,input().split()))
x=int(input())
low=0
high=len(arr)-1
ind=len(arr)
while(low<=high):
    mid=(low+high)//2
    if(arr[mid]>=x):
        ind=mid
        high=mid-1
    else:
        low=mid+1
print(ind)
            --------------upperbound--------------------

arr=list(map(int,input().split()))
x=int(input())
low=0
high=len(arr)-1
ind=len(arr)
while(low<=high):
    mid=(low+high)//2
    if(arr[mid]>x):
        ind=mid
        high=mid-1
    else:
        low=mid+1
print(ind)

DAY-6
-------------------product of numbers-------------
n=int(input())
prod=1
while n!=0:
    rem=n%10
    prod*=rem
    n//10
    print(prod)

--------------product of sum of even and odd----------

n = int(input())  # Input number
odd = 0  # Sum of odd digits
even = 0  # Sum of even digits

while n > 0:
    rem = n % 10  # Get the last digit
    if rem % 2 == 0:
        even += rem  # Add to even sum
    else:
        odd += rem  # Add to odd sum
    n //= 10  # Remove the last digit

discount = even * odd  # Calculate the discount
print(discount)

         ------------------lowerbound---------------------
nums=list(map(int,input().split()))
sum=0
d={0:1}
count=0
for i in nums:
    sum+=i
    rem=sum-k
    if(rem in d):
        count+=d[rem]
    if(sum in d):
        d[sum]+=1
    else:
        d[sum]=1
print(count)


    -------------------------upperbound-----------------------
arr=list(map(int,input().split()))
x=int(input())
low=0
high=len(arr)-1
ind=len(arr)
while(low<=high):
    mid=(low+high)//2
    if(arr[mid]>x):
        ind=mid
        high=mid-1
    else:
        low=mid+1
print(ind)

'''





