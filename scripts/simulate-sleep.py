import json
import time

from disneylandClient import (
    new_client,
    Job,
    RequestWithId,
)

from .help import STATUS_FINAL, dump_data

path = "outputSleepReal.json"

descriptor = {
    "input": [],

    "container": {
        "workdir": "",
        "name": "als23/sleep:latest",
        "cpu_needed": 1,
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


def main():
    stub = new_client()
    TOTAL_JOBS_TODO = 0

    jobs = []
    outputlist = []
    for i in range(15, 17):
        dsc = descriptor
        dsc['container']['cmd'] = "sh -lc 'python3 run.py 60 {} > /output/test.txt'".format(i)
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
                    timevar = float(x[0][13:])
                    d = json.loads(jobs[idx].input)
                    cmd = d['container']["cmd"]
                    param = int(cmd[23:cmd.find(" ", 24)])
                    temp = cmd.find(" ", 24)
                    cores = int(cmd[temp:cmd.find(">") - 1])
                    outputlist.append(
                        {"cores": cores, "program": {"image": d['container']["name"], "cmd": cmd}, "time": timevar,
                         "paramsvector": [param]})
                    print("result:", x)

    dump_data(outputlist, path)

    print("All done!")


if __name__ == '__main__':
    main()
