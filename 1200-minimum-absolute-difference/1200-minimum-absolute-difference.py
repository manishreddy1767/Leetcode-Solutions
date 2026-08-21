class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        l = []
        arr.sort()
        d = arr[1]-arr[0]
        for i in range(2,len(arr)):
            if arr[i]-arr[i-1]<=d:
                d = arr[i]-arr[i-1]
        for i in range(len(arr)):
            if arr[i]-arr[i-1]==d:
                l.append([arr[i-1],arr[i]])
        return l