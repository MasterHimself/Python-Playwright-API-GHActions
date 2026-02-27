import os
import yaml

class ConfigReader:
    def __init__(self, env: str | None = None) -> None:
        config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
        with open(config_path, "r", encoding="utf-8") as file:
            self.config: dict = yaml.safe_load(file) or {}

        default_env = self.config.get("env", "qa")
        self.env = env or default_env

        environments = self.config.get("environments", {})
        if self.env not in environments:
            raise KeyError(f"Environment '{self.env}' not found in config.yaml")

        self.env_config: dict = environments[self.env] or {}

    def get_environment(self) -> str:
        return self.env

    def get_base_url(self) -> str:
        return str(self.env_config["base_url"]).rstrip("/")

    def get_api_url(self) -> str:
        return str(self.env_config["api_url"]).rstrip("/")

    def get_db_config(self) -> dict:
        return dict(self.env_config.get("db", {}))

    def get_resolutions(self) -> list[tuple[int, int]]:
        raw = self.env_config.get("resolutions", []) or []
        return [(int(w), int(h)) for w, h in raw]
