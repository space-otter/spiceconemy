from csv import reader


def parse_records():
    with open("resources/dataset.csv", "r") as file:
        csv_reader = reader(file, delimiter=",")
        header = next(csv_reader)  # Skip the header row
        records = [tuple(row) for row in csv_reader]
    return header, records


def main():
    # Your main code here
    header, records = parse_records()
    print("Parsed Records:")
    for col in header:
        print(col)


# is a common Python idiom that ensures the main() function only runs when the script is executed directly,
# not when it is imported as a module in another script.
if __name__ == "__main__":
    main()
