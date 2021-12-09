# Change public IP address on DDNS
data "http" "dynudns" {
    url = "https://api.dynu.com/nic/update?hostname=${var.ddns_hostname}&myip=${hcloud_server.minecraft.ipv4_address}&username=${var.ddns_username}&password=${var.ddns_password}"
}
