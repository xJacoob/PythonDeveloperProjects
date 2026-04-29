from DataManagement import DataManagement

def main():
    data = DataManagement("C:/Users/kubak/Documents/Programming/PycharmProjects/Easy Rider Bus Company/Easy Rider Bus Company/task/easyrider/data.json")
    data.load_data()
    data.validate_type_and_empty()
    data.validate_data()

    number_of_stops = data.count_number_of_stops()
    data.validate_arrival()

    errors = sum(data.errors.values())
    print(f"Type and field validation: {errors} errors")

    for key, value in data.errors.items():
        print(f"{key}: {value}")

    print(f"\nLine names and number of stops: ")

    for key, value in number_of_stops.items():
        print(f"bus_id: {key} stops: {value}")

    print()

    start_stop_validation = data.check_start_stop()

    if start_stop_validation:
        print(f"There is no start or end stop for the line: {start_stop_validation}")
    else:
        data.check_start_demand_finish_stop()


if __name__ == "__main__":
    main()