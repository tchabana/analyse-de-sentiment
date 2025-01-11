import csv

# Nom du fichier CSV original et du fichier de sortie
input_file = './data/sentiment-train-mini.csv'
output_file = './data/sentiment-train-mini-output.csv'

# Ouvrir le fichier CSV en lecture
with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.reader(infile)
    rows = []

    # Parcourir chaque ligne et modifier la première colonne si nécessaire
    for row in reader:
        if row[0] == '4':
            row[0] = '1'  # Remplacer 4 par 1
        rows.append(row)

# Écrire les lignes modifiées dans un nouveau fichier CSV
with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(rows)


