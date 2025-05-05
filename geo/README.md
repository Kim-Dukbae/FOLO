# 🗺️ KoreaMapLoader - 대한민국 GIS 행정구역 로딩 도구

`KoreaMapLoader`는 국토교통부에서 제공하는 행정구역 Shapefile 데이터를 불러와,  
대한민국의 **시·군·구 단위** 또는 **읍·면·동 단위**의 경계 정보를 추출하는 파이썬 유틸리티입니다.  
FOLO(Finding Optimal Location Optimization) 알고리즘에서 **지리적 검색 공간을 정의**하는 데 사용됩니다.

---

## 메서드 소개
> 📌 폴더명은 'SIG', 'EMD'를 포함해야 하며, 자동 탐지됩니다.<br>
> 국토교통부 파일을 다운받아서 그대로 상위 폴더 안에 저장해주세요.

### ✅ `load_korea_gpd()`
- 국토교통부의 EMD(읍면동) / SIG(시군구) shapefile을 자동 탐색 및 로딩
- 좌표계(CRS)를 WGS84 (`EPSG:4326`)로 통일(위도, 경도로 변환.)
- 반환값: `emd_gpd`, `sig_gpd` (GeoDataFrame 2개)

### ✅ `select_region_geometry(emd_gpd, sig_gpd)`
- 특정 시군구의 이름을 기반으로 **읍면동 경계만 필터링**하여 반환
- 결과는 해당 지역의 **지오메트리(Polygon)** 정보를 포함한 GeoDataFrame

## 🛠️ region(지역명) 한계
현재는 '동대문구', '은평구', '동작구' 등과 같이 시·군·구 단위의 정확한 행정구역 명칭을 문자열로 직접 입력해야 합니다. <br>
입력된 지역명이 GIS 데이터의 A2 컬럼과 정확히 일치해야만 정상 작동합니다.(추후 개선해보겠습니다..)

🔎 예시: <br>
✅ '강남구' → 가능 <br>
❌ '서울특별시 강남구' → 인식 불가
