import argparse
from osgeo import gdal
from tqdm import tqdm
from pathlib import Path
from typing import Union

def extract_all_bands(input_raster: Union[str, Path], output_dir: Union[str, Path]):
    """
    Extracts all bands from a raster and saves them as separate GeoTIFF files.
    Parameters:
    input_raster (str): Path to the input raster file.
    output_dir (str): Directory where the output GeoTIFF files will be saved.
    """
    input_raster = Path(input_raster)

    with gdal.Open(input_raster, gdal.GA_ReadOnly) as raster:
        # Get the number of bands
        if raster is not None:
            num_bands = raster.RasterCount
            print(f"Number of bands: {num_bands}")
        else:
            print("Failed to open raster file.")   

    for band_number in tqdm(range(1, num_bands + 1)):
        extract_band(input_raster, Path(output_dir) / f"{input_raster.stem}_band{band_number}.tif", band_number)

def extract_band(input_raster: Union[str, Path], output_raster: Union[str, Path], band_number: int):
    """
    Extracts a specified band from a raster and saves it as a new GeoTIFF file.

    Parameters:
    input_raster (str): Path to the input raster file.
    output_raster (str): Path to the output GeoTIFF file.
    band_number (int): The band number to extract (1-based index).    
    """        

    # Open the input raster
    dataset = gdal.Open(input_raster, gdal.GA_ReadOnly)
    if dataset is None:
        raise RuntimeError("Failed to open input raster.")

    # Select the band to extract (1-based index)
    band = dataset.GetRasterBand(band_number)

    # Get metadata from original dataset
    geotransform = dataset.GetGeoTransform()
    projection = dataset.GetProjection()
    nodata_value = band.GetNoDataValue()

    # Get raster dimensions
    cols = dataset.RasterXSize
    rows = dataset.RasterYSize

    # Create the output raster with the same dimensions as the input
    driver = gdal.GetDriverByName("GTiff")
    out_dataset = driver.Create(output_raster, cols, rows, 1, band.DataType)

    # Write the band data to the output file
    out_band = out_dataset.GetRasterBand(1)
    out_band.WriteArray(band.ReadAsArray())

    # Set metadata for the output raster
    out_dataset.SetGeoTransform(geotransform)
    out_dataset.SetProjection(projection)
    if nodata_value is not None:
        out_band.SetNoDataValue(nodata_value)

    # Flush data and close files
    out_band.FlushCache()
    out_dataset = None
    dataset = None

    print(f"Single band {band_number} written to {output_raster}")
    
def main():
    parser = argparse.ArgumentParser(description="Extract a single band from a raster and save it as a GeoTIFF.")
    
    parser.add_argument("input_raster", help="Path to the input raster file.")
    parser.add_argument("output_raster", help="Path to the output GeoTIFF file.")
    parser.add_argument("band_number", type=int, help="Band number to extract (1-based index).")

    args = parser.parse_args()

    extract_band(args.input_raster, args.output_raster, args.band_number)

if __name__ == "__main__":
    main()