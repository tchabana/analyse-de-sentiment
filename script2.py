import pandas as pd

# Chargement du fichier CSV
input_file = "./data/train.csv"  # Remplacez par le chemin de votre fichier CSV
output_file = "./data/train-output.csv"  # Nom du fichier de sortie

# Lire le fichier CSV
df = pd.read_csv(input_file)

# Supprimer la colonne 'source'
df = df.drop(columns=["source"])

# Remplacer les labels
label_mapping = {"negative": 0, "positive": 1}
df["label"] = df["label"].replace(label_mapping)

# Sauvegarder le fichier modifié
df.to_csv(output_file, index=False)

print(f"Le fichier modifié a été sauvegardé sous le nom {output_file}.")