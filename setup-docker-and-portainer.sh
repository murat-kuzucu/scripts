#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
NC='\033[0m'

# Update and install essential tools
echo -e "${GREEN}Updating the system and installing essential tools...${NC}"
sudo apt update -y && sudo apt upgrade -y
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common wget gnupg lsb-release

# Add Docker GPG key and repository
echo -e "${GREEN}Adding Docker GPG key and repository...${NC}"
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
echo -e "${GREEN}Installing Docker...${NC}"
sudo apt update -y
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Start and enable Docker service
sudo systemctl start docker
sudo systemctl enable docker
echo -e "${GREEN}Docker has been successfully installed and started.${NC}"

# Set permissions for Docker socket
echo -e "${GREEN}Setting permissions for the Docker socket...${NC}"
sudo chmod 777 /var/run/docker.sock

# Add user to the Docker group (recommended way for security)
echo -e "${GREEN}Adding the current user to the 'docker' group...${NC}"
sudo usermod -aG docker $USER

# Create Docker volume for Portainer
echo -e "${GREEN}Creating a Docker volume for Portainer...${NC}"
docker volume create portainer_data

# Install Portainer
echo -e "${GREEN}Installing Portainer...${NC}"
docker run -d \
  --name=portainer \
  --restart=always \
  -p 9000:9000 \
  -p 9443:9443 \
  -v /var/run/docker.sock:/var/run/docker.sock \
  -v portainer_data:/data \
  portainer/portainer-ce:latest

# Display success message with Portainer access details
echo -e "${GREEN}Portainer has been successfully installed. Access it using the following URL:${NC}"
echo -e "${GREEN}http://<your_server_ip>:9000${NC}"

# Cleanup unused packages
echo -e "${GREEN}Cleaning up unnecessary packages...${NC}"
sudo apt autoremove -y && sudo apt autoclean -y

echo -e "${GREEN}Setup complete! Docker and Portainer are ready to use.${NC}"
echo -e "${GREEN}Note: You may need to log out and back in for Docker group permissions to take effect.${NC}"
