import json
import os

directory_name = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(directory_name, "user_data.json")) as f:
    user_data = json.load(f)
