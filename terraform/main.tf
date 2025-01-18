# Proveedor de AWS
provider "aws" {
  region = var.region
}

# Módulo para el S3 Bucket
module "s3_bucket" {
  source      = "./modules/s3"
  bucket_name = "${var.project_name}-data-bucket"
  environment = var.environment
  project_name = var.project_name
}

# Módulo para el Kinesis Stream
module "kinesis_stream" {
  source      = "./modules/kinesis"
  stream_name = "${var.project_name}-data-stream"
  environment = var.environment
  shard_count = 1
  project_name = var.project_name
}

# Módulo para IAM Role
module "iam_role" {
  source          = "./modules/iam"
  project_name    = var.project_name
  environment     = var.environment
  kinesis_arn     = module.kinesis_stream.kinesis_arn
  s3_bucket_arn   = module.s3_bucket.bucket_arn
}
