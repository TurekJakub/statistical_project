#!/usr/bin/env python3

import os
import pathlib
import subprocess

pathlib.Path("../resources/playoffs").mkdir(parents=True, exist_ok=True)

os.chdir("../resources/playoffs")

season = 2006

while season <= 2026:
    subprocess.run(
        [f"wget https://www.hockey-reference.com/playoffs/NHL_{season}.html"],
        shell=True,
        check=False,
    )

    subprocess.run(
        [f"mv ./NHL_{season}.html {season - 1}_{season}.html"], shell=True, check=False
    )

    season += 1

print("All playoffs dataset successfully imported")
