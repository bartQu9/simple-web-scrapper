from lib import ResourceSettings, Capability, OneShootSourceHandler
import requests
import validators


class HttpCapable(Capability):
    pass


class HttpsCapable(Capability):
    pass


class HttpResSettings(ResourceSettings):
    def __init__(self, url: str, auth_info: tuple):
        self.url = url
        self.auth = auth_info

    def validate_settings(self):
        pass



class HttpOneShootSourceHandler(OneShootSourceHandler):
    capabilities = [HttpCapable, HttpsCapable]

    def __init__(self, settings: ResourceSettings):
        super().__init__(settings)
