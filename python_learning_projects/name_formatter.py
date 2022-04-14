def name_formatter(first_name,last_time,middle_name=""):
    "formats the name and then prints it"
    if middle_name:
        formatted_name = first_name.title() + " " + middle_name.title() + " " + last_time.title()
    else:
        formatted_name = first_name.title() + " " + last_time.title()
    return formatted_name
