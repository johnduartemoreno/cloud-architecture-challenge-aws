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

output "dynamo_table_name" {
  description = "Dynamo Table Name"
  value       = module.dynamo.table_name
}

output "lambda_kinesis_processor_name" {
  description = "Lambda function name for Kinesis processing"
  value       = module.lambda.kinesis_processor_name
}

output "lambda_summary_name" {
  description = "Lambda function name for data summary"
  value       = module.lambda.summary_lambda_name
}

output "lambda_summary_arn" {
  description = "ARN of the summary Lambda function"
  value       = module.lambda.summary_lambda_arn
}

output "lambda_kinesis_processor_arn" {
  description = "ARN of the Kinesis processor Lambda function"
  value       = module.lambda.kinesis_processor_arn
}
