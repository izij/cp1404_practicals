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
