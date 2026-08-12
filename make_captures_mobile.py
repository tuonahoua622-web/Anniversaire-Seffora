import os, time
from playwright.sync_api import sync_playwright

OUT = r"C:\Users\DELL\Anniversaire-captures\mobile"
os.makedirs(OUT, exist_ok=True)
URL = "https://tuonahoua622-web.github.io/Anniversaire-Seffora/"

def shot(page, name):
    path = os.path.join(OUT, name)
    page.screenshot(path=path)
    print("saved", path)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 390, "height": 844}, device_scale_factor=2)
    page.goto(URL, wait_until="networkidle")
    time.sleep(2)
    shot(page, "1-accueil.png")

    page.click("#btn-welcome")
    time.sleep(1.4)
    shot(page, "2-transition.png")

    page.click("#s-transition")
    time.sleep(1.4)
    shot(page, "3-intro-lettres.png")

    page.click("#btn-enter-letters")
    time.sleep(1.4)
    shot(page, "4-enveloppes.png")

    page.click("#btn-to-finale")
    time.sleep(1.4)
    shot(page, "5-finale.png")

    browser.close()
print("DONE")
