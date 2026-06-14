fruit_inventory = [
    ["사과", 50, 12],
    ["바나나", 120, 15],
    ["딸기", 30, 14],
    ["수박", 15, 11],
    ["포도", 80, 16]
]

fruit_inventory.sort(key=lambda x: -x[2])
print(fruit_inventory)