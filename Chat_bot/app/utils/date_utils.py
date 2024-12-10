from datetime import datetime, timedelta

# Функция для форматирования времени для напоминаний
def format_reminder_time(remind_at: datetime) -> str:
    return remind_at.strftime('%Y-%m-%d %H:%M:%S')

# Функция для получения следующего дня для повторяющейся привычки
def get_next_occurrence(frequency: str) -> datetime:
    today = datetime.now()
    
    if frequency == 'ежедневно':
        return today + timedelta(days=1)
    elif frequency == 'еженедельно':
        return today + timedelta(weeks=1)
    elif frequency == 'ежемесячно':
        return today.replace(month=today.month + 1) if today.month < 12 else today.replace(year=today.year + 1, month=1)
    return today

# Функция для отслеживания прогресса по цели
def calculate_goal_progress(target_date: datetime, current_date: datetime, total_steps: int) -> int:
    delta_days = (current_date - target_date).days
    progress = max(0, min(100, (delta_days / total_steps) * 100))
    return round(progress)