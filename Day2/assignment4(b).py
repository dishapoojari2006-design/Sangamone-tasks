from datetime import date, timedelta
doors = [False] * 100
for current_round in range(1, 101):
    for door in range(current_round, 101, current_round):
        doors[door - 1] = not doors[door - 1]
today = date.today()
after_4_weeks = today + timedelta(weeks=4)
lucky = []
unlucky = []
for i in range(100):
    if doors[i]:
        lucky.append(i + 1)
    else:
        unlucky.append(i + 1)
print("\n" + "=" * 50)
print("LETTER TO PRIME MINISTER")
print("=" * 50)
print("To,")
print("The Prime Minister\n")
print("Subject: Release of Lucky Prisoners\n")
print("Respected Sir,\n")
print("The following prisoners are identified as lucky prisoners and may be released today.\n")
print("Lucky Prisoners:")
for prisoner in lucky:
    print(prisoner)
print(f"\nRelease Date: {today}")
print("\nThank you.")
print("\nYours faithfully,")
print("Prison Superintendent")
print("\n" + "=" * 50)
print("LETTER TO JAILER")
print("=" * 50)
print("To,")
print("The Jailer\n")
print("Subject: Release of Unlucky Prisoners\n")
print("Respected Sir,\n")
print("The following prisoners are unlucky prisoners.")
print("They will be released after four weeks.\n")
print("Unlucky Prisoners:")
for prisoner in unlucky:
    print(prisoner)
print(f"\nRelease Date: {after_4_weeks}")
print("\nThank you.")
print("\nYours faithfully,")
print("Prison Department")