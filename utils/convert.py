# By Icarus747
# Contributors: S7R4nG3
# Created 10/11/2020
import sys
from mgrs import MGRS

class CoordConvert:
    def __init__(self, input_format, input_data):
        self.coord      = MGRS()
        self.conversion = {}

        lat, lon = {}, {}
        if input_format.lower() == 'mgrs':
            self.conversion['mgrs'] = str(input_data)
            latd, lond = self.coord.toLatLon(input_data)
            lat['d'],lat['m'],lat['s'] = self.coord.ddtodms(latd)
            lon['d'],lon['m'],lon['s'] = self.coord.ddtodms(lond)
            dms_string = ('N ' if lat['d'] > 0 else 'S ') + '{:.0f} {:.0f} {:.4f}, '.format(lat['d'],lat['m'],lat['s']) + ('E ' if lon['d'] > 0 else 'W ') + '{:.0f} {:.0f} {:.4f}'.format(abs(lon['d']),lon['m'],lon['s'])
            self.conversion['dd']  = '{:.6f} {:.6f}'.format(latd, lond)
            self.conversion['dms'] = '{}'.format(dms_string)
        if input_format.lower() == 'dd':
            input_data = tuple(eval(input_data))
            self.conversion['dd'] = '{:.6f} {:.6f}'.format(float(input_data[0]), float(input_data[1]))
            to_mgrs = self.coord.toMGRS(input_data[0],input_data[1])
            lat['d'],lat['m'],lat['s'] = self.coord.ddtodms(input_data[0])
            lon['d'],lon['m'],lon['s'] = self.coord.ddtodms(input_data[1])
            dms_string = ('N ' if lat['d'] > 0 else 'S ') + '{:.0f} {:.0f} {:.4f}, '.format(lat['d'],lat['m'],lat['s']) + ('E ' if lon['d'] > 0 else 'W ') + '{:.0f} {:.0f} {:.4f}'.format(abs(lon['d']),lon['m'],lon['s'])
            self.conversion['mgrs'] = '{}'.format(to_mgrs)
            self.conversion['dms']  = '{}'.format(dms_string)
        if input_format.lower() == 'dms':
            input_data = list(eval(input_data))
            dms_string = ('N ' if input_data[0][0] > 0 else 'S ') + '{:.0f} {:.0f} {:.4f}, '.format(input_data[0][0],input_data[0][1],input_data[0][2]) + ('W ' if input_data[1][0] > 0 else 'E ') + '{:.0f} {:.0f} {:.4f}'.format(input_data[1][0],input_data[1][1],input_data[1][2])
            self.conversion['dms'] = str(dms_string)
            lat_float, lon_float = tuple(float(i) for i in input_data[0]), tuple(float(j) for j in input_data[1])
            lat_string = '{:.0f}{:.0f}{:.2f}'.format(lat_float[0],lat_float[1],lat_float[2]) + ( 'N' if lat_float[0] > 0 else 'S' )
            lon_string = '{:.0f}{:.0f}{:.2f}'.format(lon_float[0],lon_float[1],lon_float[2]) + ( 'W' if lon_float[0] > 0 else 'E' )
            lat_to_dd = self.coord.dmstodd(lat_string)
            lon_to_dd = self.coord.dmstodd(lon_string)
            to_mgrs = self.coord.toMGRS(lat_to_dd, lon_to_dd)
            self.conversion['dd']   = '{:.6f} {:.6f}'.format(lat_to_dd,lon_to_dd)
            self.conversion['mgrs'] = '{}'.format(to_mgrs)

if __name__ == '__main__':
    coord = CoordConvert(sys.argv[1], sys.argv[2])
    print(coord.conversion)