# Create network
resource "hcloud_network" "network" {
  name     = "${var.hostname}-network"
  ip_range = var.ip_range
}

# Create subnet
resource "hcloud_network_subnet" "network_subnet" {
  network_id   = hcloud_network.network.id
  type         = "cloud"
  network_zone = var.network_zone
  ip_range     = var.ip_range
}

# Associate subnet with server and add private IP
resource "hcloud_server_network" "network_server" {
  server_id  = hcloud_server.instance.id
  network_id = hcloud_network.network.id
  ip         = var.ip_server
}
