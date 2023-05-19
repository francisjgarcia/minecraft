# Create instance
resource "hcloud_server" "instance" {
  location     = var.location
  server_type  = var.server_type
  image        = var.os_type
  name         = var.hostname
  ssh_keys     = [hcloud_ssh_key.ssh_key.id]
  firewall_ids = [hcloud_firewall.firewall.id]
}
