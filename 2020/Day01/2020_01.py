from pathlib import Path
from aocd import get_data, submit
import subprocess
def part1(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    ans = 0
    lines = list(map(int, lines))
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            if lines[i] + lines[j] == 2020:
                ans = (lines[i]* lines[j])
    return ans
    


def part2(filename="input.txt"):
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read().splitlines()
    ans = 0
    lines = list(map(int, lines))
    for i in range(len(lines)):
        for j in range(i, len(lines)):
            for k in range(j, len(lines)):
                if lines[i] + lines[j] + lines[k]== 2020:
                    ans = (lines[i]* lines[j] *lines[k])
    return ans

if __name__ == "__main__":
    day = 5
    year = 2022
    with Path(__file__).with_name('input.txt').open("w") as inputData:
        inputData.write(get_data(day=day, year=year))
    result = subprocess.run(["aocd", f"{year}", f"{day}", "--example"], capture_output=True, text=True)
    lines = result.stdout.splitlines()  
    trimmed_lines = lines[3:-6] 
    with Path(__file__).with_name('sample.txt').open("w") as sampleData:
        sampleData.write("\n".join(trimmed_lines))
    # print(p1ans:=part1())
    # print(part2("sample.txt"))
    # print(p2ans:=part2())
    # submit(p2ans)
    