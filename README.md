# Smart Parking System

![1](https://github.com/dmh1g19/smart-parking/assets/97964514/8dbb41a6-f915-4cb4-8809-cce824ea17b5)
![2](https://github.com/dmh1g19/smart-parking/assets/97964514/a107b1f7-ea4a-4d54-98c1-7b98e11bf31b)
![3](https://github.com/dmh1g19/smart-parking/assets/97964514/0b3051aa-57ca-4619-83a2-7f21428e92f1)

## Description

The Smart Parking System is an IoT solution designed to improve parking efficiency in urban areas using LoRaWAN technology. This system uses various sensors and devices to provide real-time data on parking space availability, helping reduce congestion and environmental impact due to unnecessary driving.

## Features

- **Real-time Parking Data:** Utilizes LoRaWAN-enabled sensors to monitor parking space availability.
- **Low Power Consumption:** Devices like the Adafruit Feather nRF52840 Express and Arduino MKR WAN 1300 ensure long battery life and wide coverage.
- **Easy Integration:** System integrates with existing urban infrastructure seamlessly.
- **User-friendly Interface:** Includes a visual application for end-users to view current parking space availability.

## Hardware Requirements

- Adafruit Feather nRF52840 Express
- Raspberry Pi Zero W 2
- Arduino MKR WAN 1300
- LoRaWAN gateway

## Software Requirements

- C++ (for microcontroller programming)
- Python (for server-side application and data handling)

## Installation

1. **Set up the Microcontrollers:**
   - Program the Adafruit Feather and Arduino MKR WAN 1300 with the provided C++ scripts.
2. **Configure the Raspberry Pi:**
   - Install the necessary libraries and tools to handle BLE communications and interfacing with Arduino.
3. **Server Setup:**
   - Deploy the visual app server to display the parking data. Ensure MQTT is configured correctly to receive data.

## Usage

1. Power up all hardware components.
2. Ensure all devices are communicating over BLE and LoRaWAN as expected.
3. Access the visual app through a web browser to view real-time data on parking availability.

## Contributing

Contributions to the Smart Parking System are welcome! Here's how you can contribute:
- **Reporting bugs**
- **Suggesting enhancements**
- **Submitting pull requests with improvements to code or documentation**

Please read [CONTRIBUTING.md](https://github.com/yourusername/smart-parking-system/blob/master/CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/yourusername/smart-parking-system/blob/master/LICENSE.md) file for details.

## Acknowledgments

- Donald Shoup for the insightful data on urban parking challenges.
- Contributors who have participated in this project.

