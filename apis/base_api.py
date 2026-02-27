class BaseAPI:
    def __init__(self, base_url: str, session: object):
        self.base_url = base_url
        self.session = session
        self.headers = {
            "Accept": "application/json",
        }

    def set_headers(self, headers: dict):
        self.headers.update(headers)

    def get(self, endpoint: str, params: dict = None):
        return self.session.get(f"{self.base_url}{endpoint}", headers=self.headers, params=params)

    def post(self, endpoint: str, data: dict | None = None, json: dict | None = None):
        return self.session.post(f"{self.base_url}{endpoint}", headers=self.headers, data=data, json=json)

    def put(self, endpoint: str, data: dict | None = None, json: dict | None = None):
        return self.session.put(f"{self.base_url}{endpoint}", headers=self.headers, data=data, json=json)

    def patch(self, endpoint: str, data: dict | None = None, json: dict | None = None):
        return self.session.patch(f"{self.base_url}{endpoint}", headers=self.headers, data=data, json=json)

    def delete(self, endpoint: str):
        return self.session.delete(f"{self.base_url}{endpoint}", headers=self.headers)

    def upload_file(self, endpoint: str, files: str):
        return self.session.post(f"{self.base_url}{endpoint}", files=files)

    def set_auth(self, username: str, password: str):
        self.session.auth = (username, password)

    def set_token_authentication(self, token: str):
        self.headers["Authorization"] = f"Bearer {token}"

    def close_session(self):
        self.session.close()