import pytest

from FSFA.Asset.asset_bond import AssetBond
from FSFA.Asset.asset_nonstandard import AssetNonstandard


class TestAssetBond:
    def teardown(self):
        pass

    def test_asset_bond(self, stagemark):
        self.asset_bond = AssetBond()
        assert self.asset_bond.assetbond1()
        self.asset_bond.end()

    @pytest.mark.skip
    def test_asset_nonstandard(self, stagemark):
        self.asset_nonstandard = AssetNonstandard()
        assert self.asset_nonstandard.assetnonstandard1()
        self.asset_nonstandard.end()