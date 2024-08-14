import ssl
import socket
import sys
import OpenSSL
from datetime import datetime

# Retrieve SSL certificate public key
def get_SSL_Certificate(host):
    try:
        certificate = ssl.get_server_certificate((host, 443),timeout=30)
    except Exception as e:
        print(f"SSL certificate could not be obtained from {host}, the error is: {str(e)}")
        sys.exit(1)
    else:
        return certificate

# Decrypt the SSL certificate public key
def load_certificate(certificate):
    try:
        certificate = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)
    except Exception as e:
        print(f"Error in loading certificate. Error: {str(e)} ")
        sys.exit(1)
    else:
        return certificate

#Get SSL certificate expiry date
def get_expiry_date(certificate):
    try:
        expiry_date_str = str(certificate.get_notAfter().decode("ascii"))
    except Exception as e:
        print(f"Error in decoding certificate expiry date. Error {str(e)}")
        sys.exit(1)
    else:
        expiry_date_str = str(certificate.get_notAfter().decode("ascii"))
        expiry_date = datetime.strptime(expiry_date_str, "%Y%m%d%H%M%SZ")
        return expiry_date

#Check SSL certificate validity
def check_certificate_expiry(host):
    certificate = get_SSL_Certificate(host)
    loaded_certificate = load_certificate(certificate)
    expiry_date = get_expiry_date(loaded_certificate)
    current_date = datetime.now()
    remaining_days = (expiry_date - current_date).days
    
    if remaining_days > 0:
        print(f"The SSL certificate for {hostname} expires on {expiry_date}.")
        print(f"Remaining days: {remaining_days}")
    else:
        print(f"The SSL certificate for {hostname} has expired!")
        print(f"Expired on: {expiry_date}")

#Script entry point        
if __name__ == "__main__":
    hostname = input("Enter hostname: ")
    check_certificate_expiry(hostname)