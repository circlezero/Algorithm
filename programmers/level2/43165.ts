// BFS 활용
const bfs_solution = (numbers: number[], target: number) => {
    let tree: number[] = [0];

    for (let i = 0; i < numbers.length; i++) {
        const tmp: number[] = [];
        const num = numbers[i];
        for (let j = 0; j < tree.length; j++) {
            tmp.push(tree[j] + num);
            tmp.push(tree[j] - num);
        }
        tree = [...tmp];
    }

    return tree.filter((num) => num === target).length;
};

//DFS 활용
const dfs = (numbers: number[], target: number, index: number) => {
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

const dfs_solution = (numbers: number[], target: number) => {
    const newNumbers = [...numbers];
    return dfs(newNumbers, target, 0);
};
