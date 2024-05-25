public class string {
    public static void main(String[] args) {
//        tipe data kumpulan karakter, teks, harus menggunakan petik dua
        String firstName = "Dzaka";
        String lastName = "Ali";

        System.out.println(firstName);
        System.out.println(lastName);

//        menggabungkan string
        String fullName = firstName + " " + lastName;

        System.out.println(fullName);

//    //Built Function
//        1. String.length(): Mengembalikan panjang (jumlah karakter) dari string.
        {
            String str = "Hello, World!";
            int panjang = str.length();
            System.out.println("Panjang string: " + panjang);
        }
//        2. String.charAt(int index): Mengembalikan karakter pada posisi tertentu dalam string berdasarkan indeks.
        {
            String str = "Hello";
            char karakter = str.charAt(1);
            System.out.println("Karakter di indeks 1: " + karakter);
        }
//        3. String.substring(int beginIndex, int endIndex): Mengembalikan substring dari string berdasarkan indeks awal dan akhir.
        {
            String str = "Hello, World!";
            String substring = str.substring(7, 12);
            System.out.println("Substring: " + substring);
        }
//        4. String.toLowerCase(): Mengonversi semua karakter dalam string menjadi huruf kecil.
        {
            String str = "Hello, World!";
            String lowerCaseStr = str.toLowerCase();
            System.out.println("String dalam huruf kecil: " + lowerCaseStr);
        }
//        5. String.toUpperCase(): Mengonversi semua karakter dalam string menjadi huruf besar.
        {
            String str = "Hello, World!";
            String upperCaseStr = str.toUpperCase();
            System.out.println("String dalam huruf besar: " + upperCaseStr);
        }
//        6. String.trim(): Menghapus spasi di awal dan akhir string.
        {
            String str = "   Hello, World!   ";
            String trimmedStr = str.trim();
            System.out.println("String setelah di-trim: \"" + trimmedStr + "\"");
        }
//        7. String.contains(CharSequence s): Memeriksa apakah suatu string mengandung sub-string tertentu.
        {
            String str = "Hello, World!";
            boolean containsWorld = str.contains("World");
            System.out.println("String mengandung 'World': " + containsWorld);
        }
//        8. String.equals(Object anObject): Memeriksa apakah dua string sama.
        {
            String str1 = "Hello";
            String str2 = "hello";
            boolean isEqual = str1.equals(str2);
            System.out.println("str1 sama dengan str2: " + isEqual);
        }
//        9. String.replace(CharSequence target, CharSequence replacement): Mengganti semua kemunculan sub-string tertentu dengan sub-string lainnya dalam string.
        {
            String str = "Hello, World!";
            String replacedStr = str.replace("World", "Universe");
            System.out.println("String setelah penggantian: " + replacedStr);
        }
//        10. String.split(String regex): Memecah string menjadi array string menggunakan regular expression sebagai pemisah.
        {
            String str = "Hello,World,Java";
            String[] parts = str.split(",");
            System.out.println("Hasil split:");
            for (String part : parts) {
                System.out.println(part);
            }
        }
    }
}
