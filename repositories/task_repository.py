import sqlite3
    
class TaskRepository:
    def __init__(self, db="tasks.db"):
        self.conn = sqlite3.connect(db, check_same_thread=False)
        self.create_table()
    
    def create_table(self):
        with open("schema.sql") as file:
            self.conn.executescript(file.read())
        self.conn.commit()

    def add_task(self, title):
        #execute needs a tuple since I have a placeholder here (?) 
        cursor = self.conn.execute(
            "INSERT INTO tasks (title) VALUES (?)", (title,)
        )
        self.conn.commit()
        return cursor.lastrowid
        

    def list_tasks(self):
        return self.conn.execute(
            "SELECT id, title, completed FROM tasks"
        ).fetchall()

    def delete_task(self, task_id):
        self.conn.execute(
            "DELETE FROM tasks WHERE id = ?", (task_id,)
        )
        self.conn.commit()


    def close(self):
        self.conn.close()