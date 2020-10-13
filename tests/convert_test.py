import pytest
from utils.convert import CoordConvert

def testMGRS():
    ''' Pulled a random MGRS coordinate from the interwebs and verify it against other sources '''
    results = CoordConvert('mgrs', '17SNU5478598457')
    assert results.conversion['mgrs'] == '17SNU5478598457'
    assert results.conversion['dd']   == '35.227667 -80.397959'
    assert results.conversion['dms']  == 'N 35 13 39.6020, W 80 23 52.6516'

def testDD():
    ''' Pulled a random decimal coordinate from the interwebs and verify it converts properly '''
    results = CoordConvert('dd', '(38.272689, -100.546875)')
    assert results.conversion['mgrs'] == '14SLH6468937202'
    assert results.conversion['dd']   == '38.272689 -100.546875'
    assert results.conversion['dms']  == 'N 38 16 21.6804, W 100 32 48.7500'

def testDMS():
    ''' Pulled some DMS coordinates and verify the conversion '''
    results = CoordConvert('dms', '[(39,38,22.3368),(106,31,24.3768)]')
    assert results.conversion['mgrs'] == '13SCD6927588859'
    assert results.conversion['dd']   == '39.639539 -106.523439'
    assert results.conversion['dms']  == 'N 39 38 22.3368, W 106 31 24.3768'
    

if __name__ == "__main__":
    testMGRS()
    testDD()
    testDMS()