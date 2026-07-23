# Stockage des justificatifs et relevés marchands.

resource "aws_s3_bucket" "documents_marchands" {
  bucket = "atlas-pay-documents-marchands"
}

resource "aws_s3_bucket_acl" "documents_marchands" {
  bucket = aws_s3_bucket.documents_marchands.id
  acl    = "public-read"
}

resource "aws_s3_bucket" "sauvegardes" {
  bucket = "atlas-pay-sauvegardes"
}

resource "aws_s3_bucket_policy" "sauvegardes" {
  bucket = aws_s3_bucket.sauvegardes.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect    = "Allow"
      Principal = "*"
      Action    = "s3:*"
      Resource  = "${aws_s3_bucket.sauvegardes.arn}/*"
    }]
  })
}
