# Zabbix-web Debug

php-fpm access_log **???**

[Nginx Php-fpm not logging 500 error anywhere](https://stackoverflow.com/questions/27452528/nginx-php-fpm-not-logging-500-error-anywhere)

[php-fpm выдает ошибку 500 в браузер](https://ru.stackoverflow.com/questions/785468/php-fpm-%D0%B2%D1%8B%D0%B4%D0%B0%D0%B5%D1%82-%D0%BE%D1%88%D0%B8%D0%B1%D0%BA%D1%83-500-%D0%B2-%D0%B1%D1%80%D0%B0%D1%83%D0%B7%D0%B5%D1%80)

Если в php скрипте есть ошибка, то сервер отдает только ошибку 500, без подробностей.

Для вывода ошибок надо в файле php.ini выставить значения следующим параметрам:
```
display_errors = On
display_startup_errors = On
error_reporting = E_ALL & ~E_DEPRECATED & ~E_STRICT
```

[zabbix gui themes don't work](https://www.google.com/search?q=zabbix+gui+themes+don%27t+work&oq=zabbix+gui+themes+dond&gs_lcrp=EgZjaHJvbWUqCQgBECEYChigATIGCAAQRRg5MgkIARAhGAoYoAEyCQgCECEYChigATIHCAMQIRiPAjIHCAQQIRiPAjIHCAUQIRiPAtIBCTI5MDUwajBqN6gCCLACAfEFU7SzkIrsEqfxBVO0s5CK7BKn&sourceid=chrome&ie=UTF-8)

If you're experiencing issues with Zabbix GUI themes not working, it's likely due to file permissions or incorrect theme definitions within the Zabbix configuration files. To resolve this, ensure that the web server user owns the frontend files (excluding the conf directory) and that the theme definitions in ZBase.php are correctly set up. 
Here's a more detailed breakdown of potential issues and solutions:

1. File Permissions:
   Problem:
   The web server user (e.g., apache or nginx) needs proper access to the Zabbix frontend files. If the files are owned by the wrong user, the browser won't be able to load the necessary CSS and images for the themes.
   Solution:
   Identify the web server user (e.g., apache, nginx, www-data).
   Change the ownership of the Zabbix frontend files to the web server user.
   Ensure that the conf directory within the frontend is owned by the Zabbix user/group.
   Example: 
   Код
```bash
   chown -R apache:apache /usr/share/zabbix/
   chown zabbix:zabbix /usr/share/zabbix/conf
```
(Replace apache:apache with your web server user and group if different). 

2. Theme Definitions:
   Problem:
   The getThemes() function in ZBase.php (or the corresponding file for your Zabbix version) might not be correctly defining the available themes.
   Solution:
   Locate the ZBase.php file (or similar) in your Zabbix frontend directory.
   Examine the getThemes() function and ensure it includes the desired themes, including any custom themes you've created.
   If necessary, modify the function to correctly point to the theme directories and files. 

3. Other Potential Issues:
   Incorrect DOCTYPE declaration:
   In some cases, an incorrect DOCTYPE declaration in page_header.php can cause rendering issues. You can try commenting out or removing line 117, which contains the DOCTYPE declaration. 

   Zabbix version compatibility:
   If you've recently upgraded Zabbix, some custom themes might not be compatible with the new version. Refer to the Zabbix documentation for any changes to the theming system or known issues with custom themes after upgrades. 

   Web server configuration:
   Double-check your web server configuration (e.g., Apache's VirtualHost or Nginx's server block) to ensure it's correctly serving the Zabbix frontend files. Pay attention to the Alias or location directives that point to the Zabbix frontend directory. 

Troubleshooting Steps:
1. Clear browser cache:
Sometimes, cached CSS or JavaScript files can cause display issues. Clear your browser's cache and try again.
2. Check server logs:
Examine the Zabbix server and web server logs for any errors related to the frontend or themes. This can provide clues about the root cause of the problem.
3. Consult Zabbix documentation:
Refer to the Zabbix documentation for detailed information on theming and any known issues.
4. Seek help from the Zabbix community:
If you're still stuck, post your issue on the Zabbix forums or other community resources, providing details about your Zabbix version, operating system, and any specific error messages you're seeing. 

## [~]
