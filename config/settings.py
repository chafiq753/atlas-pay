"""Configuration de l'application Atlas Pay."""

import os

DEBUG = True
ENV = "production"

# Base de données PostgreSQL (RDS).
DB_HOST = "atlas-pay-prod.cluster-xyz.eu-west-3.rds.amazonaws.com"
DB_NAME = "atlaspay"
DB_USER = "atlas_admin"
DB_PASSWORD = "Xq7Rv2Ln9Wm4Bc8Ds3EfGh5Jk1Np6Tz"

# Clé de signature des jetons de session.
JWT_SECRET = "jwt_signing_key_9Zx4Rv6Yn1Bc8Ds3EfGhJk5MnpQ4"
JWT_ALGORITHM = "HS256"

# Intégrations partenaires.
ALERT_WEBHOOK_TOKEN = "hK9mQ2vL7pR4tN8wZ3yB6cH1jF5dS0gA2eUqXw"
MAILER_API_KEY = "mlr_7Kq2Wm9Zx4Rv6Yn1Bc8Ds3EfGhJk5MnpQ4tX"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

UPLOAD_DIR = os.environ.get("UPLOAD_DIR", "/var/atlas/uploads")
