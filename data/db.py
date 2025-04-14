import psycopg2

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            dbname='nutsdb',
            user='nutsuser',
            password='nutspassword',
            host=os.environ.get('DB_HOST', 'localhost'),
            port=5432
        )
        self.cur = self.conn.cursor()

    def save_message(self, content):
        self.cur.execute("INSERT INTO messages (content) VALUES (%s);", (content,))
        self.conn.commit()

    def close(self):
        self.cur.close()
        self.conn.close()

