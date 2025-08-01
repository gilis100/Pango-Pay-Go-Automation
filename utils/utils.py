from pages.login_page import LoginPage
from pages.parking_page import ParkingPage

def login_and_go_to_parking(driver, username="admin", password="password"):
    driver.get("http://localhost:5000")

    login_page = LoginPage(driver)
    login_page.login(username, password)
    assert login_page.verify_login_successful(), "Login failed"

    return ParkingPage(driver)
