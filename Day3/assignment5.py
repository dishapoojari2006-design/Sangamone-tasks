from datetime import datetime, timedelta
utc = datetime.utcnow()
print("Current UTC Time :", utc)

san_francisco = utc - timedelta(hours=7)
print("San Francisco :", san_francisco)

new_york = utc - timedelta(hours=4)
print("New York :", new_york)

london = utc + timedelta(hours=1)
print("London :", london)

dubai = utc + timedelta(hours=4)
print("Dubai :", dubai)

bangalore = utc + timedelta(hours=5, minutes=30)
print("Bangalore :", bangalore)

singapore = utc + timedelta(hours=8)
print("Singapore :", singapore)

tokyo = utc + timedelta(hours=9)
print("Tokyo :", tokyo)

sydney = utc + timedelta(hours=10)
print("Sydney :", sydney)

wellington = utc + timedelta(hours=12)
print("Wellington :", wellington)