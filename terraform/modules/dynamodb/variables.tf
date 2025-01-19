variable "table_name" {
  description = "DynamoDB table name"
  type        = string
  default     = "aws-data-ingestion-table"
}

variable "hash_key" {
  description = "Primary Key"
  type        = string
}

variable "environment" {
  description = "Ambiente (development, staging, production)"
  type        = string
}

variable "project_name" {
  description = "Project identifier"
  type        = string
  default     = "aws-data-ingestion"
}
