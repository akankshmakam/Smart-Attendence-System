# Smart Attendance System

The Smart Attendance System is a computer vision-based project that automates attendance marking using face detection and ID card recognition. It offers real-time attendance marking and stores data in a spreadsheet for easy access and analysis.

## Features

- Face Detection
- ID Card Recognition
- Real-time Attendance
- Data Storage

## Technologies Used

- Python
- OpenCV
- Face Recognition Library
- Tesseract OCR
- Google Sheets API

## Installation

1. Clone the repository.
2. Install required dependencies with `pip`.

## How It Works

The Smart Attendance System combines face detection and ID card recognition algorithms. When an individual enters the camera's view, their face is captured using OpenCV's face detection library. The system then compares the detected face with the database using the Face Recognition Library to identify the individual.

Attendance data is automatically stored and updated in the configured Google Sheets spreadsheet.

## Future Enhancements

- Integration with biometric authentication for increased security.
- Support for multiple cameras to cover larger areas.
- Advanced data analytics for attendance trends and patterns.

## License

This project is licensed under the MIT License. Feel free to use and modify it for your needs.
