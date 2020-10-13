#!/usr/bin/env python3
# By Icarus747
# Created 10/11/2020

# Used for converting DCS MGRS grid coordinates to Lat/Long coordinates.

import mgrs
import re


def main():
    m = mgrs.MGRS()
    # dcs = '38TLN046623'
    dcs = input("Enter MGRS cord.\n\r")
    dcs = validate_mgrs(dcs)
    dd = m.toLatLon(dcs)

    lat = m.ddtodms(dd[0])
    Lat = round(lat[1] + lat[2] / 60, 1)

    long = m.ddtodms(dd[1])
    Long = round(long[1] + long[2] / 60, 1)

    print(f"N {int(lat[0])} {Lat}")
    print(f"E 0{int(long[0])} {Long}")


def validate_mgrs(dcs):
    pattern = r'^\b\d{2}[a-z]{3}\d{6,10}\b'
    if re.match(pattern, dcs.lower()):
        return dcs
    else:
        print("Verify MGRS grid and try again.\n\r")
        main()

if __name__ == '__main__':
    main()
