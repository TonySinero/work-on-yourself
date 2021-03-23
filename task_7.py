def dym_santim (x):
    inch = float(2.54) * x
    print(f'{x} (дюймы) = {round(inch,2)} (сантиметры)')
    return inch

def santim_dym (x):
    inch = float(0.39) * x
    print(f'{x} (сантиметры) = {round(inch,2)} (дюймы)')
    return inch

def mile_km (x):
    inch = float(1.609) * x
    print(f'{x} (мили) = {round(inch,2)} (киллометры)')
    return inch

def km_mile (x):
    inch = float(0.621) * x
    print(f'{x} (киллометры) = {round(inch,2)} (мили)')
    return inch

def funt_kg (x):
    inch = float(0.453) * x
    print(f'{x} (фунты) = {round(inch,2)} (киллограмы)')
    return inch

def kg_funt (x):
    inch = float(2.204) * x
    print(f'{x} (киллограмы) = {round(inch,2)} (фунты)')
    return inch

def unci_gram (x):
    inch = float(28.349) * x
    print(f'{x} (унции) = {round(inch,2)} (граммы)')
    return inch

def gram_unci (x):
    inch = float(0.035) * x
    print(f'{x} (граммы) = {round(inch,2)} (унции)')
    return inch

def gal_litr (x):
    inch = float(3.785) * x
    print(f'{x} (галлоны) = {round(inch,2)} (литры)')
    return inch

def litr_gal (x):
    inch = float(0.264) * x
    print(f'{x} (литры) = {round(inch,2)} (галлоны)')
    return inch

def pint_litr (x):
    inch = float(0.473) * x
    print(f'{x} (пинты) = {round(inch,2)} (литры)')
    return inch

def litr_pint (x):
    inch = float(2.113) * x
    print(f'{x} (литры) = {round(inch,2)} (пинты)')
    return inch


if __name__ == '__main__':
    mapping = {
        '1': dym_santim,
        '2': santim_dym,
        '3': mile_km,
        '4': km_mile,
        '5': funt_kg,
        '6': kg_funt,
        '7': unci_gram,
        '8': gram_unci,
        '9': gal_litr,
        '10': litr_gal,
        '11': pint_litr,
        '12': litr_pint,
    }
    num_of_function = input('введи число от 1 до 12. Для завершения введи 0\n')
    while num_of_function != 0:
        num_of_function = input('введи число от 1 до 12\n')
        func = mapping.get(num_of_function)
        num_to_convert = int(input('введи значение для конвертации\n'))
        func(num_to_convert)


















