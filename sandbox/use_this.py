start: list[str] = ["1", "3", "5", "7", "3"]

most_common: str = ""
frequency: dict[str, int] = dict()
i: int = 0
while i < len(start):
    value = start[i]
    if value not in frequency:
        frequency[value] = 1
    else:
        frequency[value] += 1
    i += 1
print(frequency)