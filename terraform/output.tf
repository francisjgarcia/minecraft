# Output server IPs
output "server_ip" {
  value = hcloud_server.instance.ipv4_address
}

# Output server URL
output "server_url" {
  value = "${var.subdomain}.${var.domain}"
}
