import pytest

from XAMS.Report.Financial.Asset_pool_registry import AssetPoolRegistry
from XAMS.Report.Financial.product import Product


class TestReport:
    # pytest.mark.skip
    def test_asset_pool_registry(self, get_registry, stagemark):
        self.asset_pool_registry = AssetPoolRegistry()
        assert self.asset_pool_registry.registry(get_registry)
        print("资产池注册表测试通过")
        self.asset_pool_registry.end()

    # pytest.mark.skip
    def test_product(self, stagemark):
        self.product = Product()
        assert self.product.product()
        print("产品信息表测试通过")
        self.product.end()