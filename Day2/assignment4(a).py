doors = [False] * 100
for current_round in range(1, 101):
    for door in range(current_round, 101, current_round):
        doors[door - 1] = not doors[door - 1]
print("Lucky Prisoners are:")

for i in range(100):
    if doors[i]:
        print(f"Prisoner {i + 1}")