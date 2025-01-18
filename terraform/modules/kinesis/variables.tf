variable "stream_name" {
  description = "Nombre del stream de Kinesis"
}

variable "shard_count" {
  description = "Cantidad de shards"
  default     = 1
}

variable "environment" {
  description = "Ambiente"
}

variable "project_name" {
  description = "Nombre del proyecto"
}
