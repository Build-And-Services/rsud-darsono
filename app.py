from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  data = [
      {
      "no":1,
      "tanggal": "23 Februari 2024",
      "status": "Proses",
      "keterangan": "Diminta: 9",
      },
         {
         "no":2,
         "tanggal": "22 Februari 2024",
         "status": "Diterima",
         "keterangan": "Diminta: 6",
      },
         {
         "no":3,
         "tanggal": "24 Februari 2024",
         "status": "Ditolak",
         "keterangan": "Diminta: 7",
      },
         {
         "no":4,
         "tanggal": "27 Februari 2024",
         "status": "Diterima",
         "keterangan": "Diminta: 7",
      },
   ]
   
  return render_template('dashboard.html', data=data, menu = 'home')

@app.route("/verifikasi")
def verifikasi():
   data= [{
      "no": 1,
        "tanggal": "23/02/2023",
        "ruangan": "Ruangan A",
        "nama_barang": "Laptop MSI modern",
        "jumlah": 14,
        "satuan": "pcs",
        "permintaan": 1,
    }, {
       "no": 2,
        "tanggal": "25/02/2023",
        "ruangan": "Ruangan B",
        "nama_barang": "Laptop MSI Leopard",
        "jumlah": 14,
        "satuan": "pcs",
        "permintaan": 1,
    }, {
       "no": 3,
        "tanggal": "27/02/2023",
        "ruangan": "Ruangan C",
        "nama_barang": "Laptop Asus modern",
        "jumlah": 14,
        "satuan": "pcs",
        "permintaan": 1,
    },{
       "no": 4,
        "tanggal": "29/02/2023",
        "ruangan": "Ruangan D",
        "nama_barang": "Laptop Lenovo modern",
        "jumlah": 14,
        "satuan": "pcs",
        "permintaan": 1,
    }]
   return render_template('verifikasi.html', data = data, menu = 'verifikasi')

@app.route("/verifikasi-detail")
def verifikasiDetail():
  return render_template('verifikasi-detail.html', menu = 'verifikasi')

@app.route("/transaksi")
def transaksi():
   data = [
      {
      "no":1,
      "tanggal": "23 Februari 2024",
      "status": "Selesai",
      "ruangan": "Ruangan A",
   },
      {
      "no":2,
      "tanggal": "22 Februari 2024",
      "status": "Proses",
      "ruangan": "Ruangan B",
   },
      {
      "no":3,
      "tanggal": "24 Februari 2024",
      "status": "Selesai",
      "ruangan": "Ruangan C",
   },
      {
      "no":4,
      "tanggal": "27 Februari 2024",
      "status": "Selesai",
      "ruangan": "Ruangan B",
   },
      {
      "no":5,
      "tanggal": "25 Februari 2024",
      "status": "Proses",
      "ruangan": "Ruangan D",
   },
   ]
   return render_template('transaksi.html',data=data, menu="transaksi")
   
@app.route("/pengajuan-barang")
def pengajuanBarang():
  return render_template('pengajuan-barang.html', menu = 'pengajuan-barang')

@app.route("/status")
def status():
   return render_template('status.html', menu="status")

if __name__ == "__main__": 
    app.run(debug=True)