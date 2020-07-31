import webbrowser as wb

def webauto():
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    URLS=(
        "gmail.com",
        "google.com"
    )

    for url in URLS:
        print("opening"+url)
        wb.get(chrome_path).open(url)


webauto()