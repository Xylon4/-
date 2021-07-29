import pytest

from FSFA.Asset.asset_bond import AssetBond
from FSFA.Asset.asset_nonstandard import AssetNonstandard


class TestAssetBond:
    def teardown(self):
        pass

    @pytest.mark.skip
    def test_asset_bond(self, get_bond, stagemark):
        self.asset_bond = AssetBond()
        assert self.asset_bond.assetbond1(get_bond)
        self.asset_bond.end()

    # @pytest.mark.skip
    def test_asset_nonstandard(self, get_nonstandard, stagemark):
        self.asset_nonstandard = AssetNonstandard()
        assert self.asset_nonstandard.assetnonstandard1(get_nonstandard)
        self.asset_nonstandard.end()