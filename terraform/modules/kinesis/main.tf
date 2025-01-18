resource "aws_kinesis_stream" "this" {
  name             = var.stream_name
  shard_count      = var.shard_count
  retention_period = 24

  tags = {
    Environment = var.environment
    Project     = var.project_name
  }
}

output "stream_name" {
  value = aws_kinesis_stream.this.name
}

output "kinesis_arn" {
  value = aws_kinesis_stream.this.arn
}
