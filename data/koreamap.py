class KoreaMapLoader:
    def __init__(self, gis_path, region):
        self.gis_path = gis_path
        self.gis_dir = sorted(os.listdir(gis_path))
        self.region = region

    def load_korea_gpd(self):
        emd_folder = next(folder for folder in self.gis_dir if 'EMD' in folder)
        sig_folder = next(folder for folder in self.gis_dir if 'SIG' in folder)

        emd_shp_path = os.path.join(self.gis_path, emd_folder,
                                    next(f for f in os.listdir(os.path.join(self.gis_path, emd_folder)) if f.endswith('.shp')))
        sig_shp_path = os.path.join(self.gis_path, sig_folder,
                                    next(f for f in os.listdir(os.path.join(self.gis_path, sig_folder)) if f.endswith('.shp')))

        emd_gpd = gpd.read_file(emd_shp_path, encoding='cp949').to_crs(epsg=4326)
        sig_gpd = gpd.read_file(sig_shp_path, encoding='cp949').to_crs(epsg=4326)
        return emd_gpd, sig_gpd

    def select_region_geometry(self, emd_gpd, sig_gpd):
        if self.region not in sig_gpd.A2.values:
            raise ValueError(f"[ERROR] '{self.region}'은 SIG 데이터(A2)에 없습니다.")
        sigungu_name = sig_gpd[sig_gpd.A2 == self.region].A4.values[0]
        return emd_gpd[emd_gpd.A4 == sigungu_name][['A0', 'A1', 'A2', 'A4', 'geometry']]
