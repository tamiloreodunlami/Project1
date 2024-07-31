def read_calls(file: open) -> {(str, str): int}:
    data = {}
    for line in file:
        line = line.replace("\n", "").strip()
        line_data = line.split(":")
        caller = line_data[0]

        for callee in line_data[1:]:
            if (caller, callee) not in data:
                data[(caller, callee)] = 1
            else:
                data[(caller, callee)] += 1
    return data


def call1to2(calls: {(str, str): int}) -> {str: {str: int}}:
    data = {}
    for call in calls:
        caller = call[0]
        callee = call[1]
        count = calls[call]
        if caller not in data:
            data[caller] = {callee: count}
        else:
            data[caller][callee] = count
    return data
            

def main():
    file = open('calls.txt')
    calls = read_calls(file)
    print(calls)
    calls2 = call1to2(calls)
    print(calls2)


if __name__ == "__main__":
    main()

