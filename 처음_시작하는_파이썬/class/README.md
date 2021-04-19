# get/set 속성값과 프로퍼티
자바에서는 외부로부터 바로 접근할 수 없는 private 객체 속성을 지원한다.  

private 속성의 값을 읽고 쓰기 위해 `getter` 메서드와 `setter` 메서드를 사용한다.

## 프로퍼티
```python
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print("inside the getter")
        return self.hidden_name
    def set_name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
    
    name = property(get_name, set_name)

```
해당 클래스는 이제 `getter`와 `setter`메서드를 name이라는 속성의 프로퍼티로 정의한다. `property()`의 첫 번째 인자는 getter 메서드, 두 번째 인자는 setter 메서드다.


```python
fowl = Duck("Howard")
fowl.name
```
```
inside the getter
"Howard"
```

`get_name()`메서드를 직접 호출할 수 있다.
```python
fowl.get_name()
```
```
inside the getter
"Howard"
```

name 속성에 값을 할당하면 `set_name()`메서드를 호출한다.
```python
fowl.name = "Daffy"
```
```
inside the setter
```

`set_name()`메서드도 여전히 호출 가능하다.

## 데코레이터
```python
class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name

    @property
    def name(self):
        print("inside the getter")
        return self.hidden_name
    
    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.hidden_name = input_name
```

name 속성에는 접근 가능하지만 `get_nmae()`, `set_name()`메서드를 볼 수 없다.

# private
private는 속성 이름 앞에 던더(__)를 붙이면 된다.
```python
class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    
    @property
    def name(self):
        print("inside the getter")
        return self.__name

    @name.setter
    def name(self, input_name):
        print("inside the setter")
        self.__name = input_name
```
이렇게 하면 이전과 같이 `Duck.name`으로 접근할 수 있지만 `__name` 속성에 바로 접근할 수 없다. 


