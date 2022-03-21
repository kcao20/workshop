# How to create a Ubuntu Virtual Machine (DigitalOcean)

1. After creating a DigitalOcean account, create a droplet with the distribution Ubuntu, choosing any plan you want
2. Add a SSH key (recommended), or a password for your VM
3. SSH into your VM through your own terminal or the DigitalOcean website
4. Update by running ``` $ apt update && apt upgrade ```

## Adding a user account

1. While you are in the root directory, add a user using ```$ adduser username```
2. Add the user to the sudo group using ``` $ usermod -aG sudo username ```
3. If you used a SSH key for root, password authentication is probably disabled for SSH so copy your local public key to the new user’s ~/.ssh/authorized_keys file to log in successfully using ```rsync --archive --chown=username:username ~/.ssh /home/username```
4. From now, everything should be done on the user account you created

## Disabling SSH through root (make sure you can ssh through your user first)
1. Open the /etc/ssh/sshd_config file in your preferred text editor e.g. ```sudo nano /etc/ssh/sshd_config```
2. Change ```PermitRootLogin yes``` to ```PermitRootLogin no```
3. Apply your changes by doing ```sudo service ssh restart```

## Installing Apache
1. Install Apache2 by running ```$ sudo apt install apache2```

## Firewall
1. Allow SSH through the firewall ```$ sudo ufw allow OpenSSH``` (make sure to do this correctly otherwise you won't ge able to regain access to your terminal)
2. Allow Apache through the firewall ```$ sudo ufw allow in "Apache"``` 
3. Activate your firewall using ```$ sudo ufw enable``` and ```$ sudo ufw status``` to check if your firewall is enabled and both OpenSSH and Apache is allowed through it
