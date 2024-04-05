def pick_a_day(day):
    match day:
        case 1:
           print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case "one" | "two":                         #Bu operand "or" olarak kullanılabilir
            print("Thursday")
        case 5 | 6 | 7:                             #integer ile de çalışır
            print("Friday")
        case _:
            print("Wrong")

pick_a_day("one")