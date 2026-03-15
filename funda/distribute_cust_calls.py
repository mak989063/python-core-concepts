requests = int(input())
computers = int(input())

result = []

evenly_dist = requests // computers
remaining_requests = requests % computers

for i in range(computers):
    result.append(evenly_dist)

for i in range(remaining_requests):
    result[i] += 1

print(result)
