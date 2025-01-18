resource "aws_lambda_function" "kinesis_processor" {
  function_name = "${var.project_name}-kinesis-processor"
  runtime       = "python3.9"
  role          = aws_iam_role.this.arn
  handler       = "kinesis_lambda.lambda_handler"

  environment {
    variables = {
      BUCKET_NAME = var.s3_bucket_name
    }
  }

  filename         = "${path.module}/kinesis_lambda.zip"
  source_code_hash = filebase64sha256("${path.module}/kinesis_lambda.zip")

  depends_on = [aws_iam_role.this]
}

resource "aws_lambda_event_source_mapping" "kinesis_to_lambda" {
  event_source_arn = var.kinesis_stream_arn
  function_name    = aws_lambda_function.kinesis_processor.arn
  starting_position = "TRIM_HORIZON"
}
