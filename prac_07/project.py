""" Project class"""


class Project:
    """ """

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Create Project object from inputs"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"{self.name}\t{self.start_date}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"
