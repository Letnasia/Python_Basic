# 0 -> 0 днів, 00:00:00
# 224930 -> 2 дні, 14:28:50
# 466289 -> 5 днів, 09:31:29
# 950400 -> 11 днів, 00:00:00
# 1209600 -> 14 днів, 00:00:00
# 1900800 - > 22 дні, 00:00:00
# 8639999 -> 99 днів, 23:59:59
# 22493 -> 0 днів, 06:14:53
# 7948799 -> 91 день, 23:59:59

date = int(input("Enter the number from 0 to 8640000: "))
day, a = divmod(date, 24 * 60 * 60)
hours, b = divmod(a, 60 * 60)
minutes, sec = divmod(b, 60)

day = str(day)
last_day = int(day[-1])
days = {0: "днів", 1: "день", 2: "дні", 3: "дні", 4: "дні", 5: "днів", 6: "днів", 7: "днів", 8: "днів", 9: "днів"}
day_name = days[last_day]

if date >= 10 * 24 * 60 * 60:
    before_last = int(day[-2])
    if before_last == 1:
        day_name = "днів"

print(f"{day} {day_name}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}")
