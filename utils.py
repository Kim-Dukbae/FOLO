import giokakao as gk
import matplotlib as mpl

### 위도,경도 추출함수 ###
# 주소가 올바르지 않다면, lation 변수에 값이 존재하지 않음.
def lat_lon(address):
    lation = gk.convert_address_to_coordinates(address)
    if lation == None:
        return  np.nan,  np.nan
    else:
        lat, lon = lation # 반환된 값은 문자열 type
        return float(lat), float(lon) # 반환된 위도, 경도를 실수형으로 캐스팅 후 반환


# 지도 출력시, 축의 값을 자세히 해주는 함수.
def format_axes_for_map(ax):
    formatter = mpl.ticker.ScalarFormatter(useOffset=False, useMathText=False)
    formatter.set_scientific(False)
    ax.xaxis.set_major_formatter(formatter)
    ax.yaxis.set_major_formatter(formatter)
    return ax
