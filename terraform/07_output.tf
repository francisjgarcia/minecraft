# Output server IPs
output "server_ip" {
    value = "${hcloud_server.minecraft.ipv4_address}"
}

# Output server URL
output "server_url" {
    value = "${var.ddns_hostname}"
}
