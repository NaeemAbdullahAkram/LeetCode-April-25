var countGood = function (nums, k) {
    let left = 0;
    let count = 0;
    let pairCount = 0;
    const freq = new Map();

    for (let right = 0; right < nums.length; right++) {
        const val = nums[right];
        freq.set(val, (freq.get(val) || 0) + 1);
        pairCount += freq.get(val) - 1;

        while (pairCount >= k) {
            count += nums.length - right;
            const leftVal = nums[left];
            pairCount -= freq.get(leftVal) - 1;
            freq.set(leftVal, freq.get(leftVal) - 1);
            left++;
        }
    }
    return count;
};