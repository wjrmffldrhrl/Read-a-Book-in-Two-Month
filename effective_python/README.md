# Effective Python

# 45. 애트리뷰트를 리팩터링하는 대신 @property를 사용하라
내장 @property 데코레이터를 사용하면, 겉으로는 단순한 애트리뷰트처럼 보이지만 실제로는 지능적인 로직을 수행하는 애트리뷰트를 정의할 수 있다.
- 간단한 수치 애트리뷰트를 그때그때 요청에 따라 계산해 제공하도록 바꿀 수 있다.

예를 들어 일반 파이썬 객체를 사용해 리키 버킷 흐름 제어 알고리즘을 구현한다고 하자.

### 리키 버킷 흐름 제어 알고리즘

```python
from datetime import datetime, timedelta

class Bucket:
    def __init__(self, period):
        self.period_dalta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0
    def __repr__(self):
        return f"Bucket(quota={self.quota})"
```

리키 버킷 알고리즘은 시간을 일정한 간격으로 구분하고, 가용 용량을 소비할 때마다 시간을 검사해서 주기가 달라질 경우에는 이전 주기에 미사용한 가용 용량이 새로운 주기로 넘어오지 못하게 막는다.
```python
def fill(bucket, amount):
    now = datetime.now()
    if(now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount
```

할당량을 소비하는 쪽에서는 어떤 작업을 하고 싶을 때마다 먼저 리키 버킷으로부터 자신의 작업에 필요한 용량을 할당 받아야 한다.
```python
def deduct(bucket, amount):
    now = datetime.now()
    if(now - bucket.reset_time) > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    else:
        bucket.quota -= amount
        return True
```

이 클래스를 사용하려면 먼저 버킷에 할당량을 채워넣고 사용할 때마다 필요한 용량을 버킷에서 빼야한다.

```python
bucket = Bucket(60)
fill(bucket, 100)

deduct(bucket, 99) # True

```

어느 순간이 되면, 버킷에 들어 있는 할당량이 데이터 처리에 필요한 용량 보다 작아지면서 더 이상 작업을 진행하지 못한다.
```python
deduct(bucket, 99) # False

```


해당 구현의 문제점은 버킷이 시작할 때 할당량이 얼마인지 알 수 없다는 것이다.
이러한 문제를 해결하기 위해 이번 주기에 재설정된 가용 용량인 max_quota와 이번 주기에 버킷에서 소비한 용량의 합계인 quota_consumed를 추적하게 변경할 수 있다.

```python
class NewBucket:
    def __init__(self, period):
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.max_quota = 0
        self.quota_consumed = 0

    def __repr__(self):
        return f"""NewBucket(max_quota={self.max_quota}, 
        quota_consumed={self.quota_consumed})
        """

    @property
    def quota(self):
        return self.max_quota - self.quota_consumed

    @quota.setter
    def quota(self, amount):
        delta = self.max_quota - amount
        
```