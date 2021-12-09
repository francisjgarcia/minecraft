# Get public IP
data "http" "myip" {
    url = "http://ipv4.icanhazip.com"
}

# Create firewall rules
resource "hcloud_firewall" "firewall" {
    name = "server-firewall"
    # SSH
    rule {
        direction = "in"
        protocol  = "tcp"
        port      = "22"
        source_ips = [
            "${chomp(data.http.myip.body)}/32"
        ]
    }
    # Web server
    rule {
        direction = "in"
        protocol  = "tcp"
        port      = "80"
        source_ips = [
            "0.0.0.0/0",
            "::/0"
        ]
    }
    # Minecraft server
    rule {
        direction = "in"
        protocol  = "tcp"
        port      = "25565"
        source_ips = [
            "0.0.0.0/0",
            "::/0"
        ]
    }
    rule {
        direction = "in"
        protocol  = "udp"
        port      = "25565"
        source_ips = [
            "0.0.0.0/0",
            "::/0"
        ]
    }
}
