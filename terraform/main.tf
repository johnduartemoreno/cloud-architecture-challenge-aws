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
  region         = var.region
  kinesis_arn     = module.kinesis_stream.kinesis_arn
  s3_bucket_arn   = module.s3_bucket.bucket_arn
}

# Módulo para Dynamo
module "dynamo" {
  source      = "./modules/dynamodb"
  table_name  = "${var.project_name}-audience-data"
  hash_key    = "record_id"
  environment = var.environment
  project_name = var.project_name
}

# Módulo para Lambda Functions
module "lambda" {
  source            = "./modules/lambda"
  project_name      = var.project_name
  environment       = var.environment
  region            = var.region
  s3_bucket_name    = module.s3_bucket.bucket_name
  kinesis_stream_arn = module.kinesis_stream.kinesis_arn
  iam_role_arn      = module.iam_role.role_arn
}

