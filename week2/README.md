# week 2

2주차 과제들

1. [인구조사 자료 데이터 가공 및 시각화](#1-인구조사-자료-데이터-가공-및-시각화)
2. [타이타닉 문제 풀기](#2-타이타닉-문제-풀기)
3. [배운 내용](#3-배운-내용)

## 1. 인구조사 자료 데이터 가공 및 시각화

week2 폴더 내부에 있는 2020_인구조사.xlsx 파일을 판다스로 불러서 전처리 작업을 한 뒤에 시각화

1. 엑셀 파일로 부터 데이터를 불러와서 전처리
2. 전처리된 데이터로부터 원하는 데이터 추출
3. 추출된 데이터를 시각화

하위 작업들

- popdataload.py 파일에 `2020_인구조사.xlsx`파일을 정제한 데이터 프레임을 반환하는 load_data() 함수 구현
- getnuminfo.py 파일에 한 지역과 다른 지역들을 비교하는 데이터프레임을 반환하는 함수들 구현
- ratiobypopulation.py 파일에 인구 대비 x의 데이터를 반환하는 함수들 구현
- vizpopulationinfo.py 파일에 인구 정보들을 시각화하는 함수들 구현
- test1.ipynb 주피터 노트북으로 구현된 함수들을 사용해보기

## 2. 타이타닉 문제 풀기

풀이한 주피터노트북 파일 이름은 `titanic_본인영어이름이니셜.ipynb`

_ex)_ `titanic_ljw.ipynb`

문제 링크: [https://www.kaggle.com/competitions/titanic/overview](https://www.kaggle.com/competitions/titanic/overview)

## 3. 배운 내용