def getBootstrapClass(screenWidth):
    if screenWidth >= 1200:
        return "lg"
    elif screenWidth >= 992:
        return "md"
    elif screenWidth >= 768:
        return "sm"
    else:
        return "xs"

