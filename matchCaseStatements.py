# Match-case statement (switch statements)

def day_of_week(day): # for the cases, when doing conditional statements, OR is |
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _: # default case
            return "Invalid"

print(day_of_week(8))