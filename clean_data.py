import csv

# ICNPO_friveg1 - Prioritert
# ICNPO_friveg2 - Sekundær
# ICNPO_friveg3 - Tertiær
# icnpo-isic - Internasjonal
# icnpony - Har beste informasjon fra de tre alternativene

# Aktivitet - Organisasjoner har beskrevet egen aktiviteter
# Org. navn kan også gi info om hvilken kategori den hører til

lookupName09 = dict()
lookupNumber09 = dict()
lookupName13 = dict()
lookupNumber13 = dict()
icnpo_set = set()
haveIcnpo = 0
missingIcnpo = 0
labelled = []
unlabelled = []

with open("organisasjoner2009.csv", mode="r") as organisasjoner:
    reader = csv.DictReader(organisasjoner)

    for row in reader:
        if (row["ICNPO"] == ""):
            continue

        if (row["Organisasjonsnummer"] != ""):
            lookupNumber09[row["Organisasjonsnummer"]] = row["ICNPO"]

        if (row["Organisasjonsnavn"] != ""):
            lookupName09[row["Organisasjonsnavn"]] = row["ICNPO"]

        icnpo_set.add(row["ICNPO"])

with open("organisasjoner2013.csv", mode="r") as organisasjoner:
    reader = csv.DictReader(organisasjoner)

    for row in reader:
        if (row["icnponr"] == ""):
            continue

        if (row["orgnr"] != ""):
            lookupNumber09[row["orgnr"]] = row["icnponr"]

        if (row["orgnavn"] != ""):
            lookupName09[row["orgnavn"]] = row["icnponr"]

        icnpo_set.add(row["icnponr"])

with open("organisasjoner.csv", mode="r") as organisasjoner:
    reader = csv.DictReader(organisasjoner)

    for row in reader:
        orgNumber = row["Organisasjonsnummer"]
        orgName = row["Navn"]
        icnpo = row["icnpony"]

        if (icnpo == "" and orgNumber in lookupNumber13):
            icnpo = lookupNumber13[orgNumber]

        if (icnpo == "" and orgName in lookupName13):
            icnpo = lookupName[orgName]

        if (icnpo == "" and orgNumber in lookupNumber09):
            icnpo = lookupNumber09[orgNumber]

        if (icnpo == "" and orgName in lookupName09):
            icnpo = lookupName09[orgName]

        if (icnpo == ""):
            missingIcnpo += 1
            unlabelled.append({
                "Organisasjonsnummer": row["Organisasjonsnummer"],
                "Navn": row["Navn"],
                "Organisasjonsformkode": row["Organisasjonsformkode"],
                "Aktivitet": row["Aktivitet"],
            })
        else:
            haveIcnpo += 1
            labelled.append({
                "Organisasjonsnummer": row["Organisasjonsnummer"],
                "Navn": row["Navn"],
                "Organisasjonsformkode": row["Organisasjonsformkode"],
                "Aktivitet": row["Aktivitet"],
                "Icnpo": icnpo
            })

        icnpo_set.add(row["icnpony"])

with open("labelled_data.csv", mode="w") as data_file:
    writer = csv.DictWriter(data_file, fieldnames=["Organisasjonsnummer", "Navn", "Organisasjonsformkode", "Aktivitet", "Icnpo"])
    writer.writeheader()
    writer.writerows(labelled)

with open("unlabelled_data.csv", mode="w") as data_file:
    writer = csv.DictWriter(data_file, fieldnames=["Organisasjonsnummer", "Navn", "Organisasjonsformkode", "Aktivitet"])
    writer.writeheader()
    writer.writerows(unlabelled)

print(icnpo_set)
print(len(icnpo_set))
print(f"Missing: {missingIcnpo}")
print(f"Have: {haveIcnpo}")
