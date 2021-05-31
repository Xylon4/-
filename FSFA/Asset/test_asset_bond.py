from FSFA.Asset.asset_bond import AssetBond


class TestAssetBond:
    def teardown(self):
        pass

    def test_asset_bond(self, stagemark):
        self.asset_bond = AssetBond()
        assert self.asset_bond.assetbond1()
        self.asset_bond.end()
