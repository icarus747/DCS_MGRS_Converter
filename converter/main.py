#!/usr/bin/env python
from mgrs import MGRS
import click


class MGRStoDDM:
    def __init__(self, mgrs_input):
        self.mgrs = MGRS()
        self.mgrs_input = mgrs_input

    @property
    def latitude(self):
        dd = self.mgrs.toLatLon(self.mgrs_input)

        return f"N {self._coord_convert(dd[0])}"

    @property
    def longitude(self):
        dd = self.mgrs.toLatLon(self.mgrs_input)
        return f"E 0{self._coord_convert(dd[1])}"

    def _coord_convert(self, coord):
        raw_coord = self.mgrs.ddtodms(coord)
        return f"{int(raw_coord[0])} {round(raw_coord[1] + raw_coord[2] / 60, 1)}"

    def __repr__(self):
        return f"MGRStoDDM(Latitude: {self.latitude}, Longitude: {self.longitude})"

    def __str__(self):
        return f"{self.latitude}, {self.longitude}"


@click.command()
@click.argument("mgrs")
def convert(mgrs):
    converter = MGRStoDDM(mgrs)
    print(converter)


if __name__ == '__main__':
    convert()
