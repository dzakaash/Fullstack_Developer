import java.util.*;

public class set_map {
    public static void main(String[] args) {
//Tipe data Set di Java biasanya diimplementasikan menggunakan kelas-kelas yang termasuk dalam paket java.util, seperti HashSet, TreeSet, dan LinkedHashSet. Setiap kelas ini memiliki karakteristik dan perilaku yang berbeda dalam hal penyimpanan dan pengurutan elemen.
//        HashSet, adalah struktur data yang menyimpan elemen-elemennya menggunakan konsep hashing. HashSet tidak mempertahankan urutan penyimpanan elemen dan tidak mengizinkan duplikasi elemen.
        Set<Integer> angkaSet = new HashSet<>();

        // Menambahkan elemen ke dalam Set
        angkaSet.add(10);
        angkaSet.add(20);
        angkaSet.add(30);
        angkaSet.add(20); // Tidak akan ditambahkan karena sudah ada

        // Menampilkan elemen-elemen dalam Set
        System.out.println("Elemen-elemen dalam Set:");
        for (Integer angka : angkaSet) {
            System.out.println(angka);
        }

//        TreeSet, struktur data yang mengimplementasikan antarmuka NavigableSet dan menyimpan elemen dalam urutan yang diatur. Elemen-elemen dalam TreeSet disimpan dalam urutan yang sesuai dengan komparator yang diberikan atau secara alami jika tidak ada komparator yang diberikan. TreeSet tidak mengizinkan duplikasi elemen dan mempertahankan elemen-elemen dalam urutan yang diatur.
        Set<Integer> numbers = new TreeSet<>();

        // Menambahkan data bilangan bulat ke dalam TreeSet
        numbers.add(5);
        numbers.add(3);
        numbers.add(8);
        numbers.add(3); // Tidak akan ditambahkan karena sudah ada

        // Menampilkan seluruh data bilangan bulat
        System.out.println("Data Bilangan Bulat:");
        for (int num : numbers) {
            System.out.println(num);
        }

//       Linked Hash Set, adalah implementasi dari antarmuka Set yang menggunakan struktur data hash table yang dihubungkan (linked hash table) untuk penyimpanan elemen-elemennya. Elemen-elemen dalam Linked Hash Set disimpan dalam urutan penyisipan, yang berarti urutan penyisipan elemen akan dipertahankan. Linked Hash Set juga mengizinkan adanya duplikasi elemen. Operasi-operasi seperti penambahan, penghapusan, dan pencarian elemen dalam Linked Hash Set memiliki kompleksitas waktu konstan O(1). Linked Hash Set cocok digunakan ketika kita perlu menyimpan elemen dalam urutan penyisipan dan memiliki akses cepat ke elemen tersebut.
        {
            Set<String> linkedHashSet = new LinkedHashSet<>();
            linkedHashSet.add("Apple");
            linkedHashSet.add("Banana");

        }

//        Di Java, tidak ada tipe data yang secara khusus disebut "dictionary". Namun, Java menyediakan struktur data yang serupa dengan dictionary dalam beberapa kelas seperti HashMap, TreeMap, LinkedHashMap, dan sebagainya.

//        HashMap, struktur data yang mengimplementasikan antarmuka Map dan menggunakan konsep hashing untuk menyimpan data. Dalam HashMap, setiap elemen disimpan sebagai pasangan kunci-nilai, di mana setiap kunci harus unik. HashMap tidak menjamin urutan penyimpanan elemen. Pencarian, penambahan, dan penghapusan elemen dalam HashMap memiliki kompleksitas waktu rata-rata O(1).
        Map<String, Integer> dataSiswa = new HashMap<>();

        // Menambahkan data siswa ke dalam HashMap
        dataSiswa.put("Alice", 85);
        dataSiswa.put("Bob", 90);
        dataSiswa.put("Charlie", 75);

        // Mendapatkan nilai berdasarkan kunci
        int nilaiAlice = dataSiswa.get("Alice");
        System.out.println("Nilai Alice: " + nilaiAlice);

        // Menampilkan seluruh data siswa
        System.out.println("Data Siswa:");
        for (Map.Entry<String, Integer> entry : dataSiswa.entrySet()) {
            String nama = entry.getKey();
            int nilai = entry.getValue();
            System.out.println(nama + ": " + nilai);
        }

//        TreeMap, struktur data yang mengimplementasikan antarmuka NavigableMap dan mengurutkan elemen berdasarkan kunci secara alami atau menggunakan komparator yang disediakan. Elemen-elemen dalam TreeMap disimpan dalam urutan yang diatur, yang berarti mereka diurutkan berdasarkan kunci. TreeMap memiliki kinerja yang lebih lambat dibandingkan HashMap, tetapi dapat digunakan untuk mendapatkan elemen dalam urutan tertentu.
        Map<String, Integer> dataBuah = new TreeMap<>();

        // Menambahkan data buah ke dalam TreeMap
        dataBuah.put("Apel", 10);
        dataBuah.put("Jeruk", 15);
        dataBuah.put("Mangga", 20);

        // Mendapatkan nilai berdasarkan kunci
        int stokJeruk = dataBuah.get("Jeruk");
        System.out.println("Stok Jeruk: " + stokJeruk);

        // Menampilkan seluruh data buah
        System.out.println("Data Buah:");
        for (Map.Entry<String, Integer> entry : dataBuah.entrySet()) {
            String namaBuah = entry.getKey();
            int stok = entry.getValue();
            System.out.println(namaBuah + ": " + stok);
        }
//        LinkedHashMap, LinkedHashMap adalah struktur data yang mengimplementasikan antarmuka Map dan menyimpan elemen dalam urutan penyisipan. Elemen-elemen dalam LinkedHashMap disimpan dalam urutan yang sama dengan urutan penyisipan mereka. LinkedHashMap dapat digunakan jika Anda memerlukan iterasi atas elemen dalam urutan penyisipan.
        Map<String, Integer> dataProduk = new LinkedHashMap<>();

        // Menambahkan data produk ke dalam LinkedHashMap
        dataProduk.put("Buku", 50);
        dataProduk.put("Pensil", 100);
        dataProduk.put("Penghapus", 80);

        // Mendapatkan nilai berdasarkan kunci
        int stokBuku = dataProduk.get("Buku");
        System.out.println("Stok Buku: " + stokBuku);

        // Menampilkan seluruh data produk
        System.out.println("Data Produk:");
        for (Map.Entry<String, Integer> entry : dataProduk.entrySet()) {
            String namaProduk = entry.getKey();
            int stok = entry.getValue();
            System.out.println(namaProduk + ": " + stok);
        }

//        //Buitl Function Set
//        1. add(E e): Menambahkan elemen baru ke dalam Set, jika belum ada.
        {
            Set<Integer> set = new HashSet<>();
            set.add(10);
            set.add(20);
//        2. contains(Object o): Memeriksa apakah Set mengandung elemen tertentu.Contoh penggunaan:
            boolean contains = set.contains(10);
//        3.  remove(Object o): Menghapus elemen tertentu dari Set, jika ada
            set.remove(10);
//         4. isEmpty(): Memeriksa apakah Set kosong (tidak mengandung elemen).
            boolean isEmpty = set.isEmpty();
//         5. size(): Mengembalikan jumlah elemen dalam Set.
            int size = set.size();
//         6. addAll(Collection<? extends E> c): Menambahkan semua elemen dari koleksi lain ke dalam Set.
            Set<Integer> otherSet = new HashSet<>();
            otherSet.add(30);
            otherSet.add(40);
            set.addAll(otherSet);
//         7. clear(): Menghapus semua elemen dari Set.
            set.clear();
//         8. iterator(): Mengembalikan iterator yang dapat digunakan untuk mengakses elemen-elemen dalam Set.
            Iterator<Integer> iterator = set.iterator();
            while (iterator.hasNext()) {
                System.out.println(iterator.next());
            }
//         9. toArray(): Mengonversi Set menjadi array.
            Object[] array = set.toArray();
//        10. containsAll(Collection<?> c): Memeriksa apakah Set mengandung semua elemen dari koleksi lain.
            boolean containsAll = set.containsAll(otherSet);
        }

//        //Built Function Map
//        1. put(K key, V value): Menambahkan pasangan kunci-nilai baru ke dalam Map. Jika kunci sudah ada, nilai yang lama akan digantikan dengan nilai yang baru.
        {
            Map<String, Integer> map = new HashMap<>();
            map.put("kunci1", 10);
            map.put("kunci2", 20);
//        2. get(Object key): Mengembalikan nilai yang terkait dengan kunci yang diberikan. Jika kunci tidak ditemukan, akan dikembalikan null.
            Integer nilai = map.get("kunci1");
//        3. containsKey(Object key): Memeriksa apakah Map mengandung kunci tertentu.
            boolean containsKey = map.containsKey("kunci1");
//        4. containsValue(Object value): Memeriksa apakah Map mengandung nilai tertentu.
            boolean containsValue = map.containsValue(10);
//        5. keySet(): Mengembalikan Set yang berisi semua kunci dalam Map.
            Set<String> keys = map.keySet();
//        6. values(): Mengembalikan Collection yang berisi semua nilai dalam Map.
            Collection<Integer> values = map.values();
//        7. entrySet(): Mengembalikan Set yang berisi semua pasangan kunci-nilai (Map.Entry) dalam Map.
            Set<Map.Entry<String, Integer>> entries = map.entrySet();
//        8. remove(Object key): Menghapus pasangan kunci-nilai yang terkait dengan kunci yang diberikan dari Map, jika ada.
            map.remove("kunci1");
//        9. clear(): Menghapus semua pasangan kunci-nilai dari Map.
            map.clear();
//        10. isEmpty(): Memeriksa apakah Map kosong (tidak mengandung pasangan kunci-nilai).
            boolean isEmpty = map.isEmpty();
        }
    }
}
