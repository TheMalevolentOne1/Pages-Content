---

---

---

#Tier-0 
#HackTheBox
#BugBountyHunter 

---

[Contents Page](Web%20Requests%20(Module%20Overview).md)
# cURL Cheat Sheet

#### Basic Commands

| Command                                               | Description                                          |
| ----------------------------------------------------- | ---------------------------------------------------- |
| `curl -h`                                             | cURL help menu                                       |
| `curl example.com`                                    | Basic GET request                                    |
| `curl -s -O example.com/index.html`                   | Download file                                        |
| `curl -k https://example.com`                         | Skip HTTPS (SSL) certificate validation              |
| `curl example.com -v`                                 | Print full HTTP request/response details             |
| `curl -I https://www.example.com`               | Send HEAD request (only prints response headers)     |
| `curl -i https://www.example.com`               | Print response headers and response body             |
| `curl https://www.example.com -A 'Mozilla/5.0'` | Set User-Agent header                                |
| `curl -u admin:admin http://<SERVER_IP>:<PORT>/`      | Set HTTP basic authorization credentials             |
| `curl http://admin:admin@<SERVER_IP>:<PORT>/`         | Pass HTTP basic authorization credentials in the URL |

#### Web Requests

| Command | Description |
| --- | --- |
| `curl -H 'Authorization: Basic YWRtaW46YWRtaW4=' http://<SERVER_IP>:<PORT>/` | Set request header |
| `curl 'http://<SERVER_IP>:<PORT>/search.php?search=le'` | Pass GET parameters |
| `curl -X POST -d 'username=admin&password=admin' http://<SERVER_IP>:<PORT>/` | Send POST request with POST data |
| `curl -b 'PHPSESSID=c1nsa6op7vtk7kdis7bcnbadf1' http://<SERVER_IP>:<PORT>/` | Set request cookies |
| `curl -X POST -d '{"search":"london"}' -H 'Content-Type: application/json' http://<SERVER_IP>:<PORT>/search.php` | Send POST request with JSON data |

#### APIs

| Command | Description |
| --- | --- |
| `curl http://<SERVER_IP>:<PORT>/api.php/city/london` | Read entry |
| `curl -s http://<SERVER_IP>:<PORT>/api.php/city/ \| jq` | Read all entries |
| `curl -X POST http://<SERVER_IP>:<PORT>/api.php/city/ -d '{"city_name":"HTB_City", "country_name":"HTB"}' -H 'Content-Type: application/json'` | Create (add) entry |
| `curl -X PUT http://<SERVER_IP>:<PORT>/api.php/city/london -d '{"city_name":"New_HTB_City", "country_name":"HTB"}' -H 'Content-Type: application/json'` | Update (modify) entry |
| `curl -X DELETE http://<SERVER_IP>:<PORT>/api.php/city/New_HTB_City` | Delete entry |

#### Browser DevTools Shortcuts

| Shortcut | Description |
| --- | --- |
| `[CTRL+SHIFT+I]` or `[F12]` | Show devtools |
| `[CTRL+SHIFT+E]` | Show Network tab |
| `[CTRL+SHIFT+K]` | Show Console tab |
