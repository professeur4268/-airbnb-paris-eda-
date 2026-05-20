import sweetviz as sv
import pandas as pd

# Charge les données nettoyées (créées par cleaning.py)
df = pd.read_csv("../data/clean/listings_clean.csv")


# Génère le rapport HTML automatique
rapport = sv.analyze(df)

rapport.show_html("../outputs/rapport_sweetviz.html")

print("✅ Rapport généré dans outputs/rapport_airbnb.html")