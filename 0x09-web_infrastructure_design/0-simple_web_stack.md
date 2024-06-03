# Single-Server Web Infrastructure for foobar.com (markdown file)

**Infrastructure Breakdown**

* **Server:** A computer running 24/7 that acts as the central hub for our website. It has all the necessary software installed to handle user requests and deliver the website content.

* **Domain Name (foobar.com):** This is the user-friendly address that people type into their browsers. It acts like a nickname for the server's actual IP address (8.8.8.8 in this example).

* **DNS Record (www):** This record in the Domain Name System (DNS) translates the user-friendly domain name "foobar.com" into the server's numerical IP address (8.8.8.8). Essentially, it's like a phone book for the internet, looking up website addresses. 

* **Web Server (Nginx):** This software on the server listens for incoming requests from user browsers. When a user requests "www.foobar.com" Nginx receives the request, retrieves the necessary website files (codebase) from the server, and sends them back to the user's browser for display. 

* **Application Server (Combined with Nginx in this case):**  In this setup, Nginx also acts as the application server.  An application server can handle dynamic content  (like user logins or shopping carts) by processing code and interacting with the database  before delivering the final web page. 

* **Database (MySQL):** This software stores all the website's data, like user accounts, product information, or blog posts. When the application server needs data to build the web page, it retrieves it from the MySQL database.

* **Communication Protocol (HTTP):** The server communicates with the user's computer using Hypertext Transfer Protocol (HTTP).  This is the language that web browsers and servers use to exchange information. 

**Issues with this Infrastructure**

* **Single Point of Failure (SPOF):** This entire website relies on one server. If the server crashes or goes offline, the website becomes unavailable (downtime). 

* **Maintenance Downtime:**  When updates or new code needs to be deployed to the web server (Nginx in this case), the server might need to be restarted, causing temporary website downtime.

* **Scalability:** This setup can't handle a sudden surge in traffic. If there are too many users trying to access the website at once, the single server can become overloaded and slow down the website significantly.

