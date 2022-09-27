class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # 建表
        g = [[] for j in range(len(vals))]
        for e in edges:
            g[e[0]].append(e[1])
            g[e[1]].append(e[0])
        # 使节点按照值排序
        nodes = [(vals[i], i) for i in range(len(vals))]
        nodes.sort()
        # 并查集
        array = [-1 for i in range(len(vals))]
        def find(i):
            if array[i] == i:
                return i 
            array[i] = find(array[i])
            return array[i]
        # 记录以i为并查集顶节点时，在该集合和它值相同的点的数量
        # 在并查集的合并中，顶节点始终是集合中值最大的那个，保证size的有效性
        size = [1 for i in range(len(vals))]
        ans = len(vals)
        for node in nodes:
            # 多次出错在把size和array的下标写成i
            v, p = node
            array[p] = p
            for j in g[p]:
                # 把相邻的检查过的（即比当前节点值小的）节点纳入
                if array[j] != -1:
                    r = find(j)
                    if vals[r] == v:
                        # 触发两个块的合并，乘法原理计算可形成的路径
                        ans += size[p]*size[r]
                        # 更新块中相等值的数量
                        size[p] += size[r]
                    array[r] = p
        return ans