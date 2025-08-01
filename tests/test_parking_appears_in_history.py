
from pages.history_page import HistoryPage
from utils.utils import login_and_go_to_parking


def test_parking_appears_in_history(driver):
    print("Verify that after ending a parking session, the vehicle appears in the history page")
    parking_page = login_and_go_to_parking(driver)

    random_plate = parking_page.generate_random_plate()
    parking_page.park_vehicle(random_plate, "A1")
    parking_page.verify_parking_started(random_plate)
    alert_text = parking_page.get_parking_alert_text()
    assert "Parking started" in alert_text
    parking_page.finish_parking(random_plate)


    parking_page.go_to_history_page()
    history_page = HistoryPage(driver)

    assert history_page.is_vehicle_in_history(random_plate)
    print("Vehicle appears in history as expected- Passed")

