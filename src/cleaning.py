import pandas as pd
import numpy as np

def load_data(path: str) -> pd.DataFrame:
    """Charge le dataset brut Airbnb."""
    df = pd.read_csv(path, compression="gzip", low_memory=False)
    print(f"Dataset chargé : {df.shape[0]:,} lignes, {df.shape[1]} colonnes")
    return df

def select_columns(df: pd.DataFrame) -> pd.DataFrame:
    """Garde uniquement les colonnes utiles."""
    col_quartier = 'neighbourhood_cleansed' if 'neighbourhood_cleansed' in df.columns else 'neighbourhood_cleanedx'
    
    colonnes = [
        'id', 'name', col_quartier, 'room_type',
        'price', 'number_of_reviews', 'review_scores_rating',
        'accommodates', 'bedrooms', 'availability_365'
    ]
    df_reduit = df[colonnes].copy()
    if col_quartier != 'neighbourhood_cleansed':
        df_reduit = df_reduit.rename(columns={col_quartier: 'neighbourhood_cleansed'})
    return df_reduit

def clean_price(df: pd.DataFrame) -> pd.DataFrame:
    """Nettoie la colonne price ou simule des données si elle est vide."""
    df = df.copy()
    
    # Si la colonne est complètement vide (remplie de NaN)
    if df['price'].isna().all():
        print("Note : La colonne 'price' d'origine est vide. Génération de prix réalistes pour l'exercice...")
        # On génère des prix aléatoires réalistes entre 45€ et 280€ la nuit
        np.random.seed(42) # Pour avoir toujours les mêmes résultats
        df['price'] = np.random.randint(45, 280, size=len(df))
    else:
        # Si elle n'est pas vide, on applique le nettoyage classique
        df['price'] = df['price'].astype(str).str.replace(r'[^\d\.]', '', regex=True)
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
    
    df = df[(df['price'] >= 10) & (df['price'] <= 5000)]
    return df

def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Gère les valeurs manquantes."""
    df = df.copy()
    df['bedrooms'] = df['bedrooms'].fillna(df['bedrooms'].median())
    df['review_scores_rating'] = df['review_scores_rating'].fillna(df['review_scores_rating'].median())
    df = df.dropna(subset=['neighbourhood_cleansed'])
    return df

def run_pipeline(input_path: str, output_path: str):
    """Pipeline complet : charge → sélectionne → nettoie → sauvegarde."""
    print("Début du pipeline de nettoyage...")
    df = load_data(input_path)
    df = select_columns(df)
    df = clean_price(df)
    df = handle_missing(df)
    df.to_csv(output_path, index=False)
    print(f"Données nettoyées sauvegardées : {df.shape[0]:,} lignes !")
    return df

if __name__ == "__main__":
    run_pipeline(
        "../data/raw/listings.csv.gz",
        "../data/clean/listings_clean.csv"
    )