# DCS_MGRS_Converter
A simple coordinate conversion utility to convert from MGRS, DD, or DMS to any of the other coordinate systems.


## Usage

TODO - A simple GUI Frontend needs to be worked in, but for now it can be executed via Python3...

```
python3 main.py <coordinate-type> <coordinates>
```

Example:
```
python3 main.py mgrs 17SNU5478598457
```

Returns:
```
{'mgrs': '17SNU5478598457', 'dd': '35.227667 -80.397959', 'dms': 'N 35 13 39.6020, W 80 23 52.6516'}
```
