## Nama Anggota
1. Muhammad Ilham Fathony Sulton  
2. Wimbuh Agus Alim  
3. Ciko Nanda P. W.  
4. M. Dhesta Prasetyo  

## Deskripsi Tugas
Tugas ini dibuat untuk menghitung luas beberapa bangun datar, yaitu:
- Lingkaran
- Segitiga
- Jajar Genjang
- Trapesium

Setiap tugas dikerjakan secara individu oleh masing-masing anggota tim, kemudian digabungkan menggunakan Git dan GitHub untuk mendukung kerja kolaboratif dalam satu repository.

## Struktur Repository

```bash
workshop-git/
├── .devcontainer/
├── .github/
│   └── workflows/
│       └── python-tests.yml
│
├── src/                         # Source code utama
│   ├── aritmatika/              # Folder perhitungan
│   ├── code-reviewer/           # Folder tugas tim
│   │   └── nama-anggota/
│   │       └── service.py       # File tugas masing-masing anggota
│   │
│   ├── tugas/                   # Folder tugas individu workshop
│   └── index.js                 # Entry point aplikasi
│
├── tests/                       # File unit testing
│
└── README.md
```

## Pembagian Fitur

### Muhammad Ilham Fathony Sulton
- Implementasi perhitungan luas lingkaran

### Wimbuh Agus Alim
- Implementasi perhitungan luas segitiga
- Pembuatan file README.md

### Ciko Nanda P. W.
- Implementasi perhitungan luas jajar genjang

### M. Dhesta Prasetyo
- Implementasi perhitungan luas trapesium

## Teknologi yang Digunakan
- Python
- Git
- GitHub
- Visual Studio Code

## Cara Menjalankan Program

### Menjalankan Service

```bash
python service.py
```

### Menjalankan Unit Test

```bash
python test_service.py
```
