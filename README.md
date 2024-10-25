# Task Management System API

Sistem manajemen tugas sederhana menggunakan Django REST Framework.

## Instalasi

1. Clone repository:  
   `git clone https://github.com/ahmadrafidev/task_management`  
   `cd task_management`

2. Buat dan aktifkan virtual environment:  
   - Untuk Linux/macOS:  
     `python3 -m venv venv`  
     `source venv/bin/activate`  
   - Untuk Windows:  
     `python -m venv venv`  
     `.\venv\Scripts\activate`

3. Install dependencies:  
   `pip install -r requirements.txt`

4. Migrasi database:  
   `python manage.py makemigrations`  
   `python manage.py migrate`

5. Jalankan server:  
   `python manage.py runserver`

Aplikasi sekarang dapat diakses di `http://127.0.0.1:8000/`.

## API Endpoints

- **GET** `/api/tasks/`: Mendapatkan daftar semua tugas (dengan pagination, filter, sorting)  
- **POST** `/api/tasks/`: Membuat tugas baru  
- **GET** `/api/tasks/<id>/`: Mendapatkan detail tugas berdasarkan ID  
- **PUT** `/api/tasks/<id>/`: Memperbarui tugas berdasarkan ID  
- **DELETE** `/api/tasks/<id>/`: Menghapus tugas berdasarkan ID  

### Contoh Request/Response

1. **Mendapatkan Daftar Tugas**  
   - **Endpoint**: `/api/tasks/`  
   - **Method**: `GET`  

   _Response_:  
   ```json
   {
       "count": 2,
       "next": null,
       "previous": null,
       "results": [
           {
               "id": 1,
               "title": "Belajar Django",
               "description": "Pelajari dasar-dasar Django REST Framework",
               "is_completed": false,
               "created_at": "2024-10-25T10:00:00Z",
               "updated_at": "2024-10-25T10:00:00Z"
           },
           {
               "id": 2,
               "title": "Kerjakan test REST API",
               "description": "Kerjakan tugas REST API untuk backend",
               "is_completed": false,
               "created_at": "2024-10-25T10:05:00Z",
               "updated_at": "2024-10-25T10:05:00Z"
           }
       ]
   }

2. **Membuat Tugas**  
   - **Endpoint**: `/api/tasks/`  
   - **Method**: `POST`  
   - **Body**: `{ "title": "Belajar Django", "description": "Pelajari dasar-dasar Django REST Framework", "is_completed": false }`  
   - **Response**: `{ "id": 1, "title": "Belajar Django", "description": "Pelajari dasar-dasar Django REST Framework", "is_completed": false, "created_at": "2024-10-25T10:00:00Z", "updated_at": "2024-10-25T10:00:00Z" }`

3. **Mendapatkan Detail Tugas**  
   - **Endpoint**: `/api/tasks/1/`  
   - **Method**: `GET`  
   - **Response**: `{ "id": 1, "title": "Belajar Django", "description": "Pelajari dasar-dasar Django REST Framework", "is_completed": false, "created_at": "2024-10-25T10:00:00Z", "updated_at": "2024-10-25T10:00:00Z" }`

4. **Memperbarui Tugas**  
   - **Endpoint**: `/api/tasks/1/`  
   - **Method**: `PUT`  
   - **Body**: `{ "title": "Belajar Django REST Framework", "description": "Pelajari Django REST Framework lebih mendalam", "is_completed": true }`  
   - **Response**: `{ "id": 1, "title": "Belajar Django REST Framework", "description": "Pelajari Django REST Framework lebih mendalam", "is_completed": true, "created_at": "2024-10-25T10:00:00Z", "updated_at": "2024-10-25T11:00:00Z" }`

5. **Menghapus Tugas**  
   - **Endpoint**: `/api/tasks/1/`  
   - **Method**: `DELETE`  
   - **Response**: `{ "message": "Tugas berhasil dihapus" }`

## Fitur Tambahan

- **Pagination**: Gunakan parameter `page` dan `page_size` untuk mengatur pagination.
  
  Contoh:
  - `/api/tasks/?page=2&page_size=5`  
    Menampilkan halaman kedua dengan 5 tugas per halaman.

- **Sorting**: Gunakan parameter `ordering` untuk mengurutkan daftar tugas berdasarkan field tertentu.

  Contoh:
  - `/api/tasks/?ordering=created_at`  
    Mengurutkan daftar tugas berdasarkan tanggal pembuatan secara ascending.
  - `/api/tasks/?ordering=-created_at`  
    Mengurutkan daftar tugas berdasarkan tanggal pembuatan secara descending.

- **Filtering**: Gunakan parameter `search` untuk melakukan pencarian berdasarkan kolom `title` dan `description`.

  Contoh:
  - `/api/tasks/?search=django`  
    Mencari tugas yang memiliki kata "django" di `title` atau `description`.

