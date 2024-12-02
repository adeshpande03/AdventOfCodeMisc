from pathlib import Path
import aocd
import subprocess
from collections import Counter


def part1(filename="input.txt"):
    ans = 0
    m = 0
    l = []
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        r = ''
        c = ''
        for letter in line[:7]:
            if letter == 'F':
                r +='0'
            else:
                r +='1'
        for letter in line[7:]:
            if letter == 'L':
                r +='0'
            else:
                r +='1'
        
        ans = (int(r, 2))
        # print(r, ans)
        l.append(ans)
    l.sort()
    print(l[-1])
        
        
    return l[-1]


def part2(filename="input.txt"):
    ans = 0
    m = 0
    l = []
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip()
        r = ''
        c = ''
        for letter in line[:7]:
            if letter == 'F':
                r +='0'
            else:
                r +='1'
        for letter in line[7:]:
            if letter == 'L':
                r +='0'
            else:
                r +='1'
        
        ans = (int(r, 2))
        # print(r, ans)
        l.append(ans)
    l.sort()
    print(l[-1])
        
    
    for x in range(len(l)):
        if l[x+1] - l[x] != 1:
            ans = (l[x] + 1)
            break
    return ans


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
    # print(part1("sample.txt"))
    # print(p1ans := part1())
    # print(part2("sample.txt"))
    print(p2ans := part2())
    # aocd.submit(p1ans)
    # aocd.submit(p2ans)
