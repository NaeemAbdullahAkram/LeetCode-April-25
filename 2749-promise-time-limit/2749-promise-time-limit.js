var timeLimit = (fn, t) => async (...args) => 
    Promise.race([
        fn(...args), 
        new Promise((_, reject) => setTimeout(() => reject('Time Limit Exceeded'), t))
    ]);

