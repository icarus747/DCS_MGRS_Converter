import pytest
from ..utils.convert import CoordConvert

def testMGRS():
    results = CoordConvert('mgrs' '17SNU5478598457')
    assert results['mgrs'] == '17SNU5478598457'
    assert results['dd']   == '35.227667 -80.397959'
    assert results['dms']  == 'N 35 13 39.6020, W 80 23 52.6516'