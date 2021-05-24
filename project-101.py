import webbrowser

#chrome_path="C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"  #for chrome
edge_path="C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

#webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path)) #for chrome
webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))

#webbrowser.get('chrome').open('https://code.whitehatjr.com/s/dashboard') #for chrome
webbrowser.get('edge').open('https://code.whitehatjr.com/s/dashboard')