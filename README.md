# Koji Tea – Gestion

Application de gestion de Koji Tea : caisse, stock et dates de validité, achats, carte et marges, manifestations, matériel, comptabilité.

- En ligne : https://gestion.koji-tea.ch
- Données : Firebase (Firestore), accès réservé aux comptes créés dans Firebase Authentication.
- Hors connexion : l'application et les données déjà chargées restent disponibles.

## Modifier l'application

Le code se trouve dans `source/`. Après une modification, reconstruire le site :

```
python3 source/build.py
```

La configuration Firebase est dans `firebase-config.js` (elle n'est pas secrète ; la sécurité vient des règles `source/standalone/firestore.rules`).
