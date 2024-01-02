numbers = [ 2, 3, 1, 4]

class Solutions(object):
    def combination(self, candidates, target):
        ret = []
        self.dfs(candidates, target, ret)
        return ret
    
    def dfs(self, numbers, target, path, ret):
        if target < 0:
            return
        if target == 0:
            ret.append(path)
            return
        for i in range(len(numbers)):
            self.dfs(numbers[i:], target-numbers[i], path+[numbers[i]], ret)

print(Solutions())
