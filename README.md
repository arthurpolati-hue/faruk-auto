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
- Le site se connecte à **Firebase** : chaque associé se connecte avec son e-mail et son mot de passe, et les données sont partagées en direct. Tant que `firebase-config.js` n'est pas rempli, les données restent dans le navigateur.
- Les données présentes au départ sont des **exemples fictifs** (bouton « Effacer les exemples »).
- Les taux (TVA sur marge, cotisations micro-entreprise) et les frais indicatifs sont des ordres de grandeur, à faire valider par un comptable.

## Brancher Firebase (une seule fois)

1. Sur https://console.firebase.google.com : **Créer un projet**.
2. **Authentication** > Méthode de connexion : activer **E-mail/Mot de passe**, puis onglet **Utilisateurs** > « Ajouter un utilisateur » pour créer un identifiant par associé.
3. **Firestore Database** > Créer une base (région `eur3` Europe, mode production).
4. **Firestore Database** > Règles : coller `firestore.rules` en remplaçant les `COLLER_UID_...` par les identifiants des associés (Authentication > Utilisateurs, colonne « Identifiant utilisateur »), puis **Publier**.
5. Roue dentée > **Paramètres du projet** > section « Vos applications » > icône Web `</>` : enregistrer l'application, puis copier l'objet `firebaseConfig` affiché dans `firebase-config.js` et pousser sur GitHub.

Pour ajouter un associé plus tard : lui créer un utilisateur dans Authentication, puis ajouter son UID dans les règles Firestore et republier.

## Modifier le site

Le code est dans `src/app.html`, les données d'exemple dans `src/demo.json`. Après une modification :

```sh
python3 build.py
```

Cela régénère `index.html` (GitHub Pages) et `faruk-auto.html` (Artifact Claude).
