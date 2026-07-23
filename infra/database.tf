# Base de données des transactions.

resource "aws_db_instance" "transactions" {
  identifier        = "atlas-pay-prod"
  engine            = "postgres"
  engine_version    = "15.4"
  instance_class    = "db.t3.medium"
  allocated_storage = 100

  db_name  = "atlaspay"
  username = "atlas_admin"
  password = "Atl@sP@y2024Prod!"

  storage_encrypted       = false
  publicly_accessible     = true
  backup_retention_period = 0
  deletion_protection     = false
  skip_final_snapshot     = true
}
