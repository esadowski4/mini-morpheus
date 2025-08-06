# AI-Powered Network Threat Detector

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

A real-time network intrusion detection system that uses machine learning to identify anomalous network traffic and potential security threats. This project is currently in development.

---

## Table of Contents

- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Project Roadmap](#project-roadmap)
- [License](#license)
- [Contact](#contact)

---

## About The Project

In an era of increasingly sophisticated cyber attacks, traditional signature-based detection methods are no longer sufficient. This project aims to build a lightweight, intelligent intrusion detection system that learns the baseline of "normal" network activity and flags suspicious deviations in real-time.

By leveraging machine learning, this tool can potentially identify zero-day threats and novel attack patterns that would otherwise go unnoticed. This serves as a practical exploration of applying AI/ML concepts to defensive cybersecurity challenges.

---

## Key Features

- **Live Packet Capture:** Sniffs network traffic directly from a network interface.
- **Data Preprocessing:** Extracts relevant features from raw packet data for analysis.
- **Anomaly Detection:** Uses an Isolation Forest model to identify outlier packets that deviate from the established baseline.
- **(Planned) Protocol-Specific Analysis:** Deeper inspection of protocols like DNS and HTTP for malicious patterns.
- **(Planned) Dockerization:** Containerizing the application for easy deployment.

---

## Built With

This project is built using the following core technologies:

* [Python](https://www.python.org/)
* [Scapy](https://scapy.net/)
* [Pandas](https://pandas.pydata.org/)
* [Scikit-learn](https://scikit-learn.org/stable/)

---

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

Make sure you have Python 3.9 or higher installed on your system.
* **Python 3.9+**

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/esadowski4/mini-morpheus.git](https://github.com/esadowski4/mini-morpheus.git)
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd mini-morpheus
    ```
3.  **Create and activate a virtual environment:**
    ```sh
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```
4.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

---

## Usage

The project currently consists of two main scripts:

1.  **Capture Data:** To capture live network traffic and save it for analysis (functionality to be added).
    ```sh
    python src/capture.py
    ```
2.  **Detect Anomalies:** To run the ML model on a sample dataset.
    ```sh
    python src/detect.py
    ```

---

## Project Roadmap

-   [x] Basic packet capture with Scapy
-   [x] Feature extraction (packet length)
-   [x] Initial anomaly detection model with Scikit-learn
-   [ ] Save/Load captured data to a `.pcap` or `.csv` file
-   [ ] Develop more sophisticated features (e.g., protocol type, port numbers)
-   [ ] Experiment with different ML models (e.g., Autoencoders with PyTorch/TensorFlow)
-   [ ] Create a simple dashboard to visualize threats
-   [ ] Containerize the application with Docker

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Contact

Eric Sadowski - [My LinkedIn](https://www.linkedin.com/in/ericsadowski/) - [My Email](esadowsk@purdue.edu)
