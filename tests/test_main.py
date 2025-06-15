from src.main import csv_to_records
import tempfile
import os


def create_test_csv():
    input = """Domain Code,Domain,Area Code (M49),Area,Element Code,Item Code (CPC),Item,Year,Unit,Import,Export ,Production,Consumption
TCL,Crops and livestock products,4,Afghanistan,5610,1654,"Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw",2014,t,283.85,21099,21500,684.85"""

    # Create a temporary directory
    with tempfile.TemporaryDirectory() as tmpdirname:
        print(f"Created temporary directory at {tmpdirname}")

        # Create a file inside it
        filepath = os.path.join(tmpdirname, "testfile.txt")
        with open(filepath, "w") as f:
            f.write("Hello inside a temp directory!")

        # Read the file back
        with open(filepath, "r") as f:
            print(f.read())
        with open("_sample.test.csv", "w") as file:
            file.write(input)


def test_csv_to_record():
    create_test_csv()

    expected = [
        (
            "TCL",
            "Crops and livestock products",
            "5610",
            "1654",
            "Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw",
            "2014",
            "t",
            "283.85",
            "21099",
            "21500",
            "684.85",
        )
    ]

    assert csv_to_records(input) == expected
