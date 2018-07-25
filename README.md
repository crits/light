# Light
Threat Intelligence Platform with a RESTful API

# Installation

Light requires Python >= 3.6

We recommend creating a virtual environment for Light to run in. Once you have
created one, you can proceed with the installation.

We want to install Falcon with Cython support, which is currently not doable
with `setuptools`, so we need to do this via the `requirements.txt` file for
now.

```bash
> pip install -r requirements.txt
> pip install .
```

A script will be installed automatically called `illuminate`. You can run that
and it will automatically load your Falcon app with Gunicorn. It should look
something like this:

```bash
(light) mgoffin@light > illuminate
[2018-07-25 12:59:46 -0400] [64800] [INFO] Starting gunicorn 19.9.0
[2018-07-25 12:59:46 -0400] [64800] [INFO] Listening at: http://127.0.0.1:8080 (64800)
[2018-07-25 12:59:46 -0400] [64800] [INFO] Using worker: sync
[2018-07-25 12:59:46 -0400] [64803] [INFO] Booting worker with pid: 64803
[2018-07-25 12:59:46 -0400] [64804] [INFO] Booting worker with pid: 64804
[2018-07-25 12:59:46 -0400] [64805] [INFO] Booting worker with pid: 64805
[2018-07-25 12:59:46 -0400] [64806] [INFO] Booting worker with pid: 64806
[2018-07-25 12:59:46 -0400] [64807] [INFO] Booting worker with pid: 64807
[2018-07-25 12:59:46 -0400] [64808] [INFO] Booting worker with pid: 64808
[2018-07-25 12:59:46 -0400] [64809] [INFO] Booting worker with pid: 64809
[2018-07-25 12:59:46 -0400] [64810] [INFO] Booting worker with pid: 64810
[2018-07-25 12:59:46 -0400] [64811] [INFO] Booting worker with pid: 64811
[2018-07-25 12:59:46 -0400] [64812] [INFO] Booting worker with pid: 64812
[2018-07-25 12:59:46 -0400] [64813] [INFO] Booting worker with pid: 64813
[2018-07-25 12:59:46 -0400] [64814] [INFO] Booting worker with pid: 64814
[2018-07-25 12:59:46 -0400] [64815] [INFO] Booting worker with pid: 64815
[2018-07-25 12:59:47 -0400] [64816] [INFO] Booting worker with pid: 64816
[2018-07-25 12:59:47 -0400] [64817] [INFO] Booting worker with pid: 64817
[2018-07-25 12:59:47 -0400] [64818] [INFO] Booting worker with pid: 64818
[2018-07-25 12:59:47 -0400] [64819] [INFO] Booting worker with pid: 64819
```

From here you can browse to `http://127.0.0.1:8080/test` and should see a
message as a response:

```
This is me, Falcon, serving a resource!
```

You can modify how `illuminate` runs with the following options:

```
usage: illuminate [-h] [-H HOST] [-P PORT] [-W WORKERS]

Start the Light app.

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  Host or IP to bind to.
  -P PORT, --port PORT  Port to bind to.
  -W WORKERS, --num-workers WORKERS
                        Number of workers to boot (default: CPU_COUNT * 2 + 1)
```
