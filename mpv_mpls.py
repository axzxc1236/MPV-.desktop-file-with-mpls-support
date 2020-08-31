from subprocess import Popen
from sys import argv
from pathlib import Path

if __name__ == "__main__" and len(argv) == 2 and argv[1][-5:].lower() == ".mpls":
    number = argv[1][-10:-5]
    print("mpls number = " + number)
    startArgs = [
        "bash",
        "-c",
        "mpv bd://mpls/" + number + " -bluray-device=../.."
    ]
    print(startArgs)
    Popen(startArgs, cwd=str(Path(argv[1]).parent.absolute()))
else:
    exit(1)