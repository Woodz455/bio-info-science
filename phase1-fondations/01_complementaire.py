"""
Étape 1 — Le brin complémentaire

Règle d'appariement de l'ADN : A <-> T et C <-> G.
Chaque lettre est TOUJOURS remplacée par sa partenaire.
"""

PAIRES = {"A": "T", "T": "A", "C": "G", "G": "C"}


def complementaire(brin: str) -> str:
    """Retourne le brin d'ADN complémentaire."""
    # À toi de jouer : parcours chaque lettre du brin,
    # cherche sa partenaire dans PAIRES, et assemble le résultat.
    resultat = ""
    for lettre in brin:
        resultat = resultat + PAIRES[lettre]
        
    return resultat


if __name__ == "__main__":
    # Ces tests sont tes propres exercices de la leçon 1.
    # Ton programme doit trouver les mêmes réponses que toi.
    assert complementaire("ATGCCA") == "TACGGT"
    assert complementaire("GATTCA") == "CTAAGT"
    assert complementaire("TGCAATCG") == "ACGTTAGC"
    print("Tous les tests passent ! 🎉")
