class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        count = dict()
        for task in tasks:
            if task not in count:
                count[task] = 0
            count[task] += 1
        
        res = 0
        for key, val in count.items():
            if val == 1:
                return -1
            elif val % 3 == 0:
                res += (val // 3)
            else:
                res += (val // 3) + 1

        return res

    
