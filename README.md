# Portal Berita - Proyek Akhir PKL

Aplikasi portal berita berbasis Django yang dibangun sebagai proyek akhir PKL. Proyek ini mencakup fitur manajemen konten, sistem user dengan otentikasi JWT, dan REST API.

## Teknologi yang Digunakan

-   **Backend**: Django, Django REST Framework
-   **Authentication**: Simple JWT for RESTful authentication
-   **Database**: SQLite (Development), dapat dikonfigurasi untuk PostgreSQL (Production)
-   **Frontend**: Django Templates dengan Bootstrap

## Fitur Utama

-   Manajemen Berita (CRUD) dengan Kategori dan Subkategori.
-   Sistem Komentar untuk setiap berita.
-   Manajemen Pengguna dengan sistem Grup dan Hak Akses (Permissions).
-   REST API untuk mengakses data berita.
-   Panel Admin kustom untuk manajemen konten.

## Panduan Instalasi (Lokal)

Berikut adalah langkah-langkah untuk menjalankan proyek ini di lingkungan lokal.

### 1. Clone Repository
```bash
git clone <URL_REPOSITORY_ANDA>
cd PortalBerita
```

### 2. Buat dan Aktifkan Virtual Environment
Disarankan untuk menggunakan virtual environment untuk mengisolasi dependensi proyek.

-   **Windows**:
    ```powershell
    python -m venv venv
    .\venv\Scripts\activate
    ```
-   **macOS/Linux**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

### 3. Install Dependensi
Install semua pustaka yang dibutuhkan dari file `requirements.txt`.
```bash
pip install -r requirements.txt
```

### 4. Konfigurasi Environment Variables
Salin file `.env.example` menjadi `.env`. File ini berisi variabel lingkungan yang dibutuhkan oleh aplikasi.
```bash
# Di Windows (Command Prompt)
copy .env.example .env

# Di Windows (PowerShell)
cp .env.example .env

# Di macOS/Linux
cp .env.example .env
```
Kemudian, buka file `.env` dan sesuaikan nilainya. Anda **wajib** mengisi `SECRET_KEY`.
```env
# Ganti dengan kunci rahasia yang kuat dan unik
SECRET_KEY='your-super-secret-key-here'

# Set ke False di lingkungan produksi
DEBUG=True
```

### 5. Jalankan Migrasi Database
Terapkan skema database awal.
```bash
python manage.py migrate
```

### 6. Buat Superuser
Buat akun admin untuk mengakses Django Admin.
```bash
python manage.py createsuperuser
```
Ikuti petunjuk untuk membuat username, email, dan password.

### 7. Jalankan Server Development
```bash
python manage.py runserver
```
Aplikasi sekarang akan berjalan di `http://127.0.0.1:8000/`.

## Struktur Proyek
```
PortalBerita/
├── api/              # Aplikasi untuk REST API
├── cat/              # Aplikasi untuk Kategori Berita
├── core/             # Pengaturan utama proyek (settings.py)
├── main/             # Aplikasi utama (views, templates)
├── manager/          # Aplikasi untuk manajemen user
├── media/            # Direktori untuk file unggahan pengguna
├── news/             # Aplikasi untuk Berita
├── static/           # Direktori untuk file statis (setelah collectstatic)
├── manage.py         # Skrip manajemen Django
├── requirements.txt  # Daftar dependensi Python
└── .env.example      # Contoh file environment
```
