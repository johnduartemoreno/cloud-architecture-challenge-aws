output "s3_bucket_name" {
  description = "Nombre del bucket S3"
  value       = module.s3_bucket.bucket_name
}

output "kinesis_stream_name" {
  description = "Nombre del stream de Kinesis"
  value       = module.kinesis_stream.stream_name
}

output "iam_role_arn" {
  description = "ARN del rol IAM"
  value       = module.iam_role.role_arn
}
