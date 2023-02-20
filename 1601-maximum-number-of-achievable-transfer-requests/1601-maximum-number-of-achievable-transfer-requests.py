class Solution:
    import itertools
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = 0
        updatedReque = []
        for items in requests:
            if len(set(items)) == 1:
                ans += 1

            else:
                updatedReque.append(items)

        allComb = []

        for i in range(len(updatedReque)+1):
            for items in list(itertools.combinations(updatedReque, i)):
                if len(items) == 0:
                    allComb.append(0)

                else:
                    tempvec = [0] * n
                    for val in items:
                        tempvec[val[0]] -= 1
                        tempvec[val[1]] += 1

                    if set(tempvec) == {0}:
                        allComb.append(len(items))

        return max(allComb) + ans
