
import os
import time
from playwright.sync_api import sync_playwright, expect

def debug_language_game():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
        page.on("pageerror", lambda err: print(f"PAGE ERROR: {err}"))

        print("Loading app...")
        page.goto("http://localhost:8000/neuroactive.html")
        time.sleep(1)

        print("Logging in...")
        page.fill("#input-username", "DebugUser")
        page.click("#btn-login")
        expect(page.locator("#view-home")).to_be_visible()

        # Test 1: Association Game
        print("Starting Word Assoc Game...")
        page.locator("button:has-text('Asociación')").click()
        time.sleep(2)

        msg_el = page.locator("#game-message")
        msg_text = msg_el.inner_text()
        print(f"WordAssoc Message: '{msg_text}'")

        if "Cargando..." in msg_text:
            print("FAILURE: WordAssoc stuck.")
            page.screenshot(path="debug_wa_stuck.png")

        # Go back
        page.click("#btn-global-back")

        # Test 2: Phrase Game
        print("Starting Phrase Game...")
        page.locator("button:has-text('Ordenar Frases')").click()
        time.sleep(2)

        msg_el = page.locator("#game-message")
        msg_text = msg_el.inner_text()
        print(f"Phrase Message: '{msg_text}'")

        if "Cargando..." in msg_text:
            print("FAILURE: Phrase stuck.")
            page.screenshot(path="debug_phrase_stuck.png")

        browser.close()

if __name__ == "__main__":
    debug_language_game()
