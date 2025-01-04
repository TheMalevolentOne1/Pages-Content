
---

#Web-Requests 
#HackTheBox 

---

[Contents Page](Web%20Requests%20(Module%20Overview).md)
[Previous Section](HyperText%20Transfer%20Protocol%20Secure%20(HTTPS).md)

**HTTP communications** mainly consist of a **HTTP request** and a **HTTP response.** 

The HTTP request sent by the client (cURL/browser) is processed by the web server.

The request contains details the server requires including the resource.

`https://url.com/pathToResource?parameter=value`

| **Field**    | **Example**        |
| ------------ | ------------------ |
| `Method`     | `https://`         |
| `Domain`     | `url.com`          |
| `Path`       | `/pathToResource`  |
| `Parameters` | `?parameter=value` |

---
# HTTP Request

Let's say we have the URL:
`https://gimmeproxy.com/api/getProxy?supportshttps=true`

The URL is a link that returns JSON format proxy information from that the service GimmeProxy obtains from free proxy lists from other services.

![[GimmeProxy-HTTP-Request.png]]
<sub>Example: HTTP Request</sub>

| **Field** | **Example**     | **Description**                                                                                                            |
| --------- | --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `Method`  | `GET`           | The HTTP method or verb, which specifies the type of action to perform.                                                    |
| `Path`    | `/api/getProxy` | The path to the resource being accessed. This field can also be suffixed with a query string (e.g. `?supportshttps=true`). |
| `Version` | `HTTP/1.1`      | The third and final field is used to denote the HTTP version.                                                              |

The lines after the ones above contain content like `Host`, `User-Agent`, `Cookie` and other possible attributes of a request. 

The headers are terminated with a new line `\n` which is necessary for the server to validate the request. Finally a request may end with the request body and data.

**HTTP version 1.x** (**x** meaning any version) sends requests in clear-text and uses a new-line character `\n` to separate the various fields and requests.

**HTTP version 2.x** on the other hand sends requests as binary data in a dictionary form.

---
# HTTP Response

![[HTTP-Response.png]]
<sub>Example: HTTP Response from GimmeProxy request earlier</sub>

As visible in the image above, the first two lines contain fields separated by spaces.

The first being the **HTTP version** (e.g. **HTTP/1.1**, **HTTP/2**, etc) and the second states the **HTTP response code** (e.g. **200 OK**)

**Response codes** are used to state a request's status and how the server has responded to it. 

The response may end with a response body, which is separated by a new line after the headers. The response body is usually defined as HTML code. 

However, it can also respond with other code such as JSON, website resources such as images style sheets or scripts, or even a document such as a PDF document hosted on a web server.

The [earlier](HTTP%20Requests%20and%20Responses.md#%20HTTP%20Response) header of the GimmeProxy HTTP Request also included a response body.

![[HTTP-Response-Body-P1.png]]
<sub>The response body is attached to the response header seen earlier</sub>

Although this proxy is not used here, it serves as an example of a **HTTP request** and **response**. It also illustrates the **JSON** format returned from the **API** when making such a request.

---

# cURL

[Previously](HyperText%20Transfer%20Protocol%20(HTTP).md#%20cURL) in **cURL**, it would only output the **response body**. 

However, **cURL** also allows us to preview the **entire HTTP request** which can become very handy when performing web penetration tests or writing exploits.

To view the **entire HTTP request** and **response**, the verbose flag `-v` can be added onto the earlier commands and it should print both the **request** and the **response**.

```sh
$ curl -v https://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0*   Trying 93.184.215.14:443...
* Connected to example.com (93.184.215.14) port 443 (#0)
* ALPN: offers h2,http/1.1
} [5 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [88 bytes data]
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
} [1 bytes data]
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
} [512 bytes data]
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0* TLSv1.3 (IN), TLS handshake, Server hello (2):
{ [155 bytes data]
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
{ [15 bytes data]
* TLSv1.3 (IN), TLS handshake, Certificate (11):
{ [3152 bytes data]
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
{ [264 bytes data]
* TLSv1.3 (IN), TLS handshake, Finished (20):
{ [52 bytes data]
* TLSv1.3 (OUT), TLS handshake, Finished (20):
} [52 bytes data]
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN: server accepted h2
* Server certificate:
*  subject: C=US; ST=California; L=Los Angeles; O=Internet�Corporation�for�Assigned�Names�and�Numbers; CN=www.example.org
*  start date: Jan 30 00:00:00 2024 GMT
*  expire date: Mar  1 23:59:59 2025 GMT
*  subjectAltName: host "example.com" matched cert's "example.com"
*  issuer: C=US; O=DigiCert Inc; CN=DigiCert Global G2 TLS RSA SHA256 2020 CA1
*  SSL certificate verify ok.
} [5 bytes data]
* using HTTP/2
* h2h3 [:method: GET]
* h2h3 [:path: /]
* h2h3 [:scheme: https]
* h2h3 [:authority: example.com]
* h2h3 [user-agent: curl/7.88.1]
* h2h3 [accept: */*]
* Using Stream ID: 1 (easy handle 0x563f15b5cd30)
} [5 bytes data]
> GET / HTTP/2
> Host: example.com
> user-agent: curl/7.88.1
> accept: */*
> 
{ [5 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [233 bytes data]
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
{ [233 bytes data]
* old SSL session ID is stale, removing
{ [5 bytes data]
< HTTP/2 200 
< accept-ranges: bytes
< age: 430286
< cache-control: max-age=604800
< content-type: text/html; charset=UTF-8
< date: Mon, 30 Dec 2024 20:02:57 GMT
< etag: "3147526947+gzip"
< expires: Mon, 06 Jan 2025 20:02:57 GMT
< last-modified: Thu, 17 Oct 2019 07:18:26 GMT
< server: ECAcc (bsb/27A0)
< vary: Accept-Encoding
< x-cache: HIT
< content-length: 1256
< 
{ [5 bytes data]
100  1256  100  1256    0     0   4488      0 --:--:-- --:--:-- --:--:--  4485
* Connection #0 to host example.com left intact
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
```

As shown above, the verbose flag is a powerful, as it allows the penetration tester to the **full HTTP request and response**. 

The request sent `GET / HTTP/1.1` along with the `Host`, `User-Agent`, and `Accept` headers. In return, the HTTP response contained the `HTTP/1.1 200 OK` indicating the status was successful. 

Similar to the request, the response also contains several headers sent by the user, including **Date**, **Content-Length**, and **Content-Type**. Finally, the **response** contains the **response body** in HTML same as [earlier](HTTP%20Requests%20and%20Responses.md#%20HTTP%20Response).

---
# Browser DevTools

Most modern browsers come with built-in developer tools (**DevTools**) which are mainly intended for developers to test their web applications.

However, the web penetration tester can use these tools as a vital asset during any web assessment, as most browsers come with **DevTools** and a majority of computer's have browsers, this means that we will be able to utilise these tools to assess and monitor different types of requests.

When a website or web application is visited/accessed our browser may send multiple web requests and handles handles multiple **HTTP responses** to render the **HTML** to the user.

In browsers like **Chrome**, or **FireFox** to reveal the **DevTools** press **CTRL+SHIFT+I** or **F12** which is used to open **Inspector** tab.

**DevTools** contains many tabs, like the **Inspector** tab, used to inspect a webpage's **HTML** and **CSS** code, allowing it to be edited. The **Network** tab, will be the main focus as it is responsible for **web requests**.



---
# Exercises

The `-vvv` flag shows an even more verbose output. Try to use this flag to see what extra request and response details get displayed with it.

Answer: 

```bash
$ curl -vvv https://example.com
*   Trying 93.184.215.14:443...
* Connected to example.com (93.184.215.14) port 443 (#0)
* ALPN: offers h2,http/1.1
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
*  CAfile: /etc/ssl/certs/ca-certificates.crt
*  CApath: /etc/ssl/certs
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.3 (OUT), TLS handshake, Client hello (1):
* TLSv1.3 (IN), TLS handshake, Server hello (2):
* TLSv1.3 (IN), TLS handshake, Encrypted Extensions (8):
* TLSv1.3 (IN), TLS handshake, Certificate (11):
* TLSv1.3 (IN), TLS handshake, CERT verify (15):
* TLSv1.3 (IN), TLS handshake, Finished (20):
* TLSv1.3 (OUT), TLS handshake, Finished (20):
* SSL connection using TLSv1.3 / TLS_AES_256_GCM_SHA384
* ALPN: server accepted h2
* Server certificate:
*  subject: C=US; ST=California; L=Los Angeles; O=Internet�Corporation�for�Assigned�Names�and�Numbers; CN=www.example.org
*  start date: Jan 30 00:00:00 2024 GMT
*  expire date: Mar  1 23:59:59 2025 GMT
*  subjectAltName: host "example.com" matched cert's "example.com"
*  issuer: C=US; O=DigiCert Inc; CN=DigiCert Global G2 TLS RSA SHA256 2020 CA1
*  SSL certificate verify ok.
* using HTTP/2
* h2h3 [:method: GET]
* h2h3 [:path: /]
* h2h3 [:scheme: https]
* h2h3 [:authority: example.com]
* h2h3 [user-agent: curl/7.88.1]
* h2h3 [accept: */*]
* Using Stream ID: 1 (easy handle 0x55beb6828d30)
> GET / HTTP/2
> Host: example.com
> user-agent: curl/7.88.1
> accept: */*
> 
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* TLSv1.3 (IN), TLS handshake, Newsession Ticket (4):
* old SSL session ID is stale, removing
< HTTP/2 200 
< age: 507074
< cache-control: max-age=604800
< content-type: text/html; charset=UTF-8
< date: Tue, 31 Dec 2024 01:18:37 GMT
< etag: "3147526947+ident"
< expires: Tue, 07 Jan 2025 01:18:37 GMT
< last-modified: Thu, 17 Oct 2019 07:18:26 GMT
< server: ECAcc (bsb/27EE)
< vary: Accept-Encoding
< x-cache: HIT
< content-length: 1256
< 
<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>
* Connection #0 to host example.com left intact
```

