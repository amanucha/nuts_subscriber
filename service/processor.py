from data.db import Database

class MessageProcessor:
    def __init__(self):
        self.db = Database()

    def validate_and_save(self, msg):
        if isinstance(msg, str) and msg.strip():
            self.db.save_message(msg.strip())
        else:
            print("Invalid message.")

    def shutdown(self):
        self.db.close()

