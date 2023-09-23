# Tyres Side Condition Checker
![tyre](https://github.com/Flychuban/Tyres-Condition/blob/main/images/tyre.jpg)

Welcome to the Tire Damage Detection Program! This software utilizes TensorFlow, a powerful machine learning framework, to check for damage on the side of a tire.
It is designed to automate the process of tire inspection, making it quicker and more accurate. 
The program is integrated with a web interface, making it user-friendly and accessible from any device with a browser.

# Features
Tire Damage Detection: Utilizes machine learning models created with TensorFlow to detect and classify damage on the side of a tire, such as cuts, punctures, and bulges.

Web Interface: Provides a user-friendly web-based interface that allows users to upload images of tires and receive instant damage assessments.</br>
![damagedtyre](https://github.com/Flychuban/Tyres-Condition/blob/main/images/damagedtyre.jpg)

## Accuracy: 

The program is not 100% accurate

[Check it out!](http://95.42.52.106:2006/DemoGumi/client/index.html)

## Accessibility: 
Accessible from any device with a web browser, making it easy to use on the shop floor or in the field.

## Prerequisites
Before using the Tire Damage Detection Program, ensure you have the following prerequisites:

Python: Install Python on your machine. You can download it from the official Python website.

TensorFlow: Install TensorFlow by running the following command:

Web Browser: To use the web interface, you need a modern web browser such as Google Chrome, Mozilla Firefox, or Microsoft Edge.

# Installation
Clone this repository to your local machine.

```
git clone https://github.com/Flychuban/Tyres-Condition/tree/main
```
```
cd tire-damage-detection
```
Install the required Python packages.
```

pip install -r requirements.txt
```
Run the program.
```
cd WebUI/server
```
```
python server.py
```
Access the web interface by double clicking on the index.html in WebUI/client

Upload an image of a tire to the web interface.

The program will analyze the image and provide a damage assessment, indicating if any damage is detected and its type (cut, puncture, bulge, etc.).

### Contributing
Contributions to this project are welcome. If you have ideas for improvements, want to extend the machine learning models, or have other enhancements in mind, please feel free to contribute by forking the repository and submitting a pull request.

### License
The Tire Damage Detection Program is provided under the MIT License. You are free to modify, distribute, and use it for personal and non-commercial purposes. Please refer to the full license documentation for more details.
