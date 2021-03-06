import collections
class Solution(object):
    def minimumSemesters(self, N, relations):
        g = collections.defaultdict(list)
        in_degree = [0]*N
        for x, y in relations:
            g[x-1].append(y-1)
            in_degree[y-1] += 1
        q = collections.deque([(1, i) for i in range(N) if not in_degree[i]])

        result = 0
        count = N
        while q:
            level, u = q.popleft()
            count -= 1
            result = level
            for v in g[u]:
                in_degree[v] -= 1
                if not in_degree[v]:
                    q.append((level+1, v))
        return result if count == 0 else -1
val=Solution()
n,m=map(int,input().split())
matrix=[]
for i in range(m):
  rows=list(map(int,input().split()))
  matrix.append(rows)
print(val.minimumSemesters(n,matrix))
