class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0
        sorted_indices = SortedList() 

        val_to_idx = {num: i for i, num in enumerate(nums1)}
        for num in nums2:
            idx_nums1 = val_to_idx[num]
            l_cnt = bisect_left(sorted_indices, idx_nums1)
            r_cnt = (len(nums1) - 1 - idx_nums1) - (len(sorted_indices) - l_cnt)

            res += l_cnt * r_cnt
            sorted_indices.add(idx_nums1)

        return res