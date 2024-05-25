public class boolean_ {
    public static void main(String[] args) {
        boolean benar = true;
        boolean salah = false;

        System.out.println(benar);
        System.out.println(salah);

//        Operasi perbandingan, >, <, >=, <=, ==, !=
        int a = 100;
        int b = 100;
        System.out.println(a > b);
        System.out.println(a < b);
        System.out.println(a >= b);
        System.out.println(a <= b);
        System.out.println(a == b);
        System.out.println(a != b);

//        Operasi Boolean, && (dan), || (atau), ! (kebalikan)
//        && hanya true jika keduanya true
//        || hanya false jika keduanya false

        var absen = 70;
        var nilai = 80;

        var lulusAbsen = absen >= 75;
        var lulusNilai = nilai >= 75;

        var lulus = lulusAbsen && lulusNilai;
        System.out.println(lulus);

//        If statement
        if (nilai >= 75 && absen >= 75){
            System.out.println("Selamat Anda Lulus");
        }
//        Else statement
        else {
            System.out.println("Anda Tidak Lulus");
        }
//        Else if statement, jika lebih dari dua cabang
        if (nilai >= 80 && absen >= 80) {
            System.out.println("Nilai Anda A");
        } else if (nilai >= 70 && absen >= 70) {
            System.out.println("Nilai Anda B");
        } else if (nilai >= 60 && absen >= 60) {
            System.out.println("Nilai Anda C");
        } else {
            System.out.println("Nilai Anda D");
        }

//        Swich statement, percabangan serupa if namun hanya menggunakan ==
        var nilaiBaru = "A";
        switch (nilaiBaru) {
            case "A":
                System.out.println("Anda lulus dengan nilai baik");
                break;
            case "B":
            case "C":
                System.out.println("Nilai Anda Baik");
                break;
            case "D":
                System.out.println("Anda Tidak Lulus");
                break;
            default:
                System.out.println("Anda Mungkin Salah Jurusan");
        }

//        Switch Lambda
        switch (nilaiBaru) {
            case "A" -> System.out.println("Wow Anda Lulus Dengan Baik");
            case "B", "C" -> System.out.println(("Nilai Anda Cukup Baik"));
            case "D" -> System.out.println("Anda Tidak Lulus");
            default -> System.out.println("Anda Sepertinya Salah Jurusan");
        }
//        Switch Yield Manual
        String ucapan;
        switch (nilaiBaru) {
            case "A" -> ucapan = "Wow Anda Lulus Dengan Baik";
            case "B", "C" -> ucapan = "Nilai Anda Cukup Baik";
            case "D" -> ucapan = "Anda Tidak Lulus";
            default -> ucapan = "Anda Sepertinya Salah Jurusan";
        }
            System.out.println(ucapan);

//        Switch Yield dengan Key
        ucapan = switch (nilaiBaru) {
            case "A" : yield "Wow Anda Lulus Dengan Baik";
            case "B", "C" : yield  "Nilai Anda Cukup Baik";
            case "D" : yield "Anda Tidak Lulus";
            default : yield "Anda Sepertinya Salah Jurusan";
        };
        System.out.println(ucapan);

//        Ternary Operator, jika if benar maka if diambil jika salah maka else yang diambil
        var nilaiTernary = 75;
        String ucapanTernary = nilaiTernary > 75 ? "Selamat Anda Lulus" : "Silahkan Coba Lagi";

        System.out.println(ucapanTernary);

//        For Loop, perulangan, selama kondisi terpenuhi
//        init statement akan dieksekusi hanya sekali di awal sebelum perulangan
//        kondisi akan dilakukan setiap perulangan, jika true maka akan dilakukan, jika false maka selesai
//        post statement akan dieksekusi setiap akhir perulangan
//        init, kondisi, post adalah optional jika tidak diisi maka bernilai true
//        for(;;) {
//            System.out.println("Perulangan Tanpa Henti");
        var counter = 1;
        for (; counter <= 10;) {
            System.out.println("Perulangan" + counter);
            counter ++;
        }

        for (var counters = 1; counters <= 10; counters ++) {
            System.out.println("Perulangan " + counters);
        }

//        while loop, versi perulangan yang lebih sederhana
        var counterss = 1;
        while (counterss <= 10) {
            System.out.println("Perulangan" + counterss);
            counterss++;
        }

//        do while loop, pengecekan kondisi yang dilakukan setelah perulangan dilakukan, bukan diawal seperti sebelumnya, maka akan dilakukan eksekusi satu kal
        var countersss = 1;
        do {
            System.out.println("Perulangan" + countersss);
            countersss++;
        } while (countersss <= 10);

//       break and continue, break menghentikan seluruh perulangan sedangkan continue berpindah ke perulangan selanjutnya
        var num = 1;
        while (true) {
            System.out.println("Perulangan " + num);
            num ++;

            if (num > 10) {
                break;
            }
        }

        for (var nums = 1; nums <=100; nums++) {
            if(nums % 2 == 0) {
                continue;
            }
            System.out.println("Perulangan Ganjil " + nums);
        }


    }
}
