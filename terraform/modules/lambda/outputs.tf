output "kinesis_processor_name" {
  description = "Name of the Kinesis processor Lambda function"
  value       = aws_lambda_function.kinesis_processor.function_name
}

output "summary_lambda_name" {
  description = "Name of the summary Lambda function"
  value       = aws_lambda_function.summary_lambda.function_name
}

output "kinesis_processor_arn" {
  description = "ARN of the Kinesis processor Lambda function"
  value       = aws_lambda_function.kinesis_processor.arn
}

output "summary_lambda_arn" {
  description = "ARN of the summary Lambda function"
  value       = aws_lambda_function.summary_lambda.arn
}
