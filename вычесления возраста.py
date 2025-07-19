def check_status(age: int, gender: str) -> None:
    if age < 2:
        print("bebelus")
    elif 2 <= age < 6:
        print("merge la gradinita")
    elif 6 <= age < 18:
        print("merge la scoala")
    elif 18 <= age < 23:
        print("merge la universitate")
    elif age >= 124:
        print("atat nu traesc")
    elif (gender == "male" and age >= 67) or (gender == "female" and age >= 65):
        print("este la pensie")
    else:
        print("lucreaza")

check_status(age=99, gender="male")