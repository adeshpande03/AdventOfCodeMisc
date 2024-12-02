from pathlib import Path
import aocd
import subprocess
from collections import Counter
import pprint


def part1(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    l = []
    def twosum(l, target):
        d = {}
        for i in range(len(l)):
            if l[i] in d:
                return True
            d[target - l[i]] = i
        return False
    for i in lines:
        l.append(int(i.strip()))
    
    for i in range(len(l) - 25):
        if not twosum(l[i:i+25], l[i+25]):
            return l[i+25]
        


def part2(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    target = part1()
    l = []
    for i in lines:
        l.append(int(i.strip()))
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if sum(l[i:j]) == target:
                return min(l[i:j]) + max(l[i:j])

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
    print(part1("sample.txt"))
    print(p1ans := part1())
    # aocd.submit(p1ans)
    print(part2("sample.txt"))
    print(p2ans := part2())
    aocd.submit(p2ans)
