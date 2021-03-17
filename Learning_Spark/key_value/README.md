# 키/값 페어
스파크는 키/값 쌍을 가지고 있는 RDD에 대해 특수한 연산들을 제공한다. 이 RDD들은 페어 RDD라 불린다.  

페어 RDD들은 각 키에 대해 병렬로 처리하거나 네트워크상에서 데이터를 다시 그룹핑하게 해 주므로 많은 프로그램에서 유용하게 사용할 수 있다. 예를 들어, 페어 RDD는 각 키로 구분해서 집합 연산이 가능한 `reduceByKey()`나 동일 키에 대한 데이터끼리 분류해서 두 RDD를 합쳐주는 `join()`같은 메소드들을 갖고 있다.  

# 페어 RDD 생성
스파크에서는 페어 RDD를 만들기 위해 키/값 데이터를 곧바로 페어 RDD로 만들어 리턴하거나 일반 RDD를 페어 RDD로 변환한다. 일반 RDD를 페어 RDD로 변환할 때 `map()`함수를 사용해서 변환을 한다.  

```python
# 첫 번째 단어를 키로 사용한 페어 RDD
pairs = lines.map(lamba x: (x.split(" ")[0], x))
```

# 페어 RDD의 트렌스포메이션
페어 RDD는 기본 RDD에서 가능한 모든 트렌스포메이션을 사용할 수 있다. 단, 페어 RDD는 튜플을 가지므로 개별 데이터를 다루는 함수 대신 튜플을 처리하는 함수를 전달해야 한다. 

<table>
<thead>
  <tr>
    <th>함수 이름</th>
    <th>목적</th>
    <th>예</th>
    <th>결과</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>`reduceByKey(func)`</td>
    <td>동일 키에 대한 값들을 합친다</td>
    <td>`rdd.reduceByKey((x, y) =&gt; x + y)`</td>
    <td>{(1,2), (3, 10)}</td>
  </tr>
  <tr>
    <td>`groupByKey()`</td>
    <td>동일 키에 대한 값들을 그룹화한다.</td>
    <td>`rdd.groupByKey()`</td>
    <td>{(1, [2]), (3, [4, 6])}</td>
  </tr>
  <tr>
    <td>`combineByKey(createCombiner, mergeValue, mergeCombiners, partitioner)`</td>
    <td>다른 결과 타입을 써서 동일 키의 값들을 합친다.</td>
    <td>생략</td>
    <td>생략</td>
  </tr>
  <tr>
    <td>`mapValues(func)`</td>
    <td>키의 변경 없이 페어 RDD의 각 값에 함수를 적용한다.</td>
    <td>`rdd.mapValues(x =&gt; x+1)`</td>
    <td>{(1, 3), (3, 5), (3, 7)}</td>
  </tr>
  <tr>
    <td>`flatMapValues(func)</td>
    <td>페어 RDD의 각 값에 대해 반복자를 리턴하는 함수를 적용하고,<br><br>리턴받은 값들에 대해 기존 키를 써서 키/값 쌍을 만든다.<br>종종 토큰 분리에 쓰인다.</td>
    <td>`rdd.flatMapValues(x =&gt; (x to 5))`</td>
    <td>{(1, 2), (1, 3), (1, 4), (1, 5), (3, 4), (3, 5)}</td>
  </tr>
  <tr>
    <td>`keys()`</td>
    <td>RDD가 가진 키들만을 되돌려 준다.</td>
    <td>`rdd.keys()`</td>
    <td>{1, 3, 3}</td>
  </tr>
  <tr>
    <td>`values()`</td>
    <td>RDD가 가진 값들만을 되돌려 준다.</td>
    <td>`rdd.values()`</td>
    <td>{2, 4, 6}</td>
  </tr>
  <tr>
    <td>`sortByKey()`</td>
    <td>키로 정렬된 RDD를 되돌려 준다.</td>
    <td>`rdd.sortByKey()`</td>
    <td>{(1, 2), (3, 4), (3, 6)}</td>
  </tr>
</tbody>
</table>