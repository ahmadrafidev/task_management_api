# Task Management System API

Sistem manajemen tugas sederhana menggunakan Django REST Framework.

## Fitur

- CRUD untuk tugas (Task)
- Fitur pagination, filter, dan sorting

## Prasyarat

Pastikan Anda memiliki Python 3.7+ dan pip di komputer lokal.

## Instalasi

### Clone repository:  

   ```bash
   git clone https://github.com/ahmadrafidev/task_management 
   cd task_management
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

### Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Migrasi database:  

   ```bash
   python manage.py makemigrations 
   python manage.py migrate
   ```

### Jalankan server:  

   ```bash
   python manage.py runserver
   ```

### Lihat Aplikasi

Aplikasi sekarang dapat diakses di `http://127.0.0.1:8000/` dan untuk melihat API yang tersedia ada di `http://127.0.0.1:8000/api/tasks/`
