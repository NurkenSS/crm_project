from datetime import datetime

class Notification:
    def __init__(self, goal_name: str, target_date: datetime):
        self.goal_name = goal_name
        self.target_date = target_date

    def send_reminder(self):
        return f"Напоминание: цель '{self.goal_name}' должна быть выполнена до {self.target_date.strftime('%Y-%m-%d %H:%M:%S')}"
