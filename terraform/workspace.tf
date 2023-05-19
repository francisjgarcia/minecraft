# Terraform workspace configuration
terraform {
  cloud {
    workspaces {
      tags = ["minecraft"]
    }
  }
}
