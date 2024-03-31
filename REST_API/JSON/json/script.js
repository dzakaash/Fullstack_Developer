// let mahasiswa = {
//     nama : 'Dzaka Ali',
//     no  : "1223456",
//     email : "dzaka.ali@gmail.com"
// }

// // console.log(mahasiswa); //objeck muncul di console inspeksi
// console.log(JSON.stringify(mahasiswa)); //objeck muncul di console sebagai json
//// stringify dari objek > json

// let xhr = new XMLHttpRequest();
// xhr.onreadystatechange = function () {
//     if (xhr.readyState == 4 && xhr.status == 200) {
//         // let mahasiswa = this.responseText;
//         let mahasiswa = JSON.parse(this.responseText); //parse dari JSON > object
//         console.log(mahasiswa);
//     }
// }
// xhr.open('GET', 'json/coba.json', true);
// xhr.send();

//fungsi untuk bikin data jadi object dengan jquery
$.getJSON('backend/json/coba.json', function (data) {
    console.log(data);
});