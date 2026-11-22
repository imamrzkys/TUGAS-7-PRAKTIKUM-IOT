# TUGAS 7 PRAKTIKUM INTERNET OF THINGS (IoT)
## Simulasi Robot Line Follower Berbasis Webots R2025a & Tinkercad

Repositori ini berisi seluruh berkas proyek, model 3D, arena simulasi, dan pengendali (*controller*) Python untuk **Tugas 7 Praktikum IoT: Simulasi Robot Line Follower**.

---

## 📌 Deskripsi Proyek

Proyek ini merealisasikan simulasi robot *differential-drive line follower* otonom di simulator robotika **Webots R2025a**. Model fisik 3D robot didesain secara kustom menggunakan **Autodesk Tinkercad**, lalu diintegrasikan ke Webots lengkap dengan material dan tekstur elektronika (*motor driver*, baterai 9V, sensor TCRT5000, motor DC kuning, roda *caster*, dan velg ban).

Robot dilengkapi dengan dua sensor inframerah (*DistanceSensor*) yang menghadap tegak lurus ke lantai untuk mendeteksi kontras antara lantai arena putih dan lintasan garis hitam.

---

## 📁 Struktur Direktori

```plaintext
TUGAS 7/
├── worlds/
│   ├── TUGAS 7.wbt              # World simulasi utama Webots R2025a
│   └── TUGAS 7_LENGKAP.wbt      # World cadangan dengan model lengkap
├── meshes/
│   ├── chassis_complete.obj     # Model 3D sasis + elektronika lengkap (Tinkercad)
│   ├── wheel_complete.obj       # Model 3D roda kiri (Tinkercad)
│   ├── wheel_right_complete.obj # Model 3D roda kanan (Tinkercad)
│   ├── obj.mtl                  # Definisi warna dan material OBJ
│   ├── chassis_line_follower.stl# Model 3D sasis dasar (format STL)
│   └── wheel_line_follower.stl  # Model 3D roda dasar (format STL)
├── controllers/
│   └── line_follower_controller/
│       └── line_follower_controller.py # Skrip controller Python pembaca garis
├── .vscode/
│   └── settings.json            # Konfigurasi path modul library Webots
├── tinker.obj                   # File mentah ekspor Tinkercad
├── obj.mtl                      # Material mentah Tinkercad
├── .gitignore
└── README.md
```

---

## 🤖 Spesifikasi Robot & Komponen

1. **Sasis & Aktuator:**
   - **Tipe Penggerak:** Diferensial 2 roda (*Two-wheel differential drive*) + 1 *front caster ball*.
   - **Aktuator:** 2 unit *RotationalMotor* (`left_motor` & `right_motor`) dengan `HingeJoint`.
   - **Massa Robot:** ~0.45 kg dengan *center of mass* seimbang.
2. **Sensorik:**
   - **Tipe:** 2 unit sensor inframerah optik TCRT5000 (`ir_left` dan `ir_right`).
   - **Orientasi:** Menghadap lurus ke bawah (sumbu -Z / arah lantai).
   - **Lookup Table:** Rentang nilai 0 – 1000 (Lantai putih ~800-1000, Garis hitam ~0-350).

---

## 🧠 Logika Algoritma Controller (`line_follower_controller.py`)

Controller membaca nilai pantulan inframerah dari kedua sensor secara periodik:

| Sensor Kiri (`ir_left`) | Sensor Kanan (`ir_right`) | Kondisi | Aksi Robot |
| :---: | :---: | :---: | :--- |
| **Hitam** | **Hitam** | Robot tepat di atas garis | **Maju lurus** (`BASE_SPEED = 4.5 rad/s`) |
| **Hitam** | **Putih** | Sensor kanan keluar garis | **Belok Kiri tajam** (Roda kiri mundur `-2.0`, roda kanan maju `5.0`) |
| **Putih** | **Hitam** | Sensor kiri keluar garis | **Belok Kanan tajam** (Roda kiri maju `5.0`, roda kanan mundur `-2.0`) |
| **Putih** | **Putih** | Keduanya keluar garis (tikungan patah) | **Pemulihan arah terakhir** (*last_turn recovery*) |

---

## 🚀 Cara Menjalankan Simulasi

1. Pastikan telah menginstal **Webots R2025a** dan **Python 3.10/3.11**.
2. *Clone* repositori ini:
   ```bash
   git clone https://github.com/imamrzkys/TUGAS-7-PRAKTIKUM-IOT.git
   ```
3. Buka **Webots R2025a**.
4. Klik **File** → **Open World...**, lalu pilih file `worlds/TUGAS 7.wbt` atau `worlds/TUGAS 7_LENGKAP.wbt`.
5. Tekan tombol **Play / Run** pada Webots untuk memulai simulasi pelacakan garis.
