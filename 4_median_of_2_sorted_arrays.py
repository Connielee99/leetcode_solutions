class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        a1, a2 = nums1, nums2
        total = len(a1) + len(a2)
        half = total // 2

        if len(a1) > len(a2):
            a1, a2 = a2, a1
        
        l, r = 0, len(a1) - 1

        while True:

            # midpoints of a1, a2
            mid_a1 = (l+r) // 2
            mid_a2 = half - mid_a1 - 2

            # left right elems
            l_a1 = a1[mid_a1] if mid_a1 >= 0 else float('-inf')
            r_a1 = a1[mid_a1+1] if (mid_a1+1) < len(a1) else float('inf')
            l_a2 = a2[mid_a2] if mid_a2 >= 0 else float('-inf')
            r_a2 = a2[mid_a2+1] if (mid_a2+1) < len(a2) else float('inf')

            if l_a1 <= r_a2 and r_a1 >= l_a2:
                # odd
                if total % 2 != 0:
                    return min(r_a1, r_a2)
                # even
                else:
                    return (max(l_a1, l_a2) + min(r_a1, r_a2)) / 2
            elif l_a1 > r_a2:
                r = mid_a1 - 1
            else:
                l = mid_a1 + 1