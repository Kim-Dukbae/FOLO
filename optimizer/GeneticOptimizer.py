import random
from shapely.geometry import Point
from haversine import haversine

class FOLOOptimizer:
    def __init__(self, polygon, facility_df, positive=[], negative=[]):
        self.polygon = polygon  # 지도 경계 Polygon
        self.facility_df = facility_df  # 시설 정보 DataFrame
        self.positive = positive  # 긍정적 요소 리스트
        self.negative = negative  # 부정적 요소 리스트
        self.history_set = set()  # 생성된 좌표 추적용
        self.survivors = []  # 생존 좌표 저장

    def random_point(self):
        minx, miny, maxx, maxy = self.polygon.bounds
        while True:
            lat = random.uniform(miny, maxy)
            lon = random.uniform(minx, maxx)
            point = Point(lon, lat)
            if point.within(self.polygon):
                return round(lat, 6), round(lon, 6)

    def generate_population(self, n):
        population = []
        while len(population) < n:
            candidate = self.random_point()
            if candidate in self.history_set:
                continue
            population.append(candidate)
            self.history_set.add(candidate)
        return population

    def fitness_function(self, candidate):
        lat, lon = candidate
        point = (lat, lon)
        score = 0

        for item in self.positive:
            name, weight, radius = item['name'], item['weight'], item['radius']
            coords = self.facility_df[self.facility_df['시설분류(소)'] == name][['위도', '경도']].itertuples(index=False, name=None)
            count = sum(1 for coord in coords if haversine(point, coord) * 1000 <= radius)
            score += weight * count

        for item in self.negative:
            name, weight, radius = item['name'], item['weight'], item['radius']
            coords = self.facility_df[self.facility_df['시설분류(소)'] == name][['위도', '경도']].itertuples(index=False, name=None)
            count = sum(1 for coord in coords if haversine(point, coord) * 1000 <= radius)
            score -= weight * count

        return score

    def select_survivors(self, population, origin_location):
        origin_score = self.fitness_function(origin_location)
        survivors = [
            p for p in population
            if self.fitness_function(p) > origin_score
        ]
        return survivors, origin_score
