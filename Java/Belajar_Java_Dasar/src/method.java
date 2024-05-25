import org.w3c.dom.ls.LSOutput;

public class method {
    public static void main(String[] args) {
//        method adalah blok kode program yang akan berjalan saat kita panggil, gunakan kata kunci void, lalu diikuti nam method, kurung () dan diakhiri dengan block. Di bahasa lain biasanya disebut function
//        kata kunci biasanya kata pertama kecil semua, setelahanya capitalize
        sayHelloWorld();
        sayHello("Dzaka", "Ali");
        sayHello("Zeke", "El");
        System.out.println(sum(200, 100));
        System.out.println(hitung(300, "+", 500));
        System.out.println(hitung(300, "-", 500));
        System.out.println(hitung(300, "tidak", 500));

        int[] values = {80, 50, 50, 50, 80};
        sayCongrats( "Eko", values);
        sayCongrats("Budi", 88, 90, 76, 88);

        sayGoodBay();
        sayGoodBay("Dzaka");
        sayGoodBay("Dzaka", "Ali");

        System.out.println(factorial(10));
    }
    static void sayHelloWorld(){
        System.out.println("Hello World 1");
        System.out.println("Hello World 2");
        System.out.println("Hello World 3");
    }
//    method paramater, mengirim informasi ke method yang dipanggil yang disimpan di dalam kurung, bisa lebih dari satu dipisahkan tanda koma
    static void sayHello(String firstName, String lastName) {
        System.out.println("Hello " + firstName + " " + lastName);
    }
//    method return value, agar method mengembalikan nilai yang kita inginkan, gunakan kata kunci return
    static int sum(int value1, int value2) {
        var total = value1 + value2;
        return total;
    }
    static int hitung(int value1, String operasi, int value2) {
        switch (operasi) {
            case "+":
                return value1 + value2;
            case "-":
                return value1 - value2;
            default :
                return 0;

        }
    }
//    method variabel argumen, untuk mengimkan data yang berisi jumlah tak tentu bisa nol atau lebih, parameter dengan tipe argumen hanya bisa ditempatkan di posisi akhir parameter
    static void sayCongrats(String name, int...values) {
        var total = 0;
        for (var value : values) {
            total += value;
        }
        var finalValue = total / values.length;
        if (finalValue >= 75) {
            System.out.println("Selamat " + name + ", Anda Lulus");
        } else {
            System.out.println("Maaf " + name + " anda tidak lulus");
        }
    }

//    method overloading, mendeklarasikan ulang nama method yang sama namun dengan parameter yang berbeda
    static void sayGoodBay(){
        System.out.println("Good Bay");
    }
    static void sayGoodBay(String name) {
        System.out.println("Good Bay " + name);
    }
    static void sayGoodBay(String firstName, String lastName) {
        System.out.println("Good Bay " + firstName + " " + lastName);
    }
//    Recursive method adalah kemampuan method memanggil dirinya sendiri. Namun, harus hati-hati karena jika memanggil terllu dalam maka akan terjadi error StackOverflow, karena stack java tidak cukup untuk menyimpannya
    static int factorial(int value) {
        if(value == 1) {
            return 1;
        } else {
            return  value * factorial(value - 1);
        }
    }
//    rekursive dibyah berpotensi overflow jika parameternya sangat besar
    static void loop(int value) {
        if(value == 0) {
            System.out.println("Selesai");
        } else {
            System.out.println("Loop " + value);
            loop(value - 1);
        }
    }
}
