

var cancellable = function(fn, args, t) {
    const cancelFn = function(){
        clearInterval(timer);
    }

    fn(...args);
    let timer = setInterval(()=>{
        fn(...args);
    }, t);

    return cancelFn;
};
