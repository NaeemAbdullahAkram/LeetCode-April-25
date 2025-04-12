var flat = function (arr, n) {
    let ans = [...arr];
    let i = 0;

    while (i < n) {
        const current = [];
        for (let ele of ans) {
            if (Array.isArray(ele)) {
                current.push(...ele);
            } else {
                current.push(ele);
            }
        }
        ans = current;
        i++;
    }

    return ans;
};
