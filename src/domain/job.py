class Job:
    def __init__(self, name: str, pA: int, pB: int, pC: int, due_date: int):
        self.name = name
        self.pA = pA
        self.pB = pB
        self.pC = pC
        self.due_date = due_date

    def __repr__(self):
        return f"Job({self.name})"
