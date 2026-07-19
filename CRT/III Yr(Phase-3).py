

DAY-1
-------Constant Window---------------
arr = list(map(int,input().split()))
k = int(input())
left = 0
right = k-1 
Sum = sum(arr[0:k])
maxSum = Sum 
n = len(arr)
while(right<n-1):
    Sum-=arr[left]
    left+=1 
    right+=1 
    Sum+=arr[right]
    maxSum = max(maxSum,Sum)
print(maxSum) 

----------Longest subarray/substring-------
class Solution:
    def maxScore(self, cardPoints, k):
        # code here.
        n = len(cardPoints)
        left = 0
        right = k-1 
        Sum = sum(cardPoints[0:k]) 
        maxSum = Sum 
        j = n-1    
        for _ in range(k):
            Sum-=cardPoints[right]
            right-=1 
            Sum+=cardPoints[j]
            j-=1 
            maxSum = max(maxSum,Sum)
        return maxSum

------------Longest substring with distinct characters--------

-----------Max consecutive ones------------
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        left,right=0,0
        maxlen=0
        zeros=0
        k=0
        while(right<n):
            if(nums[right]==0):
                zeros+=1
            #shrink
            while(zeros>k):
                if(nums[left]==0):
                    zeros-=1
                left+=1
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen
        
----------Fruits into Basket------------
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits) 
        left,right = 0,0 
        maxLen = 0 
        d = {} 
        while(right<n):
            if(fruits[right] in d):
                d[fruits[right]]+=1 
            else:
                d[fruits[right]] = 1 
            # shrink 
            while(len(d)>2):
                d[fruits[left]]-=1 
                if(d[fruits[left]] == 0):
                    del d[fruits[left]] 
                left+=1 
            maxLen = max(maxLen,right-left+1)
            right+=1 
        return maxLen 
    
---------Longest Repeating Character Replacement----------
class Solution(object):
    def minWindow(self, s, t):
        n=len(s)
        left,right=0,0
        maxlen=0
        d={}
        maxF=0
        while(right<n):
            if(s[right] in d):
                d[s[right]]+=1
            else:
                s[right]=1
                maxF=max(maxF,d[s[right]])
            #shrink
            while((right-left+1)-maxF>k):
                d[s[left]]-=1
                if(d[s[left]]==0):
                    del d[s[left]]
                left+=1
            maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen
    
DAY-2
----------Minimum Window Substring----------


------Binary Subarrays with Sum----------
class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        sum=0
        cnt=0
        n=len(nums)
        left,right=0,0
        while(right(n)):
            sum+=nums[right]
            while(sum>goal):
                sum-=nums[left]
                left+=1
                cnt+=(right-left+1)
                right+=1
            return cnt
        return numSubarraysWithSum(nums,goal)-numSubarraysWithSum(nums,goal-1)
       
Greedy Algorithms:
-----------Assign Cookies----------------
class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i=0
        j=0
        while(i<len(g) and j<len(s)):
            if(s[j]>=g[i]):
                i+=1
            j+=1
        return i
    
-----------Lemonade Change---------------
class Solution(object):
    def lemonadeChange(self, bills):
        five=0
        ten=0
        for dollar in bills:
            if(dollar==5):
                five+=1
            elif(dollar==10):
                ten+=1
                if(five>0):
                    five-=1
                else:
                    return False
            elif(dollar==20):
                if(five>0 and ten>0):
                    five-=1
                    ten-=1
                elif(five>=3):
                    five-=3
                else:
                    return False
        return True
    
----------Jump Game-------------
class Solution(object):
    def canJump(self, nums):
        max_reach = 0  
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
        return True

--------------SJF--------------- 
class Solution:
    def solve(self, bt):
        bt.sort()
        wait_time=0
        total_time=0
        for i in bt:
            wait_time+=total_time
            total_time+=i
        return wait_time//len(bt)

DAY-3
-----------N-Queens--------------
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def canWePlace(row,col,mat):
            # top - left 
            r,c= row,col
            while(r>=0 and c>=0):
                if(mat[r][c] == "Q"): 
                    return False 
                r-=1 
                c-=1 
            # top 
            r,c = row,col 
            while(r>=0):
                if(mat[r][c] == "Q"):
                    return False 
                r-=1 
            # top-right 
            r,c = row,col 
            while(r>=0 and c<n):
                if(mat[r][c] == "Q"):
                    return False 
                r-=1 
                c+=1 
            return True 
        def backtrack(row,mat,n,ans):
            if(row == n):
                temp = [] 
                for r in mat:
                    temp.append("".join(r))
                ans.append(temp)
                return
            for col in range(0,n):
                if(canWePlace(row,col,mat)):
                    mat[row][col] = "Q"
                    backtrack(row+1,mat,n,ans)
                    mat[row][col] = "." 
        mat = [] 
        for _ in range(0,n):
            lst = ["."]*n 
            mat.append(lst)
        row = 0
        ans = [] 
        backtrack(row,mat,n,ans)
        return ans 
    
------------Sudoku solver------------
class Solution:
    def solveSudoku(self, board):
        # code here
        def canWePlace(row,col,num,board):                 
            # row and col check 
            for i in range(0,9):  
                if(board[row][i] == num or board[i][col] == num):
                    return False 
            start_row , start_col = 3*(row//3),3*(col//3)
            for i in range(start_row,start_row+3):
                for j in range(start_col,start_col+3):
                    if(board[i][j] == num):
                        return False 
            return True 
        def solve(board):
            n = 9               
            for row in range(0,n):
                for col in range(0,n):
                    if(board[row][col] == 0):
                        for num in range(1,10):
                            if(canWePlace(row,col,num,board)):
                                board[row][col] = num
                                if(solve(board)): 
                                    return True 
                                board[row][col] = 0 
                        return False
            return True
        solve(board)
        
-------------Word Search---------------------
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row,col,board,word,ind):
            if(ind == len(word)):
                return True 
            for r,c in [[-1,0],[1,0],[0,-1],[0,1]]:
                nr = r+row 
                nc = c+col 
                if(nr>=0 and nr<n and nc>=0 and nc<m and board[nr][nc] == word[ind]):
                    board[nr][nc] = '.'
                    if(backtrack(nr,nc,board,word,ind+1)):
                        return True 
                    board[nr][nc] = word[ind] 
            return False 
        n = len(board) # no of rows 
        m = len(board[0]) # no of cols
        for row in range(0,n):
            for col in range(0,m):
                if(board[row][col] == word[0]): 
                    board[row][col] = "." 
                    if(backtrack(row,col,board,word,1)):
                        return True 
                    board[row][col] = word[0]
        return False

DAY-4
------------Rat In a Maze-------------
class Solution:
    def ratInMaze(self, maze):
        # code here
        def backtrack(row,col,directions,tempString,ans,n):
            if(row==n-1 and col==n-1):
                ans.append(tempString)
                return
            for dire,r,c in directions:
                nr=row+r
                nc=col+c
                if(nr>=0 and nr<n and nc>=0 and nc<n and maze[nr][nc]==1):
                    maze[nr][nc]="."
                    backtrack(nr,nc,directions,tempString+dire,ans,n)
                    maze[nr][nc]=1
        n=len(maze)
        directions=[['D',1,0],['L',0,-1],['R',0,1],['U',-1,0]]
        ans=[]
        tempString=""
        row=0
        col=0
        maze[row][col]="."
        backtrack(row,col,directions,tempString,ans,n)
        maze[row][col]=1
        return ans
    
DP:
1.Recursive(Top-Bottom approach)
2.Memoization(Top-Bottom approach)
3.Tabulation(Bottom-Top approach)
4.Space Optimization

Fibonacci Series:
--------------1.Recursive----------
def fibo(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    return fibo(n-1)+fibo(n-2)

def fibo(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    a=fibo(n-1)
    b=fibo(n-2)
    return a+b        #T.C:-O(2^n)  S.C:-O(N)

----------2.Memoization----------
def fibo(n):
     if(n==0):
        return 0
    if(n==1):
        return 1
    if(dp[n]==-1):
        dp[n]=fibo(n-1,dp)+fibo(n-2,dp)
    return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fibo(n,dp))        #T.C:-O(N)  S.C:-O(N)+O(N)

-----------3.Tabulation------------
def fibo(n,dp):
    dp[0]=0
    dp[1]=1
    for ind in range(2,n):
        dp[ind]=dp[ind-1]+dp[ind-2]
    return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fibo(n,dp))     #T.C:-O(N)  S.C:-O(N)

----------4.Space Optimization----------
def fibo(n):
    prev2=0
    prev=1
    for i in range(2,n+1):
       curr=prev+prev2
       prev2=prev
       prev=curr
    return prev
n=int(input())
print(fibo(n))    #T.C:-O(N)   S.C:-O(1)

-----------Climbing Stairs---------
def fibo(n):
    if(n==0):
        return 0
    if(n==1):
        return 1
    oneJump=solve(n-1)
    twoJump=solve(n-2)
    return oneJump+twoJump
return solve(n)

----------Frog Jump------------
def frogJump(n,heights):       #recursive
    def backtrack(ind,heights):
    if(ind==0):
        return 0
    oneJump=backtrack(ind-1,heights)+abs(heights[ind]-heights[ind-1])
    twoJump=float("inf")
    if(ind>1):
        twoJump=backtrack(ind-2,heights)+abs(heights[ind]-heights[ind-2])
    ind=n-1
    backtrack(ind,heights)
return min(oneJump+twoJump)

def frogJump(n,heights):    #Memoization
    def backtrack(ind,heights,dp):
    if(ind==0):
        return 0
    if(dp[ind]!=1):
        return dp[ind]
    oneJump=backtrack(ind-1,heights)+abs(heights[ind]-heights[ind-1])
    twoJump=float("inf")
    if(ind>1):
        twoJump=backtrack(ind-2,heights)+abs(heights[ind]-heights[ind-2])
    dp[ind]=min(oneJump,twoJump)
    return dp[ind]
dp=[-1]*n
ind=n-1
return backtrack(ind,heights)

def frogJump(n,heights):    #Tabulation
    def backtrack(ind,heights,dp):
        dp[0]=0
        for ind in range(1,len(heights)):
            oneJump=backtrack(ind-1,heights)+abs(heights[ind]-heights[ind-1])
            twoJump=float("inf")
            if(ind>1):
                twoJump=backtrack(ind-2,heights)+abs(heights[ind]-heights[ind-2])
            dp[ind]=min(oneJump,twoJump)
    return dp[i]
dp=[-1]*n
i=n-1
return backtrack(i,heights,dp)

DAY-5
-------------N-meetings in one room------------
class Solution:
    def maximumMeetings(self,start,end):
        n=len(start)
        mat=[]
        for ind in range(0,n):
            mat.append([start[ind],end[ind]])
        mat.sort(key=lambda x:x[1])
        c=1
        endTime=mat[0][1]
        for row in range(1,n):
            if(mat[row][0]>endTime):
                c+=1
                endTime=mat[row][1]
        return c
    
----------Non-Overlapping Intervals--------
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])
        c=1
        endTime=intervals[0][1]
        for row in range(1,n):
            if(intervals[row][0]>=endTime):
                c+=1
                endTime=intervals[row][1]
        return n-c

----------Job sequencing problem-------------
class Solution:
    def jobSequencing(self, deadLine, profit):
        # code here
        n=len(jobs)
        jobs.sort(key=lambda x:-x[2])
        maxDeadline=0
        for row in range(0,n):
            maxDeadline=max(maxDeadline,jobs[row][1])
        days=[-1]*(maxDeadline+1)
        count,maxProfit=0,0
        for row in range(0,n):
            for deadLine in range(jobs[row][1],0,-1):
                if(days[deadLine]==-1):
                    days[deadLine]=jobs[row][0]
                    count+=1
                    maxProfit+=jobs[row][2]
                    break
        return[count,maxProfit]
                
        
        
        

        
        
        
