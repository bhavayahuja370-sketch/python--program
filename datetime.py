from datetime import date

date1 = date(2026, 8, 18)
date2 = date(2026, 8, 9)
diff = date2 - date1
print("day", diff.days)
