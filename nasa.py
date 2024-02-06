def read_astronaut_data(file_path):
    astronauts_data = []
    with open(file_path, 'r') as file:
        next(file)
        for line in file:
            astronaut_info = line.strip().split(',')
            astronauts_data.append(astronaut_info)
    return astronauts_data


def count_birth_months(astronauts_data):
    birth_months_count = {}
    for astronaut_info in astronauts_data:
        birth_date = astronaut_info[4]
        birth_month = int(birth_date.split('/')[0])
        birth_months_count[birth_month] = birth_months_count.get(birth_month, 0) + 1
    return birth_months_count


def display_top_months(birth_months_count):
    sorted_months = sorted(birth_months_count.items(), key=lambda x: x[1], reverse=True)
    total_astronauts = sum(birth_months_count.values())

    print("A három leggyakoribb hónap")
    for i, (month, count) in enumerate(sorted_months[:3]):
        percentage = (count / total_astronauts) * 100
        print(f"{i + 1}. Hónap {month}: {percentage:.1f}%")


def main():
    file_path = "astronauts.csv.csv"
    astronauts_data = read_astronaut_data(file_path)
    birth_months_count = count_birth_months(astronauts_data)
    display_top_months(birth_months_count)


main()
