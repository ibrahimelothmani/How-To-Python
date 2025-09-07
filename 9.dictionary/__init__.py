student = {
    "name": "Ibrahim",
    "age": 27,
    "email": "ibrahim@gmail.com"
}

if __name__ == "__main__":
    print(student)
    print(student.get("name"))
    print(student.get("age"))
    print(student.get("email"))

    print("###################################")
    print(list(student.keys()))
    print(list(student.values()))
    print("###################################")
    print("update a dictionary")
    student["name"] = "yassine"
    student["age"] = 17
    student["email"] = "yassine@gmail.com"
    print(student)
