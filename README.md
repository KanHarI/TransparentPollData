# TransparentPollData
A python3 API for the transparent poll data: https://drive.google.com/drive/folders/1PXEALN640Y8rcoziKEaIg5RkoNWAnjW5?fbclid=IwAR3Gyo0DwxnHgXXUu7RNBUwRPaBgjBHitKDjAT2WBIyeGZBIYiL8Zx750uk

# Requirements:
pandas: `py -3 -m pip install pandas`

# Running demographics tests:
`py -3 -m Demographics --gender` for gender analysis of voters for each party
`py -3 -m Demographics --gender --age` for gender and age analysis of voters for each party
Running with the `--pop-w` flag runs analysis after correcting for sample bias
`py -3 -m Demographics --gender --pop-w` will return analysis after sampling correction.
etc...
