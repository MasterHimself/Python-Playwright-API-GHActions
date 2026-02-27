from apis.base_api import BaseAPI

class ProductsApi(BaseAPI):
    def __init__(self, base_url: str, session):
        super().__init__(base_url, session)
    def get_all_products(self):
        return self.get("/productsList")

    def get_product_by_id(self, product_id: int):
        return self.get(f"/productDetails/{product_id}")