public class noprimitive {
    public static void main(String[] args) {
        //        tipe data bukan primitiv, hasil perkembangan dari tipe data primitiv, nama tipenya berbeda walau hanya huruf besar
        Integer iniInteger = 100;
        Long iniLong = 100000L;

        Byte iniByte = null;

        System.out.println(iniByte);

        iniByte = 100;

        System.out.println(iniByte);

//      konversi
        int iniInt = 100;
        Integer iniObject = iniInt;

//        bukan primitive ke primitive

        short iniShort = iniObject.shortValue();
        long iniLong2 = iniObject.longValue();
        float iniFloat = iniObject.floatValue();

        Long amount = 1000000L;
        amount.intValue();
    }
}
