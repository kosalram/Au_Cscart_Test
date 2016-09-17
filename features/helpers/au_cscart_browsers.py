from enum import Enum


class Browsers(Enum):
    chrome = 1
    firefox = 2
    internetexplorer = 3
    phantom = 4
    opera = 5

    @classmethod
    def get_browser(self, b):
        return {"Chrome": self.chrome, "Google Chrome": self.chrome, "Firefox": self.firefox, "FireFox": self.firefox,
            "Internet Explorer": self.internetexplorer, "IE": self.internetexplorer, "Phantom": self.phantom}[b]