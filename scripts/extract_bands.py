from ihme_vaccine_rasters import extract_band, extract_all_bands

input_raster = "/workspaces/IHME_vaccine_rasters/data/mcv1_cov_mean_raked_2000_2023.tif"
output_raster = "/workspaces/IHME_vaccine_rasters/data/mcv1_cov_mean_raked_2000_2023_band1.tif"
band_number = 1

# extract_band(input_raster=input_raster, output_raster=output_raster, band_number=band_number)

extract_all_bands(input_raster=input_raster, output_dir="/workspaces/IHME_vaccine_rasters/data")