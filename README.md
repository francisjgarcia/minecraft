# Minecraft

![Minecraft](https://repository-images.githubusercontent.com/643003222/a4797d8e-236e-4552-a2d7-ebc141097d5f)

## Table of contents
- [Minecraft](#minecraft)
  - [Table of contents](#table-of-contents)
  - [Description](#description)
  - [Requirements](#requirements)
- [Terraform Cloud](#terraform-cloud)
- [Hetzner Cloud](#hetzner-cloud)
- [SSH Keys](#ssh-keys)
- [Deploy infrastructure](#deploy-infrastructure)
  - [Terraform](#terraform)
  - [Ansible](#ansible)
  - [Docker](#docker)
- [Destroy infrastructure](#destroy-infrastructure)
- [Mods](#mods)
  - [Ansible](#ansible-1)
  - [Docker](#docker-1)
- [Github Actions](#github-actions)
  - [Secrets](#secrets)
  - [Environment variables](#environment-variables)
  - [Backup](#backup)

## Description

This repository contains the code to deploy a Minecraft server in Hetzner using Terraform, Ansible and Docker.

## Requirements
Before to deploy the infrastructure and provision the server, you must need the following resources:
- Terraform
- Ansible
- Docker (optional)
- Terraform Cloud
- Cloudfare
- Hetzner Cloud


# Terraform Cloud
To save the state of the deployment, you can use **[Terraform Cloud](https://app.terraform.io/)**. To do this, you must create an account and create an API token.

Next, you must export the following environment variables:

Export the token of your Terraform Cloud account:
```bash
export TF_TOKEN_app_terraform_io="<TERRAFORM-CLOUD-TOKEN>"
```

Before, you must create an organization in Terraform Cloud. Then, export the name of the organization:
```bash
export TF_CLOUD_ORGANIZATION="<TERRAFORM-CLOUD-ORGANIZATION>"
```

This is a workspace when you save the state of the deployment:
```bash
export TF_WORKSPACE="<TERRAFORM-CLOUD-WORKSPACE>"
```

# Hetzner Cloud
You need to create an account in **[Hetzner Cloud](https://www.hetzner.com/)**. Then, you must create a project and generate an API token.

Next, you must export the following environment variables to connect with the Hetzner Cloud API:

```bash
export TF_VAR_hcloud_token="<HETZNER-TOKEN>"
```

Also, you must export the following environment variables to configure the server, to choose the location and the server type you can see in **[Hetzner Cloud Prices](https://www.hetzner.com/cloud#pricing)**.

```bash	
export TF_VAR_hostname="<HOSTNAME>"
export TF_VAR_location="<LOCATION>"
export TF_VAR_server_type="<SERVER-TYPE>"
```	

# Cloudflare
You need to create an account in **[Cloudflare](https://www.cloudflare.com/)**. Then, you must have a domain and generate an API token with permissions to manage the DNS.

Next, you must export the following environment variables to connect with the Cloudfare API:

```bash
export TF_VAR_cloudflare_token="<CLOUDFLARE-TOKEN>"
export TF_VAR_cloudflare_zone_id="<CLOUDFLARE-ZONE-ID>"
```

Also, you must export the following environment variables to configure which domain and subdomain you want to use:

```bash
export TF_VAR_domain="<DOMAIN>"
export TF_VAR_subdomain="<SUBDOMAIN>"
```

# SSH Keys
You must create a public and private key to connect with the server. You can use the following command:

```bash
ssh-keygen -t rsa -b 4096 -C "Minecraft Server"
```

And next, you need evaluate the ssh-agent and add the private key:

```bash
eval $(ssh-agent)
ssh-add /path/to/private/key
```

If you want to deploy the terraform code in local, you must copy the public key in the path *terraform/minecraft.pub*

```bash
cp /path/to/public/key.pub terraform/minecraft.pub
```

# Deploy infrastructure

## Terraform
To deploy the infrastructure, also export the before environment variables, you must execute the following commands:

```bash
cd terraform
terraform init
```

To check the changes that you are going to deploy:

```bash
terraform plan
```

And finally, to deploy the infrastructure:

```bash
terraform apply
```

## Ansible
To provision the server, you must edit the file *ansible/variables.yml* and change the variables to adapt the server to your needs.

If you need know all options, you can see in the **[documentation](https://itzg.github.io/docker-minecraft-docs/)** of the image.

Next, to provisioning the server, you must execute the following commands:

```bash
ansible-playbook -u root -i '<SERVER-IP or DNS>,' ansible/playbooks/main.yml
```

## Docker
If you like deploy the server in local to test the server, you can use Docker, you can use Docker. To do this, you must execute the following commands:

Before to deploy the server, you must create a .env file copying the .env.example file and change the variables to adapt the server to your needs at same that you did in the file *ansible/variables.yml*.

```bash
cd docker
cp .env.example .env
```

Next, you must run the docker-compose command:

```bash
docker-compose up -d
```

# Destroy infrastructure
You must execute an ansible playbook to backup the server after destroy the infrastructure.

```bash
ansible-playbook -u root -i '<SERVER-IP or DNS>,' ansible/playbooks/backup.yml
```

Next, you can destroy the infrastructure:

```bash
cd terraform
terraform destroy
```

# Mods

## Ansible
If you want to install mods, you must configure previously the server type to using *forge* and next, you must edit the file *ansible/variables.yml* and add the download mods list in the variable *minecraft_mods* and changue the variable *enable_mods* to *true*.

Also if you like to install the voicechat mod, you must add it in the variable *minecraft_mods* and changue the variable *enable_voicechat* to *true*.

## Docker
To use mods in the local docker deployment, you must edit the file *docker/.env* and using a server type with *forge*. Next, you must run the docker-compose command and copy the mods that you want to install to the path *docker/data/mods*.

```bash
docker-compose up -d
cd docker/data/
cp /path/to/mods docker/data/mods
```

Next, you must restart the server:

```bash
docker-compose restart
```

# Github Actions

To automate the deployment, you can use **Github Actions**. You must *fork* this repository or using the repository template and create the following secrets and environment variables:

## Secrets

```bash
TERRAFORM_CLOUD_TOKEN="<TERRAFORM-CLOUD-TOKEN>" # Token of your Terraform Cloud account
HETZNER_TOKEN="<HETZNER-TOKEN>" # Token of your Hetzner Cloud account
CLOUDFLARE_TOKEN="<CLOUDFLARE-TOKEN>" # Token of your Cloudflare account
CLOUDFLARE_ZONE_ID="<CLOUDFLARE-ZONE-ID>" # Zone ID of your domain in Cloudflare
SSH_PRIVATE_KEY="<SSH-PRIVATE-KEY>" # Private key to connect with the server
SSH_PUBLIC_KEY="<SSH-PUBLIC-KEY>" # Public key to connect with the server
```
## Environment variables

```bash
TERRAFORM_CLOUD_ORGANIZATION="<TERRAFORM-CLOUD-ORGANIZATION>" # Organization name of your Terraform Cloud account
SERVER_LOCATION="<SERVER-LOCATION>" # Location of the Hetzner server
SERVER_TYPE="<SERVER-TYPE>" # Server type of the Hetzner server
HOSTNAME="<HOSTNAME>" # Hostname of the Hetzner server
DOMAIN="<DOMAIN>" # Domain created in Cloudflare
SUBDOMAIN="<SUBDOMAIN>" # Subdomain created in Cloudflare
```

## Backup
One of the github actions make a backup of the server every day at **03:00 UTC**. You can change the time in the file *.github/workflows/backup.yml*.

If you make public the repository, the storage of the backup is free and the backup content is save during **90 days** (by default, if you want to change it, configure the artifact and log retention in the settings of you repository), even you make public the repository, the backup content is **private**.

If you have forked the repository, you must enable the backup github action.
