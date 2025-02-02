import json
from pathlib import Path
from src.domain.job import Job

def load_instance(file_path: str):
    """
    read the instance file and return a list of Job objects.
    The instance file must be a JSON file with the following format:
    {
      "jobs": [job1, job2, ...],
      "processing_times": {
        "MachineA": [pA1, pA2, ...],
        "MachineB": [pB1, pB2, ...],
        "MachineC": [pC1, pC2, ...]
      },
      "due_dates": [due1, due2, ...]
    }
    """
    instance_path = Path(file_path)
    with instance_path.open("r", encoding="utf-8") as f:
        data = json.load(f)
    if "jobs" in data and "processing_times" in data and "due_dates" in data:
        job_names = data["jobs"]
        proc = data["processing_times"]
        due_dates = data["due_dates"]
        jobs = []
        for i, name in enumerate(job_names):
            pA = proc["MachineA"][i]
            pB = proc["MachineB"][i]
            pC = proc["MachineC"][i]
            due = due_dates[i]
            jobs.append(Job(name, pA, pB, pC, due))
        return jobs
    else:
        raise ValueError("JSON file format is invalid.")
