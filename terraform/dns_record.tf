# Create a DNS record for the Minecraft server
resource "cloudflare_record" "dns_record" {
  zone_id = var.cloudflare_zone_id
  name    = "${var.subdomain}.${var.domain}"
  value   = hcloud_server.instance.ipv4_address
  type    = "A"
}
