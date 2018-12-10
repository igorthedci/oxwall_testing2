from value_models.user import User
from datetime import datetime


class Status:
    def __init__(self, text="", user=None, photo_source=None):
        self.text = text
        self.user = user
        self.photo_source = photo_source
        self.time_created = datetime.now()


if __name__ == "__main__":
    status = Status(user= User())