resource "aws_lambda_function" "kinesis_processor" { 
  function_name = "${var.project_name}-kinesis-processor"
  runtime       = "python3.9"
  role          = var.iam_role_arn
  handler       = "kinesis_lambda.lambda_handler"

  environment {
    variables = {
      BUCKET_NAME = var.s3_bucket_name
    }
  }

  filename         = "${path.module}/kinesis_lambda.zip"
  source_code_hash = filebase64sha256("${path.module}/kinesis_lambda.zip")
  
}

resource "aws_lambda_event_source_mapping" "kinesis_to_lambda" {
  event_source_arn = var.kinesis_stream_arn
  function_name    = aws_lambda_function.kinesis_processor.arn
  starting_position = "TRIM_HORIZON"
}

resource "aws_lambda_function" "summary_lambda" {
  function_name    = "${var.project_name}-lambda-summary"
  runtime          = "python3.9"
  role             = var.iam_role_arn
  handler          = "lambda_summary.lambda_handler"
  filename         = "${path.module}/lambda_summary.zip"
  source_code_hash = filebase64sha256("${path.module}/lambda_summary.zip")

  timeout          = 30  # Aumentar el tiempo de ejecución para evitar timeout
  memory_size      = 512 # Aumentar memoria para mejorar rendimiento

  environment {
    variables = {
      DYNAMODB_TABLE = "${var.project_name}-processed-data"
    }
  }
}
