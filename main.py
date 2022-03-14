number_of_tickets = int(input("Введите количество билетов, которые вы хотите приобрести: "))
visitors = [int(input(f"Введите возраст посетителя №{i+1}: ")) for i in range(number_of_tickets)]
price = 0
for age in visitors:
    if age > 25:
        price += 1390
    elif 18 <= age <= 25:
        price += 990
if number_of_tickets > 3:
    price -= int(price * 0.1)
print(f"Сумма к оплате: {price} рублей")