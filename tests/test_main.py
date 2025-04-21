from src.main import map_records

def test_map_to_record_list():
    input = [
        [
            "TCL",
            "Crops and livestock products",
            276,
            "Germany",
            5610,
            1654,
            "Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw",
            2022,
            "t",
            19092.44,
            5313.95,
            0,
            13778.49,
        ],
        [
            "TCL",
            "Crops and livestock products",
            276,
            "Germany",
            5610,
            1654,
            "Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw",
            2023,
            "t",
            15158.73,
            5221.55,
            0,
            9937.18,
        ],
    ]

    expected = [
        {
            "domain_code": "TCL",
            "domain": "Crops and livestock products",
            "area_code": 276,
            "area": "Germany",
            "item_code": 5610,
            "item": "Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw",
            "year": 2022,
            "unit": "t",
            "import_quantity": 19092.44,
            "export_quantity": 5313.95,
            "production": 0,
            "consumption": 13778.49,
        },
        {
            "domain_code": "TCL",
            "domain": "Crops and livestock products",
            "area_code": 276,
            "area": "Germany",
            "item_code": 5610,
            "item": "Anise, badian, coriander, cumin, caraway, fennel and juniper berries, raw",
            "year": 2023,
            "unit": "t",
            "import_quantity": 15158.73,
            "export_quantity": 5221.55,
            "production": 0,
            "consumption": 9937.18,
        },
    ]
    assert map_records(input) == expected
