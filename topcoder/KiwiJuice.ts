
type KiwiInfoTypes = {
    /**
     * capacities : 병의 용량
     */
    capacities: number[];
    /**
     * bottles : 현재 주스 용량 
     */
    bottles: number[];
    /**
     * fromId : 옮길 병의 index 
     */
    fromId: number[];
    /**
     * toId : 옮겨질 병의 index
     */
    toId: number[];
}

const solution = (kiwiInfo: KiwiInfoTypes) => {
    const {capacities, bottles, fromId, toId}  = kiwiInfo;

    for(let i=0; i<fromId.length; i++) {
        const fromIndex = fromId[i];
        const toIndex = toId[i];

        if(bottles[toIndex] === bottles[fromIndex]) continue;
        bottles[toIndex] += bottles[fromIndex];
        bottles[fromIndex] = 0;
        if(capacities[toIndex] < bottles[toIndex]) {
            bottles[fromIndex] = bottles[toIndex] - capacities[toIndex]; 
            bottles[toIndex] = capacities[toIndex];
        }
    }

    return bottles;
}

const Bettersolution = (kiwiInfo: KiwiInfoTypes) => {
    const {capacities, bottles, fromId, toId}  = kiwiInfo;

    for(let i=0; i<fromId.length; i++) {
        const fromIndex = fromId[i];
        const toIndex = toId[i];

        if(bottles[toIndex] === bottles[fromIndex]) continue;
        const sum = bottles[toIndex] + bottles[fromIndex];
        bottles[toIndex] = Math.min(sum, capacities[toIndex]);
        bottles[fromIndex] = sum - bottles[toIndex]
    }

    return bottles;
}

const exampleInfo: KiwiInfoTypes = {
    capacities:[20, 20],
    bottles: [5, 8],
    fromId: [0],
    toId: [1]
}