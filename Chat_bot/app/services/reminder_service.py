from app.schemas.reminder import ReminderSchema

class ReminderService:
    reminders = []

    @classmethod
    def add_reminder(cls, reminder: ReminderSchema):
        cls.reminders.append(reminder)
        return reminder

    @classmethod
    def get_all_reminders(cls):
        return cls.reminders