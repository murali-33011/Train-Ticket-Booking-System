
---

Train Ticket Booking System 🚆  

This project is a Train Ticket Booking System built using Python and MySQL. It allows users to book train tickets, view available trains, cancel reservations, and manage passenger details efficiently.  

## Features  
- User Registration & Login – Secure authentication system  
- Book Train Tickets – Select train, class, and book tickets  
- View Available Trains – Fetch train details from the database  
- Cancel Bookings – Modify or cancel reservations  
- Admin Panel – Manage train schedules and bookings  

## Technologies Used  
- Python – Core application logic  
- Python modules - pandas || time || mysql.connector || matplotlib.pyplot || 
- MySQL – Database to store user and train data  
- MySQL Connector for Python – To interact with the database  
- Tkinter (Optional) – GUI for an interactive experience  

## Installation Guide  

1. Install Dependencies  
Make sure you have Python and MySQL installed. Then, install the required libraries:  
```
pip install mysql-connector-python
```

2. Set Up MySQL Database  
- Open MySQL and create a new database:  
```
CREATE DATABASE train_booking;
```
- Use the provided SQL script (train_booking.sql) to create tables.  

3. Run the Application  
Execute the Python script to start the booking system:  
```
python train_booking.py
```

## Database Structure  
- Users Table – Stores user login details  
- Trains Table – Contains train schedules and details  
- Bookings Table – Stores ticket reservations  

## Future Enhancements  
- Add online payment integration  
- Implement a web-based interface  
- Improve user interface with a graphical dashboard  

## Contributors  
[N MURALIKRISHNAN] – Developer & Database Designer  

---
