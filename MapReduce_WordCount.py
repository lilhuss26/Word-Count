import re

def mapper(line):
    for word in line.strip().split():
        yield (word, 1)

def reducer(word, values):
    return (word, sum(values))

with open("Football Analytics With Python & R Learning Data Science Through the Lens of Sports.txt", "r") as f:
    data = f.readlines()

for i in range(len(data)):
    data[i] = re.sub(r"[^\w\s]+|\s+", " ", data[i].strip())

mapped_data = []
for line in data:
  mapped_data.extend(mapper(line))

grouped_data = {}
for word, count in mapped_data:
  grouped_data.setdefault(word, []).append(count)

reduced_data = []
for word, values in grouped_data.items():
  reduced_data.append(reducer(word, values))

reduced_data = sorted(reduced_data,reverse=True)
print(reduced_data[:10])