import os
from raster_bands import extract_all_bands
os.chdir(os.path.dirname(__file__))
input_raster = "../data/mcv1_cov_mean_raked_2000_2023.tif"
extract_all_bands(input_raster=input_raster, output_dir="../data")