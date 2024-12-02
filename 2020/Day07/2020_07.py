from pathlib import Path
import aocd
import subprocess
from collections import Counter
import pprint


def part1(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    d = {}
    for line in lines:
        line = line.strip()[:-1]
        line = line.replace("bags", "bag").replace('contain ', '').replace(',', '')
        line = line.split(" bag")
        line = [x.strip() for x in line]
        line = [x for x in line if x]
        d[line[0]] = {(' '.join(item.split(' ')[1:])):item.split(' ')[0] for item in line[1:]}
    # pprint.pprint(d)
    s = set()
    td = ["shiny gold"]
    while td:
        bag = td.pop()
        for i in d:
            if d[i].get(bag, 0):
                s.add(i)
                td.append(i)
        
    # print(s)
    return len(s)


def part2(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.readlines()
    d = {}
    for line in lines:
        line = line.strip()[:-1]
        line = line.replace("bags", "bag").replace('contain ', '').replace(',', '').replace('no other', '1')
        line = line.split(" bag")
        line = [x.strip() for x in line]
        line = [x for x in line if x]
        d[line[0]] = {(' '.join(item.split(' ')[1:])):item.split(' ')[0] for item in line[1:]}
    # pprint.pprint(d)
    s = set()
    td = [('shiny gold', 1)]
    while td:
        # print(td)
        bag, num = td.pop(0)
        # print(ans)
        s.add(bag)
        if bag == '':
            ans += num
            continue
        num = int(num)
        ans += num
        for i in d[bag]:
            if i == '':
                ans += num
                if bag in s:
                    s.remove(bag)
                continue
            td.append((i,num *  int(d[bag][i])))
        if bag not in s:
            ans -= num
        # print(s)
    ans -=1
    # ans += len(s)
    # print(s)
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
    print(part2("sample.txt"))
    print(p2ans := part2())
    # aocd.submit(p1ans)
    aocd.submit(p2ans)
