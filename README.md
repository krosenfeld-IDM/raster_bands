# Raster Bands
Extract bands from a multi-channel raster. Requires GDAL.

This can be useful if you're trying to open a .tiff file using Pillow and run into something like:
```bash
More samples per pixel than can be decoded: 24
Traceback (most recent call last):
  File "open_sesame.py", line 13, in <module>
    raster = Image.open(raster_file)
  File "/home/user/.venv/lib/python3.10/site-packages/PIL/Image.py", line 3532, in open
    raise UnidentifiedImageError(msg)
```

## Recommended usage
Using [pixi](https://pixi.sh/latest/):
```
pixi install
```
`scripts/extract_bands.py` provides an example to extract and save individual bands from a file.

