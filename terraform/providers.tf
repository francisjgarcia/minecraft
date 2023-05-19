terraform {
  required_providers {
    # Hetzner Cloud provider
    hcloud = {
      source  = "hetznercloud/hcloud"
      version = "~> 1.38.2"
    }
    # Cloudflare provider
    cloudflare = {
      source  = "cloudflare/cloudflare"
      version = "~> 4.5.0"
    }
  }
}

# Hetzner Cloud token for API access
provider "hcloud" {
  token = var.hcloud_token
}

# Cloudflare token for API access
provider "cloudflare" {
  api_token = var.cloudflare_token
}
