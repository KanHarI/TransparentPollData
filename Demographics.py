
import pandas
import argparse
import pickle

VOTE_19_IDX = "Vote19"
VOTE_15_IDX = "Vote15"
ARAB = "Arab"
GENDER = "Gender"
AGE = "Age"
RELIGION = "Religion"
RELIGIOSITY = "Religiosity"
POP_W = "pop_w"
AREA = "Area"
FAMILYSTATUS = "FamilyStatus"
PROFESSION = "Profession"
BORNPLACE = "Bornplace"
FAMILYNUMBER = "FamilyNumber"
INCOME = "Income"
EDUCATION = "Education"

AGE_CHECKPOINTS = [22, 35, 45, 55, 70]
AGE_DICT = {
    1 : "18-22",
    2 : "23-35",
    3 : "36-45",
    4 : "45-55",
    5 : "55-70",
    6 : "70+"
}

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

PARTIES_15 = [
    "Likud",
    "Avoda",
    "Meretz",
    "Liberman",
    "Kahlon",
    "Gimel",
    "Shas",
    "Joint",
    "Lapid",
    "Bait",
    "Yachad",
    "Other",
    "No",
    "Couldnt"
]

def create_person(row, *, religion=False, gender=False, age=False, area=False, income=False, profession=False, education=False, pop_w_corrections=False):
    person = dict()
    if religion:
        if row[ARAB] == 1:
            person["religion"] = row[RELIGION]
        else:
            person["religion"] = row[RELIGIOSITY]
    if age:
        age_param = 1
        for chk in AGE_CHECKPOINTS:
            if row[AGE] > chk:
                age_param += 1
        person["age"] = AGE_DICT[age_param]
    if income:
        person["income"] = row[INCOME]
    if profession:
        person["profession"] = row[PROFESSION]
    if education:
        person["education"] = row[EDUCATION]
    if area:
        person["area"] = row[AREA]
    if gender:
        person["gender"] = row[GENDER]
    if pop_w_corrections:
        return person, row[POP_W]
    else:
        return person, 1.0


def main(args):
    data = pandas.read_csv("TransPollData.csv")
    population = dict()
    for party in PARTIES_19:
        population[party] = dict()
    parameters = {
        "religion": args.religion,
        "age": args.age,
        "income": args.income,
        "profession": args.profession,
        "education": args.education,
        "area": args.area,
        "gender": args.gender,
        "pop_w_corrections": args.pop_w
    }
    for i in range(len(data)):
        person, w = create_person(data.loc[i], **parameters)

        # pickling required to use person, which is a dictionary, as index in array
        person = pickle.dumps(person)
        voting_to = data.loc[i][VOTE_19_IDX]
        voting_to = voting_to if type(voting_to) is str else None
        party_dict = population[voting_to]
        if person in party_dict:
            party_dict[person] += w
        else:
            party_dict[person] = w
    print("Results: \n ==============")
    for party in PARTIES_19:
        print("\n{party}:".format(party=party))
        party_pop = population[party]
        party_pop_idx = sorted(party_pop.keys(), key=lambda x:-party_pop[x])
        party_pop = {idx: party_pop[idx] for idx in party_pop_idx}
        party_sum = sum(party_pop.values())
        for pop, val in party_pop.items():
            print("{pop}: {val}%".format(pop=pickle.loads(pop), val=int(val/party_sum*100+0.5)))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--religion", action="store_true")
    parser.add_argument("--age", action="store_true")
    parser.add_argument("--income", action="store_true")
    parser.add_argument("--profession", action="store_true")
    parser.add_argument("--education", action="store_true")
    parser.add_argument("--area", action="store_true")
    parser.add_argument("--gender", action="store_true")
    parser.add_argument("--pop-w", action="store_true")
    args = parser.parse_args()
    main(args)
