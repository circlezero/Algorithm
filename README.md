# 알고리즘 공부

## 푸는 알고리즘 사이트
1. [BOJ](https://www.acmicpc.net/)
2. [Codility](https://app.codility.com/programmers/)
3. [Programmers](https://programmers.co.kr/)
4. [Algospot](https://algospot.com/)

---

## 알고리즘 풀이에 자주 활용 되는 파이썬 기능들

### ● For loop
알고리즘 풀이를 하면서 항상 빠짐없이 사용되는 기능이죠

for 문에 관해서는 아래의 3가지만 알면 된다고 생각합니다.

> 1. **for i in A**
> 2. **for i in Range(len(A))**
> 3. **for i,v in A**

코드를 통해서 하나씩 살펴보겠습니다.

#### 1. for i in A
```
A = [1, 20, 300]
for i in A:
    print(i)

# Output
# 1
# 20
# 300
```
여기서 i는 iterator가 되겠고 A는 Iterable Object 입니다.

iterator랑 iterable에 대해서 모르신다면! 밑의 링크를 참조하세요

[Python Docs-Glossary](https://docs.python.org/3/glossary.html#term-iterable) / [Python Docs-Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html#functional-howto-iterators)

A는 문자열, 배열, 튜플 등 다 사용 가능합니다.

#### 2. for i in range(len)
```
for i in range(10):
    print(i)

# Output
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
```
아실거라 믿습니다. 🤗

#### 3. for i,v in A
```
A = ['a', 'b', 'c', 'd', 'e']
for i,v in enumerate(A):
    print(i, v)

# Output
# 0 a
# 1 b
# 2 c
# 3 d
# 4 e
```
[enumerate()](https://docs.python.org/3/library/functions.html#enumerate)는 python built-in 함수로 enumerate object를 반환해준다고 합니다.

index와 value를 편하게 사용할 수 있어 종종 사용하곤 합니다.

---
## 정리할것들

### ● List

### ● 입출력
input() 보다는 sys.stdin.readline()을 사용하자

### ● 수학
log
pow == **
lambda

### ● Collections