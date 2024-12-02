from pathlib import Path
import aocd
import subprocess
from collections import Counter
import pprint


def part1(filename="input.txt"):
    a = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    s = set()
    idx = 0
    while True:
        if idx in s:
            return a
        s.add(idx)
        if lines[idx].startswith("nop"):
            idx += 1
        elif lines[idx].startswith("acc"):
            a += int(lines[idx].split()[1])
            idx += 1
        else:
            idx += int(lines[idx].split()[1])


def part2(filename="input.txt"):
    a = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    def loop(lines = lines):
        a = 0
        s = set()
        idx = 0
        while True:
            if idx == len(lines):
                return 1, a
            if idx in s:
                return 0, a
            s.add(idx)
            if lines[idx].startswith("n"):
                idx += 1
            elif lines[idx].startswith("a"):
                a += int(lines[idx].split()[1])
                idx += 1
            else:
                idx += int(lines[idx].split()[1])
    for i in range(len(lines)):
        if lines[i].startswith("nop"):
            lines[i] = lines[i].replace("nop", "jmp")
            b, a = loop()
            if b:
                return a
            lines[i] = lines[i].replace("jmp", "nop")
        elif lines[i].startswith("jmp"):
            lines[i] = lines[i].replace("jmp", "nop")
            b, a = loop()
            if b:
                return a
            lines[i] = lines[i].replace("nop", "jmp")

if __name__ == "__main__":
    day, year = aocd.get_day_and_year()
    with Path(__file__).with_name("input.txt").open("w") as inputData:
        inputData.write(aocd.get_data(day=day, year=year))
    result = subprocess.run(
        ["aocd", f"{year}", f"{day}", "--example"], capture_output=True, text=True
    )
    lines = result.stdout.splitlines()
    trimmed_lines = lines[3:-6]
    with Path(__file__).with_name("sample.txt").open("w") as sampleData:
        sampleData.write("\n".join(trimmed_lines))
    # print(part1("sample.txt"))
    # print(p1ans := part1())
    # aocd.submit(p1ans)
    print(part2("sample.txt"))
    print(p2ans := part2())
    aocd.submit(p2ans)
