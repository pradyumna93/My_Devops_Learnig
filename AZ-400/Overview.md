# ☁️ **Microsoft Azure – Complete Overview**

## 🌐 What Is Microsoft Azure?

**Microsoft Azure** is a **cloud computing platform** offering a collection of **online services** that organizations use to **build, deploy, and manage applications** — without owning any on-premises servers or data centers.

🔹 You access it over the Internet.
🔹 You **pay only for what you use** (consumption-based pricing).
🔹 It provides **global data centers** for high availability and scalability.

---

## 🧩 Core Azure Building Blocks

### **1. Compute**

Azure compute provides resources for running applications, containers, and serverless workloads.

| Service                             | Type                 | Description                                                              |
| ----------------------------------- | -------------------- | ------------------------------------------------------------------------ |
| **Virtual Machines (VMs)**          | IaaS                 | Full control of OS and apps. Used for “lift & shift” migrations.         |
| **App Services**                    | PaaS                 | Host web/mobile apps without managing servers.                           |
| **Azure Container Instances (ACI)** | CaaS                 | Run single containers quickly with minimal management.                   |
| **Azure Kubernetes Service (AKS)**  | CaaS / Orchestration | Run and scale multi-container applications.                              |
| **Azure Functions**                 | FaaS / Serverless    | Run small pieces of code (“functions”) on demand. Pay only when it runs. |

🧠 **Tip:**

* VMs → Full control
* App Service → Simplified deployment for apps
* ACI / AKS → Containers & orchestration
* Functions → Serverless event-driven workloads

---

### **2. Storage**

Azure offers multiple storage options to handle various data types — files, objects, and databases.

| Service                                             | Type                          | Use Case                                                        |
| --------------------------------------------------- | ----------------------------- | --------------------------------------------------------------- |
| **Blob Storage**                                    | Object Storage                | Store images, videos, logs, backups (Hot, Cool, Archive tiers). |
| **File Storage**                                    | Managed File Shares (SMB/NFS) | Mountable file shares across VMs.                               |
| **Data Lake Storage Gen2**                          | Big Data Analytics            | Hadoop-compatible analytics storage.                            |
| **Azure SQL Database**                              | RDBMS (PaaS)                  | Managed version of Microsoft SQL Server.                        |
| **Azure Database for MySQL / PostgreSQL / MariaDB** | RDBMS (Open Source)           | Fully managed open-source databases.                            |
| **Azure Synapse Analytics**                         | Data Warehouse                | Enterprise analytics and data warehousing.                      |
| **Azure Cosmos DB**                                 | NoSQL                         | Globally distributed, highly scalable NoSQL database.           |
| **Azure Cache for Redis**                           | In-memory Cache               | Fast caching for frequently accessed data.                      |

🧠 **Tip:**
Blob = unstructured
SQL = structured
Cosmos = globally scalable
Redis = high-speed cache

---

### **3. Networking**

Azure networking connects your cloud resources securely and efficiently.

| Concept                          | Description                                                                      |
| -------------------------------- | -------------------------------------------------------------------------------- |
| **VNet (Virtual Network)**       | Private network in Azure to connect resources like VMs, AKS clusters, etc.       |
| **Subnet**                       | Logical subdivision of a VNet.                                                   |
| **Public IP Address**            | Allows inbound Internet access.                                                  |
| **Network Security Group (NSG)** | Firewall rules for controlling inbound/outbound traffic.                         |
| **VNet Peering**                 | Connect multiple VNets privately across regions or subscriptions.                |
| **VPN Gateway**                  | Secure connection between on-prem and Azure using encrypted tunnels.             |
| **ExpressRoute**                 | Dedicated private connection between on-prem and Azure — faster & more reliable. |

🧠 **Tip:**

* VPN → Over public Internet (secure but slower)
* ExpressRoute → Private dedicated link (fast, enterprise-grade)

---

## ⚙️ **Other Major Azure Categories**

| Area                      | Services                                          |
| ------------------------- | ------------------------------------------------- |
| **AI & Machine Learning** | Azure Cognitive Services, Machine Learning Studio |
| **DevOps**                | Azure DevOps Services, GitHub Actions             |
| **Monitoring & Security** | Azure Monitor, Defender for Cloud, Key Vault      |
| **Identity & Access**     | Azure Active Directory (Entra ID)                 |
| **Integration**           | Logic Apps, Service Bus, Event Grid               |

---

## 💬 **Quick Q&A**

| **Question**                                         | **Answer**                                                                        |
| ---------------------------------------------------- | --------------------------------------------------------------------------------- |
| What is Azure?                                       | Microsoft’s public cloud platform for hosting and managing services.              |
| What are the 3 core components of Azure?             | Compute, Storage, Networking                                                      |
| What is IaaS vs PaaS vs SaaS?                        | IaaS → VMs; PaaS → App Service; SaaS → Fully managed software (e.g., Office 365). |
| Which service runs containers in Azure?              | ACI and AKS                                                                       |
| Which service offers serverless computing?           | Azure Functions                                                                   |
| What’s the difference between Blob and File Storage? | Blob = object-based, File = shared filesystem                                     |
| What is the relational database service in Azure?    | Azure SQL Database                                                                |
| What’s the NoSQL database service?                   | Azure Cosmos DB                                                                   |
| How to connect on-prem network to Azure?             | VPN Gateway or ExpressRoute                                                       |
| What is the pricing model of Azure?                  | Pay-as-you-go (consumption-based)                                                 |

---

## 📈 **Pro Tip for Real-World Use**

* Use **Azure Resource Manager (ARM)** or **Bicep/YAML pipelines** for IaC.
* Secure credentials with **Azure Key Vault**.
* Optimize cost using **Azure Cost Management**.
* Always use **Tags**, **Policies**, and **RBAC** for governance.

---