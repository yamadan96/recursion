def canProcessOrder(beef,chicken,salad,coffee,tea):
    mainDish = beef != chicken
    drink = coffee != tea
    return mainDish and drink



