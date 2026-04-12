def isThereSchool(day: str,isHoliday: bool) -> bool:
    isWeekend = (day == "Sunday") or (day == "Saturday")
    return not (isWeekend or isHoliday)


