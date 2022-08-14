from bs4 import BeautifulSoup
import base64
import json

class Listener():
    ROBOT_LISTENER_API_VERSION = 2
    report = []

    def send_message(self, event, name=None, attrs=None, message=None, path=None):
        info = {}
        info["event"] = event

        if name:
            info["name"] = name
        if path:
            info["path"] = path
        if message:
            if (message["message"].__contains__("<img")):
                soup = BeautifulSoup(message["message"], "html.parser")
                imageSrc = soup.img.get("src")
                if (imageSrc.__contains__("data:image/png;base64,")):
                    info["image"] = imageSrc
                else:
                    with open(imageSrc, "rb") as img_file:
                        b64_string = base64.b64encode(img_file.read())
                        info["image"] = "{}{}".format(
                            "data:image/png;base64,", b64_string.decode('utf-8'))
            info.update(message)
        if attrs:
            info.update(attrs)

        self.report.append(info)

    def start_suite(self, name, attrs):
        self.send_message("start_suite", name, attrs)

    def end_suite(self, name, attrs):
        self.send_message("end_suite", name, attrs)

    def start_test(self, name, attrs):
        self.send_message("start_test", name, attrs)

    def end_test(self, name, attrs):
        self.send_message("end_test", name, attrs)

    def start_keyword(self, name, attrs):
        self.send_message("start_keyword", name, attrs)

    def end_keyword(self, name, attrs):
        self.send_message("end_keyword", name, attrs)

    def log_message(self, message):
        self.send_message("log_message", message=message)

    def close(self):
        self.send_message("close")
        with open("report.json", "w") as write_file:
            json.dump(self.report, write_file, indent=4)
