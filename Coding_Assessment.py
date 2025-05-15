from mimetypes import init


def sort(width, height, length, mass):
    volume = width * height * length
    bulky = volume >= 1_000_000 or max(width, height, length) >= 150
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    elif bulky or heavy:
        return "SPECIAL"

    else:
        return "STANDARD"

#Sample Test cases
print(sort(100, 100, 100, 10))
print(sort(200, 100, 50, 10))
print(sort(200, 200, 50, 25))
