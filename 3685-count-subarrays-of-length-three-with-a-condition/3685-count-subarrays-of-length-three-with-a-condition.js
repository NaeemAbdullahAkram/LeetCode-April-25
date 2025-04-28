var countSubarrays = function(nums) {
    let count = 0;
    const n = nums.length;
    for (let i = 0; i < n - 2; i++) {
        let first = nums[i];
        let sec = nums[i + 1];
        let third = nums[i + 2];
        if (first + third === sec / 2) {
            count++;
        }
    }
    return count;
};