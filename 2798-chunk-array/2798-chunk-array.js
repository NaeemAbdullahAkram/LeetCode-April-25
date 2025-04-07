/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let list = [];
    let secondaryList = [];

    for (let i = 0; i < arr.length; i++) {
        secondaryList.push(arr[i]);
        if (secondaryList.length === size) {
            list.push([...secondaryList]); 
            secondaryList = []; 
        }
    }

    if (secondaryList.length > 0) {
        list.push([...secondaryList]); 
    }

    return list;
};