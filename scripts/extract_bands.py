from ihme_vaccine_rasters import extract_all_bands
input_raster = "/workspaces/IHME_vaccine_rasters/data/mcv1_cov_mean_raked_2000_2023.tif"
extract_all_bands(input_raster=input_raster, output_dir="/workspaces/IHME_vaccine_rasters/data")