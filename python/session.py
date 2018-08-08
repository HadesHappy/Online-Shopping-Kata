
from modelobjects import Cart, LocationServices


class Session:
    def __init__(self):
        self.contents = {}
        self.put("CART", Cart())
        self.put("LOCATION_SERVICE", LocationServices())

    def put(self, key, value):
        self.contents[key] = value

    def get(self, key):
        return self.contents[key]

    def save_all(self):
        for key, value in self.contents.items():
            value.save_to_database()

    def __repr__(self):
        contents = '\n'.join(f"{k}={v}" for k, v in self.contents.items())
        return f"""Session(
{contents}
)"""
