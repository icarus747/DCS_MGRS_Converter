import pytest
from converter.main import MGRStoDDM

class TestMGRSWrapper:
    @pytest.mark.parametrize("mgrs_code", ["38TLN046623"])
    def test_output_is_str(self, mgrs_code):
        converter = MGRStoDDM(mgrs_code)
        assert str(converter)

    @pytest.mark.parametrize("mgrs_code", ["38TLN046623"])
    def test_latitude(self, mgrs_code):
        converter = MGRStoDDM(mgrs_code)
        assert converter.latitude.startswith('N')

    @pytest.mark.parametrize("mgrs_code", ["38TLN046623"])
    def test_longitude(self, mgrs_code):
        converter = MGRStoDDM(mgrs_code)
        assert converter.longitude.startswith('E 0')
