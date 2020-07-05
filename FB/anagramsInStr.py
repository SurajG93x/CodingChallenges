from collections import Counter

class Solution:
    def findAnagrams(self, s, p):
        if not s or len(p)> len(s):
            return []
        lookup_p=Counter(p)
        p_idx=len(p)-1
        result=[]
        window = Counter(s[:p_idx])
        for i in range(p_idx,len(s)):
            if s[i] not in window:
                window[s[i]]=1
            else:
                window[s[i]]+=1
            if window == lookup_p:
                result.append(i-p_idx)
            window[s[i-p_idx]]-=1
            if window[s[i-p_idx]]==0:
                del window[s[i-p_idx]]
        return result

if __name__ == '__main__':
    f = Solution()
    s = "cbaebabacd"
    p = "abc"
    print(f.findAnagrams(s,p))