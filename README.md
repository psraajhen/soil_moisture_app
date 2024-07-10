# Soil Moisture Monitor

This project is a web-based soil moisture monitoring system using a Raspberry Pi, ADC115, and analog soil moisture sensors. The application reads data from the soil moisture sensors and displays it in real-time on a web page with a user-friendly interface.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-time monitoring of soil moisture levels.
- User-friendly web interface to display sensor data.
- Visual gauges for easy data interpretation.

## Requirements

- Raspberry Pi with Python 3 installed.
- ADC115 Analog-to-Digital Converter.
- Analog soil moisture sensors.
- Internet connection for the Raspberry Pi.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/soil-moisture-monitor.git
    cd soil-moisture-monitor
    ```

2. **Install the required dependencies:**

    ```sh
    pip3 install -r requirements.txt
    ```

3. **Connect the hardware:**

    - Connect the ADC115 to the Raspberry Pi.
    - Connect the soil moisture sensors to the ADC115.

## Usage

1. **Run the application:**

    ```sh
    python3 app.py
    ```

2. **Open a web browser and navigate to:**

    ```
    http://<your-raspberry-pi-ip-address>:5000
    ```

3. **View the soil moisture levels in real-time on the web interface.**



