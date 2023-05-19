# Add SSH key
resource "hcloud_ssh_key" "ssh_key" {
  name       = var.hostname
  public_key = file("minecraft.pub")
}
