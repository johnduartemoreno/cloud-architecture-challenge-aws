resource "aws_dynamodb_table" "this" {
  name           = "${var.project_name}-processed-data"
  billing_mode   = "PAY_PER_REQUEST"
  hash_key       = "record_id"

  attribute {
    name = "record_id"
    type = "S"
  }

  tags = {
    Environment = var.environment
    Project     = var.project_name
  }
}
