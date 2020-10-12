#!/usr/bin/env python3
# By Icarus747
# Created 10/11/2020

# Used for converting DCS MGRS grid coordinates to Lat/Long coordinates.

import mgrs


def main():
    m = mgrs.MGRS()
    # dcs = '38TLN046623'
    dcs = input("Enter MGRS cord.")

    dd = m.toLatLon(dcs)

    lat = m.ddtodms(dd[0])
    Lat = round(lat[1] + lat[2] / 60, 1)

    long = m.ddtodms(dd[1])
    Long = round(long[1] + long[2] / 60, 1)

    print(f"N{int(lat[0])} {Lat}")
    print(f"E0{int(long[0])} {Long}")


if __name__ == '__main__':
    main()
    # TODO: Error handeling for incorect MGRS grid.
