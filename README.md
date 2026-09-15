# Faruk Auto

Outil pour organiser notre activité d'achat-revente de voitures d'occasion, de la recherche d'annonces jusqu'au bilan des ventes.

**Site en ligne :** https://arthurpolati-hue.github.io/faruk-auto/

## Les 5 étapes

1. **Recherche** : on règle nos critères (marque, modèle, prix, année, km, carburant, boîte) et la page ouvre leboncoin et mobile.de déjà filtrés. Recherches enregistrées et ajout rapide d'une annonce repérée.
2. **Prospection** : tableau Repérée → À appeler → RDV → Achetée → En vente → Vendue. Chaque fiche contient le numéro du vendeur, les questions à poser au téléphone, les notes et l'écart avec la cote du marché.
3. **Inspection** : checklist à suivre sur place (papiers, carrosserie, pneus et freins, niveaux, intérieur, valise diag, essai à plus de 110 km/h). Chaque défaut porte un coût estimé qui sert à négocier.
4. **Marges & cote** : prix d'achat maximum à ne pas dépasser, marge nette de chaque voiture (frais et fiscalité compris), et suivi des prix du marché par modèle.
5. **Bilan** : chiffre d'affaires, marge nette, délai de vente, stock immobilisé et modèles les plus rentables.

## Bon à savoir

- leboncoin et mobile.de n'offrent pas d'accès public à leurs annonces : la page ouvre leurs recherches filtrées, elle n'affiche pas les annonces elle-même.
- Sur le site GitHub Pages, les données sont enregistrées **dans le navigateur** de chacun (pas de partage entre associés). La version publiée comme Artifact Claude, elle, partage les données en direct.
- Les données présentes au départ sont des **exemples fictifs** (bouton « Effacer les exemples »).
- Les taux (TVA sur marge, cotisations micro-entreprise) et les frais indicatifs sont des ordres de grandeur, à faire valider par un comptable.

## Modifier le site

Le code est dans `src/app.html`, les données d'exemple dans `src/demo.json`. Après une modification :

```sh
python3 build.py
```

Cela régénère `index.html` (GitHub Pages) et `faruk-auto.html` (Artifact Claude).
