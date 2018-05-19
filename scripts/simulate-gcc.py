import json
import time

from disneylandClient import (
    new_client,
    Job,
    RequestWithId,
)

from .help import STATUS_FINAL, dump_data

path = "outputGCC.json"

descriptor = {
    "input": ["git:https://github.com/andreiSaw/paper2018"],

    "container": {
        "workdir": "",
        "name": "als23/makegcc:latest",
        "cpu_needed": 16,
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
    for i in range(16, 17):
        dsc = descriptor
        dsc['container']['cmd'] = "sh -lc '/input/images/makegcc/run.sh {} > /output/test.txt 2>&1'".format(i)
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
                    sxtemp = x[0]
                    d = json.loads(jobs[idx].input)
                    cmd = d['container']["cmd"]
                    temp = cmd.find(" ", 36)
                    cores = int(cmd[temp:cmd.find(">") - 1])
                    tempvar = sxtemp[sxtemp.find("run { date "):]
                    substr = "elapsed = "
                    tempvar = tempvar[tempvar.find(substr):]
                    tempvar = tempvar[len(substr):tempvar.find(" ", len(substr))]
                    timevar = float(tempvar)
                    paramsvector = "--enable-languages=c,c++,fortran --disable-multilib --disable-bootstrap --build=x86_64-linux-gnu"
                    outputlist.append(
                        {"cores": cores, "program": {"image": d['container']["name"], "cmd": cmd}, "time": timevar,
                         "paramsvector": paramsvector})
                    print("result:", x)

    dump_data(outputlist, path)

    print("All done!")


if __name__ == '__main__':
    main()
