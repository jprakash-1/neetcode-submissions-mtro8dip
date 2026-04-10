class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False 

        s1_hash = [0]*26
        s2_hash = [0]*26 
        for char in s1: 
            s1_hash[ord(char) - ord("a")] += 1 

        for char in s2[:n1]:
            s2_hash[ord(char) - ord("a")] += 1 
        
        print(s1_hash)
        print(s2_hash)
        
        if s1_hash == s2_hash:
            return True

        for index in range(n1, n2): 
            s2_hash[ord(s2[index]) - ord("a")] += 1 
            s2_hash[ord(s2[index - n1]) - ord("a")] -= 1 
            if s1_hash == s2_hash:
                return True 


        return False

