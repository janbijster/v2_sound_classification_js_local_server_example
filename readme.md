# Local server example to process recorded data

## installation

You need python3 and pip. Install flask:
```
pip3 install flask
```
or
```
pip3 install flask --user
```

## Run example
```
python3 app.py
```

## CORS
The browser will block an ajax request on a https page to an unsecured address and it won't accept a self-signed certificate either.
So the easiest way to make it work with the sound-js webapp is to run that in a browser-mode with security disabled:

Windows:
```
"[PATH_TO_CHROME]\chrome.exe" --disable-web-security --disable-gpu --user-data-dir=~/chromeTemp
```

OSX:
```
open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security
```

Linux:
```
google-chrome --disable-web-security
```