# How to create a Ubuntu Virtual Machine (DigitalOcean)

1. After creating a DigitalOcean account, create a droplet with the distribution Ubuntu, choosing any plan you want
2. Add an SSH key (recommended), or a password for your VM
3. SSH into your VM through your own terminal or the DigitalOcean website
4. Update by running ``` $ apt update && apt upgrade ```
5. Install Apache2 by running ```$ apt install apache2```
6. Allow Apache through the firewall ```$ ufw allow in "Apache"``` 
7. Activate your firewall using ```$ ufw enable``` and ```$ ufw status``` to check if your firewall is enabled and Apache is allowed through it

## Adding a user account

1. While you are in the root directory, add a user using ```$ useradd username```
2. Add the user to the sudo group using ``` $ usermod -aG sudo username ```
