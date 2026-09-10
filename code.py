A = 5
B = 3
C = 7

klasnoe_nazwanie = ~(A & B) | ~(A | C)

otvet = ~A | ~B

print(f"Исходное выражение: {klasnoe_nazwanie}")
print(f"Упрощенное выражение: {otvet}")  
print(f"Результаты совпадают? {klasnoe_nazwanie == otvet}")  