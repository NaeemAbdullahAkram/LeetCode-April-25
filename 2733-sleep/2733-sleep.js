async function sleep(millis) {
    let ans = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(millis);
        }, millis);
    })

    return ans;
}
 let t = Date.now()
 sleep(100).then(() => console.log(Date.now() - t)) // 100