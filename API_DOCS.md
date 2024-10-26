# API Documentation

File ini berisi dokumentasi untuk Task Management API.

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
   - **Body**:
      ```json
      { 
        "title": "Belajar Django", 
        "description": "Pelajari dasar-dasar Django REST Framework", 
        "is_completed": false 
      } 
   - **Response**: 
      ```json
      { 
        "id": 1, 
        "title": "Belajar Django", 
        "description": "Pelajari dasar-dasar Django REST Framework", 
        "is_completed": false, 
        "created_at": "2024-10-25T10:00:00Z", 
        "updated_at": "2024-10-25T10:00:00Z" 
      }

3. **Mendapatkan Detail Tugas**  
   - **Endpoint**: `/api/tasks/1/`  
   - **Method**: `GET`  
   - **Response**: 
      ```json
      { 
        "id": 1, 
        "title": "Belajar Django", 
        "description": "Pelajari dasar-dasar Django REST Framework",
        "is_completed": false, 
        "created_at": "2024-10-25T10:00:00Z", 
        "updated_at": "2024-10-25T10:00:00Z" 
      }

4. **Memperbarui Tugas**  
   - **Endpoint**: `/api/tasks/1/`  
   - **Method**: `PUT`  
   - **Body**: 
     ```json
      { 
        "title": "Belajar Django REST Framework", 
        "description": "Pelajari Django REST Framework lebih mendalam", "is_completed": true 
      }  
   - **Response**: 
      ```json
      { 
        "id": 1, 
        "title": "Belajar Django REST Framework", 
        "description": "Pelajari Django REST Framework lebih mendalam", "is_completed": true, 
        "created_at": "2024-10-25T10:00:00Z", 
        "updated_at": "2024-10-25T11:00:00Z" 
      }

1. **Menghapus Tugas**  
   - **Endpoint**: `/api/tasks/1/`  
   - **Method**: `DELETE`  
   - **Response**: 
      ```json
      { 
        "message": "Tugas berhasil dihapus" 
      }

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