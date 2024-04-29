import java.util.Date;

public class integer {
    public static void main(String[] args) {
//tipe data integer, byte(1 bit, 2 digit), short(2 bit, 4 digit), int(3 bit, 9 digit), long (8 bit, 19 digit, tambahkan : diakhir jika dibedakan dengan int)
        byte intByte = 100;
        short intShort = 1000;
        int intInt = 1000000000;
        long intLong = 1000000000;
        long intLong2 = 100000000L;

//tipe data floating, float(4 bit, tambahkan F diakhir), doube(8 bit, bisa tambahkan D diakhir)
        float intFloat = 10.10F;
        double intDouble = 10.10D;
        double intDouble2 = 10.10;

//Kode literals
        int decimalInt = 34;
        int hexInt = 0xFFFFF;
        int binaryDecimal = 0b01010101;

//Kode Underscore, hanya digunakan untuk pemisah saja
        long balance = 1_000_000_000;

//Konversi tipe data number
//Widening Casting (Otomatis): byte>short>int>long>float>double
//Nerrowing Casting (manual), bisa loncat
//        byte iniByte = 10;
//        short iniShort = iniByte;
//        int iniInt = iniShort;
//
//        int iniInt2 = 1000;
//        byte iniByte2 = (byte) iniInt2; // harus berhati-hati jika mengubah tipe data yang kapasitasnya berbeda

//        Operasi Matematika
//        Penjumlahan, +
//        Pengurangan, -
//        Perkalian, *
//        Pembagian, /
//        Modulus, %
        int a = 100;
        int b = 10;

        System.out.println(a+b);
        System.out.println(a-b);
        System.out.println(a*b);
        System.out.println(a/b);
        System.out.println(a%b);

//        Augemented Assignment, operasi ke diri sendiri
        int c = 100;
        c += 10;
        System.out.println(c);

        c -= 10;
        System.out.println(c);

        c *= 10;
        System.out.println(c);

//        Unary Operator, ++ (tambah 1), -- (kurang 1), - (negative), +(positive), !(kebalikan)
        int d = 100;

        d++;
        System.out.println(d);

        d--;
        System.out.println(d);

//        //Buitl FUnction
//        1. Abs(int), mengembalikan nilai absolut dari bilangan bulat yang diberikan.
        {
            int number = -10;
            int absNumber = Math.abs(number);
            System.out.println("Nilai absolut dari " + number + " adalah " + absNumber);
        }

//        2. Math.max(int a, int b), mengembalikan nilai terbesar dari dua bilangan bulat yang diberikan.
        {
            int x = 10;
            int y = 20;
            int maxNumber = Math.max(x, y);
            System.out.println("Nilai terbesar antara " + x + " dan " + y + " adalah " + maxNumber);
        }

//        3. Math.min(int a, int b),  mengembalikan nilai terkecil dari dua bilangan bulat yang diberikan.
        {
            int x = 10;
            int y = 20;
            int minNumber = Math.min(x, y);
            System.out.println("Nilai terkecil antara " + x + " dan " + y + " adalah " + minNumber);
        }

//        4. Integer.parseInt(String), mengonversi string menjadi bilangan bulat.
        {
            String strNumber = "100";
            int number = Integer.parseInt(strNumber);
            System.out.println("String " + strNumber + " diubah menjadi integer: " + number);
        }

//        5. Integer.valueOf(int), mengonversi bilangan bulat primitif menjadi objek Integer.
        {
            int number = 100;
            Integer integerValue = Integer.valueOf(number);
            System.out.println("Integer value dari " + number + " adalah " + integerValue);
        }

//        6. Integer.bitCount(int i), menghitung jumlah bit yang diatur ke 1 dalam representasi biner dari bilangan bulat yang diberikan.
        {
            int number = 10; // Representasi biner: 1010
            int bitCount = Integer.bitCount(number);
            System.out.println("Jumlah bit yang diatur ke 1 dalam " + number + " adalah " + bitCount);
        }

//        7. Integer.toString(int), mengonversi bilangan bulat menjadi string.
        {
            int number = 100;
            String strNumber = Integer.toString(number);
            System.out.println("Integer " + number + " diubah menjadi string: " + strNumber);
        }

//        8. Integer.toBinaryString(int), mengonversi bilangan bulat menjadi string biner.
        {
            int number = 10;
            String binaryString = Integer.toBinaryString(number);
            System.out.println("Representasi biner dari " + number + " adalah " + binaryString);
        }

//        9. Integer.toHexString(int), mengonversi bilangan bulat menjadi string heksadesimal.
        {
            int number = 255;
            String hexString = Integer.toHexString(number);
            System.out.println("Representasi heksadesimal dari " + number + " adalah " + hexString);
        }

//        10. Integer.valueOf(String), mengonversi string menjadi objek Integer.
        {
            String strNumber = "100";
            Integer integerValue = Integer.valueOf(strNumber);
            System.out.println("String " + strNumber + " diubah menjadi integer: " + integerValue);
        }

    }
}
