## 컴프리헨션
하나 이상의 이터레이터로부터 파이선의 자료구조를 만드는 방법

### 리스트 컴프리헨션
#### 기본적인 방법
```python
number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
number_list
```
`[1, 2, 3, 4, 5]`

#### range
```python
number_list = []
for number in range(1, 6):
    number_list.append(number)

number_list
```

or

```python
number_list = list(range(1, 6))
number_list
```
`[1, 2, 3, 4, 5]`

#### 리스트 컴프리헨션  
`[표현식 for 항목 in 순회 가능한 객체 if 조건]`
```python
number_list = [number for number in range(1, 6)]
number_list
```
`[1, 2, 3, 4, 5]`
```python
number_list = [number - 1 for number in range(1, 6)]
number_list
```
`[0, 1, 2, 3, 4]`
```python
a_list = [number for number in range(1, 6) if number % 2 == 1]
a_list
```
`[1, 3, 5]`

#### 2중 반복문
기존 2중 반복문
```python
rows = range(1, 4)
cols = range(1, 3)
for row in rows:
    for col in cols:
        print(row,col)
```
```
1 1
1 2
2 1
2 2
3 1
3 2
```
컴프리헨션
```python
rows = range(1, 4)
cols = range(1, 3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)
```
```
1 1
1 2
2 1
2 2
3 1
3 2
```

### 딕셔너리 컴프리헨션
`{키_표현식 : 값_표현식 for 표현식 in 순회 가능한 객체}`
```python
word = 'letters'
letter_counts = {letter : word.count(letter) for letter in word}
letter_counts
```
`{'1': 1. 'e': 2. 't': 2. 'r': 1, 's': 1}`

위 예제는 `e`와 `t`에서 두 번씩 조회를 하기 때문에 딕셔너리 결과에는 영향이 없지만 비 효율적이다.  
이를 아래와 같이 바꾸면 더 좋다

```python
word = 'letters'
letter_counts = {letter : word.count(letter) for letter in set(word)}
letter_counts
```
`{'1': 1. 'e': 2. 't': 2. 'r': 1, 's': 1}`

### 셋 컴프리헨션
`{표현식 for 표현식 in 순회 가능한 객체}`
```python
a_set = {number for number in range(1, 6) if number % 3 == 1}
a_set
```
`{1, 4}`

### 제너레이터 컴프리헨션
