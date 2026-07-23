# Droits du pipeline de déploiement.

resource "aws_iam_policy" "deploiement" {
  name        = "atlas-pay-deploiement"
  description = "Politique utilisee par la CI/CD"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "*"
      Resource = "*"
    }]
  })
}

resource "aws_cloudtrail" "audit" {
  name                          = "atlas-pay-audit"
  s3_bucket_name                = aws_s3_bucket.sauvegardes.id
  enable_log_file_validation    = false
  include_global_service_events = false
}
