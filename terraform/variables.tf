# Hetzner Cloud API Token
variable "hcloud_token" {
  description = "Hetzner Cloud API Token"
  type        = string
}

# Cloudflare API Token
variable "cloudflare_token" {
  description = "Cloudflare API Token"
  type        = string
}

# Cloudflare Zone ID
variable "cloudflare_zone_id" {
  description = "Cloudflare zone ID"
  type        = string
}

# Cloudflare domain
variable "domain" {
  description = "Domain for the DNS"
  type        = string
}

# Cloudflare subdomain
variable "subdomain" {
  description = "Subdomain for the DNS"
  type        = string
}

# Hostname for the instance
variable "hostname" {
  description = "Hostname for the instance"
  type        = string
}

# Instance location
variable "location" {
  description = "Server location"
  type        = string
}

# Instance type
variable "server_type" {
  description = "Hetzner server type"
  type        = string
}

# Instance OS
variable "os_type" {
  description = "Hetzner OS server type"
  default     = "debian-11"
  type        = string
}

# Network zone for the firewall
variable "network_zone" {
  description = "Hetzner cloud network zone"
  default     = "eu-central"
  type        = string
}

# IP range for the firewall
variable "ip_range" {
  description = "IP range for the firewall"
  default     = "10.0.1.0/24"
  type        = string
}

# IP for the instance
variable "ip_server" {
  description = "IP range for the instance"
  default     = "10.0.1.2"
  type        = string
}
