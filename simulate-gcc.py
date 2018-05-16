import time
import json
import os
import types

from disneylandClient import (
    new_client,
    Job,
    RequestWithId,
)

STATUS_IN_PROCESS = {Job.PENDING, Job.PULLED, Job.RUNNING}
STATUS_FINAL = {Job.COMPLETED, Job.FAILED}
path = "outputGCC.json"

descriptor = {
    "input": [],

    "container": {
        "workdir": "",
        "name": "als23/makegcc:latest",
        "cpu_needed": 8,
        "max_memoryMB": 1024,
        "min_memoryMB": 512,
    },

    "required_outputs": {
        "output_uri": "none:",
        "file_contents": [
            {"file": "test.txt", "to_variable": "out"}
        ]
    }
}


def load_data():
    if not os.path.isfile(path):
        return []
    with open(path, "r") as json_data:
        statelist = json.load(json_data)
        if isinstance(statelist, list):
            return statelist
        return []


def main():
    stub = new_client()
    TOTAL_JOBS_TODO = 0

    jobs = []
    outputlist = []
    for i in range(4, 5):
        dsc = descriptor
        dsc['container']['cmd'] = "sh -lc './run.sh {}'".format(i)
        job = Job(
            input=json.dumps(dsc),
            kind="docker",
        )
        job = stub.CreateJob(job)
        jobs.append(job)
        print("Job", job)
        TOTAL_JOBS_TODO += 1

    while TOTAL_JOBS_TODO > 0:
        time.sleep(3)
        for idx, job in enumerate(jobs):
            if job.status in STATUS_FINAL:
                continue
            jobs[idx] = stub.GetJob(RequestWithId(id=job.id))
            print("[{}] Job :\n {}\n".format(time.time(), jobs[idx]))

            if jobs[idx].status in STATUS_FINAL:
                TOTAL_JOBS_TODO -= 1
                if jobs[idx].status == Job.FAILED:
                    print("Job failed!")
                else:
                    x = json.loads(jobs[idx].output)
                    outputlist.append({"cores": idx + 1, "program": json.loads(jobs[idx].input), "time": x, "paramsvector": ""})
                    print("result:", x)

    with open(path, "w") as f:
        json.dump(outputlist, f)

    print("All done!")


if __name__ == '__main__':
    main()
