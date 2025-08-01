
from utils.utils import login_and_go_to_parking


def test_same_vehicle_two_users(driver):
    print("Verify duplicate parking prevention for the same vehicle across different users")
    parking_page = login_and_go_to_parking(driver)
    random_plate = parking_page.generate_random_plate()
    parking_page.park_vehicle(random_plate, "A1")
    parking_page.verify_parking_started(random_plate)
    parking_page.logout()
    login_and_go_to_parking(driver,"user2", "password")
    parking_page.park_vehicle(random_plate, "A2")
    error_text = parking_page.get_parking_alert_text()
    assert "already parked" in error_text

    parking_page.finish_parking(random_plate)
