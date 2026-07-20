class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        lookup = {}
        window = {}

        # Frequency of s1
        for ch in s1:
            lookup[ch] = lookup.get(ch, 0) + 1

        left = 0

        # Sliding window on s2
        for right in range(len(s2)):
            window[s2[right]] = window.get(s2[right], 0) + 1

            # Shrink window if its size exceeds len(s1)
            if right - left + 1 > len(s1):
                window[s2[left]] -= 1
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1

            # Compare frequency maps
            if window == lookup:
                return True

        return False