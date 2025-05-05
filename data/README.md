# Dataset 소개

이 프로젝트에서 사용하는 위도·경도 데이터는 국토교통부 VWorld에서 제공한 행정구역 경계 데이터를 기반으로 작성되었습니다.

## 데이터 출처
- **법정동 경계 데이터**: [국토교통부 VWorld 법정동 경계 데이터](https://www.vworld.kr/dtmk/dtmk_ntads_s002.do?svcCde=NA&dsId=21)

  
- **GIS 전용 파일 포맷**
  - `.shp` — 지리 정보(공간 좌표) 파일  
  - `.dbf` — 속성 정보(행정구역명 등) 데이터베이스  
  - `.prj` — 좌표계 정보  
  - `.shx` — 인덱스 파일  
  - `.cst`, `.fix` — 기타 시스템 관련 메타데이터

> ⚠️ 해당 데이터는 [CC BY-NC-ND] 라이선스를 따릅니다.  
> 따라서 **변경된 형태의 데이터(.csv 등)는 공유하지 않으며**,  
> 데이터 이용을 원하시는 분은 위 링크를 통해 직접 다운로드해 주시기 바랍니다.
> 위에 파일이 전부 작업 디렉토리에 존재해야 실행가능합니다.


# 초보자를 위한 상세 설명
## step0
 사용하는 라이브러리의 버전이 동일해야 오류 발생이 없습니다.
```python
import sys
print(f"Python version: {sys.version}") # Python version: 3.11.12 
```
 제공되는 함수를 사용하면 보다 편리한 작업이 가능합니다.
```python
!git clone https://github.com/Kim-Dukbae/FULO
```

## step1: 데이터 경로 설정
📂 project 작업 폴더  
  └── 📂 GIS  
    └── 📁 법정동

## step2: 데이터 불러오기.
```python
!git clone https://github.com/Kim-Dukbae/FULO
```

