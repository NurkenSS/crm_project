from typing import List, Optional  # Добавить импорт Optional
from datetime import datetime
from .schemas.goal import GoalSchema

class GoalService:
    def __init__(self):
        self.goals = []

    def create_goal(self, goal_data: GoalSchema) -> GoalSchema:
        new_goal = goal_data.dict()
        new_goal['created_at'] = datetime.now()
        new_goal['updated_at'] = datetime.now()
        self.goals.append(new_goal)
        return GoalSchema(**new_goal)

    def get_goals(self) -> List[GoalSchema]:
        return [GoalSchema(**goal) for goal in self.goals]

    def get_goal_by_name(self, name: str) -> Optional[GoalSchema]:
        for goal in self.goals:
            if goal['name'] == name:
                return GoalSchema(**goal)
        return None
