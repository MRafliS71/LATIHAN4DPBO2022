# LATIHAN4DPBO2022
/Saya Muhammad Rafli Syaputra mengerjakan Tugas Latihan 1 dalam mata kuliah Desain dan Pemrograman Berorientasi Objek untuk keberkahanNya maka saya tidak melakukan kecurangan seperti yang telah dispesifikasikan. Aamiin../

## Gambaran Peta Desain

![image](https://user-images.githubusercontent.com/99678525/157269896-b8115c35-3175-4dd2-931b-1ef850b3725c.png)

Pada kasus kendaraan atau Vehicle, desain yang digunakan merupakan Hierarchical Inheritance, sedangkan pada desain Person atau orang menggunakan desain Multiple Inheritance.

Vehicle disini berperan sebagai parent class, dikarenakan pada kelas ship dan kelas airplane keduanya memiliki kesamaan hierarki yaitu sejatinya keduanya merupakan sebuah kendaraan atau vehicle. Dengan begitu atribut kendaraan seperti nama, jenis bahan bakar, medan jalan, kecepatan, dan kapasitas penumpang dapat dipergunakan pada kelas ship maupun airplane.

Multiple inheritance disini dapat terjadi dikarenakan Driver merupakan seseorang atau Person yang pastinya memiliki atribut yang orang(person) miliki seperti NIK, identitas, dan lain-lain. Di sisi lain, Driver juga merupakan sebuah profesi dimana pastinya memiliki legalitas atau administrasi dalam profesinya, seperti asal perusahaan, NIP, jabatan, dan lain sebagainya. Dengan begitu dapat disimpulkan bahwa driver memiliki 2 parent yaitu job dan person. 
