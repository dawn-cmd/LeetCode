from typing import List


class Solution:
    
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        children = [[] for _ in range(len(parents))]
        for i in range(1, len(parents)):
            children[parents[i]].append(i)
        bulk = [0 for i in range(len(parents))]

        def dfs(now: int, bulk: List[int]) -> int:
            bulk[now] = 1
            for child in children[now]:
                bulk[now] += dfs(child, bulk)
            return bulk[now]
        
        dfs(0, bulk)
        max_sc = 0
        num_mx = 0
        for i in range(len(parents)):
            score = 1
            if i != 0:
                score *= bulk[0] - bulk[i]
            for child in children[i]:
                score *= bulk[child]
            if score == max_sc:
                num_mx += 1
            elif score > max_sc:
                max_sc = score
                num_mx = 1
        return num_mx

def main():
    print(Solution().countHighestScoreNodes(parents = [-1,2,0,2,0]))

if __name__ == "__main__":
    main()