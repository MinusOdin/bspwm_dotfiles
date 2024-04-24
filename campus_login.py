#!/usr/bin/env python3
import subprocess
import time

# --- set the link below
url = "https://campusvirtual.ub.edu/my/courses.php"
# --- don't change anything below

appcommand = ["chromium", url]

def run(cmd):
    subprocess.Popen(cmd)
    time.sleep(0.2)


def run_chromium():
    run(appcommand)

run_chromium()
time.sleep(5)
cmd1 = ["xdotool", "key", "z+v+g+i+Tab"]
cmd2 = ["xdotool", "type", "Arbeljul-1121\n"]

for cmd in [cmd1, cmd2]:
    run(cmd)
