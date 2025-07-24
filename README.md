# 🎬 Movie Ticket Booking System (Django)

A web-based movie ticket booking system built with Django. This system allows users to browse movies, book tickets, make payments, and manage their bookings. Admins can manage movie details, prices, theatres, and view bookings through a calendar.

---

## 📌 Project Description

- **User Side:**
  - Register and login securely.
  - Browse all available movies.
  - Book tickets based on available seats.
  - Pay the amount securely via Stripe.
  - View booking history.

- **Admin Side:**
  - Manage movie information.
  - Set ticket prices and manage screens.
  - Manage theatre names and showtimes.
  - View and manage bookings using a calendar.
  - Uses Django's built-in admin panel.

- **Database:**
  - MySQL is used as the primary database.
  - You must install and configure MySQL before running the project.

---

## 🧰 Technologies Used

- **Backend:** Django
- **Frontend:** HTML, CSS (Bootstrap), JavaScript
- **Database:** MySQL
- **Authentication:** Django-Allauth
- **Email:** SMTP with Gmail
- **Payments:** Stripe Payment Gateway
- **Calendar Integration:** For viewing booked shows
- **Virtual Environment:** Python venv

---
```markdown
## ⚙️ Project Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/RajashekaraRedddy/Movie-Ticket-Booking-System.git
cd Movie-Ticket-Booking-System

2️⃣ Create Virtual Environment
```bash
python -m venv env
env\Scripts\activate  # For Windows
# OR
source env/bin/activate  # For Linux/macOS

3️⃣ Install Django
```bash
pip install django

4️⃣ Install Dependencies (if available)
```bash
pip install -r requirements.txt

5️⃣ MySQL Setup
Install MySQL Server.
Create a new database (e.g., movie_db).
Update the DATABASES section in movie_ticket_booking/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'movie_db',
        'USER': 'your_mysql_username',
        'PASSWORD': 'your_mysql_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

6️⃣ Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate

7️⃣ Create Superuser
```bash
python manage.py createsuperuser

8️⃣ Run the Development Server
```bash
python manage.py runserver

