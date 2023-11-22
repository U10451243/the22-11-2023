import webbrowser
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser('C:\Program Files\Google\Chrome\Application\chrome.exe'))

from time import sleep

def openPage(url):
    webbrowser.get('chrome').open(url)
    sleep(1)

x=int(input("Enter number of tabs (int): "))
link=input("Enter EXACT link: ")

for a in range(0,x):
        openPage(link)