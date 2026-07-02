# Atlas Pay

Plateforme de paiement en ligne pour marchands marocains.
API REST (Flask) + infrastructure AWS gérée par Terraform.

> ⚠️ **Projet de démonstration.** Ce dépôt sert de cible de scan à iac-guard :
> il contient volontairement des vulnérabilités et des secrets factices.
> Ne pas déployer, ne pas exécuter.

## Architecture

| Dossier | Rôle |
|---|---|
| `src/` | API Flask : authentification, paiements, accès base |
| `config/` | Configuration de l'application |
| `infra/` | Infrastructure AWS (Terraform) |
| `tests/` | Tests unitaires |

## Développement

```bash
pip install -r requirements.txt
python -m src.app
```

## Branches

- `main` — production
- `develop` — intégration
- `feature/*` — développements en cours

## Sécurité

Chaque push et chaque pull request déclenche un scan iac-guard
(Gitleaks, Checkov, Semgrep). Une fusion vers `main` est refusée si un
problème de gravité `high` ou supérieure est détecté.
