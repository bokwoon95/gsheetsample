# gsheetsample
sample on how to use google sheet's api to write to an existing google sheet. parsexml.py will extract the name and value from the xml file and write it into a google sheet of your choosing (provided by your google sheet ID).

1) Using command prompt/powershell or a terminal, navigate to this directory containing parsexml.py. Run the command `pip install -r requirements.txt`

2) Follow steps 1 & 2 of [https://developers.google.com/sheets/api/quickstart/python](https://developers.google.com/sheets/api/quickstart/python). You will download a credentials.json file which you need to place in the same directory as parsexml.py.

3) Open parsexml.py and change the Spreadsheet ID in the line `SPREADSHEET_ID = '1_9T4Wik9u6v7tBOORhurPPF4YLCjQMw03kvTdp3I1Gk'` to your own google sheet's spreadsheet ID. Note that you must already have an existing google sheet created for this.

4) Run `python parsexml.py`. You should be directed to a google login page to login. If this works you can skip step 4a

4a) You may need to run `python parsexml.py --noauth_local_webserver` instead, just follow the instructions shown in the console. Go to the link given to you, copy the verification code shown in the browser by visting the link and paste it back in the console.

5) After that wait for the script to complete and check your google sheet again
