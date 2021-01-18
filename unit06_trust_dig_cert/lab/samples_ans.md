![esecurity](https://raw.githubusercontent.com/billbuchanan/esecurity/master/z_associated/esecurity_graphics.jpg)

# Lab 6: Trust and Digital Certificates


## A	Introduction

### A.1	

Serial Number: 702958

Effective date: 4/24/2008 9:18:42 PM

Name:  Fred Smith

Issuer: Self signed

What is CN used for: Common Name

What is OU used for: Organisational Unit

What is O used for: Organisational

What is L used for: Location


### A.3	
<pre>
$ openssl s_client -connect www.live.com:443
CONNECTED(00000005)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
verify return:1
depth=1 C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1
verify return:1
depth=0 C = US, ST = Washington, L = Redmond, O = Microsoft Corporation, CN = outlook.com
verify return:1
---
Certificate chain
 0 s:C = US, ST = Washington, L = Redmond, O = Microsoft Corporation, CN = outlook.com
   i:C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1
 1 s:C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1
   i:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIHzjCCBragAwIBAgIQCoH8ucQ1FhbxdOc4Y7FvoTANBgkqhkiG9w0BAQsFADBL
MQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMSUwIwYDVQQDExxE
aWdpQ2VydCBDbG91ZCBTZXJ2aWNlcyBDQS0xMB4XDTE5MTIyNDAwMDAwMFoXDTIx
MTIyNDEyMDAwMFowajELMAkGA1UEBhMCVVMxEzARBgNVBAgTCldhc2hpbmd0b24x
EDAOBgNVBAcTB1JlZG1vbmQxHjAcBgNVBAoTFU1pY3Jvc29mdCBDb3Jwb3JhdGlv
bjEUMBIGA1UEAxMLb3V0bG9vay5jb20wggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAw
ggEKAoIBAQDLFi2juwqukpMR/dNzYseJ2nU9LPCnrpyYbnFxRxf8m3L8Z+n3XREd
LmTZ0lIK2V2sgJnR+16PvnTeuLlT0XVnaDWsE2/6bR6T3zCI9HlmB5mYgBAKrLq6
yB1yZlf+DqaGFZUVRu1rgAt4DTZvc4liwve3n04Cm7/XZAluv223SGMc6sdRi8cq
IHaPTZsJW2GQeFkvIjb7/Cz6IzwVS7bj62cWRYQeq08Nl3hEOgOPwbWDLmLj7hDe
UbPzdZuh2Mo2PhF1CbZXz2IGRMcsgou6+Tu2s/MhexemAwKwqQntoE5rEdPc2GcC
...
kdLxzsCguY8dsdvU+iKBqqTGrF0+aq++Yu+wSgj8wLUa3jUPJ1/Cd4k/kAKQCCL5
LvT0BheI4kzyqQW/QykMpTRbpctzLgA0IZctBRXj4xsI1aUYj1ZoaKy/XFMO0lGK
Ta7iKyY7UwpRxq2+i4DBGcgnN4mFXif6qMC6LVS2H43fPQ==
-----END CERTIFICATE-----
subject=C = US, ST = Washington, L = Redmond, O = Microsoft Corporation, CN = outlook.com

issuer=C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1

---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: RSA
Server Temp Key: ECDH, P-384, 384 bits
---
SSL handshake has read 3978 bytes and written 472 bytes
Verification: OK
---
New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
Server public key is 2048 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-RSA-AES256-GCM-SHA384
    Session-ID: 752A8406875DA02E17A539E7676182F6EBDC880FE5DA95BE0531B733E6EB054B
    Session-ID-ctx: 
    Master-Key: 4E1B4A0FB630888BA14231377A314568F7B9BABBF5298E79E09561B904DC739DF52F2B1288A78F5DCAEFABFF73D23A3D
    PSK identity: None
    PSK identity hint: None
    SRP username: None
    TLS session ticket lifetime hint: 36000 (seconds)
 ...
    </pre>
    
Can you identity the certificate chain?
<pre>
Certificate chain
 0 s:C = US, ST = Washington, L = Redmond, O = Microsoft Corporation, CN = outlook.com
   i:C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1
 1 s:C = US, O = DigiCert Inc, CN = DigiCert Cloud Services CA-1
   i:C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
   </pre>

What is the subject on the certificate?
<pre>
outlook.com
</pre>

Who is the issuer on the certificate?
<pre>
DigiCert Cloud Services CA-1
</pre>



