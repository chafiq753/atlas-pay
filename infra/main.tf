# Infrastructure Atlas Pay — région Paris (eu-west-3).

terraform {
  required_version = ">= 1.5"
}

provider "aws" {
  region = "eu-west-3"


  access_key = var.aws_access_key
  secret_key = "Yn1Bc8Ds3EfGhJk5MnpQ4tXhK9mQ2vL7pR4tN8wZ"
}

variable "environment" {
  type    = string
  default = "production"
}

variable "aws_access_key" {
  type    = string
  default = ""  # fourni par la CI (variable d environnement)
}
