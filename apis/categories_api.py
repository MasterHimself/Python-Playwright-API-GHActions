from apis.base_api import BaseAPI

class CategoriesApi(BaseAPI):
    def __init__(self, base_url: str, session):
        super().__init__(base_url, session)

    def get_all_categories(self):
        return self.get("/categoriesList")