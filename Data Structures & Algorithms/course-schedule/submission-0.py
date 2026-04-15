class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        ans = 0
        ind = [0 for _ in range(numCourses)]

        adjL= defaultdict(list)
        for i in pre:
            adjL[i[1]].append(i[0])
            ind[i[0]]+=1

        q = deque()
        for i in range(numCourses):
            if(ind[i]==0):
                q.append(i)
        
        while q:
            node = q.popleft()
            ans+=1
            for i in adjL[node]:
                ind[i]-=1
                if(ind[i]==0):
                    q.append(i)

        if(ans == numCourses):
            return True
        else:
            return False
        

        