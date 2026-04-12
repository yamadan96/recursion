def weekly7DaysSales(ticketPrice):
    # 基準価格
    standard_price = 250
    # 価格が$10変化するごとに変化する人数
    change_per_10_dollars = 700
    # 基準価格での購入人数
    base_sales = 150000

    # 購入人数の計算
    number_of_sales = base_sales + change_per_10_dollars * (standard_price - ticketPrice)
    return number_of_sales
