class TaskManager:
    def __init__(self, repo):
        self.repo = repo

    def add_task(self, task):
        return self.repo.add_task(task)

    def list_tasks(self):
        return self.repo.get_tasks()

    def delete_task(self, index):
        return self.repo.delete_task(index)