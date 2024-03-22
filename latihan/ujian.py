# # No.1 Tringle or Not
# # diberikan 3 garis, tentukan apakah garis-garis tersebut dapat membentuk segitiga tak berdegenrasi
# # jika ketiga garis tersebut diletakkan dengan ujung-ujungnya sdisatukan sedemikian rupa
# # sehingga membentuk segitiga yang sudut-sudutnya bukan nol pada setiap titik sudutnya
# # maka terbentuklah segitiga tak berdegenarsi
# def triangleOrNot(a, b, c):
#     result = []
#     i = 0
#     while i < len(a):
#         a_t = b[i] + c[i]
#         b_t = a[i] + c[i]
#         c_t = a[i] + b[i]
#         if a_t > a[i] and b_t > b[i] and c_t > c[i]:
#             result.append("Yes") 
#         else:
#             result.append("No")
#         i += 1
#     return result
# print(triangleOrNot([7, 10, 7], [2, 3, 4], [2, 7, 4]))
    
    
# # No. 2 No Pairs Allowed
# # Untuk setip kata dalam daftar kata, jika ada dua karakter berdekatan yang sm, ubah salah satunya
# # tentukan jumlah minimum substansi sehingga string terakhir tidak mengandung karakter sama yang berdekatan
# def minimalOperations(words):
#     arr = []
#     for i in range(len(words)):
#         count = 0
#         j = 0
#         while j < len(words[i]):
#             if j < len(words[i])-1:
#                 if words[i][j] ==  words[i][j+1]:
#                     count += 1
#                     if j < len(words[i])-2:
#                         if words[i][j] ==  words[i][j+2]:
#                             j += 1
#             j += 1
#         arr.append(count)
#     return arr
# print(minimalOperations(["ab", "aab", "abb", "abab", "abaaaba"])) #0 1 1 0 1
# print(minimalOperations(["obqocctrbbddbwfyroyzsvqoxpirvtdxzwwacohretkfbpbnekfflmbsjnpyymafuyzwggkatxbnzrlxbffyvgcianltlspivdlifeaywggvahvtudgpqcivcqexexgpxxeqamaokprftefyxzdldppouayioxgfwzwqanazzutdmirzxdivjafilglzimjjqraqilrrumxtmqkwqnlakbxyvynxbgbcyutnedrvpcltnbxmkljyowovcjawxkpzyttjsilgvngdfbeikwyumvxczettukedbhybugandzrafbznxuvbanvqchaefbktobiitxlbregamlptlfwjyorpextwfzuayehifvkvibwivkpiuetgxqswpwexabdkfieszhiwmtiqdchkbeyivpykuwouiuxzopebpzxlmjsojwwpnwzezpmuantbgofwkypcdbyuzcfgjdffxxrdnxxyxugselirkniusmjivdlonqnpaiqfcrvkzmawigsjwyodpxbbbdpxjsvxrlmeqospuvsmnmlgthrcgunkcksbxlyngcyqggdcygdijkmsdalckikphzimlysikbemmvcuydnzbzlehxucathwjcpihoctzgbpuvvdiqjanroimapawbkrladvamwoguloizzvwqkfnnxcylxotqiglizvigfkrvvrrnhocsuvlpdvpbsdffetehbugxdmtzutwyknelmcwimqqgmbmzrofhujdbkwszvbtsidpfukilbvrcemlutfkuijsjvybypqvqpikhvsdgfssewezkfkamdebnphpartubkoffoqekguehuiahgevnxkhqnntbcjjrpteyfxnoxdtsppvolhzhaziqiwpwltyezudaljsbzttjzvlsqevvevmfrttsrjduxkhvgzpkwhbvlzexdenzturlutvorhcqgqlkameealodtwkihewpwvxhufulvkdfviovckwbzuijsmyuiyfekwqqglebqwozqnxzhkkuwmdnmxiozqpsyegouyploekkbgerlsvvfvhhrggjfmblkpeiehnztkbvblnpfdjgpllbjmjossmvcuvzkjpudzhfvneuvzwvlxqkkjddezcwwgxedqskhylrbzxocpxrngrftsuvlqtovisbfrgtsozghjlqdpwqbncgbhirrogzpzukswflkpduscsluzaegoiwnxmtzseearsvcfgkzqgpexmwphgbcxzkvpeatctrsofhykihsnvxwjzhcdwcewdwjgozmnqdlyqnwuzcbsogudefippcjlcedsxxyqvjumbveflymqywhdhbeaebkqpqdicxsjesztafwibrtnkkprlxqkrbsbwrwmntkugzkpglhkymjbxagrebbvntxuhrllpdrhxgqomjdjherblzjxiqonvhngsmkkwpgcllbjthztwqjnkxpyiiombbrzsvxvcfibdaajvluesikjjqwqxysclrydkjnnsgrbhzmjlsjoigrjtujjvjlyyacxwddegvzgzbbxvajodxshpifrgosoymrwmkiwwigkyltppuaygobkxxdetgalaceaebohynmrmrrrqsbihjzcsccwmrxcmxkzredypssiuiqqhyiezguzipyxzyefbqsuquttfuzkmbxagtgwupsgkmqpjdlgrphbbbnmfkymoopgscucozmlqgnspynsyugjwlaujsfpmsenzhhpujjxqpfmqzwrubdmzutjlrarbwqnrmzcvnamqjnawhzudevfkmqxmrpyhnnkitvxuhdovwwryzflhofqgfvrkqszjqcogvhuaesgrjvxazuejhwjyrzbguiekolmsulvclvckyymndjjyqsiorgstnqtycztgpwhpiwqzciapbmiwaxlntusjnithlrqmzaxksofieqietaknewvfmtqfsazshrcswvdwvxojlkasgltustotjjbfkzfubwkmujlgohotylskqzjrhryxkcxtblhhfwhfremklbjvfkqwhpsavfkqrmuwrlsueafvxivdrxtoboekgotacnpwgwuqpvqyhymlvsjbtsnsyagnkvutwfhyeanbioqpruefhspbrheejhgqdsqmpprkmptitenbpzzhchvcgpviogpudcvrfeayuzfwosozrrataemkpdilnbxzdmccweizhhcabkrzwivbmugltnkxrlypztgfxxcnwngzpnficlvdecafxzpwhxlvdfehwpoeuzppnyfzzufsqpzdqajbsblgkpwumubreimkirvucdfgerzxnjrtlnvnyzsfjhhulrugatvoqupgdmleteusifswngcahmymmpiqsvqiiaonvjyyjfxzavsfpiyasbvsrncomxlostrynbvmnvfxzffxoopmbezehdghozyedqfqrxtkkohpkildvwpolqxkrteqqmklffykzmlofffpgsxbouhostzkhoeoergriqmttqtlaaurkgjmgqirrxdntjubryhqttusnnsadqfaowgjsiafzpjurnrgvegbfaymvqoaxdyliwvlhkeebbyqzgpssvkjcptvorhptwnnrijqaowbltrwdyyyohxdwhjlfetydhzzgjfxyhoxfxunklcjsrpgenjvspgadsffvekqbfipltfvdtrerlppslyjaxcvxqfgbhyrvjimqwjoxaknbznvzaqhozdtqisupybtfucajlbuhohfxrkspjwjfseysalcdolbajnfublqgrwylpukxopjmzgphfojslwrbdstwnzesmqlbbaeuwlolwkuqeiipdgfkigxkaaarlwudidcefyosyytfaumicmpwqfrmffbznyzqfjwjuzzqldiovmzgvbpmtmbwuunhmozhhcotgumpvwyvmzxirwkmllffhsymlelfwnckpoqxxrkckkywzsjzrizyvblbtuvqzvmjhmrisryymajmfvbyefmzmmkdoggfrvmculynfaisgwvnfevbfflmuzfconltqaqwcfgfwlqhvngbymfqbnekthebtpguxhbstiovqmrmuaaerqfbtvpoliyobnjhuwamntuhdypwodcmgljsemtiddussabgdqotppmjkqrknogjccuphkpgajeuffkyfprbkhcqwogjgqomkeevqzmqllkxwtmflthcybetlkncidnkbddcrjuiefpxxsefrxagftsccadeuqxiewopclktldzdrmrhhzsmhyucqvkgryimceqsadmmnqrsyvumhojlaaeswzjefismmjuffrinthynwfgnvjobhzncycenzmvsuoaasyqllcapmskslumbzbapwhgrtmxoomlmfhchznotpngojrorhurebdxpemmpbjzpkgzthrvuwensdhlvlqwmsuznptmctwrrocacxlsrgvmkxpxcrjabyxvvgxrqsmqenzwrkrieueexamnydlgkvzzdrwnzuafbbabpiutqvsljcccuugasbrkqngadstsrzfwxrypenwuqfusmeciiabhotfzbjlytfuoprdipwtgoguvypjcxguokurvezbtweofcjcadtdeqtffmrheqnwfyshqelaonlpoadqduayobjcxtfknpttjgafuwzrbaulwoqcrfrdnjuorfujxihnxedpjvocmdkexcxalddkogqgqesmnavnhjbnmkfoyccsqqupxcpbpdbrqlmklsgdpdnvfntguvgjynpdqpsptjgqsquhijqwkieeuyarvlvxwvbsninwvcnjiyvkzfjdnvreaybsimpgadyfjlujpttpuwoivosmhfcrxdwnavcagqmvjrsbstdkvkutgnqylwbdoxanvywnfbedgupugwtiutfrdrjohoqwipjifhdwbddkpqyuybvrtqjeidiedhrdaefkprrbbgwjsihxsskjztpsoduydimddlafignleoiangfwzfipdhnrtzzkqzbujdfxflutitrvqtfwenlxwlkkxqxkrqamymrbrxnarykmmgezdsvgdkqmgwegkerbwopbwtyimzzgnycmfmepnrqsrfhgbttnevkpigkvylcviqzabqgjyrkjevswmbyeofcaajsqvraemhejbbbhwaosylrzlptitzxwcqsibasiuhmumvhazcqjkeahmgxsclxkrlhjksepzslkedymtxovichoorwagruioxlplylvrshxpyjterrugubrdrbctgcciswykekanlyihgvwiolsduzgulsgsjczbsdwpeiqynsaqdutjzwohlmopgftjbmhifexrlzilevdtonklgevsoqcjzayuhzfrkrqebyhwlfjclvmfkmhsajargvgllyxzijadyjnkpqyuxtrrhtsgduairopdazujvlryzrqcjxulabsrchxbawfdvnhcnphpxohuuidpdvwvfdqutytghxajgirhagjbrhkryeuaxagsjadxogxougwjewlslbpkvyqluzcmzdscbkpbibfecrpfnyewjbsembjgobktigyggnnfvrdoinnunjtigghfmukprorlabxztniyxacphcarywszlzuhassuuuglswemzgmoweldaknuhpocxbkcsqiyyhlotnvlzbllxoahtvgvskojcsyymsmqmbshcuxptrvzazpgkiehvmdlpcwouziljjibnyrfsmphjvfgtpxxuadjkgvxkanodydfwulteznzonwnhughfiascdrtkybykkdyuvhergtoizaoqjmwsatttmfobmhzckgxomsiadgxfegmywodsftdesdkwuhsdgueagfwhukustpmhxlgvdpgiwjapvfuoeidtqmcjsrqtzryaysztgnwqrigcdvykykfuugegqkbgckygxdogytxatpdplwrzbifrjgfrphzuebdmltsndllnzjdyezdjrjlrcvjkiuoirbldcqudrlozqtpiymqrevbrbichicrhybmzoafuxmjaaukoymijwgevtsnkdejfunliyqnbdincmbafyjiwqygsczizsajosqmrovohiccnvgwtdgvapcgwhqpnbcanoggvhahfrgkupbozdiqkxfhpkkxwiegmtqroqkfaobhysftnpqqrxdwonxofbdxqtgphzazcfsulnsfavrxabrvxqllvywtjzivzlyypjhavfmrzymwkbocdljzcwsrrzbqhfchyuicfluefmyicomecmfluhxswdqssyckfrurzmnvscfdulzvlexdlvhzawsmcivgyfdaezjfuijfkeqqepjprqjmbtzexzylnyrqzprfyfgsfwusoygzsjkbiznaaayjtjlblkwctassnyqpiqvduhatanxsibsyfjizpqddqvamihpsdncehnhcpnqzhznzddkmpfqelfxyclqegcgzobbhmgjvuzohpuipchcuzkxczrlsjjuymfvkmhsqccdmmrwqzuarutpbdxmjiejlsfbqogygzdrtrvjzmlxuxjlvxswbqqfvrtylzjkwsscfyvxbxnjjpnaplxsegudxcaegejeeqklaxtguvirwsclsessoqsxhtbgkujhodmuuyrfypyuoxsgvrqtpnttbqledvuuptyapnapqkbteyezxluzmogtwyrllylrlsodblfxeukugtpbculdzcmkvajpediiuvnajcgntvkgxhydnjsgcafjkmsuebesnxyatprghvtbsktjezmpfzrkupwjxhziguqqgwavtlmnderuugnnzlokqlntwxajuvmumgyibzjqilnisodfsfrxvhglnadwsfktcgcsiyvmcoxgtyqereiwnyzejerymknegpntteymqkofdvgzodobelrxflheopujqiifsntkmccppoqbqdgatifvxttoatmioblcztgsihjrgkghjynulafquhghfzwwzwquqtotvzrcjktnxboqsdznvntyqozgbuxcfepumhsndejsrbjupftfjvqlsvbrskhnaawukapnxwyngoqjkcbmqotfmdvewvbjxvhueeukamlfmuegpdxvvqgsfqozxibryosgbkqnrzdapnltwbofynkxcvsereneevpxqgbgqvvqasxcjohcnzsyrvtltymhugrltxsdpgckynpkfktqnarzdfvhbuddypazajrwbnfaxqbutdysbujbercypzgiqvrsajeuqiwazifhzfiwlooiekksfjxycuvwwidinzszvwfllxzcztjwyvinboswhzqpojrxgezjaxxmxurrfshlspmignuwieucsaenqzzzwlhisayybtcrdmhalxybnomyqysrwmoitvszwqxzwfxhptrymfudppneurwsdsrjqsvgzxcyqskurhzwkbbxdsvydwisiqxiutypjkpzchcioqqpnvukoammoybzujpnmnivonccttyeyrixxdokxaimjhrfsoamtldygrovebcleifdzqaehsokcykewobkuaehdezgmeqdvejuyunpolujlwknvarohhysbysthqwupenhypkfdvnzmsnqbuknvjlekcaeugqurgpjlcoiupkfywxlkrmjymjnvtftkygcmmhbbzhfhphmznbsxkdlzgpkakaaegkmbgfrhyvwfxnzkxtsopovhfjgvnxciasjjelcldkgjemrpgpblapbnbolbcbebpmavhujmpfjvxojuqqixhplrsxenkfeganxmgznquhixjwkaggauxkxuysmdsxoiucudkyolwmeobpgavsptabyvzwrokhtpcolyycbncldfaecexovdvqhyizowumprawwhvljelzukpegoqzazetjgioejfnfgbnnxenyrvjqgrejbzjfjxphgqmgiluhgkhqqhusgfqgaoucrwwybseuuibwychtaakdokobktnlhueainmatlruwvfaxzfsllzqngfdccuefrfhzvvvvrbssumetxxnjltzhoefgchypcpmkxtnzrhsnrwhgrynwsjkwsgvdxfdvimclirbofffcikeksjryywokkayenpkjovvpfqldnkpfjxmadaonnjglemigrlvawrabzlrjkjkhvrthyicynstfstmecrvglhxamxzmvezzvmmakguhafeknnzxcxkdqxxxdpiaqucgttfjwglanpqyncwiusyadafdtaeoovgecpvgypmhetuiibqxkxspaacqwskohagpstzfiewvrxpusyjmaordcsojqukqaurswaanrhorquhdrbenwgdedukgeccryidzazrwzmlkycxopnfkvewbroktlokcxgdfqbqlnprmmyjebycgequkcnqkxuujtjntwmkydolcixwmzkpvcwukcitvfesxxclucrzzhdqvnlqktohcybyxljorxxldcekgprxsykzqvvnktnkehiyirwgbchiufwkmqxfjgqqzjdzfnodbepkajiizzxcggmoqyajmwsvhwsueoeibftrigomdinvgfufdihjlaojigwobmzrqtvhplnwmlbzglgjpqnvywfrljvesmxlhwnofiacxbbfypeuliwvioelgjmidclgswztufgvqvswjzlkfwbekllncmaghqsiufdpdkukdsysazizgvfkdhhgujwlsbbbxnmiqqplunlprqekapimtzuimgxkjsitqxzmudsdfxfmgoivuqveumbwocilnomhogmhugygrlsgtjkfudxplzyfryueuchpphkwjwagstwryiifygzlgeszvwhrjthzyjrgpzeancwvxvsfspncshycoymrvsroxcezqknktpxjvizrdlrtlwkcecykgsfrpusytdvjalmxopsyatjklwtxpjwiiqhczriwxzakjdztcseuiwfkccnoudkyuvcgfhhfxmpoxdymtbaecgjptmmsnahsblwldgjntnhonozftdzpdzjdxyjtqfaizswpzgvuiuwvmmlyzjwujcufflzjwikubmbcbicluznjmotbcptcwfqwifidtjrrllznndjomeproqybczcuijinuuxwzvkdpvkktsxnqbgfzdebqtfribaxttuihbjjbuwvyroudpztxmnouiqftfrqznwwqjjizxmnklvrqnkfbefqbyybgdhyavwcpuivieggbakuuulfnrakadzgcbuwrtkyundylnpkqolyrgbheboaupdmjyonepqefeeohzfgaiuugzkrlaanfbfftpoxrtoeesaykmqxmragzyherjidyvmqgihidiclymddggxqinaunovpivrombiddsgoxelrmlrrzeslppcxljvcudolgrqxcsagaumknxefkxojjmzzbkipcjxvwvhbcqlirsndmvjhtxjypeegzncduuaynzwkfjnxpkibhwoppryaefienyryxvkukkqwsrudzxliwkgahlcbnwlhgtavgqtqyqxrllrewgxkrgacpppoxqaotyiyhuqzalfbjbimyffhzrqdqnczgrajnfojeifwcixiuetfjkqeinfrdqlafyedbeypohqwdbhntevlocuzbxqjtvmizwvpgkplnettalbobzkvgsiejugyiahnhrqzfqunslvvfyyohqaeinkwirdpuftgchmktabizoogbfpsuxbudtunaefxqsebcnxhmkvatwssioiyhpbufhaopwwdblcdojnkgjtwzudjfregikjgquhjfdiqomwfkmxnuwtwhddjfomrmrrctyjacmoxqyydshdaxeaqtnzaonzgvbjdnfnwmkrxvlrwyslyeyrbuofndnqteccmziuupxuoidluzfvqdlmfmmlualbtfvalsfrpqcsfjsslmajmtwowbxargdszancgxectsqqloljmnbtnbkapzgfgvjteudbvlxhxkknsaxikrptcvkaxgcwtplmxuovugkaqnjpyvpalsgzpeidmejfyawdlftrgvtfmbvquiogobjgqxobcdplzrtwouvvhynjffzexjnwrzimhihrwlszctoontqvfczetrxcmrdhaskwjhacsciqrbgmgvlgsahdtuhmypeluwxfktjvunttjahbkhtvssqmlclnnvxsoqyfluxsqtimnamdwszusbglbxosagwdawburaukgghxhvhcijmforpyorqfzcuoloknwtgtzbcshookcirookqvsggqtwoyozutpfgyptcuovopefkubynqnzsawdgcrlwzngpmnzgylezyoafrxvimseidyqqwxlspvadgljbnsaprbryhrtzruawrrhxivjfjdopmhlmfcfzpyvmcrnmlkmwnyhvbmlqcqqymvtuvxsgnuqmalrhxpufihmebscmxjtjckgduuoaushkjjsvvxmhuqfwobgbsybiqouqlulwsfzzeawdfoitccykikbnwjqvdfbclhhuihqaloyootujccfandbvsxilusfbswxhttdznddcjuloiwmsxkqxoqenuxqgyuhrueytlxgyqchuuvhddmolqdvhdkzaaybwmdnqapampbyefxehjrhhwlnutppgmxlywtvgkmjivblzlsmfavpchiwglblcqwoxkzxfzpwtppsbzirlenmdyubgpuezovonrlleidndh"])) #0 1 1 0 1

# #No. 3 Longest Even Length Word
# # Misalkan sebuah string, kalimat, kata-kata yang dipisahkan oleh spasi
# # dimana setiap kata merupakan substring yang hanya terdiri dari huruf abjad bahasa inggris
# # Temukan kata pertama dalam kalimat yang panjangnya bilangan genap dan lebih besar dari atau sama dengan panjang kata lain yang panjangnya genap dalam kalimat tersebut
# # jika ada beberapa kata yang memenuhi kriteria, return kata yang muncul pertama kali dalma kalimat
# def longestEvenWord(sentence):
#     longest = "00"
#     sentences = " " + sentence + " "
#     for i in range(len(sentences)):
#         for j in range(len(sentences)):
#             if i < j:
#                 if sentences[i] == " " and sentences[j] == " ":
#                     if len(sentences[i+1:j]) > len(longest) and len(sentences[i+1:j])%2 == 0:
#                         longest = sentences[i+1:j]
#                     break
#     return longest
# def longestEvenWord(sentence):
#     words = sentence.split()
#     longest = ""
#     for word in words:
#         if len(word) % 2 == 0 and len(word) > len(longest):
#             longest = word
#     if longest == "":
#         longest = "00"
#     return longest
# print(longestEvenWord("you"))

# #No. 4 Maximum Information, 
# # Ada jaringan komputer yang terdiri dari n server, atau node
# # diberi nomor dari satu sampai n
# # setip node memiliki nilai keamanan security_cal[i]
# # Seorang peretas harus memilih titik awal, mulai melompati jaringan yang menyusupi server di sepanjang jalan hingga mencapai akhir
# # Dari node x, hacker dapat melompat ke node (x + k)
# # Jik node (x + k) tidak ada, lompatan keluar dari jaringan dan peretasan berakhir
# # Awalnya peretas memiliki akses ke 0 sever dengan nilai kemaanan 0
# # Nilai kemanan pada setiap node yang disusupi ditambah ke jumlah nilai keamanan peretas, dan nilainya mungkin negatif
# # Tugasnya adalah memiliki node awal secara optimal sehingga peretes dapat menyusupi server dengan jumlah nilai kemaann semaksimal mungkin
# def gainMaxValue(security_val, k):
#     max_count = min(security_val)
#     for i in range(len(security_val)):
#         count = 0
#         j = i
#         while j < len(security_val):
#             if i <= j:
#                 count += security_val[j]
#                 j += k
#         if count > max_count:
#             max_count = count
#     return max_count
# def gainMaxValue(security_val, k):
#     max_count = sum(security_val[0::k])
#     for i in range(len(security_val)):
#         count = sum(security_val[i::k])
#         if count > max_count:
#             max_count = count
#     return max_count
# def gainMaxValue(security_val, k):
#     return max(sum(security_val[i::k]) for i in range(len(security_val)))
# print(gainMaxValue([2, 5, -8, -6, -7], 3))

# # No. 5 FizzBuzz
# # Diberikan nomor n, untuk setiap bialngn bulat i dalam rentang 1 hingga n inklusif
# #cetak satu nilai perbaris, 
# # jika i adalah kelipatan 3 dan 5 cetak FizzBuzz,
# # jika i kelipatan 3(tetapi bukan 5), cetak Fizz.
# # jika i kelipatan 5 (tetapi bukan 3), cetak Buzz
# # jika i bukan keduany ceetak nilai i
# def fizzBuzz(n):
#     for i in range(1, n+1):
#         word = ""
#         if i % 3 == 0:
#             word += "Fizz"
#         if i % 5 == 0:
#             word += "Buzz"
#         if i % 3 != 0 and i % 5 != 0:
#             word = i
#         print(word)
# print(fizzBuzz(15))

##########################
# No. 1 K-Subarrys
# k-subarray dari sebuah array adalah subaray(elemen yang berdekatan), jumlah unsur-unsurnya habis dibagi k
# tentukan jumlah k-subarray yang dikandung dari sebuah array
def kSub(k, nums):
    k_subarray = []
    for i in range(len(nums)):
        subarray = []
        for j in range(len(nums)):
            if i <= j:
                subarray.append(nums[j])
                if sum(subarray) % k == 0:
                    k_subarray.append(subarray)
    return len(k_subarray)
print(kSub(5, [5, 10, 11, 9, 5]))

# No. 2 error Log Extraction
def extractErrorLogs(logs):
    failed_log = []
    for log in logs:
        if "failed" in log:
            failed_log.append(log)
    for h in range(len(failed_log)):
        for i in range(0, len(failed_log)-h-1):
            # ini tahun [0][6:10]
            if int(failed_log[i][0][6:10]) > int(failed_log[i+1][0][6:10]):
                failed_log[i], failed_log[i+1] = failed_log[i+1], failed_log[i]
            elif int(failed_log[i][0][6:10]) == int(failed_log[i+1][0][6:10]):
                # ini bulan [0][3:5]
                if int(failed_log[i][0][3:5]) > int(failed_log[i+1][0][3:5]):
                    failed_log[i], failed_log[i+1] = failed_log[i+1], failed_log[i]
                elif int(failed_log[i][0][3:5]) == int(failed_log[i+1][0][3:5]):
                    # ini hari [0][0:2]
                    if int(failed_log[i][0][0:2]) > int(failed_log[i+1][0][0:2]):
                        failed_log[i], failed_log[i+1] = failed_log[i+1], failed_log[i]
                    elif int(failed_log[i][0][0:2]) == int(failed_log[i+1][0][0:2]):
                        # ini jam [1][0:2]
                        if int(failed_log[i][1][0:2]) > int(failed_log[i+1][1][0:2]):
                            failed_log[i], failed_log[i+1] = failed_log[i+1], failed_log[i]
                        elif int(failed_log[i][1][0:2]) == int(failed_log[i+1][1][0:2]):
                            # ini menit [1][3:5]
                            if int(failed_log[i][1][3:5]) > int(failed_log[i+1][1][3:5]):
                                failed_log[i], failed_log[i+1] = failed_log[i+1], failed_log[i]
    hence = []
    for j in range(len(failed_log)):
        text = ""
        for fail in failed_log[j]:
            text += fail
            if fail != failed_log[-1]:
                text += " "
        hence.append(text)
    return hence
print(extractErrorLogs([["01-01-2022", "18:00", "CRITICAL", "failed"], 
["01-01-2023", "15:00", "ERROR", "failed"], 
["01-01-2023", "16:00", "SUCCESS", "established"], ["01-02-2023", "15:00", "ERROR", "failed"], ["30-01-2023", "15:00", "ERROR", "failed"], ["01-05-2023", "16:00", "ERROR", "failed"], ["01-05-2023", "16:30", "ERROR", "failed"], ["01-01-2023", "12:00", "SUCCESS", "established"], ["01-01-2024", "01:00", "ERROR", "failed"]]))

# 3. Paper Sheets
# bangun datar peregi panjang h*w
# dilipat menjadi h1*w1 dengan jumlah gerak minimum
# hany dilipat sejajar dengan tepinya dan setelah dilipat dimensinya harus bilangan bulat
# def minMoves(h, w, h1, w1):
#     moves = 0
#     ha = h
#     while ha != h1 and ha > h1:
#         if ha/2 > int(ha/2):
#             ha = int(ha/2) + 1
#             moves += 1
#         else:
#             ha = int(ha/2)
#             moves += 1
#     wa = w
#     while wa != w1 and wa > w1:
#         if wa/2 > int(wa/2):
#             wa = int(wa/2) + 1
#             moves += 1
#         else:
#             wa = int(wa/2)
#             moves += 1
#     return moves
# print(minMoves(8, 4, 6, 1)) # 3
# print(minMoves(2, 3, 2, 2)) # 1
# print(minMoves(6, 3, 3, 1)) # 3

# No. 4 Counting Bits
# berapa banyak 1-bit dalam representasi binernya?
# representasi biner dengan n memiliki k bit signifikan yang diindeks dari 1 hingga k. Apa posisi masing-masing 1-bit dalam urutan menaik?
# def getOneBits(n):
    

# No. 5 Maximize the Value
# Susun ulang array bilangan bulat sehingga nilai terhitung U dimaksimalkan.
# diantara pengaturan yang memenuhi pengujian tersebut pilihlah susunan dengan ururtan mnimal
# 
# def rearrange(arr):