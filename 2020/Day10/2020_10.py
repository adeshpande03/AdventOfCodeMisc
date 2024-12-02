from pathlib import Path
import aocd
import subprocess
from collections import Counter
from itertools import groupby
import numpy as np
import math

def part1(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    lines = [0] + [int(x) for x in lines]
    lines.sort()
    lines.append(lines[-1] + 3)
    d = list(np.diff(lines))
    return (d.count(1) * d.count(3))
    # print(lines)


def part2(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    lines = [0] + [int(x) for x in lines]
    lines.sort()
    lines.append(lines[-1] + 3)
    d = list(np.diff(lines))
    def count_arrangements(differences):
        return math.prod(
            (2 ** (len(m) - 1)) - (len(m) == 4)
            for k, g in groupby(differences)
            if k == 1 and len((m := list(g))) > 1
        )
    return count_arrangements(d)


if __name__ == "__main__":
    day, year = aocd.get_day_and_year()
    with Path(__file__).with_name("input.txt").open("w") as inputData:
        inputData.write(aocd.get_data(day=day, year=year))
    result = subprocess.run(
        ["aocd", f"{year}", f"{day}", "--example"], capture_output=True, text=True
    )
    lines = result.stdout.splitlines()
    trimmed_lines = lines[3:-6]
    # with Path(__file__).with_name("sample.txt").open("w") as sampleData:
    #     sampleData.write("\n".join(trimmed_lines))
    print(part1("sample.txt"))
    print(p1ans := part1())
    # aocd.submit(p1ans)
    print(part2("sample.txt"))
    print(p2ans := part2())
    aocd.submit(p2ans)
