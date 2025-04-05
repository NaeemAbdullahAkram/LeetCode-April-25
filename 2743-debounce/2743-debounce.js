var debounce = function(fn, t) {
    let timer;
    return function(...args) {
        clearTimeout(timer); // If new event happens in less than t time then it cancel previous event. It does not affect NULL timer ...
        timer = setTimeout(()=>{
            fn(...args);
        }, t);
    }
};
