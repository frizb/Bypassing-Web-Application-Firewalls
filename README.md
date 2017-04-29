# Bypassing-Web-Application-Firewalls
A series of python scripts for generating weird character combinations for bypassing web application firewalls (WAF).
These python scripts have been created to fuzz wierd combinations:

 * URL Escape Characters 
 * HTML Escape Characters
 * Binary Characters

These scripts were created during an assessment, while trying to bypass a Web Application Firewall (WAF) in order to exploit a XSS vulnerability.
When I tried to send a > or < character the WAF would block the request.
