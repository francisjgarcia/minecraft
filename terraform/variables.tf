variable "hcloud_token" {
    description = "Hetzner Cloud API Token"
    type = string
}

variable "location" {
    description = "Server location. Choose between nbg1, fsn1 or hel1"
    default = "nbg1"
    type = string
}

variable "server_type" {
    description = "Hetzner server type"
    default = "cpx21"
    type = string
}

variable "os_type" {
    description = "Hetzner OS server type"
    default = "debian-11"
    type = string
}

variable "minecraft_port" {
    description = "Minecraft external server port"
    default = "25565"
    type = string
}

variable "ip_range" {
    description = "IP range for the firewall"
    default = "10.0.1.0/24"
    type = string
}

variable "ip_server" {
    description = "IP range for the instance"
    default = "10.0.1.2"
    type = string
}

variable "hostname" {
    description = "Hostname for the instance"
    default = "minecraft"
    type = string
}

variable "agent" {
    description = "If you want to use the SSH agent"
    default = false
}

variable "ssh_private_key" {
    description = "Private Key to access the server"
    default = "~/.ssh/minecraft.pk"
}

variable "ssh_public_key" {
    description = "Public Key to authorized the access for the server"
    default = "~/.ssh/minecraft.pub"
}

variable "ddns_username" {
    description = "DDNS username"
    type = string
}

variable "ddns_password" {
    description = "DDNS password"
    type = string
}

variable "ddns_hostname" {
    description = "FQDN for the instance"
    default = "example.minecraft.com"
    type = string
}