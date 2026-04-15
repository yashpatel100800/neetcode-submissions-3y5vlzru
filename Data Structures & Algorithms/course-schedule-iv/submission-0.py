class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjL = defaultdict(list)
        for u, v in prerequisites:
            adjL[v].append(u)

        preMap = defaultdict(set)

        def dfs(node):
            if node in preMap:
                return preMap[node]

            neiSet = set()

            if len(adjL[node]) == 0:
                preMap[node] = neiSet
                return neiSet

            for nei in adjL[node]:
                neiSet.add(nei)                 # ✅ add direct prerequisite
                neiSet.update(dfs(nei))         # ✅ add indirect prerequisites

            preMap[node] = neiSet               # ✅ store result
            return neiSet

        for i in range(numCourses):
            dfs(i)                              # ✅ no need for if-check now

        # answer queries
        ans = []
        for u, v in queries:
            ans.append(u in preMap[v])

        return ans
