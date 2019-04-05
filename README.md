# TransparentPollData
A python3 API for the transparent poll data. Based on:

Lazar-Telem, Yonatan & Elkayam-Shalem, Haggai (2019). The Transparent Poll. Published Online [Data File and code book]. Available online: http://bit.ly/transpolldata

# Requirements:
pandas: `py -3 -m pip install pandas`

# Running demographics analysis:
`py -3 -m Demographics --gender` for gender analysis of voters for each party

`py -3 -m Demographics --gender --age` for gender and age analysis of voters for each party

Running with the `--pop-w` flag runs analysis after correcting for sample bias

`py -3 -m Demographics --gender --pop-w` will return analysis after sampling correction.

(By default, the analysis does not fix sample bias - pass the `--pop-w` to fix sampling bias!)

Run `py -3 -m Demographics --help` for full parameters list

etc...
