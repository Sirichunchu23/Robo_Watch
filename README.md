# RoboWatch 🤖👁️

### Autonomous Multi-Robot Surveillance and Monitoring System

## 📌 Overview

**RoboWatch** is an intelligent autonomous robotic surveillance system designed for continuous monitoring, anomaly detection, and collaborative robot coordination in industrial, warehouse, campus, and smart security environments.

The project focuses on:

* Autonomous robot patrolling
* Supervisor–Assistant robot coordination
* Dynamic task reassignment
* Failover recovery
* Connection recovery using backtracking
* Abnormal activity detection and response

RoboWatch ensures uninterrupted surveillance even when robots fail, disconnect, or encounter obstacles.

---

# 🚀 Features

## 🛰️ Autonomous Patrol Monitoring

Robots continuously monitor assigned areas and remain at strategic checkpoints until abnormal movement or activity is detected.

### Behavior:

* Stay idle at predefined monitoring points
* Detect unusual motion/activity
* Automatically navigate toward the detected location
* Resume surveillance after inspection

---

## 🤝 Multi-Robot Coordination

The system supports:

* One **Supervisor Robot**
* Multiple **Assistant Robots**

The supervisor coordinates:

* Path allocation
* Surveillance zones
* Task distribution
* Connectivity management

---

## 🔋 Automatic Supervisor Failover

If the supervisor robot fails or becomes inactive:

* The assistant robot with the **highest battery percentage**
  automatically becomes the new supervisor.
* Tasks continue without interruption.
* Network topology is re-established dynamically.

### Advantages:

* No single point of failure
* Increased system reliability
* Self-healing architecture



## 📡 Connection Recovery & Backtracking

If an assistant robot loses connection:

1. The robot stops the current task
2. Backtracks to the last known connected path
3. Reconnects to the supervisor
4. Resumes the interrupted task from the exact stopping point

### Benefits:

* Reliable communication
* Reduced task loss
* Autonomous recovery mechanism



# 🧠 System Architecture

```text
                    +------------------+
                    | Supervisor Robot |
                    +------------------+
                      /      |       \
                     /       |        \
                    /        |         \
         +-------------+ +-------------+ +-------------+
         | Assistant 1 | | Assistant 2 | | Assistant 3 |
         +-------------+ +-------------+ +-------------+

```

---

# ⚙️ Technologies Used

| Technology                 | Purpose              |
| -------------------------- | -------------------- |
| Python                     | Core logic           |
| ROS / ROS2                 | Robot communication  |
| OpenCV                     | Vision processing    |
| SLAM                       | Mapping & navigation |
| MQTT/WebSockets            | Robot communication  |
| NumPy                      | Data processing      |
| LiDAR / Ultrasonic Sensors | Obstacle detection   |
| AI/ML Models               | Activity detection   |


# 🛠️ Installation

## Prerequisites

* Python 3.10+
* ROS/ROS2 installed
* Ubuntu 20.04+ recommended
* Camera/LiDAR support (optional for hardware deployment)

## Run RoboWatch

### Start Supervisor Robot

```bash
python supervisor/task_manager.py
```

### Start Assistant Robot

```bash
python assistant/patrol.py
```

---

# 🔄 Workflow

## Normal Monitoring Flow

```text
1. Robots stay at monitoring positions
2. Sensors detect abnormal movement/activity
3. Robot moves toward activity location
4. Supervisor updates robot states
5. Monitoring resumes
```

---

## Supervisor Failure Recovery

```text
1. Supervisor becomes inactive
2. Assistants share battery status
3. Highest battery robot elected
4. New supervisor initialized
5. System continues operation
```

---

## Connection Loss Recovery

```text
1. Assistant loses signal
2. Current task paused
3. Robot backtracks to reconnect
4. Connection restored
5. Task resumed automatically
```

---

# 🧪 Future Enhancements

* AI-powered threat classification
* Real-time dashboard monitoring
* Cloud-based robot coordination
* Drone integration
* Voice alert system
* Edge AI deployment
* Human tracking system
* Thermal vision support

---

# 📸 Use Cases

## 🏭 Industrial Monitoring

* Factory surveillance
* Hazard detection
* Worker safety monitoring

## 🏢 Smart Buildings

* Night patrol systems
* Unauthorized access detection

## 🎓 Campus Security

* Autonomous campus patrol
* Emergency alert assistance

## 📦 Warehouses

* Inventory zone monitoring
* Intrusion detection

---

# 📊 Advantages

* Autonomous recovery system
* High reliability
* Fault-tolerant architecture
* Scalable multi-robot support
* Real-time surveillance
* Reduced human intervention

---

# 🔐 Safety & Reliability

RoboWatch is designed with:

* Fail-safe recovery
* Continuous connectivity checks
* Dynamic task reassignment
* Collision avoidance
* Supervisor redundancy

## ⭐ RoboWatch — Smarter Surveillance Through Collaborative Robotics 🚀
