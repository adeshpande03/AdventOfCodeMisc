from pathlib import Path
import aocd
import subprocess
from collections import Counter


def part1(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    ans = 0
    col, row = 0, 0
    while row < len(lines):
        if lines[row][col] == "#":
            ans += 1
        col = (col + 3) % len(lines[row])
        row += 1

    return ans


def part2(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    def go(rp, cp, lines=lines):
        ans = 0
        col, row = 0, 0
        while row < len(lines):
            if lines[row][col] == "#":
                ans += 1
            col = (col + cp) % len(lines[row])
            row += rp
        return ans
    return go(1, 1) * go(1, 3) * go(1, 5) * go(1, 7) * go(2, 1)


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
    print(part2("sample.txt"))
    print(p2ans := part2())
    # aocd.submit(p1ans)
    # aocd.submit(p2ans)
