import csv
import random

data = []
labels = {
    '1100': 0,
    '1200': 1,
    '1300': 2,
    '1310': 3,
    '2100': 4,
    '2200': 5,
    '2300': 6,
    '2400': 7,
    '3100': 8,
    '3200': 9,
    '3300': 10,
    '3400': 11,
    '4100': 12,
    '4200': 13,
    '4300': 14,
    '5100': 15,
    '5200': 16,
    '6100': 17,
    '6200': 18,
    '6300': 19,
    '7100': 20,
    '7200': 21,
    '7300': 22,
    '8100': 23,
    '8200': 24,
    '9100': 25,
    '10100': 26,
    '11100': 27,
    '11200': 28,
    '11300': 29,
    '12100': 30,
    '13100': 31,
    '14100': 32,
}

with open("labelled_data.csv", mode="r") as organisasjoner:
    reader = csv.DictReader(organisasjoner)

    for row in reader:
        data.append({
            "text": f"Organisasjonsnavn: {row["Navn"]}\nAktivitet: {row["Aktivitet"]}",
            "label": labels[row["Icnpo"]]
        })

random.shuffle(data)

# Define the split ratio (e.g., 80% training, 20% testing)
split_ratio = 0.8
split_index = int(len(data) * split_ratio)

# Split the data
train = data[:split_index]
test = data[split_index:]

with open("org-classifier/train.csv", mode="w") as data_file:
    writer = csv.DictWriter(data_file, fieldnames=["text", "label"])
    writer.writeheader()
    writer.writerows(train)

with open("org-classifier/test.csv", mode="w") as data_file:
    writer = csv.DictWriter(data_file, fieldnames=["text", "label"])
    writer.writeheader()
    writer.writerows(test)
