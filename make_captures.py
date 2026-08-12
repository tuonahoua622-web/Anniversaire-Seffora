import os, time
from playwright.sync_api import sync_playwright

OUT = r"C:\Users\DELL\Anniversaire-captures"
os.makedirs(OUT, exist_ok=True)
URL = "https://tuonahoua622-web.github.io/Anniversaire-Seffora/"

def shot(page, name):
    path = os.path.join(OUT, name)
    page.screenshot(path=path)
    print("saved", path)

with sync_playwright() as p:
    browser = p.chromium.launch(channel="msedge", headless=True)
    page = browser.new_page(viewport={"width": 1280, "height": 800})
    page.goto(URL, wait_until="networkidle")
    time.sleep(2)
    shot(page, "1-accueil.png")

    # MERCI
    page.click("#btn-welcome")
    time.sleep(1.4)
    shot(page, "2-transition.png")

    # aller a l'intro (clic n'importe ou sur transition)
    page.click("#s-transition")
    time.sleep(1.4)
    shot(page, "3-intro-lettres.png")

    # LES DECOUVRIR
    page.click("#btn-enter-letters")
    time.sleep(1.4)
    shot(page, "4-enveloppes.png")

    # TERMINER
    page.click("#btn-to-finale")
    time.sleep(1.4)
    shot(page, "5-finale.png")

    browser.close()
print("DONE")
