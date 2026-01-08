# ⚙️ Decentralized Multi-Agent Pickup and Delivery Simulation

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)  
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📌 Overview

This project implements a **multi-agent pickup-and-delivery simulation** that reflects key principles of **distributed systems**.  
Each robot operates as an **autonomous agent** with its own local state, **energy level, workload, position, and task history**, and makes decisions **independently**, without a centralized task allocator.

Task allocation is achieved through an **auction-based bidding mechanism**, where agents compute local costs and compete for parcels. This demonstrates:
- **Decentralized coordination**
- **Distributed decision-making**
- **Emergent global behavior from local interactions**

The system is implemented in a **cyber-physical simulation setting**, making it relevant to real-world multi-robot and logistics systems.

---

## 🔧 Methodology

### 1. Autonomous Agent Modeling
- Each robot maintains local state variables:
  - Energy level  
  - Current workload  
  - Spatial position  
  - Task execution history  
- No global controller assigns tasks.

### 2. Auction-Based Task Allocation
- When a new parcel appears, agents:
  - Compute a **local cost function** (distance, energy, load penalties)
  - Submit bids independently
- The parcel is assigned to the lowest-cost bidder, illustrating **market-based coordination**.

### 3. Distributed Scheduling and Resource Awareness
- Energy and load penalties influence bidding behavior
- Enables adaptive task distribution under heterogeneous agent conditions

### 4. Fault Tolerance and Recovery
- **Auction timeouts** and a **reassignment watchdog** detect:
  - Failed agents  
  - Delayed execution  
- Unfinished tasks are reintroduced, emulating **failure detection and recovery** in distributed systems.

### 5. Asynchronous Coordination
- Communication is implicit via shared state (parcels and bids)
- Agents act under **partial and evolving system information**

---

## 📊 Distributed Systems Perspective

From a distributed systems standpoint, the simulation captures:

- **Decentralization** (no single point of control or failure)
- **Scalability** with increasing agents and tasks
- **Dynamic task scheduling**
- **Fault tolerance and recovery**
- **Emergent system-level behavior**

This makes the project a practical case study linking **distributed algorithms** with **multi-robot systems**.

---

## 🌍 Application Domains

- Automated warehouse and fulfillment centers  
- Swarm and fleet robotics systems  
- Autonomous logistics and delivery hubs  
- Smart factories and distributed manufacturing systems  
- Port, airport, and hospital material-handling robots  
- Research testbeds for distributed coordination and multi-agent control

---

## 🚀 Git Files Download

#### Step 1: Obtain the Code or Zip Donwload it
```bash
git clone https://github.com/md-jawad-117/CSE707_Project.git
```

## 🚀 CSV File Directory Change

#### Step 2: Navigate to Project Files and Change Folder Directory
```bash
Scripts/Config.py
```

## 🚀 Enviroment Making

#### Step 3: Go to Main Directory (With Readme.md) & Create a Python Enviroment
```bash
python -m venv venv
venv\Scripts\activate
```

## 🚀 Enviroment Setup

#### Step 4: Pygame and Numpy Version Install
```bash
pip install -r Environment-Config.txt
```

## 🚀 Run

#### Step 5: Run Code
```bash
python Scripts/main.py
```




