# certificate_exp_date_checker
Certificate Expiry Date Checker Script

The purpose of this script is to check and display the expiration date of the SSL/TLS certificate for the input hostname.

## Prerequisites:

* Python 3.12.5
* OpenSSL 3.0.13

>How to install(Mac):
>```sh
>pip3 install pyOpenSSL
>```

## How to run script(Mac):

```txt
python3 certificate_expiraty_date_checker.py
```

## Input
Target hostname - Script will ask you to enter desired hostname to get SSL/TLS certificate expiration date from

## Example Input:
```sh
Enter hostname: bbc.com
```
## Example Output for valid SSL/TLS certificate expiration date:
```sh
The SSL certificate for bbc.com expires on 2025-07-19 06:26:04.
Remaining days: 338
```