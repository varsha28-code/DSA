''
Variation No.1
--------------------------Binary search---------------------------
def binary_search(arr,target):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==target):
            return mid
        elif(arr[mid]<target):
            low=mid+1
        elif(arr[mid]>target):
            high=mid-1
    return -1
arr=list(map(int,input().split()))
target=int(input())
print(binary_search(arr,target))


#lower bound=smallest element in the array where element greater than or equal to x.
#[1,1,2,3,,3,4,5,6,7],x=2     ans=2
#array sorted----binary search
#upper bound=smallest element in the array where element greater than x.
#[1,1,2,3,3,4,5,6,7],x=2     ans=3
#floor=largest element in the array where element less than or equal to x.
#[1,2,3,4,6,7],x=5    ans=4
#T.C=O(log N)----Binary Search


-----------------------------Lower Bound----------------------------(Ceil in A sorted Array)
def lowerBound(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>=target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=list(map(int,input().split()))
target=int(input())
print(lowerBound(arr,target))

-----------------------------Upper Bound----------------------------
def upperBound(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]>target):
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
arr=list(map(int,input().split()))
target=int(input())
print(upperBound(arr,target))

---------------------------Floor in A Sorted array----------------------------
def findFloor(arr,target):
    low=0
    high=len(arr)-1
    ans=-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]<=target):
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans
arr=list(map(int,input().split()))
target=int(input())
print(findFloor(arr,target))


#First position=lower bound
#Last position=upper bound-1

------------------------Find First and Last Position in Sorted Array--------------------------
def lowerBound(arr,target):
    low=0
    high=len(arr)-1
    ans=len(arr)
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans
def higherBound(arr, target):
    low=0
    high=len(arr)-1
    ans = len(arr)
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
def findFirstAndLast(arr, target):
    first = lowerBound(arr, target)
    last = higherBound(arr, target) - 1
    if first <= last and last < len(arr) and arr[first] == target and arr[last] == target:
        return [first, last]
    else:
        return [-1, -1]
arr=list(map(int,input()))
target=int(input())
print(findFirstAndLast(arr, target))



Variation No.2
#Rule 1-->Check for the sorted half
#Rule 2-->Check target exists in the sorted half
----------------------Search in Rotated Sorted Array-----------------------
def RotatedSearch(arr,key):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return mid
        #check left half is sorted or not
        if(arr[low]<=arr[mid]):
            #check ele exists in sorted left half
            if(arr[low]<=key<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        #check right half is sorted or not
        if(arr[mid]<=arr[high]):
            #check ele exists in sorted right half
            if(arr[mid]<=key<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return -1
arr=list(map(int,input().split()))
key=int(input())
print(RotatedSearch(arr,key))

-----------------------Search in Rotated Sorted Array  2---------------------
def RotatedSearch(arr,key):
    low=0
    high=len(arr)-1
    while(low<=high):
        mid=(low+high)//2
        if(arr[mid]==key):
            return True
        if(arr[mid]==arr[high]):
            low+=1
            high-=1
        #check left half is sorted or not
        elif(arr[low]<=arr[mid]):
            #check ele exists in sorted left half
            if(arr[low]<=key<=arr[mid]):
                high=mid-1
            else:
                low=mid+1
        #check right half is sorted or not
        elif(arr[mid]<=arr[high]):
            #check ele exists in sorted right half
            if(arr[mid]<=key<=arr[high]):
                low=mid+1
            else:
                high=mid-1
    return False
arr=list(map(int,input().split()))
key=int(input())
print(RotatedSearch(arr,key))

--------------------Sorted and Rotated Minimum------------------------
def findMin(arr):
    low=0
    high=len(arr)-1
    ans=float("inf")
    while(low<=high):
        mid=(low+high)//2
        #left half
        if(arr[low]<=arr[mid]):
            if(arr[low]<=ans):
                ans=arr[low]
            low=mid+1
            #right half
        elif(arr[mid]<=arr[high]):
            if(arr[mid]<=ans):
                ans=arr[mid]
            high=mid-1
    return ans
arr=list(map(int,input().split()))    
print(findMin(arr))   
           
--------------------Find Kth Rotation----------------------------
def findKth(arr):
    low=0
    high=len(arr)-1
    ans=float("inf")
    min_index=0
    while(low<=high):
        mid=(low+high)//2
        if(arr[low]<=arr[mid]):
            if(arr[low]<=ans):
                ans=arr[low]
                min_index=low
            low=mid+1
        elif(arr[mid]<=arr[high]):
            if(arr[mid]<=ans):
                ans=arr[mid]
                min_index=mid
            high=mid-1
    return min_index
arr=list(map(int,input().split()))    
print(findKth(arr))


Variation No.3(B.S on answers)
----------------------Square Root----------------------      
def floorSqrt(n):
    low=0
    high=n
    while(low<=high):
        mid=(low+high)//2
        if(mid*mid>n):
            high=mid-1
        else:
            low=mid+1
    return high
n=int(input())
print(floorSqrt(n))

----------------------Find nth root of m----------------
def nthRoot(n,m):
    low=1
    high=m
    while(low<=high):
        mid=(low+high)//2
        if(mid**n==m):
            return mid
        elif(mid**n>m):
            high=mid-1
        else:
            low=mid+1
    return -1
n=int(input())
m=int(input())
print(nthRoot(n,m))
           
------------------Smallest Divisor----------------------(Koko eating Bananas)
from math import ceil
def smallestDivisor(arr,k):
    low=1
    high=max(arr)
    while(low<=high):
        div=(low+high)//2
        Sum=0
        for nums in arr:
            Sum+=ceil(num/div)
        if(Sum>k):
            low=div+1
        else:
            high=div-1
    return low
arr=list(map(int,input().split()))
k=int(input())
print(smallestDivisor(arr,k))

-----------------Minimum days to make M bouquets-----------------------
def minDaysBloom(arr,k,m):
    if(m*k>len(arr)):
        return -1
    low=min(arr)
    high=max(arr)
    while(low<=high):
        day=(low+high)//2
        bloomed_flowers=0
        no_of_bouquets=0
        for num in arr:
            if(day>=num):
                bloomed_flowers+=1
                if(bloomed_flowers==k):
                    no_of_bouquets+=1   
                    bloomed_flowers=0     
            else:
                bloomed_flowers=0         #adjacency  
        if(no_of_bouquets>=m):
            high=day-1
        else:
            low=day+1
    return low
arr=list(map(int,input().split()))
k=int(input())
m=int(input())
print(minDaysBloom(arr,k,m))

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------Day-2
-------------Next greatest elemnent(NGE)-------------------arr=[6,0,8,1,3]  ans=[8,8,-1,3,-1](aestroid--collision)    Monotonic stacks
arr=[6,0,8,1,3]
n=len(arr)
ans=[]       #T.C:O(N**2)
for i in range(0,n):
    flag=1
    for j in range(i+1,n):
        if(arr[j]>arr[i]):
            ans.append(arr[j])
            flag=0
            break
    if(flag==1):
        ans.append(-1)
print(ans)

#Time complexity is very high so we should optimize the above code....
#Optimized Code:Using stack Data structure to solve the problem


arr=list(map(int,input().split()))
stack=[]
n=len(arr)
ans=[0]*n
for i in range(n-1,-1,-1):
    currEle=arr[i]
    while(len(stack)!=0 and stack[-1]<=currEle):
        stack.pop()
    if(len(stack)==0):
        ans[i]=-1
    else:
        ans[i]=stack[-1]
    stack.append(currEle)
print(ans)

--------------Previous greatest element----------------  
arr=list(map(int,input().split()))
stack=[]
n=len(arr)
ans=[0]*n
for i in range(0,n):
    currEle=arr[i]
    while(len(stack)!=0 and stack[-1]<=currEle):
        stack.pop()
    if(len(stack)==0):
        ans[i]=-1
    else:
        ans[i]=stack[-1]
    stack.append(currEle)
print(ans)


------------Previous smallest element------------------
arr=list(map(int,input().split()))
stack=[]
n=len(arr)
ans=[0]*n
for i in range(0,n):
    currEle=arr[i]
    while(len(stack)!=0 and stack[-1]>=currEle):
        stack.pop()
    if(len(stack)==0):
        ans[i]=-1
    else:
        ans[i]=stack[-1]
    stack.append(currEle)
print(ans)

----------------Next smallest element-------------------
arr=list(map(int,input().split()))
stack=[]
n=len(arr)
ans=[0]*n
for i in range(n-1,-1,-1):
    currEle=arr[i]
    while(len(stack)!=0 and stack[-1]>=currEle):
        stack.pop()
    if(len(stack)==0):
        ans[i]=-1
    else:
        ans[i]=stack[-1]
    stack.append(currEle)
print(ans)


---------------Trapping rain water--------------------Formulae:--min(lh,rh)-bh [4,2,0,3,2,5]
def trap(height):
    n=len(height)
    left_height=[0]*n
    left_height[0]=height[0]
    for i in range(1,n):
        left_height[i]=max(left_height[i-1],height[i])
    right_height=[0]*n
    right_height[n-1]=height[n-1]
    for i in range(n-2,-1,-1):
        right_height[i]=max(right_height[i+1],height[i])
    water_trapped=0
    for i in range(0,n):
        water_trapped+=min(left_height[i],right_height[i])-height[i]
    return water_trapped
height=list(map(int,input().split()))
print(trap(height))

--------------------------LRU Cache-----------------------
class Node:
    def __init__(self,key=-1,value=-1):
        self.prev = None 
        self.key = key 
        self.value = value 
        self.next = None 
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.mpp = {} 
        self.head = Node() # 1000 
        self.tail = Node() # 2000 
        self.head.next = self.tail 
        self.tail.prev = self.head
    def addAfterHead(self,newNode):
        nextNode = self.head.next # 2000 
        newNode.prev = self.head # 3000.prev =  1000 
        self.head.next = newNode # 1000.next = 3000  
        newNode.next = nextNode # 3000.next = 2000 
        nextNode.prev = newNode # 2000.prev = 3000 
    def deleteNode(self,node):
        prevNode = node.prev # 1000  
        nextNode = node.next # 3000 
        prevNode.next = nextNode # 1000.next = 3000 
        nextNode.prev = prevNode # 3000.prev = 1000 
        node.prev = None 
        node.next = None 
    def get(self, key: int) -> int:
        if(key not in self.mpp):
            return -1 
        node = self.mpp[key]
        self.deleteNode(node) 
        self.addAfterHead(node) 
        return node.value 
    def put(self, key: int, value: int) -> None:
        if(key in self.mpp):
            node = self.mpp[key]
            node.value = value 
            self.deleteNode(node) 
            self.addAfterHead(node)
            return 
        if(self.cap == len(self.mpp)):
            node = self.tail.prev 
            self.deleteNode(node) 
            del self.mpp[node.key] 
        newNode = Node(key,value)
        self.addAfterHead(newNode)
        self.mpp[key] = newNode


--------------------- 1.Largest rectangle in histogram -------------Formulae:--(height*(nse-pse-1))                                                                                    Day-3
def largestRectArea(heights):
    def findNSE(heights):
        stack=[]
        n=len(heights)
        ans=[0]*n
        for i in range(n-1,-1,-1):
            currEle=heights[i]
            while(len(stack)!=0 and heights[stack[-1]]>=currEle):
                +stack.pop()
            if(len(stack)==0):
                ans[i]=n
            else:
                ans[i]=stack[-1]
            stack.append(i)
        return ans
    def findPSE(heights):
        stack=[]
        n=len(heights)
        ans=[0]*n
        for i in range(0,n):
            currEle=heights[i]
            while(len(stack)!=0 and heights[stack[-1]]>=currEle):
                stack.pop()
            if(len(stack)==0):
                ans[i]=-1
            else:
                ans[i]=stack[-1]
            stack.append(i)
        return ans
    nse=findNSE(heights)
    pse=findPSE(heights)
    area=0
    maxArea=0
    n=len(heights)
    for i in range(0,n):
        area=heights[i]*(nse[i]-pse[i]-1)
        maxArea=max(maxArea,area)
    return maxArea
heights=list(map(int,input().split()))
print(largestRectArea(heights))

------------------------2.asteroid-collision-----------------
def asteroidCollision(asteroids):
    n=len(asteroids)    #4 7 1 1 -3 -7 17 15 -16      #1 -2 -3
    stack=[]
    for i in range(0,n):
        if(asteroids[i]>0):
            stack.append(asteroids[i])
        else:
            while(len(stack)!=0 and stack[-1]>0 and stack[-1]<abs(asteroids[i])):
                  stack.pop()
            if(len(stack)!=0 and stack[-1]==abs(asteroids[i])):
                  stack.pop()
            elif(len(stack)==0 or stack[-1]<0):
                stack.append(asteroids[i])
    return stack
    
asteroids=list(map(int,input().split()))
print(asteroidCollision(asteroids))

-----------------------3.Valid Parenthesis---------------------------------
def isValid(s):
    stack=[]
    for i in s:
        if(i in "({["):
            stack.append(i)
        else:
            if(len(stack)==0):
                return False
            x=stack.pop()
            if(x=="(" and i==")" or x=="{" and i=="}" or x=="[" and i=="]"):
                continue
            else:
                return False
    return len(stack)==0
s="({})"
print(isValid(s))

-------------------4.Hare-Tortoise--------------------------
def middleEle(head):
    slow=head
    fast=head
    while(fast!=None and fast.next!=None):
        slow=slow.next
        fast=slow.next.next
    return slow
print(middleEle(head))

#Floyd's cycle finding algorithm   
    

------------5.Detect loop in Linked list--------------
def detectLoop(head):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=slow.next.next
        if(slow==fast):
            return True
    return False
head=
print(detectLoop(head))

------------6.find first node of the loop in Linked list------------
def firstNode(data):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=slow.next.next
        if(slow==fast):
            fast=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            return slow.data
    return -1 

----------7.find length of the loop in Linked List-------------
def firstNode(data):
    slow=head
    fast=head
    while(fast and fast.next):
        slow=slow.next
        fast=slow.next.next
        if(slow==fast):
            fast=head
            while(slow!=fast):
                slow=slow.next
                fast=fast.next
            fast=fast.next
            c=1
            while(slow!=fast):
                fast=fast.next
                c+=1
            return c
    return 0

-----------8.Hands in a clock---------------------
def angleClock(hour,minutes):
    hour_angle=((hour)+(minutes)/60)*30
    min_angle=minutes*6
    diff=abs(hour_angle-min_angle)
    if(diff>180):
        return 360-diff
    return diff
    
----------1. Level Order Traversal-----------------------------------------------------------------------------------------------------------------------------------                Day-4
from collections import deque
def levelOrder(root):
    ans=[]
    q=deque([root])
    while(len(q)>0):
        level=[]
        for i in range(len(q)):
            node=q.popleft()
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
            level.append(node.data)
        ans.append(level)
    return ans
root=
print(levelOrder(root))

------------2. Zigzag Tree Order Traversal----------------
from collections import deque
def zigzaglevelOrder(root):
    ans=[]
    level_count=0
    q=deque([root])
    while(len(q)>0):
        level=[]
        for i in range(len(q)):
            node=q.popleft()
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
            level.append(node.val)
        if(level_count%2==1):   #odd level
            ans.append(level[::-1])  #reverse list so we get(R to L)
        else:
            ans.append(level)
        level_count+=1
    return ans

----------------3. Tree Boundary Traversal---------------
def :
    def isLeafNode(root):
        if(root.left==None and root.right==None):
            return True
        return False
    def addLeftNodes(root,result):
        curr=root.left
        while(curr):
            if(isLeafNode(curr)==False):
                result.append(curr.data)
            if(curr.left):
                curr=curr.left
            else:
                curr=curr.right
    def addLeafNodes(root,result):
        if(isLeafNode(root)==True):
            result.append(root.data)
            return
        if(root.left):
            addLeafNodes(root.left,result)
        if(root.right):
            addLeafNodes(root.right,result)
    def addRightNodes(root,result):
        temp=[]
        curr=root.right
        while(curr):
            if(isLeafNode(curr)==False):
                temp.append(curr.data)
            if(curr.right):
                curr=curr.right
            else:
                curr=curr.left
        result.extend(temp[::-1])
    if(LeafNode(root)):
        return [root.data]
    result=[]
    result.append(root.data)
    addLeftNodes(root,result)
    addLeafNodes(root,result)
    addRightNodes(root,result)
    return result

-------------4. Vertical Order Traversal of a Binary Tree-----------
from collections import defaultdict,deque
class Solution:
    def verticalTraversal(root):
        q=deque([(root,0,0)])
        d=defaultdict(lambda:defaultdict(list))
        while(len(q)>0):
            node,vertical,level=q.popleft()
            if(node.left):
                q.append((node.left,vertical-1,level+1))
            if(node.right):
                q.append((node.right,vertical+1,level+1))
            d[vertical][level].append(node.val)
        result=[]
        for i in sorted(d):
            col=[]
            for j in sorted(d[i]):
                col.extend(sorted(d[i][j]))
            result.append(col)
        return result

------------------5. Top view of a Binary Tree--------------------
from collections import deque
class Solution:
    def topView(root):
        q=deque([(root,0,0)])
        d=defaultdict(lambda:defaultdict(list))
        while(len(q)>0):
            node,vertical,level=q.popleft()
            if(node.left):
                q.append((node.left,vertical-1))
            if(node.right):
                q.append((node.right,vertical+1))
            if(vertical not in d):
                d[vertical]=node.data
        ans=[]
        for i in sorted(d):
            ans.append(d[i])
        return ans


------------------7.Left view------------------------
from collections import deque
def levelOrder(root):
    ans=[]
    q=deque([root])
    while(len(q)>0):
        level=[]
        for i in range(len(q)):
            node=q.popleft()
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
            level.append(node.data)
        ans.append(level[0])
    return ans

-----------------8.Right view---------------------
from collections import deque
def levelOrder(root):
    ans=[]
    q=deque([root])
    while(len(q)>0):
        level=[]
        for i in range(len(q)):
            node=q.popleft()
            if(node.left):
                q.append(node.left)
            if(node.right):
                q.append(node.right)
            level.append(node.data)
        ans.append(level[-1])
    return ans

-----------------------
from collections import deque
class Solution:
    def amountOfTime(root,start):
        def get_parent_address(root):
            mpp={}
            q=deque([root])
            while(len(q)>0):
                node=q.popleft()
                if(node.left):
                    mpp[node.left]=node
                    q.append(node.left)
                if(node.right):
                    mpp[node.right]=node
                    q.append(node.right)
            return mpp
        def inorder(root,start):
            if(root==None):
                return None
            if(root.val==start):
                return root
            path1=inorder(root.left,start)
            if(path!=None):
                return path1
            path2=inorder(root.right,start)
            return path1 or path2
        d=get_parent_address(root)
        startNode=inorder(root,start)
        time=0
        visited=set([startNode])
        que=deque([startNode])
        while(len(que)>0):
            for i in range(len(que)):
                node=que.popleft()
                #parent
                if(node in d and d[node] not in visited):
                    visited.add(d[node])
                    que.append(d[node])
                #left
                if(node in d and node.left not in visited):
                    visited.add(node.left)
                    que.append(node.left)
                #right
                if(node in d and node.right not in visited):
                    visited.add(node.right)
                    que.append(node.right)
            time+=1
        return time-1

-------------------BST---------------------------
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def createBST(arr):
    root=None
    for data in arr:
        if(root==None):
            root=Node(data)
        else:
            curr=root
            while(True):
                if(data<curr.data):
                    if(curr.left==None):
                        curr.left=Node(data)
                        break
                    else:
                        curr=curr.left
                elif(data>curr.data):
                    if(curr.right==None):
                        curr.right=Node(data)
                        break
                    else:
                        curr=curr.right
    print(root.left.data) 
arr=list(map(int,input().split()))
createBST(arr)

-------------Search for a Number in BST-----------
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
def searchBST(root,val):
    while(root!=None and root.val!=val):
        if(val<root.val):
            root=root.left
        elif(val>root.val):
            root=root.right
    return root
root=
val=
searchBST(root,val)

-----------Ceil in BST--------------------
class Solution:
    def findCeil(root,x):
        ans=-1
        while(root!=None):
            if(root.data>=x):
                ans=root.data
                root=root.left
            else:
                root=root.right
        return ans

------------Floor in BST------------------                
class Solution:
    def findFloor(root,x):
        ans=-1
        while(root!=None):
            if(root.data<=x):
                ans=root.data
                root=root.right
            else:
                root=root.left
        return ans
                
----------BFS of graph-------------------
def bfs(adj):
    n=len(adj)
    visited=[0]*n
    startNode=0
    visited[startNode]=1
    q=deque([startNode])
    ans=[]
    while(len(q)>0):
        node=q.popleft()
        for i in adj(node):
            if(visited[i]==0):
                visited[i]=1
        ans.append(node)
    return ans

------------DFS of graph---------
def dfs(node,vis,adj,ans):
    ans.append(node)
    for i in adj[node]:
        if(vis[i]==0):
            vis[i]=1
            dfs(i,vis,adj,ans)
n=len(adj)
vis=[0]*n
startNode=0
vis[startNode]=1
ans=[]
dfs(startNode,vis,adj,ans)
return ans

----------Number of Islands------
flood fill algorithm
rotten oranges

----------Number of islands----------------
def 









    -------------Flood fill-----------
def floodFill(image):
    if(image[sr][sc]==color):
        return image
def dfs(sr,sc,image,n,m):
    for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
        ur=sr+r
        uc=sc+c
        if(ur>=0 and ur<n and uc>=0 and uc<m and image[ur][uc]==num):
            image[ur][uc]=color
            dfs(ur,uc,image,n,m)
n=len(image)  #no.of rows
m=len(image[0])  #no.of columns
num=image[sr][sc]
image[sr][sc]=color
dfs(sr,sc,image,n,m)
return image

----------Rotten oranges-------------------
from collections import deque
def rottenOranges(grid):
    n=len(grid)
    m=len(grid[0])
    q=deque()
    for i in range(n):
        for j in range(m):
            if(grid[i][j]==2):
                q.append((i,j,0))
    time=0
    while(len(q)>0):
        row,col,time=q.popleft()
        for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
            ur=row+r
            uc=col+c
            if(ur>=0 and ur<n and uc>=0 and uc<m and grid[ur][uc]==1):      #out of bound condition
                grid[ur][uc]=2
                q.append((ur,uc,time+1))
    for i in range(n):
        for j in range(m):
            if(grid[i][j]==1):
                return -1
    return time

----------Number of enclaves-----------'''
from collections import deque
def numEnclaves(grid):
    n=len(grid)
    m=len(grid[0])
    vis=[]
    for i in range(n):
        lst=[0]*m
        vis.append(lst)
    q=deque()
    for i in range(n):
        for j in range(m):
            if((i==0 or j==0 or i==n-1 or j==m-1) and grid[i][j]==1):
                q.append((i,j))
                vis[i][j]=1
    while(len(q)>0):
        row,col=q.popleft()
        for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
            ur=row+r
            uc=col+c
            if(ur>=0 and ur<n and uc>=0 and uc<m and grid[ur][uc]==1 and vis[ur][uc]==0):      #out of bound condition
                vis[ur][uc]=1
                q.append((ur,uc))
    count=0
    for i in range(n):
        for j in range(m):
            if(grid[i][j]==1 and vis[i][j]==0):
                count+=1
    return count




