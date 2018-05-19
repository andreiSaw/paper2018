import json
import os

from disneylandClient import Job


def load_data(path):
    if not os.path.isfile(path):
        return []
    with open(path, "r") as json_data:
        statelist = json.load(json_data)
        if isinstance(statelist, list):
            return statelist
    return []


STATUS_IN_PROCESS = {Job.PENDING, Job.PULLED, Job.RUNNING}
STATUS_FINAL = {Job.COMPLETED, Job.FAILED}


def dump_data(outputlist, path):
    statelist = load_data(path)
    statelist.extend(outputlist)
    with open(path, "w") as f:
        json.dump(statelist, f)
