import pytest
from utils.utils import login_and_go_to_parking

#Validations cases
@pytest.mark.parametrize(
    "plate, expected_error",
    [
         ("123", "License plate must be exactly 8 digits"),
         ("", "Please fill out this field."),
         ("121212121", None),
         ("abcdefgd", None),
         ("12345678",  "License plate cannot be a sequential pattern"),
         ("11111111", "License plate cannot have all identical digits"),
        ("00000000", "Invalid license plate number"),
    ]
)

def test_plate_field_validations(driver, plate, expected_error):
        print("Form validation for parking fields")
        parking_page = login_and_go_to_parking(driver)
        parking_page.enter_plate_num(plate)

        if plate == "":
            print("Checking HTML5 required field validation...")
            parking_page.click_start_parking()
            is_invalid, message = parking_page.get_required_field_validation_message()
            assert is_invalid, "Expected field to be invalid"
            assert expected_error in message

        elif expected_error:
            actual_error = parking_page.get_validation_error_text()
            print(f"Validation error: {actual_error}")
            assert expected_error == actual_error, f"Expected error: {expected_error}, got: {actual_error}"
        else:
            actual_value = parking_page.get_plate_field_value()
            print(f"Plate value: {actual_value}")
            assert len(actual_value) <= 8, "Plate input should be max 8 characters"
