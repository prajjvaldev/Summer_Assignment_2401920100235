class Solution:
    def checkInclusion(self, s1, s2):
        m, n = len(s1), len(s2)

        if m > n:
            return False

        count1 = [0] * 26
        window = [0] * 26

        for i in range(m):
            count1[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1

        if count1 == window:
            return True

        for i in range(m, n):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - m]) - ord('a')] -= 1

            if count1 == window:
                return True

        return False
