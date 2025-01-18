variable "project_name" {
  description = "Nombre del proyecto"
}

variable "environment" {
  description = "Ambiente"
}

variable "s3_bucket_arn" {
  description = "ARN del bucket S3"
}

variable "kinesis_arn" {
  description = "ARN del stream de Kinesis"
}
