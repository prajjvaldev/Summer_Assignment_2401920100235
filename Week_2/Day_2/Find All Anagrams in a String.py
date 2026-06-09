class Solution:
    def findAnagrams(self, s, p):
        result = []

        if len(s) < len(p):
            return result

        p_count = [0] * 26
        window_count = [0] * 26

        for ch in p:
            p_count[ord(ch) - ord('a')] += 1

        window_size = len(p)

        for i in range(len(s)):
            window_count[ord(s[i]) - ord('a')] += 1

            if i >= window_size:
                window_count[ord(s[i - window_size]) - ord('a')] -= 1

            if p_count == window_count:
                result.append(i - window_size + 1)

        return result
