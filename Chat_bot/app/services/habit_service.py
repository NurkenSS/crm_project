from datetime import datetime
from app.schemas.habit import HabitSchema

class HabitService:
    habits = []

    @classmethod
    def add_habit(cls, habit: HabitSchema):
        cls.habits.append(habit)
        return habit

    @classmethod
    def get_all_habits(cls):
        return cls.habits