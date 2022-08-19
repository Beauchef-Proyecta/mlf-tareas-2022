import requests


class RobotClient:
    def __init__(self, address, port=5000):
        self.address = address
        self.port = port
        self.base_url = f"http://{address}:{port}"
        self.connected = False

    def connect(self):
        if self.connected:
            print("already connected :)")
            return

        url = f"{self.base_url}/connect"
        response = requests.get(url)
        if response.status_code == 200:
            self.connected = True
            print(response.text)

    def move_xyz(self, x, y, z):
        params = {"x": x, "y": y, "z": z}
        url = f"{self.base_url}/move"
        response = requests.get(url, params=params)
        print(response.text)
