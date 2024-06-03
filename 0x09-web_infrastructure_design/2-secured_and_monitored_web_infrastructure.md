# Secure Web Infrastructure

**Components:**

* **3 Web Servers (Identical):** These servers run the Nginx web server software. They serve static content and handle user requests.
* **1 Application Server:** This server  processes website logic and interacts with the database.
* **1 Load Balancer (HAProxy):** This acts as a traffic director, distributing incoming user requests across the two web servers.
* **1 Database Server (MySQL):** This stores all website data.
* **3 Firewalls:** These firewalls sit in front of each server, filtering incoming and outgoing traffic.
* **1 SSL Certificate:** This encrypts communication between users' browsers and the web servers.
* **3 Monitoring Clients:** These agents collect data from each server for centralized monitoring.

**Explanation of Additions:**

* **Firewalls:**  These act as security gateways, inspecting incoming and outgoing traffic based on predefined rules. They block malicious attempts and enhance overall security.

* **HTTPS with SSL Certificate:**  The website uses HTTPS, which leverages an SSL certificate to encrypt communication between web servers and user browsers. This safeguards sensitive data transmission, like login credentials or credit card information.

* **Monitoring Clients:**  These software agents installed on each server collect performance metrics, resource utilization, and application logs. The collected data is sent to a centralized monitoring service like Sumologic for analysis and alerting.

**Monitoring Web Server QPS (Queries Per Second):**

Monitoring tools can track web server QPS by collecting data on the number of requests processed by the web server within a specific timeframe. This helps identify potential bottlenecks and optimize server performance.

**Issues and Considerations:**

* **SSL Termination at Load Balancer:**  While terminating SSL at the load balancer can improve performance by offloading encryption/decryption tasks, it requires managing the SSL certificate on the load balancer, introducing a potential security risk if the certificate private key is compromised. 

* **Single MySQL Write Server:**  This configuration creates a single point of failure (SPOF).  Consider implementing a MySQL master-slave replication setup for redundancy. The primary (master) handles writes, while replicas (slaves) synchronize data and can potentially handle read-only requests, improving scalability and fault tolerance.

* **Homogeneous Servers:**  Having all servers with the same components (database, web server, and application server) simplifies management but reduces isolation. If a security vulnerability affects one component, all servers become susceptible. Consider separating functionalities for enhanced security.  For example, dedicate servers for web serving and application logic, with the database on a separate server.

