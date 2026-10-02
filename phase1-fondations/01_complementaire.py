"""
Étape 1 — Le brin complémentaire

Règle d'appariement de l'ADN : A <-> T et C <-> G.
Chaque lettre est TOUJOURS remplacée par sa partenaire.
"""

PAIRES = {"A": "T", "T": "A", "C": "G", "G": "C","N": "N"}


def complementaire(brin: str) -> str:
    """Retourne le brin d'ADN complémentaire."""
    brin = brin.upper()  # Convertit le brin en majuscules pour uniformiser la recherche dans PAIRES
    # À toi de jouer : parcours chaque lettre du brin,
    # cherche sa partenaire dans PAIRES, et assemble le résultat.
    for lettre in brin:
        if lettre not in PAIRES:
            raise ValueError(f"Lettre invalide dans le brin est : {lettre}")
        
    return "".join(PAIRES[lettre] for lettre in brin)


if __name__ == "__main__":
    # Ces tests sont tes propres exercices de la leçon 1.
    # Ton programme doit trouver les mêmes réponses que toi.
    assert complementaire("ATGCCA") == "TACGGT"
    assert complementaire("GATTCA") == "CTAAGT"
    assert complementaire("TGCAATCG") == "ACGTTAGC"
    assert complementaire("atgc") == "TACG" # TEST LETTRE MINUSCULE.
    assert complementaire("ATNGC") == "TANCG" # TEST LETTRE INCONNU.
    print("Tous les tests passent ! 🎉")

