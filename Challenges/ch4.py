day = input("Enter a day: ")

if __name__ == "__main__":
    print("This is a script to identify the day of the week.")
    while day not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        day = input("Please enter a valid day: ")

    while day:
        if day == "Monday":
            print("Monday is the first day of the week.")
            break
        elif day == "Tuesday":
            print("Tuesday is the second day of the week.")
            break
        elif day == "Wednesday":
            print("Wednesday is the third day of the week.")
            break
        elif day == "Thursday":
            print("Thursday is the fourth day of the week.")
            break
        elif day == "Friday":
            print("Friday is the fifth day of the week.")
            break
        elif day == "Saturday":
            print("Saturday is the sixth day of the week.")
            break
        elif day == "Sunday":
            print("Sunday is the seventh day of the week.")
            break
        else:
            print("Invalid day. Please try again.")
            day = input("Enter a day: ")
            continue
