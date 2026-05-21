## Tuple exercises

# Return student ID details
def get_student():
    return ("10", "Ram", 3.8)

sid, name, gpa = get_student()
print(f"Student {sid}: {name} has GPA {gpa}")



# Calculate the distance between two places
def distance(stop_a, stop_b):
    x1, y1 = stop_a
    x2, y2 = stop_b
    
    dx = x2 - x1
    dy = y2 - y1
    
    dist = (dx * dx + dy * dy) ** 0.5
    return dist

d = distance((0, 0), (3, 4))
print(d) 



# List of tuples of student names and marks
scores = [
    ("Ram", 85, 90),
    ("Hari", 78, 88),
    ("Shyam", 92, 85),
    ("Dev", 88, 88),
]

totals = []
for name, test1, test2 in scores:
    total = test1 + test2
    totals.append((name, total))

best_name = totals[0][0]
best_total = totals[0][1]

for name, total in totals:
    if total > best_total:
        best_total = total
        best_name = name

print(f"Top student: {best_name} with {best_total}")