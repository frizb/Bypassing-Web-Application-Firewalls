# Bypassing-Web-Application-Firewalls-And-XSS-Filters
A series of python scripts for generating weird character combinations and lists for BurpSuite Pro for bypassing web application firewalls (WAF) and XSS filters.
These python scripts have been created to fuzz wierd combinations:

 * URL Escape Characters 
 * HTML Escape Characters
 * Binary Characters

These scripts were created during an assessment, while trying to bypass a Web Application Firewall (WAF) in order to exploit a XSS vulnerability.
Differnt webservers and browsers interpret URL and strange characters differently which could lead to the bypassing of security controls.
When I tried to send a > or < character the WAF would block the request.

The following URL escapes I have noticed are traslated to < > ' by Apache2 based web servers:

%(N%(n%)S%)U%)^%)s%)u%*C%*E%*c%*e%,.%.#%1N%1n%2S%2U%2^%2s%2u%3C%3E%3c%3e%5.%7#%:C%:E
%:c%:e%HN%Hn%IS%IU%I^%Is%Iu%JC%JE%Jc%Je%L.%N#%XN%Xn%YS%YU%Y^%Ys%Yu%ZC%ZE%Zc%Ze%\.%^#
%hN%hn%iS%iU%i^%is%iu%jC%jE%jc%je%l.%n#%xN%xn%yS%yU%y^%ys%yu%zC%zE%zc%ze%|.

