# BI 도구와 모니터링
## 스프레드시트에 의한 모니터링
데이터를 살펴보고 싶을 때 이용하는 것이 애드 혹 분석이라면.  
> Ad-hoc 분석  
> - 분석을 하고 싶을 때만 특정 목적을 가지고 수작업으로 하는 일회성 데이터 분석  
> - 데이터 마트를 만들지 않고 데이터 레이크, 데이터 웨어하우스에 직접 연결  

보다 계획적으로 데이터의 변활를 추적해 나가는 것이 **모니터링**이다.  
데이터의 변화를 모니터링하고 만약 예상과 다른 움직임이 있다면, 그때는 행동을 해야 한다.  

## 데이터에 근거한 의사 결정
프로젝트의 현황을 파악하기 위한 숫자로 업계마다 중요한 지표인 **KPI(Key Performance Indicator)**가 자주 이용된다.

### KPI의 예시
- 웹 서비스의 KPI
    - DAU(Daily Active User) : 서비스를 이용한 1일 유저의 수
    - ARPPU(Average Revenue Per Paid User) : 유료 고객 1인당 평균 매출
- 온라인 광고의 KPI
    - CTR(Click Through Rate) : 고아고의 표시 횟수에 대한 클릭 비율  
    - CPC(Cost Per Click) : 1회 클릭에 대해서 지불한 광고비

KPI 모니터링에서 의식하고 싶은 것은 그것이 **행동 가능**한 것인가 이다. 즉, 그 결과에 따라 자신의 다음 행동이 결정될지의 여부다.  
자신의 행동을 결정할 때 직감에 의잫는 것이 아니라 객관적인 데이터를 근거하여 판단하는 것을 **데이터 기반 의사 결정**이라고 한다.

### 월간 보고서
#### 목표
||2017년 1월|2017년 2월|2017년 3월|
|---|---|---|---|
|매출|60,000|70,000|80,000|
|원가율|30%|30%|30%|
#### 실적
||2017년 1월|2017년 2월|2017년 3월|
|---|---|---|---|
|매출|59,900|63,300|72,400|
|원가|17,000|20,000|29,000|
|원가율|28%|32%|40%|

위와 같은 보고서가 있을때 우리는 원가율이 목표를 웃돌고 있는 것을 명확히 알 수 있다.  
이런 형태의 보고서 작성에 사용되는 것이 스프레드시트다. 원시적이지만, 숫자를 입력하는 정도는 유연성이 있으며 함부로 시스템화하면 나중에 손 보는 것이 오히려 어려워진다.  

스플레드시트의 어려운점은 
1. 보고서에 입력하는 숫자를 어디선가 계산해야한다.
2. 상세한 내역을 조사할 수 있게 하기 힘들다.  

두 가지 이다.  
첫 번째를 위해 데이터 웨어하우스의 배치 처리가 있고, 두 번째를 위해 BI도구가 사용된다.  

## 변화를 파악하고 세부 사항을 이해하기
BI 도구는 고속의 집계 엔진을 내장하고 있어 수백만 레코드 정도의 스몰 데이터라면 순식간에 그래프를 그려준다. 애드 혹 분석 등에서 대화형으로 데이터를 시각화하고 싶을 때 특히 편리하다.  

