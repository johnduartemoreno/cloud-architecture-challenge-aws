resource "aws_iam_role" "this" {
  name               = "${var.project_name}-${var.environment}-role"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com", "kinesis.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy" "this" {
  name   = "${var.project_name}-${var.environment}-policy"
  role   = aws_iam_role.this.id
  policy = data.aws_iam_policy_document.access_policy.json
}

data "aws_iam_policy_document" "access_policy" {
  statement {
    actions   = ["s3:*"]
    resources = ["${var.s3_bucket_arn}/*"]
  }

  statement {
    actions   = ["kinesis:*"]
    resources = [var.kinesis_arn]
  }
}

output "role_arn" {
  value = aws_iam_role.this.arn
}
