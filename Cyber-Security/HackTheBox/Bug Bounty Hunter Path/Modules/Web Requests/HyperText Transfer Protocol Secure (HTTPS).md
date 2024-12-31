
---

#Web-Requests 
#HackTheBox 

---

[Contents Page](Web%20Requests%20(Module%20Overview).md)
[Previous Section](HyperText%20Transfer%20Protocol%20(HTTP).md)

One of the significant drawbacks of **HTTP** is that all the data transferred is in clear/plain text, making it readable to anyone who could be performing a **MiTM (Man in The Middle) attack** to view the transferred data.

![[mitm-attack-diagram.png]]
<sub>MiTM Diagram</sub>

As a way to counter this, **HTTPS** (HTTP Secure) was created, in which all communications are transferred in an encrypted formatted.

Examples of **HTTPS encryption formats** include:
- **TLS** (Transport Layer Security)
- **SSL** (Secure Sockets Layer)** _(deprecated, replaced by TLS)_
- **AES** (Advanced Encryption Standard)
- **RSA** (Rivest-Shamir-Adleman)
- **ECDSA** (Elliptic Curve Digital Signature Algorithm)
- **ECDHE** (Elliptic Curve Diffie-Hellman Ephemeral)
- **ChaCha20**
- **SHA-256** (Secure Hash Algorithm 256-bit)
- **HMAC** (Hash-based Message Authentication Code)
and [**many more.**](https://en.wikipedia.org/wiki/HTTPS)

HTTPS was developed so even if communications were intercepted by a third party they would be transferred in an encrypted format and therefore data would not be able to be extracted from it. As a result of this, HTTPS has become mainstream scheme for websites on the internet.

HTTP is slowly being phased out and soon most web browsers will block attempts to visits HTTP websites.

[Article: Deprecating Non Secure HTTP](https://blog.mozilla.org/security/2015/04/30/deprecating-non-secure-http/)
[Article: Chrome continues HTTP phase-out by removing 'secure' icon from HTTPS sites](https://www.itpro.com/security/30496/chrome-continues-http-phase-out-by-removing-secure-icon-from-https-sites)
<sub>Articles detailing the slow process of the HTTP phase out.</sub>

---

# HTTPS Overview

In examining a HTTP request, it can be seen that the effect of not securing communications between the client (web browser) and a web application.

![[HTTP-Request-Login.png]]
 <sub>Example: the content of an HTTP login request.</sub>

As the image presents HTTP is not secure, as the login credentials can be seen in clear-text in the request. 

HTTP makes it trivially easy for someone on the **same network** (such as a public Wi-Fi network, `e.g. coffee shop: Starbucks, Costa, Cafe Nero)`) to capture the HTTP request, read, review (helped by it being in clear-text), and exploit the credentials for malicious purposes.

![[HTTPS-Request.webp]]
<sub>Example: someone intercepts and analyses traffic from a HTTPS request.</sub>

As shown in the image above, the data is transferred as a single encrypted stream, which makes it very difficult for someone to capture information such as the credentials earlier.

Websites that enforce HTTPS can be clearly identified through the [URL](HyperText%20Transfer%20Protocol%20(HTTP).md#%20Uniform%20Resource%20Locator%20(URL)) `scheme` specifically being `https://`. 

![[HTTPS-Google-HTB-Example.webp]]
<sub>For example: https://google.com</sub>

Visiting websites that are HTTPS like Google, is recommended as traffic would be encrypted.

While HTTPS encrypts the actual data being transferred, some metadata can still be visible in request headers:
- Host: Shows which website is being accessed
- User-Agent: Reveals browser/device information
- Referrer: Indicates which page you came from

This means that while an attacker can't read the contents of your communication (like passwords or messages), they might still be able to see which websites you're visiting. This is an important privacy consideration - HTTPS provides strong security for data content, but not complete anonymity for browsing behaviour.

---
# HTTPS Flow

If `http://` is typed instead of `https://` to visit a website that enforces HTTPS as its standard, then when the request hits the web server, it will detect that the request came from port **80** (Default HTTP port) and redirect the client to port **443** (Default HTTPS port) instead.

The way the web server handles the redirect is done by the `301 Moved Permanently` response code. 

![[High-Level-HTTPS-Flow.webp]]
<sub>Example: how HTTPS operates at a high level</sub>

The client (browser) sends a **Client Hello** packet, providing the web server with details such as its supported encryption methods and other preferences.

The server then responds with a **Server Hello** message, selecting the encryption settings that it will use for the session.

A **key exchange** process follows, during which the server sends its SSL certificate to the client. The client verifies the server's certificate for authenticity.

Afterward, the client sends its **own certificate** for verification by the server. Finally, an encrypted handshake is initiated to confirm that both encryption and data transfer are functioning correctly.

Depending on the circumstances, an attacker may be able to perform an HTTP downgrade attack, which downgrades HTTPS communication to HTTP, making the data transferred in clear text.

This is done by performing a MiTM (Man-in-The-Middle) proxy to transfer all the traffic through the attacker's host without the user's knowledge or permission. However, most modern browsers, servers, and web applications are protected against this attack.

---
# cURL for HTTPS

**cURL** should automatically handle all **HTTPS** communication standards and perform a secure handshake and then encrypt and decrypt the data automatically. 

However, if a website was ever requested that had an invalid or outdated SSL certificate, then cURL by default would not proceed with the communication to protect against aforementioned MiTM attacks.

```bash
$ curl https://inlanefreight.com

curl: (60) SSL certificate problem: Invalid certificate chain
More details here: https://curl.haxx.se/docs/sslcerts.html
```
<sub>Example: how cURL  operates against an invalid/outdated SSL certificate</sub>

Modern browsers do the same, warning the user against visiting a website with an invalid SSL certificate.

An issue may be faced when testing a local web application or with a web application hosted for practice purposes. As such web applications may not have yet implemented a valid SSL certificate. Therefore the certification check can be skipped with the `-k` flag.

```bash
$ curl -k http://google.com

<HTML><HEAD>
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```
<sub>Example: how cURL uses the -k flag to ignore SSL check.</sub>

As the example above shows the request went through and as a result we received a response.

The response states `301 Permanently Moved` which indicates google does not support HTTP.

---
###### **No Exercises** for this section.

---

[Next Section](HTTP%20Requests%20and%20Responses.md)