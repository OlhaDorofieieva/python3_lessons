import re

my_string = "Place of delivery of goods: 82172, Ukraine, Lviv Region, Stryi, str. Doroshenko, 1. Deadline for delivery of goods: 31.12.2024"


if __name__ == '__main__':
    data = {
        'country': re.search(r'\b\w*krain\w*\b', my_string).group(),
        'region': re.search(r'(?<=Region\,\s)\b\w+\b', my_string).group(),
        'city': re.search(r'\b\w+\b(?=\sRegion)', my_string).group(),
        'postal': re.search(r'\d{5}', my_string).group(),
        'address': re.search(r'str\.\s\w+\,\s\d', my_string).group(),
        'deadline': re.search(r'\d\d\.\d\d.\d\d\d\d$', my_string).group(),
    }
    print(data)
