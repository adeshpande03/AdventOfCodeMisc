from pathlib import Path
import aocd
import subprocess
from collections import Counter


def part1(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    lines = lines.split("\n\n")
    lines = [line.replace("\n", " ") for line in lines]
    # print(lines)
    for line in lines:
        # print(line)
        d = {s.split(":")[0]: s.split(":")[1] for s in line.split(" ")}
        # print(d)
        if d.get("cid", 0) == 0 and len(d) == 7:
            ans += 1
        elif len(d) == 8:
            ans += 1

    return ans


def part2(filename="input.txt"):
    ans = 0
    with Path(__file__).with_name(filename).open("r") as f:
        lines = f.read()
    lines = lines.split("\n\n")
    lines = [line.replace("\n", " ") for line in lines]
    for line in lines:
        d = {s.split(":")[0]: s.split(":")[1] for s in line.split(" ")}
        print(d)
        if len(d) < 8:
            if d.get("cid", 0) == 0 and len(d) == 7:
                pass
            else:
                continue
        if (
            1920 <= int(d["byr"]) <= 2002
            and 2010 <= int(d["iyr"]) <= 2020
            and 2020 <= int(d["eyr"]) <= 2030
        ):
            if d["hgt"][-2:] == "cm" and 150 <= int(d["hgt"][:-2]) <= 193:
                if d["hcl"][0] == "#" and len(d["hcl"]) == 7 and max(d["hcl"]):
                    if d["ecl"] in [
                        "amb",
                        "blu",
                        "brn",
                        "gry",
                        "grn",
                        "hzl",
                        "oth",
                    ]:
                        if len(d["pid"]) == 9:
                            ans += 1
            elif d["hgt"][-2:] == "in" and 59 <= int(d["hgt"][:-2]) <= 76:
                if d["hcl"][0] == "#" and len(d["hcl"]) == 7:
                    if d["ecl"] in [
                        "amb",
                        "blu",
                        "brn",
                        "gry",
                        "grn",
                        "hzl",
                        "oth",
                    ]:
                        if len(d["pid"]) == 9:
                            ans += 1

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
