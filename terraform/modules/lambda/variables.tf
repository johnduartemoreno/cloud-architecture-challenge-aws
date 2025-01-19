variable "project_name" {
  description = "Project name"
  type        = string
}

variable "environment" {
  description = "Environment"
  type        = string
}

variable "region" {
  description = "AWS Region"
  type        = string
}

variable "s3_bucket_name" {
  description = "S3 bucket name for storing processed data"
  type        = string
}

variable "kinesis_stream_arn" {
  description = "Kinesis stream ARN for event source"
  type        = string
}

variable "iam_role_arn" {
  description = "IAM role ARN for Lambda functions"
  type        = string
}
