# Distributed Web Infrastructure

**Components:**

* **2 Web Servers (Identical):** These servers run the Nginx web server software. They serve static content and handle user requests.
* **1 Application Server:** This server  processes website logic and interacts with the database.
* **1 Load Balancer (HAProxy):** This acts as a traffic director, distributing incoming user requests across the two web servers.
* **1 Application Files:**  The website's codebase resides on a central location accessible by all servers.
* **1 Database (MySQL):** This stores all website data,  accessed by the application server.

**Explanation of Additions:**

* **Web Servers (x2):**  Adding redundancy eliminates a single point of failure (SPOF). If one server fails, the other can handle requests.
* **Load Balancer (HAProxy):**  Distributes traffic evenly between web servers, improving performance and scalability for handling high traffic volumes.  HAProxy can be configured with various distribution algorithms, such as **Round Robin**, which distributes requests sequentially to each server. 
* **Active-Passive vs. Active-Active:** This infrastructure utilizes an **Active-Passive** load balancer setup. HAProxy remains active, directing traffic to the primary web server. If the primary fails, HAProxy detects it and starts directing traffic to the secondary server, providing failover capabilities.  An **Active-Active** setup utilizes both web servers simultaneously for load balancing, offering higher availability but requiring more complex configuration.

**Database Cluster (Primary-Replica):**

This setup include a MySQL database cluster with a **Primary** node and one **Replica** nodes.

* **Primary Node:** This is the main database server that receives all write requests (data updates) from the application server. It ensures data integrity and consistency.
* **Replica Node(s):** These are copies of the primary database, kept in sync through replication mechanisms. They can handle read requests from the application server, reducing load on the primary and improving performance.  In case of a primary node failure, a replica can be promoted to become the new primary, minimizing downtime.

**Security Concerns and Monitoring:**

While not depicted here, additional security measures are crucial:

* **Firewalls:**  These act as security gateways, filtering incoming and outgoing traffic, blocking potential threats.
* **HTTPS:** Secure Sockets Layer encrypts communication between the web servers and users' browsers, protecting sensitive data.
* **Monitoring:**  Monitoring tools track server health, application performance, and database activity, allowing proactive issue identification and resolution.

**Remaining SPOFs:**

* **Application Server:**  A single point of failure remains. Consider high-availability solutions for the application server in critical deployments.
* **Database Cluster (Optional):** If no redundancy exists for the database cluster (only one primary node), it becomes a potential SPOF.

