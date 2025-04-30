from tqdm import tqdm

class FOLO:  # Finding Optimal Location Optimization
    def __init__(self, gis_path=None, region=None):
        self.gis_path = gis_path
        self.region = region

        self.korea_map = KoreaMapLoader(gis_path=gis_path, region=self.region)
        self.emd_gpd, self.sig_gpd = self.korea_map.load_korea_gpd()
        self.selected_geometry = self.korea_map.select_region_geometry(self.emd_gpd, self.sig_gpd)

    def plot(self, color='lightblue', edge='black'):
        fig, ax = plt.subplots(figsize=(5, 5))
        self.selected_geometry.plot(ax=ax, color=color, edgecolor=edge)
        formatter = mpl.ticker.ScalarFormatter(useOffset=False, useMathText=False)
        formatter.set_scientific(False)
        ax.xaxis.set_major_formatter(formatter)
        ax.yaxis.set_major_formatter(formatter)
        plt.show()

    def training(self, origin_address, facility_df, positive, negative,
              n=30, generations=50, eary_stop=10):
        lat, lon = lat_lon(origin_address)
        if np.isnan(lat) or np.isnan(lon):
            raise ValueError("주소를 다시 확인해주세요.")

        origin_location = (round(lat, 6), round(lon, 6))
        optimizer = FOLOOptimizer(polygon=self.selected_geometry.geometry.union_all(),
                                  facility_df=facility_df,
                                  positive=positive,
                                  negative=negative)

        survivors, origin_score = optimizer.select_survivors(
            optimizer.generate_population(n), origin_location
        )

        no_change_count = 0
        prev_survivors_set = set(survivors)

        for generation in tqdm(range(generations), desc="FOLO 최적화 진행 중"):  # 첫 세대는 위에서 수행
            new_population = optimizer.generate_population(n)
            combined = survivors + new_population

            # 중복 제거 후 생존 위치 재선택
            survivors, _ = optimizer.select_survivors(combined, origin_location)
            current_survivors_set = set(survivors)

            if current_survivors_set == prev_survivors_set:
                no_change_count += 1
            else:
                no_change_count = 0

            if no_change_count >= eary_stop:
                print(f"[조기 종료] {generation+1}세대에서 {eary_stop}세대 동안 연속 변화 없음")
                break

            prev_survivors_set = current_survivors_set

        # 최종 생존 위치 점수 계산 및 정렬
        ranked = [
            {'lat': lat, 'lon': lon, 'score': optimizer.fitness_function((lat, lon))}
            for lat, lon in survivors
        ]
        ranked = sorted(ranked, key=lambda x: x['score'], reverse=True)

        return ranked
