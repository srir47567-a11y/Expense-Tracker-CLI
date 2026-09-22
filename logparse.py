import re
LOG_PATTERN = re.compile(r'(?P<ip>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<method>\S+) (?P<path>\S+) [^"]*" (?P<status>\d{3}) (?P<size>\d+|-)')


def read_file(path):
    with open(path) as file:
        for line in file:
            line=line.strip()
            if not line:
                continue
            yield line

def parse_line(line):
    
    match = LOG_PATTERN.match(line)

    if not match:
        return None

    data = match.groupdict()

    data["status"] = int(data["status"])

    if data["size"] == "-":
        data["size"] = 0
    else:
        data["size"] = int(data["size"])

    return data

if __name__ == "__main__":
    for line in read_file("sample.log"):
        parsed = parse_line(line)
        if parsed is None:
            print("FAILED TO PARSE:", repr(line))
        else:
            print(parsed)