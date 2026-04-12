def nameInitials(firstName,lastName):
    if not firstName or not lastName:
        raise ValueError("Both firstName and lastName must be non-empty strings.")
    return firstName[0] + "." + lastName[0]
