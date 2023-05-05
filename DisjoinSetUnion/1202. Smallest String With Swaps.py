from collections import defaultdict
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent=[i for i in range(len(s))]

        def find(a,parent):
            if a==parent[a] : return a
            parent[a]=find(parent[a],parent)
            return parent[a]
        size=len(pairs)
        for i in range(size):
            pairs.append([pairs[i][1],pairs[i][0]])
        for u,v in pairs:
            p_u=find(u,parent)
            p_v=find(v,parent)
            if p_u!=p_v:
                parent[p_v]=p_u
        lst=['']*len(s)
        dict=defaultdict(list)
        for i in range(len(parent)):
            dict[parent[i]].append(i)
        
        for values in dict.values():
            temp_s=[]
            for i in values:
                temp_s.append(s[i])
            temp_s.sort()
            j=0
            for i in values:
                lst[i]=temp_s[j]
                j+=1
        return ''.join(lst)
        