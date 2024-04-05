def pick_a_day(day):
    switch = {
        "monday": "Beginning",
        "tuesday": "Segundo",
        "wednesday": "A movie",
        "thursday": "1 to go",
        "friday": "Friyayyyyyy!"
    }
    return switch.get(day, "Enjoy your weekend!")                      #bunun yerine

    # day_picked = switch.get(day, "Enjoy your weekend!")              Bu 2 satır kod ile de direkt print edebiliriz
    # print(day_picked)

day = input("Pick a day:\n")
print(pick_a_day(day))                                            #burada tekrar print kullanmamıza gerek kalmaz

# pick_a_day("monday")
