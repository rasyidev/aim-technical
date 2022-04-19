# Model Deployment Menggunakan Platform Heroku

> Dalam modul ini kita akan melakukan deployment terhadap aplikasi flask pada M7S1 bagian ke-3. 
> Dalam proses deployment ini, kita akan menggunakan platform Heroku, salah satu platform untuk deployment aplikasi berbasis web. 
> Heroku menyediakan cara deployment melalui tiga cara yaitu melalui Command Line Interface (Heroku CLI), Github repository, dan application registry. 
> Dalam modul ini yang akan kita gunakan adalah Heroku CLI.

## Deployment Requirements (Project Python Berbasis Web)
- Heroku CLI
- Aplikasi Berbasis Web (flask, django, dll)
- Procfile
- requirements.txt
- runtime.txt

> `requirements.txt` berisi dependency module yang digunakan dalam pengembangan model dan aplikasi flask. 
> Dalam proses pengembangan kita telah membuat _Conda Virtual Environment_ dengan nama `flask`. 
> Di dalam environment tersebut tidak semua module kita butuhkan pada saat deployment sehingga perlu kita hapus. 
> Module yang tidak kita butuhkan pada saat deployment salah satunya yaitu module `nb_conda_kernels`. 
> Untuk itu semua dependency `nb_conda_kernels` tidak perlu kita tambahkan pada `requirements.txt`.
> Hal ini dilakukan agar ukuran dependency module pada saat proses deployment menjadi lebih ringkas dan kecil sehingga tidak membebani server tempat kita
> men-deploy aplikasi. Dalam hal ini, platform Heroku menyediakan `500Mb` (untuk versi gratis) storage untuk menyimpan file aplikasi beserta modulenya.
