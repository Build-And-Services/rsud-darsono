from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return render_template('dashboard.html')

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
   return render_template('verifikasi.html', data = data)

if __name__ == "__main__": 
    app.run(debug=True)