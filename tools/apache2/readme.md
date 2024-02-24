# Apache2 Configuration for Public Project Website

This service is running to host our public project website using Apache2.

If you want to run this demonstration on your own server, follow these steps:
1. Create a New Site Configuration:

* Create a new site configuration file in the sites-enabled directory of Apache2.
* You can name it according to your domain name or project (sudo nano /etc/apache2/sites-enabled/apt_domain.conf).

2. Set Up Document Root:
* Create a new folder for your project website (e.g., /var/www/apt_domain) or choose a different path next to the default (/var/www/html).
* Make sure the ownership and permissions are set appropriately for the web server to access the files.

3. Edit Site Configuration:
* Open the newly created site configuration file (sudo nano /etc/apache2/sites-enabled/apt_domain.conf).
* Update the DocumentRoot directive to point to the directory where your project files are located.

**Here's an example of the configuration**

```
<VirtualHost *:80>
        ServerName our_apt_apache.com
        #ServerAlias www.our_apt_apache.com

        ServerAdmin kali@our_apache.com
        DocumentRoot /var/www/apt_domain

        ErrorLog ${APACHE_LOG_DIR}/error-my_domain.log
        CustomLog ${APACHE_LOG_DIR}/access-my_domain.log combined
</VirtualHost>
```

------

For further details, please refer to the following [link](https://www.youtube.com/watch?v=6Guk-lv7QJQ&fbclid=IwAR2QPBrfvFQ5lK42MFcDUv50GA9DtNt9a9RRoO9CdiBAO0EJwKyI1R7IqSM)