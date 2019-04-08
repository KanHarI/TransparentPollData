
import pandas

PARTIES_19 = [
    "Likud",
    "Lavan",
    "Avoda",
    "NYamin",
    "UYamin",
    "Meretz",
    "Liberman",
    "Kahlon",
    "Gesher",
    "Gimel",
    "Shas",
    "Hadash",
    "Balad",
    "Zehut",
    "Float",
    "Other",
    "No",
    None # Did not answer
]

VOTE_19_IDX = "Vote19"
VOTE_TEND = "VoteTend"
POP_W = "pop_w"

if __name__ == "__main__":
	data = pandas.read_csv("TransPollData.csv")
	support = {k: 0.0 for k in PARTIES_19}
	for i in range(len(data)):
		row = data.loc[i]
		party = row[VOTE_19_IDX]
		if party in ["Float", "No", None] or type(party) != str:
			continue
		tend = row[VOTE_TEND]
		support[party] += row[POP_W]*tend
	support_sum = sum(support.values())
	support = {k: v/support_sum for k,v in support.items()}
	print(support)
