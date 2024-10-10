class Goal:
    def __init__(self, username, goal_name, target_amount):
        self.username = username
        self.goal_name = goal_name
        self.target_amount = target_amount

    def to_dict(self):
        return {
            "username": self.username,
            "goal_name": self.goal_name,
            "target_amount": self.target_amount,
        }
