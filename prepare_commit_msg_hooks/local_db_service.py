import os
import json

CONFIG_COLLECTION_KEY = "config"

default_db = {
    CONFIG_COLLECTION_KEY: {
      "openai_api_key": ""
    }
}

class LocalDbService:
    def __init__(self):
      current_file_directory = os.path.dirname(os.path.abspath(__file__))

      self.db_path = os.path.join(current_file_directory, '.ai-commit-msg','local_db.json')
      print("db_path: ", self.db_path)
      # Ensure the directory exists
      os.makedirs(os.path.dirname(self.db_path), exist_ok=True)

      # check if file exist
      if not os.path.exists(self.db_path):
          self.create_db()

    def create_db(self):
        with open(self.db_path, 'w') as db:
            json.dump(default_db, db)

    def get_db(self):
        with open(self.db_path, 'r') as db:
            return json.load(db)

    def set_db(self, data):
        with open(self.db_path, 'w') as db:
            json.dump(data, db)

    def append_db(self, data):
        with open(self.db_path, 'a') as db:
            db.write(data)