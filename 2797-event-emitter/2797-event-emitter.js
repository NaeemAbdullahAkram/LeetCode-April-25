class EventEmitter {
    constructor() {
        this.callTable = {};
    }

    subscribe(eventName, callback) {
        if(this.callTable[eventName])
            this.callTable[eventName].push(callback);
        else
            this.callTable[eventName] = [callback];

        return {
            unsubscribe: () => {
                this.callTable[eventName] = this.callTable[eventName].filter((fn) => fn != callback);        
            }
        };
    }
        emit(eventName, args = []) {
        if(!this.callTable[eventName]){
            return [];
        }

        return this.callTable[eventName].map((fn) =>fn(...args));
    }
}