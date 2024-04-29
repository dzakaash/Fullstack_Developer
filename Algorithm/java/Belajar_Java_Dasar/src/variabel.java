import java.util.Date;

public class variabel {
    public static void main(String[] args) {
//variable adalah tempat untuk menyimpan data
//scope, variable hanya bisa diakses di dalam area dimana mereka dibuat {}, baik areanya berupa method atau block
//java adlah static type yang mana harus menyimpan satu tipe data dalam satu variabel
//        tidak langsung
        String name;
        name = "Dzaka Ali";

        System.out.println(name);
//        langsung
        int age = 30;
        String address = "Indonesia";

        System.out.println(age);
        System.out.println(address);

//        java versi 10 keatas bisa identifikasi tipe data, hanya dengan kata kunci var, namun harus variabel langsung
        var newName = "Jack";
        var newAge = "25";

        System.out.println(newName);
        System.out.println(newAge);

//        kata kunci final, digunakan jika ada variabel yang datanya tidak boleh diubah, sehingga variabelnya konstan
        final String apple = "Belajar Java";

        //        Expression, semua operasi (variabel, operator, pemanggilan method) yang menghasilkan satu nilai
        int value2;
        value2 = 10;

//        Statement, kalimat lengkap dalam bahasa, berisi ekspresi komplit dan diakhiri titik koma
//        assignment statement
        double aValue = 8933.234;
//        increament statement
        aValue++;
//        method invocation statement
        System.out.println("Hello World");
//        object creation statement
        Date date = new Date();

//        Block, kumpulan statement yang terdiri dari nol atau lebih statement, block diawali dan diakhiri dengan kurung kurawal {}, tujuannya mengrouping code
        {
            System.out.println("Hello World 1");
            System.out.println("Hello World 2");
            System.out.println("Hello World 3");
        }
    }
}
