def season(attribute):
    if attribute == "snow":
        return "winter"
    elif attribute == "sun":
        return "summer"


def range_list(first_number, second_number):
    range_list = []
    for i in range(first_number, second_number):
        range_list.append(i)

    return range_list