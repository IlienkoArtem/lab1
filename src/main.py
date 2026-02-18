import math

def solve_quadratic(a, b, c):
    print(f"Розв'язуємо рівняння: {a}x^2 + {b}x + {c} = 0")
    
    # Обчислюємо дискримінант: D = b^2 - 4ac
    discriminant = b**2 - 4*a*c
    print(f"Дискримінант (D) = {discriminant}")

    if discriminant > 0:
        # Два корені: x = (-b ± √D) / 2a
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Рівняння має два корені: x1 = {round(x1, 2)}, x2 = {round(x2, 2)}"
    elif discriminant == 0:
        # Один корінь: x = -b / 2a
        x = -b / (2*a)
        return f"Рівняння має один корінь: x = {round(x, 2)}"
    else:
        return "Рівняння не має дійсних коренів."

if __name__ == "__main__":
    result = solve_quadratic(1, -5, 6)
    print(result)
    print("Результат: Об'єднана версія MAIN + DEVELOP")