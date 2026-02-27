from apis.base_api import BaseAPI

class SearchApi(BaseAPI):
    def search_product(self, query: str):
        endpoint = "/searchProduct"
        payload = {"search_product": query}
        return self.post(endpoint, data=payload)