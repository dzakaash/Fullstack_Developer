package Algorithm.java.Belajar_Java_Dasar.src;

import java.util.*;
import java.util.stream.IntStream;

public class array {
    public static void main(String[] args) {
//        Array adalah struktur data yang digunakan untuk menyimpan sekumpulan elemen dengan tipe data yang sama. Elemen-elemen dalam array diindeks secara linear, dimulai dari indeks 0 hingga N-1, di mana N adalah jumlah elemen dalam array. Ukuran array (jumlah elemen) ditentukan pada saat pembuatannya dan tidak dapat diubah setelahnya. Deklarasi array dilakukan dengan menentukan tipe data elemen dan jumlah elemen yang akan disimpan.
        String[] stringArray;
        stringArray = new String[3];

        stringArray[0] = "Dzaka";
        stringArray[1] = "Ali";
        stringArray[2] = "Saiful";

        System.out.println(stringArray[0]); //Dzaka
        System.out.println(stringArray[1]); //Ali
        System.out.println(stringArray[2]); //Saiful
        System.out.println(stringArray); //[Ljava.lang.String;@7b23ec81

        stringArray[0] = "Zeke";
        System.out.println(stringArray[0]);

//        Array Initializer
        String[] namaNama = {
                "Dzaka", "Ali", "Saiful"
        };

        int[] arrayInt = new int[]{
                1, 2, 3, 4, 5, 6, 7, 8, 9, 10
        };

        long[] arrayLong = {
                10L, 20L, 30L
        };

//        Operasi Array
//        mengubah variabel
        arrayLong[0] = 15L;
//        mengetahui panjang Array;
        System.out.println(arrayLong.length);
//        menghapus data Array tidak mungkin karena panjangnya sudah fix, hanya bisa diganti nilainy jadi tidak bernilai
        namaNama[1] = null;
        arrayLong[2] = 0;

//        Array di dalam array
        String[][] members = {
                {"Dzaka", "Ali"},
                {"Zack", "Al"},
                {"Jeck", "El"}
        };
        System.out.println(members[0][0]); //Dzaka

//        List, List adalah antarmuka (interface) yang merepresentasikan sebuah koleksi elemen yang diurutkan dan dapat berubah-ubah. List dapat menyimpan elemen-elemen dengan tipe data yang sama atau berbeda. List memungkinkan duplikasi elemen dan mempertahankan urutan penyimpanan elemen. Ukuran List dapat berubah secara dinamis sesuai dengan penambahan atau penghapusan elemen.
        {
            List<Integer> numbers = new ArrayList<>(); // Membuat ArrayList untuk menyimpan bilangan bulat
            List<String> words = new LinkedList<>(); // Membuat LinkedList untuk menyimpan string

        }
//        ArrayList, implementasi dari antarmuka List yang menggunakan larik (array) sebagai struktur penyimpanan datanya. memungkinkan akses cepat ke elemen berdasarkan indeksnya. Dapat tumbuh atau menyusut secara otomatis sesuai dengan kebutuhan, artinya ukurannya dapat berubah secara dinamis saat elemen-elemen ditambahkan atau dihapus. Mengandung elemen-elemen dengan tipe data yang sama atau berbeda. Tidak bersifat thread-safe, artinya tidak aman digunakan dalam lingkungan multithreading tanpa sinkronisasi eksternal.
        {
            List<String> namaList = new ArrayList<>();
            namaList.add("Alice");
            namaList.add("Bob");
        }
//        LinkedList, implementasi dari antarmuka List yang menggunakan struktur data berantai (linked list) sebagai struktur penyimpanan datanya. Disimpan sebagai objek yang mengandung referensi ke elemen berikutnya dalam daftar. Efisien untuk operasi penambahan atau penghapusan elemen di tengah daftar karena tidak memerlukan realokasi memori seperti ArrayList. Kurang efisien dalam mengakses elemen secara acak karena harus melakukan traversal dari awal atau akhir daftar. Tidak bersifat thread-safe dan tidak cocok untuk penggunaan dalam lingkungan multithreading tanpa sinkronisasi eksternal.
        {
            List<Integer> angkaList = new LinkedList<>();
            angkaList.add(1);
            angkaList.add(2);
        }
//        Vector, kelas yang mirip dengan ArrayList tetapi bersifat thread-safe. Vector menggunakan larik (array) sebagai struktur penyimpanan datanya dan memungkinkan tumbuh atau menyusut secara otomatis. Bersifat thread-safe, penggunaan Vector lebih aman dalam lingkungan multithreading. Kinerja Vector biasanya lebih lambat daripada ArrayList karena setiap operasi pada Vector harus disinkronisasi. Memiliki metode-metode yang sama dengan ArrayList untuk menambah, menghapus, atau mengakses elemen-elemennya.
        {
            List<Double> vectorList = new Vector<>();
            vectorList.add(3.14);
            vectorList.add(2.71);
        }
//        for loop
        String[] names = {
                "Dzaka", "Ali", "Saiful", "Husna"
        };
        for (var i = 0; i < names.length; i++) {
            System.out.println(names[i]);
        }
//        for each, untuk mengambil data array satu per satu
        for (var value : names) {
            System.out.println(value);
        }

//        IntStream: Bagian dari API Java 8 yang menyediakan aliran (stream) dari nilai-nilai primitif integer. Dapat digunakan untuk melakukan operasi seperti filtering, mapping, dan reduksi pada kumpulan nilai integer. Memiliki metode-metode fungsional yang memungkinkan penggunaannya dalam ekspresi lambda. Memungkinkan pemrosesan paralel yang efisien untuk operasi-operasi besar pada data integer.
        {
            int[] numbers = {1, 2, 3, 4, 5};
            IntStream stream = Arrays.stream(numbers);
            stream.forEach(System.out::println);
        }

//        //Built Function
//        1. Arrays.sort(T[] a): Mengurutkan elemen-elemen dalam array.
        {
            int[] numbers = {3, 1, 4, 1, 5, 9, 2, 6};
            Arrays.sort(numbers);
            System.out.println("Array setelah diurutkan: " + Arrays.toString(numbers));
        }
//        2. Arrays.copyOf(T[] original, int newLength): Membuat salinan array dengan panjang yang ditentukan.
        {
            int[] originalArray = {1, 2, 3, 4, 5};
            int[] newArray = Arrays.copyOf(originalArray, 3);
            System.out.println("Salinan array: " + Arrays.toString(newArray));
        }
//        3. Arrays.equals(T[] a, T[] b): Memeriksa apakah dua array memiliki elemen-elemen yang sama.
        {
            int[] array1 = {1, 2, 3};
            int[] array2 = {1, 2, 3};
            boolean isEqual = Arrays.equals(array1, array2);
            System.out.println("Array1 sama dengan array2: " + isEqual);
        }
//        4. Arrays.fill(T[] a, T val): Mengisi semua elemen array dengan nilai tertentu.
        {
            int[] numbers = new int[5];
            Arrays.fill(numbers, 10);
            System.out.println("Array setelah diisi: " + Arrays.toString(numbers));
        }
//        5. Arrays.toString(T[] a): Mengonversi array menjadi string.
        {
            int[] numbers = {1, 2, 3, 4, 5};
            String arrayString = Arrays.toString(numbers);
            System.out.println("Array dalam bentuk string: " + arrayString);
        }
//        6. Arrays.binarySearch(T[] a, T key): Mencari nilai tertentu dalam array yang telah diurutkan.
        {
            int[] numbers = {1, 2, 3, 4, 5};
            int index = Arrays.binarySearch(numbers, 3);
            System.out.println("Index dari nilai 3: " + index);
        }
//        7. Arrays.copyOfRange(T[] original, int from, int to): Membuat salinan bagian tertentu dari array.
        {
            int[] originalArray = {1, 2, 3, 4, 5};
            int[] newArray = Arrays.copyOfRange(originalArray, 1, 3);
            System.out.println("Salinan bagian array: " + Arrays.toString(newArray));
        }
//        8. Arrays.asList(T... a): Mengonversi array menjadi objek List.
        {
            String[] fruits = {"Apple", "Banana", "Orange"};
            List<String> fruitList = Arrays.asList(fruits);
            System.out.println("List buah: " + fruitList);
        }
//        9. Arrays.stream(T[] array): Membuat aliran (stream) dari array.
        {
            int[] numbers = {1, 2, 3, 4, 5};
            IntStream stream = Arrays.stream(numbers);
            ((IntStream) stream).forEach(System.out::println);
        }
//        10. Arrays.fill(T[] a, int fromIndex, int toIndex, T val): Mengisi bagian tertentu dari array dengan nilai tertentu.
        {
            int[] numbers = {1, 2, 3, 4, 5};
            Arrays.fill(numbers, 1, 4, 10);
            System.out.println("Array setelah diisi bagian tertentu: " + Arrays.toString(numbers));
        }
//        11. Filtering, Operasi filtering digunakan untuk menyaring atau memilih elemen-elemen tertentu dari kumpulan nilai berdasarkan kondisi atau predikat tertentu. Dalam konteks kumpulan nilai integer, filtering memungkinkan kita untuk menyaring elemen-elemen yang memenuhi kondisi tertentu.
        {
            IntStream numbers = IntStream.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
            IntStream evenNumbers = numbers.filter(n -> n % 2 == 0);
            evenNumbers.forEach(System.out::println); // Output: 2 4 6 8 10
        }
//        12. Mapping (Pemetaan): Operasi mapping digunakan untuk mengubah setiap elemen dalam kumpulan nilai menjadi nilai lain sesuai dengan suatu fungsi pemetaan (mapping function) yang diberikan. Dalam konteks kumpulan nilai integer, mapping memungkinkan kita untuk mengubah setiap elemen menjadi nilai lain sesuai dengan fungsi yang diberikan.
        {
            IntStream numbers = IntStream.of(1, 2, 3, 4, 5);
            IntStream squaredNumbers = numbers.map(n -> n * n);
            squaredNumbers.forEach(System.out::println); // Output: 1 4 9 16 25
        }
//        3. Reduksi (Reduction): Operasi reduksi digunakan untuk menggabungkan semua elemen dalam kumpulan nilai menjadi satu nilai tunggal berdasarkan suatu operasi tertentu. Dalam konteks kumpulan nilai integer, reduksi memungkinkan kita untuk menghitung jumlah, nilai maksimum, nilai minimum, atau melakukan operasi reduksi lainnya pada seluruh elemen dalam kumpulan nilai.
        {
            IntStream numbers = IntStream.of(1, 2, 3, 4, 5);
            int sum = numbers.reduce(0, (a, b) -> a + b);
            System.out.println("Jumlah: " + sum); // Output: 15
        }
    }
}
//Thread-safe adalah istilah yang digunakan untuk menggambarkan sebuah program atau komponen program yang dapat beroperasi dengan benar saat diakses oleh multiple thread secara bersamaan tanpa menghasilkan kesalahan atau konsistensi yang tidak diinginkan. Artinya, ketika sebuah program atau komponen program dikatakan thread-safe, itu berarti program tersebut dirancang sedemikian rupa sehingga dapat dijalankan oleh beberapa thread secara bersamaan tanpa menghasilkan perilaku yang tidak terduga atau tidak konsisten.