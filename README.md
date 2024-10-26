# Task Management System API

Sistem manajemen tugas sederhana menggunakan Django REST Framework.

## Fitur

- CRUD untuk tugas (Task)
- Fitur pagination, filter, dan sorting

## Prasyarat

Pastikan Anda memiliki Python 3.7+ dan pip di komputer lokal.

## Instalasi

### Clone Repository:  

   ```bash
   git clone https://github.com/ahmadrafidev/task_management_api.git 
   cd task_management_api
   ```

### Buat dan aktifkan virtual environment:  

1. Untuk Linux/macOS:  
   
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
   
2. Untuk Windows:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

### Install Dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Migrasi Database:  

   ```bash
   python manage.py makemigrations 
   python manage.py migrate
   ```

### Jalankan Server:  

   ```bash
   python manage.py runserver
   ```

### Jalankan Test:  

   ```bash
   python manage.py test
   ```

### Lihat Aplikasi

Aplikasi sekarang dapat diakses di `http://127.0.0.1:8000/` dan untuk melihat API yang tersedia ada di `http://127.0.0.1:8000/api/tasks/`
