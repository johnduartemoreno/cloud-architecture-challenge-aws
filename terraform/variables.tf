variable "region" {
  description = "Región donde se despliega la infraestructura"
  default     = "us-east-1"
}

variable "project_name" {
  description = "cloud-architecture-challenge-aws"
  default     = "aws-data-ingestion"
}

variable "environment" {
  description = "Ambiente (development, staging, production)"
  default     = "development"
}
