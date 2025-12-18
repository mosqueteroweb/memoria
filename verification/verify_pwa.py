from playwright.sync_api import sync_playwright, expect
import time

def verify_app(page):
    print("Navigating to app...")
    page.goto("http://localhost:8000/neuroactive.html")

    # Check title
    print("Checking title...")
    expect(page).to_have_title("NeuroActive 2.2 - Senior Edition")

    # Login
    print("Performing login...")
    page.fill("#input-username", "Test User")
    page.click("#btn-login")

    # Wait for Home
    print("Waiting for home screen...")
    expect(page.locator("#view-home")).to_be_visible()

    # Wait a bit for animations
    time.sleep(1)

    # 1. Verify Stroop (Checks if game_data.js loaded colors correctly)
    print("Starting Stroop game...")
    page.click("button[onclick=\"app.startGame('stroop')\"]")

    expect(page.locator("#view-game")).to_be_visible()

    # Wait for game content
    time.sleep(1)

    # Check if buttons with color names appear (ROJO, AZUL, VERDE)
    # These come from GAME_DATA.stroop.colors
    print("Checking Stroop buttons...")
    expect(page.get_by_role("button", name="ROJO")).to_be_visible()
    expect(page.get_by_role("button", name="AZUL")).to_be_visible()
    expect(page.get_by_role("button", name="VERDE")).to_be_visible()

    page.screenshot(path="verification/stroop_verification.png")
    print("Stroop verification screenshot saved.")

    # Go back
    page.click("#btn-global-back")

    # 2. Verify Language Order (Checks GAME_DATA.languageOrder.phrases)
    print("Starting Language Order game...")
    # Need to wait for transition
    time.sleep(1)
    page.click("button[onclick=\"app.startGame('languageOrder')\"]")

    # Wait for game to init
    time.sleep(1)

    # The game picks a random phrase. We check if the bank contains words from one of the phrases.
    # phrases = ["El cielo es azul", "Me gusta el pan", "Hoy hace sol", ... ]
    # We can just check if there are buttons in the bank.

    print("Checking Language Order bank...")
    bank_buttons = page.locator("#game-area button")
    count = bank_buttons.count()
    print(f"Found {count} word buttons.")

    if count == 0:
        raise Exception("No buttons found in Language Order game!")

    page.screenshot(path="verification/language_verification.png")
    print("Language verification screenshot saved.")

if __name__ == "__main__":
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        try:
            verify_app(page)
        except Exception as e:
            print(f"Error: {e}")
            page.screenshot(path="verification/error.png")
        finally:
            browser.close()
