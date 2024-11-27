students = [
    {
        "name":"Reyhan",
        "fav_nr": 5,
        "hobbies": ["running", "painting"]
    },
    {
        "name":"Karen",
        "fav_nr": 1,
        "hobbies": ["pokemon", "sleeping"]
    },
    {
        "name":"Ezhil",
        "fav_nr": 7,
        "hobbies": ["gardening", "cooking", "sleeping"]
    }
]

for student in students:
    for hobby in student["hobbies"]:
        if hobby == "sleeping":
            print("I love sleeping too,", student["name"])


for student in students:
    if student["name"] == "Karen":
        for hobby in student["hobbies"]:
            print(hobby)


for student in students:
    if student["name"] == "Karen":
        print(student["hobbies"])