// BFS 활용
function solution(numbers, target) {
    let tree = [0];
    let answer = 0;
    for (const num of numbers) {
        const tmp = [];
        for (const parent of tree) {
            tmp.push(parent + num);
            tmp.push(parent - num);
        }
        tree = [...tmp];
    }
    return tree.filter((num) => num === target).length;
}

//DFS 활용
const dfs = (numbers, target, index) => {
    let answer = 0;
    if (index === numbers.length) {
        const sum = numbers.reduce((acc, cur) => acc + cur);
        if (sum === target) return 1;
        else return 0;
    }

    answer += dfs(numbers, target, index + 1);
    numbers[index] *= -1;
    answer += dfs(numbers, target, index + 1);

    return answer;
};

const solution = (numbers, target) => {
    const newNumbers = [...numbers];
    return dfs(newNumbers, target, 0);
};
