# Task Management System API

Sistem manajemen tugas sederhana menggunakan Django REST Framework.

## Fitur

- CRUD untuk tugas (Task)
- Fitur pagination, filter, dan sorting

## Prasyarat

Pastikan Anda memiliki Python 3.7+ dan pip di komputer lokal.

## Instalasi

### Clone repository:  

   `git clone https://github.com/ahmadrafidev/task_management`  
   `cd task_management`

### Buat dan aktifkan virtual environment:  

1. Untuk Linux/macOS:  
   1. `python3 -m venv venv`  
   2. `source venv/bin/activate`  
   
2. Untuk Windows:  
   1. `python -m venv venv`  
   2. `.\venv\Scripts\activate`

### Install dependencies:  

   `pip install -r requirements.txt`

### Migrasi database:  
   `python manage.py makemigrations`  
   `python manage.py migrate`

### Jalankan server:  
   `python manage.py runserver`

### Lihat Aplikasi

Aplikasi sekarang dapat diakses di `http://127.0.0.1:8000/` dan untuk melihat API yang tersedia ada di `http://127.0.0.1:8000/api/tasks/`
