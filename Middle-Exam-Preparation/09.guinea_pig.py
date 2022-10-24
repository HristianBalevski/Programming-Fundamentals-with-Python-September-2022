quantity_food_in_kilograms = float(input())
quantity_hay_in_kilograms = float(input())
quantity_cover_in_kilograms = float(input())
guinea_weight_in_kilograms = float(input())

for day in range(1, 31):
    quantity_food_in_kilograms -= 0.300

    if quantity_cover_in_kilograms <= guinea_weight_in_kilograms * 1/3 or quantity_hay_in_kilograms <= 0 or \
            quantity_food_in_kilograms <= 0.300:
        print("Merry must go to the pet store!")
        break

    if day % 2 == 0:
        quantity_hay_in_kilograms -= quantity_food_in_kilograms * 0.05
    if day % 3 == 0:
        quantity_cover_in_kilograms -= guinea_weight_in_kilograms * 1/3

else:
    print(f'Everything is fine! Puppy is happy! Food: {quantity_food_in_kilograms:.2f}, '
          f'Hay: {quantity_hay_in_kilograms:.2f}, Cover: {quantity_cover_in_kilograms:.2f}.')