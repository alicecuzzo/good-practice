import requests

def ok_function():
    print('Do some boiajoew')
    return 24


def download_text_from_web():
    r= requests.get('https://docs.python.org/3/library/unittest.mock.html')
    print('got text')
    m = requests.get('https://docs.google.com/document/d/1QV3zLaG20DLFMvTzsOlrI_YsMOU-5kN3il1NmpvZ0FY/edit#')
    return r.text

def countWords(text):
    return len(text)

def do_text_analysis():
    text = download_text_from_web()
    world_count = countWords(text)
    return world_count
