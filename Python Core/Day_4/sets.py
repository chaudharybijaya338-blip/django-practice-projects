## Set Exercises


# Extract unique users from a list of wifi users in campus
logins = ["S101", "S102", "S101", "S103", "S102", "S104", "S101"]
unique_users = set()
for sid in logins:
    unique_users.add(sid)
print("Unique users:", unique_users)
print("Count:", len(unique_users))



# Filtering using sets
banned = {"copy", "paste", "cheat", "plagiarism", "ghost"}
essay_words = ["I", "did", "not", "copy", "or", "cheat", "honest"]
clean_words = []
for word in essay_words:
    if word not in banned:
        clean_words.append(word)
print(clean_words)



# Set opeartions ( & | - )
ram_courses = ["CS101", "MATH201", "PHY101", "ENG102"]
hari_courses = ["CS101", "CHEM301", "PHY101", "HIS101"]
set_a = set()
for course in ram_courses:
    set_a.add(course)
set_b = set()
for course in hari_courses:
    set_b.add(course)
# Set operations
both = set_a & set_b           # Intersection: in A AND in B
only_alice = set_a - set_b      # Difference: in A but NOT in B
all_unique = set_a | set_b      # Union: in A OR in B (or both)
print("Both:", both)
print("Only Alice:", only_alice)
print("All unique:", all_unique)



# Password Strength Checker using sets
def password_strength(pwd):
    unique_chars = set()
    for ch in pwd:
        unique_chars.add(ch)
    count = 0
    for _ in unique_chars:
        count += 1
    if count >= 8:
        return "Strong"
    else:
        return "Weak"
print(password_strength("hello123"))    # Weak  (7 unique: h,e,l,o,1,2,3)
print(password_strength("helo123!@"))   # Strong (8 unique)