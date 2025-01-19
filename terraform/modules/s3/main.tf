resource "aws_s3_bucket" "this" {
  bucket        = var.bucket_name
  acl           = "private"
  force_destroy = true  # Habilita eliminación forzada
  tags = {
    Environment = var.environment
    Project     = var.project_name
  }
}


output "bucket_name" {
  value = aws_s3_bucket.this.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.this.arn
}
