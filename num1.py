import math
def solve(a, b, c):

    discriminant = b ** 2 - 4 * a * c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return tuple(sorted((root1, root2)))
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(abs(discriminant)) / (2 * a)
        return tuple(sorted(((real_part, imaginary_part), (real_part, -imaginary_part))))

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
roots = solve(a, b, c)
print("Корни уравнения в порядке возрастания:", roots)


