import csv

TVA = 0.20

with open("catalogue_fournisseur.csv", newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    produits = []

    for row in reader:
        if row["nom"] and row["prix_ht"]:
            prix_ht = float(row["prix_ht"])
            row["prix_ttc"] = round(prix_ht * (1 + TVA), 2)
            produits.append(row)

with open("catalogue_nettoye.csv", "w", newline="", encoding="utf-8") as outfile:
    fieldnames = produits[0].keys()
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(produits)
