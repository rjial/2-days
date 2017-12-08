# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image hitori biasa = "hitori_biasa.png"
#image hitori senang = "hitori_happy.png"
image hitori senang = "2.png"
image hitori senang2 = "6.png"
image hitori tanya = "1.png"
image hitori rencananesedih = "hitori_rencananesedih.png"

define a = DynamicCharacter("name", color="#c8ffc8")
define h = Character("Hitari", color="#59a3a8")
define gk = Character("???", color="#ff0000")
define k = Character("Koira", color="#6344a5")
define b = Character("Beni", color="#2eda32")
define d = Character("Bu Delia", color="#1500ff")

define he = Character("º»¼½¾¿ÀÁÂÃÄÅÆ", color="#0000ff")

# The game starts here.



label start:

    $ ragelemmoleh = False
    $ raisokngesave = False
    $ renpy.block_rollback()



label prompt_for_name:
    $ gkoira = glitchtext(8)
    $ ui.text("Ketik Nickname Anda", xalign=0.5, yalign=0.4)
    $ ui.input('', xalign=0.5, yalign=0.5)
    $ name = ui.interact()
    if name == '':
        $ name = 'Kontol'


label scene_01:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    # scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    show black
    with dissolve

    centered "Suara alarm berbunyi. . ."

    hide black
    with dissolve

    a "Namaku [name], Aku menjalani kehidupan layaknya orang normal"

    a "Aku tinggal bersama adikku , status single , hoby hanya melihat kartun 2D tetapi aku menutup-nutupinya"

    a "Sebagai seorang kakak dan juga seorang OSIS aku harus lebih tegas"

    # This ends the game.

    # return

label scene_02:

    "Suatu Hari di sekolah"

    show hitori senang


    h "Kakak.. kakak!!"

    a "Ohh, maaf-maaf aku melamun"

    hide hitori senang

    show hitori tanya



    h "Moh, apakah ada sesuatu?"

    a "Tidak-tidak ada apa-apa kok"

    hide hitori tanya

    show hitori senang2

    h "Akhir-akhir ini cuaca semakin panas ya kak"

    a "i.., i.., iya"

    hide hitori senang2

    show hitori tanya

    h "Apa kakak kecapekan karena cuaca seperti ini?"

    a "Tidak-tidak, mana mungkin, hehehe....."

    hide hitori tanya

    show hitori senang2

    h "Kakak kan otaku hahaha"

    a "Ah bisa aja kamu ini"

    hide hitori senang2

    show hitori senang

    h "Omong-omong kak aku pulang agak terlambat nanti, jadi nanti pulang saja langsung"

    hide hitori senang

    menu:
        "Tidak , kita akan pulang bersama-sama , aku akan menunggumu":
            jump scene_02_01
        "Baiklah , aku akan memasak makanan kesukaanmu nanti":
            jump scene_02_02
        "Emang ada urusan apa?":
            jump scene_02_03

label scene_02_01:

    show hitori senang2

    h "Tidak kak , jangan. Lebih baik kakak menunggu saja dirumah oke. Soalnya ini sampai malam"

    #show hitori rencananesedih

    a "Ohh, Oke"

    "*Suara bel berbunyi*"

    hide hitori senang2

    show hitori senang

    h "Baik kak , aku kembali ke kelas dulu . Bye Bye"

    hide hitori senang

    jump scene_02_01_01

label scene_02_02:

    h "Benarkah?? Terima kasih kakak!"

    a "Ya sama-sama. Hati-hati ya"

    h "Baik!"

    "*Suara bel berbunyi*"

    h "Baik kak , aku kembali ke kelas dulu . Bye Bye"


    jump scene_02_01_01

label scene_02_03:

    h "Anggota ekskulku kena hukuman piket hari ini, sudah lama ekskulku tidak piket"

    a "Ohh , jadi sampai jam berapa?"

    h "kira-kira sih......."

    "*Suara bel berbunyi*"

    h "Baik kak, aku kembali ke kelas dulu nanti aku hubungi. Bye bye"

    a "Oooii!..."

    a "Ya sudahlah"

    jump scene_02_03_01

label scene_02_03_01:

    a "Adikku belum muncul-muncul di gerbang sekolah"

    menu:
        "Menunggunya":
            jump scene_02_03_01_01
        "Menuju rumah duluan":
            jump scene_02_03_01_02
        "Mencarinya":
            jump scene_02_03_01_03

label scene_02_03_01_01:

    a "Lebih baik aku menunggunya disini"

    "Jam 8 Malam"

    h "Loh kakak??, apa yang kakak sedang lakukan disini?"

    a "Tentu saja menunggumu aku khawatir"

    h "Ma-maaf, seharusnya aku memberitaumu lebih awal tadi"

    a "Baik-baik, ayo kita pulang"

    jump scene_03

label scene_02_03_01_02:

    a "Lebih baik aku menunggunya dirumah"

    jump scene_02_01_01

label scene_02_03_01_03:

    a "Lebih baik aku harus mencarinya"

    jump scene_02_03_01_03_01

label scene_02_03_01_03_01:

    h "Kakak? Apa yang kakak lakukan"

    a "Ya, kamu masih belum memberitahu jam pulangmu"

    h "Kira-kira malam kak"

    a "Malam?"

    menu:
        "Tidak , lebih baik kita pulang! Meskipun ekskul kau harus mematuhi jam keluarga":
            jump scene_02_03_01_03_01_01
        "Baiklah , hati-hati . salam keteman-temanmu, jangan sampai larut malam":
            jump scene_02_03_01_03_01_02

label scene_02_03_01_03_01_01:

    h "Tetapi kak"

    a "Tidak, aku telah berjanji ke mama papa Hitari, ini demi kebaikanmu"

    h "Ba-baik (wajah Hitari sedikit menangis)"

    $ ragelemmoleh = True
    jump scene_03

label scene_02_03_01_03_01_02:

    h "Iya kak, terima kasih"

    a "Ya sama-sama"

    $ ragelemmoleh = False
    jump scene_03

label scene_02_01_01:

    a "Sudah hampir jam 8 malam , Hitari masih belum pulang."

    "*Suara HP*"

    "SMS “aku perjalanan pulang diantar temanku , kakak tidur saja dulu”"

    a "Heh... Tidak ada pilihan lain selain mematuhi perintahnya."

    "SMS “baik hati-hati di jalan”"


label scene_03:

    a "Aku bangun pagi seperti biasa"

    a "Melihat HP tidak ada satu notif pun , kecuali yang dilihat 1 sms"

    if ragelemmoleh:
        jump scene_03_alt
    else:
        jump scene_sms_tolong

label scene_sms_tolong:

    "SMS 'TOLONG AKU' "

label scene_04:

    a "Aku langsung bergegas ke kamar Hitari."

    "*Tap-tap-tap-tap*"

    a "HITARI!!"

label scene_05:

    a "Hitari bangun!!!!"

    "Membukakan pintu ternyata Hitari masih tidur nyenyak"

    a "Aku tunggu di meja makan, aku akan masakan sosis bakar"

    "*menutup pintu*"

    a "SMS itu dari siapa ya?, ah tak penting yang penting aku harus segera memasak"

label scene_06:

    h "Moohh , sosis lagi?"

    a "Maaf, maaf besok aku buatkan omelet"

    h "Asik, makasih. Aku suka kakak"

    a "Iya iya"

    h "Omong-omong kakak maafkan aku, HP ku hilang di taman belakang sekolah kemarin"

    a "Tunggu dulu?, Apa? Tapi kenapa kamu bisa sms kemarin?"

    h "SMS?"

label scene_07:

    a "Ini buktinya..."

    h "Mana, nggak ada gitu"

    a "Huh?"

    "*melihat HP*"

    a "Mungkin sudah kehapus kali ya, omong-omong kenapa kok bisa hilang? Kemalingan?"

    h "Karena aku lari ketakutan"

    a "Kenapa?"

    h "Aku melihat sebuah putih-putih di taman kemarin saat pulang ekskul"

    a "......?"

    h "Apa kakak percaya hantu?"

    menu:
        "Ya":
            jump scene_07_01
        "Tidak":
            jump scene_07_02

label scene_07_01:

    a "Iya aku percaya"

    h "Ahaha, Cuma bercanda kok kak. Ekspresi kakak keliatan banget tuh. Baik kak, baik kak ayo kita berangkat sekolah"

    jump scene_08

label scene_07_02:

    a "Mana mungkin aku percaya, hantu itu kan tidak ada"

    h "Benar juga ya, memang dia tidak ada. Baik kak ayo kita berangkat sekolah"

    jump scene_08

label scene_08:

    "Sekolahku menerima siswa smp dan juga sma. Sekolah ini sudah memiliki prestasi yang sangat besar, dan siswa siswi disini semuanya sangat ramah-ramah"

    gk "Ohayou"

    a "Ohh pagi juga Koira"

    k "Pagi...., Tidur larut?"

    a "Ahahaha..... Tidak kok"

    k "Wajahmu kriput tuh, hahaha"

    a "Mungkin sibuk dengan tugas OSIS"

    k "Repot ya jadi OSIS, suara nadamu juga sangat berbeda sekarang, apa karena LDKS hari sabtu kemarin?"

    a "Ya semacam itulah, baiklah ayo kita masuk. Aku ingin istirahat di kelas"

    k "Baik-baik"

label scene_09:

    gk "Yo [name]-kun"

    a "Pagi Bento"

    gk "Jangan panggil aku itu, panggil aku Beni"

    a "Baik-baik, pagi juga, jadi ada apa?"

    b "Apa kamu mau ikut sepulang sekolah denganku sepak bola?"

    menu:
        "Ya":
            jump scene_09_01
        "Tidak":
            jump scene_09_02

label scene_09_01:

    b "Bagus, aku tunggu di lapangan nanti"

    jump scene_10

label scene_09_02:

    b "Kenapa? Apa kamu masih capek? Maaf deh"

    a "Maaf aku lihat dulu, kemungkinan bisa kok, kemungkinan?"

    b "Iya-iya.... Santai aja, ok"

label scene_10:

    "Pelajaran telah dimulai, guruku sangatlah cantik. Dia layaknya artis. Semua pelajaran mudah diterangkan olehnya"

    "Saat jam pelajaran berakhir"

    d "Tolong bantu ibu sebentar"

    a "Ba-Baik bu"

label scene_11:

    d "Terima kasih ya, telah membantuku membawa berkas sebanyak ini"

    a "Tidak masalah kok bu"

    d "Ohh omong-omong gudang olahraga sekolah masih berantakan, jadi tolong kamu bereskan ya, ini kunci gudang olahraga, tolong nanti sore kamu rapikan dulu terus kembalikan ke satpam ya"

    a "Baik"

label scene_12:

    b "Apa yang kau lakukan dengan bu delia tadi....? Ha?"

    k "Benar apa yang kau bantu?"

    a "Cuma membawa berkas saja kok"

    b "Beneran??"

    a "Iya"

    b "Beneran??"

    a "Iya"

    b "Beneran, nih??"

    a "Iya kok bener, heh...."

    k "Ohh kupikir apaan Ha..Ha..Ha"

    a "Oh iya......"

label menu_scene_12:

    menu:
        "Beni, bisa anterin aku nanti ke gudang olahraga":
            jump scene_12_01
        "Koira, bisa anterin aku nanti ke gudang olah raga":
            jump scene_12_02

label scene_12_01:

    b "Maaf, aku nanti sepakbola apa kau lupa?"

    a "Ahh maaf, janji kita di tunda dulu ya sepakbolanya. Aku ada tugas dari Bu Deli"

    #jump menu_scene_12

    menu:
        "Koira, bisa anterin aku nanti ke gudang olah raga":
            jump scene_12_02

label scene_12_02:

    k "Ki-kita berdua??"

    a "Iya cuma membantu menata barang"

    k "Ba-baik tidak masalah"

label scene_13:

    k "Ehm anu..., [name]-kun"

    a "Iya?"

    k "Apa ada seseorang yang kamu suka?"

    a "Ehm....., tidak-tidak ada"

    k "Benarkah syukurlah"

    a "Memang kenapa?"

    k "Berarti kita senasib"

    a "Ada-ada aja deh"

    k "Hehehe"

label scene_14:

    a "Kotornya"

    k "Iya"

    a "Ayo kita cepat selesaikan"

    "[name] dan Koira membersihkan gudang tersebut"

    a "Ehm tolong itu taruh disitu"

    k "Baik, eh ini dimana?"

    a "Mungkin disebelah sana"

    k "Oke"

    a "Ini kira-kira di letakkan dimana ya"

    k "Mungkin di atas sana"

    a "Iya benar"

    k "Bisa kau bantu aku mengangkat ini, sangat berat"

    a "Baik"

    "*Setelah Selesai*"

    a "Fuhh... akhirnya selesai, terimakasih koi"

label scene_15:

    $ gtext = glitchtext(32)

    k "[gtext]{nw}"

    a "Koi???"

    k "[name]-kun, apa kau mau?"

    a "Apa?"

    k "Apa kau mau..., apa kau mau menjadi pacarku apa kau mau?"

    a "Apa yang kau katakan?"

    k "Aku bilang, apa kau mau jadi pacarku??"

    a "Tu-tunggu dulu....."

    menu:
        "Ya":
            jump scene_15_01
            #$ pacarekoira = True
        "Tidak":
            jump scene_15_02
            #$ pacarekoira = False

label scene_15_01:

    "*blushing Koira*"

    k "Te-Terima kasih [name]-kun,..... Eh apa itu?"

    jump scene_16

label scene_15_02:

    a "Maaf Ko-"

    k "Apa itu di belakangmu?"

    jump scene_16

label scene_16:

    "Sebuah tembok digudang"

    k "Ayo kita mengeceknya"

    a "Iya ayo"

label scene_17:

    "Ternyata lubang ini tembus di taman"

    a "Taman ini, bukankah kata Aoi ya? Kenapa sangat berbeda dari biasanya...hei Koi..."

    $ gtext = glitchtext(20)

    "[gtext]{nw}"

    $ gtext = glitchtext(31)

    "[gtext]{nw}"

    $ gtext = glitchtext(48)

    "[gtext]{nw}"

    $ gtext = glitchtext(23)

    "[gtext]{nw}"

label scene_18:

    "Wajah Koira kembali tak kelihatan, Sampai melihatku seperti menakutkan lalu kembali normal"

    k "Hei bukankah disini menakutkan?"

    a "Ya, ayo kita lekas pergi"

    k "[name]-kun, apa itu putih-putih di pohon?"

    a "Hmm? Tidak ada apa-apa"

    k "pohon sebelah sana...."

    k "Ah dia menghilang"

    a "Jangan nakut-nakutin dong ayo kita pergi"

    k "Apa kau tidak melihatnya tadi? Aku tidak bohong loh!"

    a "Ya nanti saja ceritanya, kita harus memberi tau ke guru tentang ini"

    k "Baik"

label scene_19:

    "Saat di dalam gudang"

    "Bu delia melihat aku"

    d "Kenapa sangat lama?"

    a "Bu disana ada sebuah lubang"

    d "Lubang?? Tidak ada gitu"

    a "Beneran bu, iya kan Koi"

    k "Apa yang kau bicarakan [name]-kun, tidak ada lubang disana"

    a "Hei apa yang kau bicarakan tadi kita kan-"

label scene_20:

    k "Justru apasih yang kau bicarakan [name]-kun, apa kau menerimaku atau tidak?"

    #k "Justru apasih yang kau bicarakan [name]-kun, apa kau menerimaku atau tidak?"

    a "Apa yang kau lakukan terakhir setelah kita bersih-bersih"

    k "Menyatakan cinta padamu, tetapi kamu tidak menjawab, tiba-tiba ada Bu Delia"

    a "Apa kata-katamu putih-putih terus barusan di taman itu"

    k "Taman? Putih-Putih?"

    d "Sudah-sudah cukup, ini sudah sore jadi waktunya kalian istirahat, mungkin tugas ini terlalu berat buat [name]-kun"

label scene_21:

    d "Kau pasti kecapekan [name]-kun"

    d "Terlalu banyak mungkin tugas untukmu"

    a "Tidak bu"

    a "Apa ibu ingat taman sekolah ini 2 tahun lalu"

    d "Iya kenapa?"

    a "Kenapa ditutup?"

    $ gtext = glitchtext(48)

    d "Apa kau lupa [gtext]{nw}"

    a "Apa?"

    d "Moh, kau pasti capek, cepatlah istirahat saja. Lagian ini bukan masalah serius kok"

    a "Baik..."


label scene_22:

    "Sorenya menjemput Hitari"

    a "Hitari, maaf aku terlambat"

    "Wajah Hitari ketakutan, melihatku perlahan-lahan"

label scene_23:

    "*Hitari zoom shitt.....*"

label scene_24:

    h "Ohh kakak, maaf ya aku melamun"

    a "Ada apa?"

    h "Tidak-tidak, tidak ada apa-apa kok"

    "Di sebuah jalan dekat stasiun"

    "Hitari tiba-tiba berhenti"

    a "Ada apa??"

label scene_25:
    $ delete_all_saves()
    $ raisokngesave = True
    centered "BERHENTI BICARA"
    with Dissolve(1.5)

    a "Aku...."

    centered "BERHENTI!!!!"
    with fade

label scene_26:

    a "Kenapa hikari, ada apa!?"

    h "Terlalu banyak suara, wajah menakutkan. Kumohon.... salahku apa!!??"

    "Wajah hitari dari menangis kemudian tertawa seperti orang gila"

    "Akhirnya kembali normal"

    h "Maaf kakak, aku tidak apa-apa"

    a "....Kau yakin?"

    h "em..."

    a "...."

label scene_27:

    #yu must be joking r8 now
    #almost a week yu moron mthrfuck

    "*tap*"

    "*tap*"

    "*tap*"

    "Hitari berjalan agak jauh dariku"

label scene_28:

    $ gtext = glitchtext(48)

    "[gtext]"

    "Yang kulihat wajahnya bukanlah Hitari , tiba-tiba kembali normal"

label scene_29:

    h "Ayo kak aku ingin merasakan omelet buatan kakak"

label scene_30:

    he "Ayo kak...."

    he "AKU"

    he "INGIN"

    "................................................................."

label scene_31:
    #nubruk kreto

    "....................................................."

    he "Kakak...."

    he "Kakak...."

    he "Kakak...."

label scene_32:

    $ gtext = glitchtext(48)

    he "[gtext]"

    "Wajah hitari menutupi layar monitor dengan wajah berantakan"

    #hilang tiba2

    jump bad_end

label scene_03_alt:

    k "Ohayou......"

    "Aku kembali menutup HP, Koira hanyalah teman dekatku saja. Dia selalu baik terhadap semua anak..."

    "Omong-omong soal baik apa aku terlalu jahat sama Hitari kemarin?"

label scene_04_alt:

    #depankamarhitari

    a "Hitari bangun!"

    "Membukakan pintu ternyata Hitari masih tidur nyenyak"

    a "Aku tunggu di meja makan, aku akan masakan sosis bakar"

    #kreeekk.....

    a "Aku harus segera memasak"

label scene_05_alt:

    #ndekdapur

    "Hitari dengan wajah lesu"

    h "Moohh , sosis lagi?"

    a "Maaf, maaf besok aku buatkan omelet"

    h "Asik, makasih. Aku suka kakak"

    a "Iya iya"

    h "Omong-omong kakak maafkan aku...."

    a "Tunggu dulu?, seharusnya aku yang minta maaf. Tetapi itu adalah janji keluarga aku harus menepatinya"

    h "Iya aku tau, tidak apa-apa itu bukan salah siapa hehe"

label scene_06_alt:

    a "Aku bangga punya adik seperti kamu"

    #blushing

    h "Ehh.....A-apa?"

    a "Ah.. tidak apa-apa, ayo kita segera ke sekolah"

    h "Baik"

    a "Kenapa?"

label scene_07_alt:

    "Sekolahku menerima siswa smp dan juga sma. Sekolah ini sudah memiliki prestasi yang sangat besar, dan siswa siswi disini semuanya sangat ramah-ramah"

    gk "Ohayou"

    a "Ohh pagi juga Koira"

    k "Pagi...., Tidur larut?"

    a "Ahahaha..... Tidak kok"

    k "Wajahmu kriput tuh, hahaha"

    a "Mungkin sibuk dengan tugas OSIS"

    k "Repot ya jadi OSIS, suara nadamu juga sangat berbeda sekarang, apa karena LDKS hari sabtu kemarin?"

    a "Ya semacam itulah, baiklah ayo kita masuk. Aku ingin istirahat di kelas"

    k "Baik-baik"

label scene_08_alt:

    gk "Yo [name]-kun"

    a "Pagi Bento"

    gk "Jangan panggil aku itu, panggil aku Beni"

    a "Baik-baik, pagi juga, jadi ada apa?"

    b "Apa kamu mau ikut sepulang sekolah denganku sepak bola?"

    menu:
        "Ya":
            jump scene_09_01
        "Tidak":
            jump scene_08_02_alt

label scene_08_01_alt:



label scene_08_02_alt:

    b "Kenapa? Apa kamu masih capek? Maaf deh"

    a "Maaf aku lihat dulu, kemungkinan bisa kok, kemungkinan?"

    b "Iya-iya.... Santai aja, ok"

label scene_09_alt:

    "Pelajaran telah dimulai, guruku sangatlah cantik. Dia layaknya artis. Semua pelajaran mudah diterangkan olehnya"

    "Saat jam pelajaran berakhir"

    d "Tolong bantu ibu sebentar"

    a "Ba-Baik bu"

label scene_10_alt:

    d "Terima kasih ya, telah membantuku membawa berkas sebanyak ini"

    a "Tidak masalah kok bu"

    d "Ohh omong-omong gudang olahraga sekolah masih berantakan, jadi tolong kamu bereskan ya, ini kunci gudang olahraga, tolong nanti sore kamu rapikan dulu terus kembalikan ke satpam ya"

    a "Baik"

label scene_11_alt:

    b "Apa yang kau lakukan dengan Bu Delia tadi....? Ha?"

    k "Benar apa yang kau bantu?"

    a "Cuma membawa berkas saja kok"

    b "Beneran??"

    a "Iya"

    b "Beneran??"

    a "Iya"

    b "Beneran, nih??"

    a "Iya kok bener, heh...."

    k "Ohh kupikir apaan Ha..Ha..Ha"

    a "Oh iya......"

label menu_scene_12_alt:

    menu:
        "Beni, bisa anterin aku nanti ke gudang olahraga":
            jump scene_12_01_alt
        "Koira, bisa anterin aku nanti ke gudang olah raga":
            jump scene_12_02_alt

label scene_12_01_alt:

    b "Maaf, aku nanti sepakbola apa kau lupa?"

    a "Ahh maaf, janji kita di tunda dulu ya sepakbolanya. Aku ada tugas dari Bu Deli"

    b "Omong-omong bagaimana kalau aku bantu agar kau bisa ikut sepak bola"

    a "Baiklah"

    jump scene_13_alter


label scene_12_02_alt:

    k "Ki-kita berdua??"

    a "Iya cuma membantu menata barang"

    k "Ba-baik tidak masalah"

label scene_13_alt:

    k "Ehm anu..., [name]-kun"

    a "Iya?"

    k "Apa ada seseorang yang kamu suka?"

    a "Ehm....., tidak-tidak ada"

    k "Benarkah syukurlah"

    a "Memang kenapa?"

    k "Berarti kita senasib"

    a "Ada-ada aja deh"

    k "Hehehe"

label scene_14_alt:

    a "Kotornya"

    k "Iya"

    a "Ayo kita cepat selesaikan"

    "[name] dan Koira membersihkan gudang tersebut"

    a "Ehm tolong itu taruh disitu"

    k "Baik, eh ini dimana?"

    a "Mungkin disebelah sana"

    k "Oke"

    a "Ini kira-kira di letakkan dimana ya"

    k "Mungkin di atas sana"

    a "Iya benar"

    k "Bisa kau bantu aku mengangkat ini, sangat berat"

    a "Baik"

    "*Setelah Selesai*"

    a "Fuhh... akhirnya selesai, terimakasih koi"

label scene_15_alt:

    $ gtext = glitchtext(48)

    k "[gtext]"

    a "Koi???"

    k "[name]-kun, apa kau mau?"

    a "Apa?"

    k "Apa kau mau..., apa kau mau menjadi pacarku apa kau mau?"

    a "Apa yang kau katakan?"

    k "Aku bilang, apa kau mau jadi pacarku??"

    a "Tu-tunggu dulu....."

    menu:
        "Ya":
            jump scene_15_01_alt
            #$ pacarekoira = True
        "Tidak":
            jump scene_15_02_alt
            #$ pacarekoira = False

label scene_15_01_alt:

    "*blushing Koira*"

    k "Te-Terima kasih [name]-kun,..... Eh apa itu?"

    jump scene_16_alt

label scene_15_02_alt:

    a "Maaf Ko-"

    k "Apa itu di belakangmu?"

    jump scene_16_alt

label scene_16_alt:

    "Sebuah tembok digudang"

    k "Ayo kita mengeceknya"

    a "Iya ayo"

label scene_17_alt:

    "Ternyata lubang ini tembus di taman"

    a "Taman ini, bukankah kata Aoi ya? Kenapa sangat berbeda dari biasanya...hei Koi..."

    $ gtext = glitchtext(48)
    "[gtext]"
    $ gtext = glitchtext(32)
    "[gtext]"
    $ gtext = glitchtext(24)
    "[gtext]"
    $ gtext = glitchtext(36)
    "[gtext]"

label scene_18_alt:

    "Wajah Koira kembali tak kelihatan, Sampai melihatku seperti menakutkan lalu kembali normal"

    k "Hei bukankah disini menakutkan?"

    a "Ya, ayo kita lekas pergi"

    k "[name]-kun, apa itu putih-putih di pohon?"

    a "Hmm? Tidak ada apa-apa"

    k "pohon sebelah sana...."

    k "Ah dia menghilang"

    a "Jangan nakut-nakutin dong ayo kita pergi"

    k "Apa kau tidak melihatnya tadi? Aku tidak bohong loh!"

    a "Ya nanti saja ceritanya, kita harus memberi tau ke guru tentang ini"

    k "Baik"

label scene_19_alt:

    "Saat di dalam gudang"

    "Bu delia melihat aku"

    d "Kenapa sangat lama?"

    a "Bu disana ada sebuah lubang"

    d "Lubang?? Tidak ada gitu"

    a "Beneran bu, iya kan Koi"

    k "Apa yang kau bicarakan [name]-kun, tidak ada lubang disana"

    a "Hei apa yang kau bicarakan tadi kita kan-"

label scene_20_alt:

    k "Justru apasih yang kau bicarakan [name]-kun, apa kau menerimaku atau tidak?"

    #k "Justru apasih yang kau bicarakan [name]-kun, apa kau menerimaku atau tidak?"

    a "Apa yang kau lakukan terakhir setelah kita bersih-bersih"

    k "Menyatakan cinta padamu, tetapi kamu tidak menjawab, tiba-tiba ada Bu Delia"

    a "Apa kata-katamu putih-putih terus barusan di taman itu"

    k "Taman? Putih-Putih?"

    d "Sudah-sudah cukup, ini sudah sore jadi waktunya kalian istirahat, mungkin tugas ini terlalu berat buat [name]-kun"

label scene_21_alt:

    d "Kau pasti kecapekan [name]-kun"

    d "Terlalu banyak mungkin tugas untukmu"

    a "Tidak bu"

    a "Apa ibu ingat taman sekolah ini 2 tahun lalu"

    d "Iya kenapa?"

    a "Kenapa ditutup?"

    $ gtext = glitchtext(120)

    d "Apa kau lupa [gtext]{nw}"

    a "Apa?"

    d "Moh, kau pasti capek, cepatlah istirahat saja. Lagian ini bukan masalah serius kok"

    a "Baik..."

label scene_22_alt:

    #malam Hari

    a "Hei boleh aku minta saran?"

    h "Apa kak?"

    a "Apa alasan perempuan menembak laki-laki?"

    h "Ya mungkin dia terlalu cinta oleh ketampanan, sifat atau hal yang mencolok bagi dia"

    a "Ohh"

    h "Jangan-jangan kakak!?"

    a "Ya aku baru saja ditembak sama Koira"

    h "He!?!?!?!"

label scene_23_alt:

    h "Jadi bagaimana kak kelanjutanya?"

    a "Ada hal yang menganjal"

    h "Kenapa?"

    a "Ada sesuatu yang aneh, aku lupa menjawab pertanyaan tersebut. Tetapi aku menemukan lubang dan menuju ke taman"

    h "Taman?"

    a "Taman belakang sekolah dulu, tetapi sekarang sudah tidak ada"

    h "Ohh yang itu"

    a "Dan setelah aku kembali, dia melupakan apa yang dia lihat. Aneh sekali y..."

label scene_24_alt:

    "*Hinata glitch face*"

    h "Ya benar sangat menyeramkan"

    a "Baik ayo tidur sudah malam"

    h "Baik, besok sosis lagi ya"

    a "Tidak, akan kubuatkan sayuran"

    h "Mohhh, baiklah"

label scene_25_alt:

    "Aku bangun terlalu siang, suara jam alarmku lupa kunyalakan"

    a "Hitari bangun"

    a "Sudah telat kita"

    h "........."

    a "Hitari cepat"

    h "........."

    "Aku menuju ke depan kamar Hitari"

    a "Hitari!"

label scene_26_alt:

    "Aku membukakan pintu kamarnya"

    "Dan yang ku lihat...."

    "Hitari menggunakan sebuah baju"

    "Aku kembali menutup pintunya"

    h "Oi ketok dulu apa kak!"

    a "Aku sudah mengetoknya"

    h "Kak??"

    a "Hitari?"

    h "Kak?? Apa yang terjadi?"

    a "Apa maksudmu?"

    h "Aku tidak bisa mendengar kak.."

    a "Apa?"

    h "Kak!!! Apa yang terjadi???"

label scene_27_alt:

    a "Tenang-tenang"

    a "Aku periksa dulu telingamu"

    "Aku memegang pundak Hitari dan segera melihat telinganya"

    h "Aduh"

    a "Tidak ada apa-apa?? Apa yang terjadi"

    h "Ada apa kak.."

    "Aku mengetik di HP"

    "*Semua akan baik-baik saja, istirahatlah, aku akan izinkan kau dulu"

    h "Baik...."

label scene_28_alt:

    "Aku lari ke sekolah"

    k "Pagi... [name]-kun"

    a "Koi ijinkan aku tidak masuk sekarang"

    k "Kenapa?"

    a "Adikku sakit, aku akan izin dulu kekelasnya"

    k "Ba-Baik..."

label scene_29_alt:

    "Di sebuah kelas aku mengijinkan Koi untuk absen."

    "Tetapi aku bertemu Bu Delia"

    d "Kenapa kau tidak masuk kekelas [name]-kun"

    a "Adikku sakit Bu, bukannya saya sudah diijinkan Koira ya Bu?"

    d "Koira?"

    d "Dia katanya ijin"

    a "Apa?"

label scene_30_alt:

    $ delete_all_saves()

    $ raisokngesave = True

    "Aku menuju kekelas lari untuk melihat Koira"

    "Tanpa disangka-sangka seluruh teman sekelas mati mengenaskan semua"

    a "Apa yang terjadi!?"

    b "[name]-kun"

    a "Apa yang terjadi Beni!?"

    b "Koi..."

    b "Dia membabi buta..."

    a "Beni!!!.... Jawab aku, Beni!!!!!"

    "*KYAAAA!!!!*"

label scene_31_alt:

    "Suara ceritan Bu Delia terdengar di ujung ruangan"

    "Aku segera pergi menuju Bu Delia"

    "Bu Delia Mati mengenaskan di pojok ruangan dengan wajah berantakan"

    "Seluruh sekolah meninggal sadis dengan wajah mengenaskan"

    "Aku mencari Koira untuk mengetahui kebenaran"

    "Dan akhirnya aku sampai di gudang penyimpanan alat olahraga"

    "Aku membukanya dan aku melihat....."

    "Segerumbulan siswa mati disana secara menumpuk...."

label scene_32_alt:

    "Aku lari meninggalkan sekolah, aku berteriak tolong tetapi tidak ada yang mendengarkanku. Semua orang mengabaikanku"

    "Sampai dirumah aku mencari hitari"

    a "Hitari!!"

    "Aku lari menuju kamar Hitari dan....."

    "Aku bertemu sama Koira dan Hitari"

    "Koira membawa pentungan baseball"

label scene_33_alt:

    "Hitari!! Cepat pergi"

    h "Kakak.... Tolong"

    k "Kenapa kau mau menjauhi aku dengan adikmu"

    a "Kau bukan Koira yang aku kenal!!"

    k "Berisik peniru [name]-kun"

    a "Peniru?"

    k "Kau bukanlah yang asli, kenapa kau tega menolakku hingga menyebarkanya ke kelas"

    a "Apa yang kau katakan!"

    k "Berisik!"

    k "Sudah lama aku menyukaimu"

    k "Tetapi kau melakukanku seperti ini!"

    k "Aku ingin semuanya lenyap!!!!!!"

label scene_34_alt:

    "Baik.. sudah basa basinya. Aku tidak peduli siapa yang akan mati"

    centered "Pilihlah dengan sesuai hatimu, meskipun kau yang palsu aku akan menuruti perintahmu. Aku sudah tidak peduli lagi dengan semuanya...."

    centered "Jadi siapa yang mau mati duluan?"

    menu:
        "Aku":
            jump scene_34_alt_aku
        "Hinata":
            jump scene_34_alt_h
        "Koira":
            jump scene_34_alt_k

label scene_34_alt_aku:

    #scare Koira

    k "Selamat tinggal"

    #layar hitam

    jump bad_end

label scene_34_alt_h:

    centered "Koira dengan cepat menghancurkan kepala Hitari dengan 1 serangan"

    centered "Selanjutnya siapa...."

    menu:
        "Aku":
            jump scene_34_alt_aku
        "Koira":
            jump scene_34_alt_k

label scene_34_alt_k:

    k "Kau memilihku? Kau memang benar-benar benci aku ya...."

    "Koira memegang kepalanya sendiri"

    "Dan memutarkanya"

    "Wajah hitari ketakutan"

    h "Apa yang kakak koira lakukan kakak!?"

    a "Tenang Hitari...."

    "Wajah Hitari menakutkan"

    a "A-Apa yang terjadi?"

    k "Cepat bunuh aku!!!"

    a "Apa yang terjadi.."

    k "Cepat bunuh aku!! Aku sudah tidak kuat dengan penderitaan ini"

    "Sesosok orang muncul didepanku tiba-tiba"

    gk "Dia mati sore jam 04.40"

    a "Siapa kau?"

    gk"Kematian sesuai 24 jam setelah melihatku."

    centered "Jadi..."

    centered "Aku ingin kau besok mati...."

    "Pandangan mata merahnya melihatku dan banyak gambaran menakutkan diseluruh benakku muncul tiba-tiba, aku tidak bisa mengendalikan pikiranku lagi"

    #layar gelap

    #Pause(1.5)

    jump bad_end

label scene_13_alter:

    "Sorenya di sebuah lorong"

    a "Kapan dimulai sepakbolanya?"

    b "1 jam lagi, ayo kita harus cepat-cepat"

    a "Baik-baik"

    b "Oh aku punya ide"

    a "Ide?"

    b "Kau kan sedikit kecapekan, berikan kuncinya ke aku"

    a "Ini"

    b "Yosh, aku akan mengajak teman-teman."

    b "Sebaiknya kamu istirahat saja ya, kamu kan sedikit capek kena tugas OSIS kemarin"

    menu:
        "Baik, terimakasih atas bantuannya":
            jump nakok_1
        "Tidak, aku akan tetap membantu. Tugas ini diberikan olehku":
            jump nakok_1

label nakok_1:

    menu:
        "Baik, terimakasih atas bantuannya":
            jump nakok_2
        "Tidak, aku akan tetap membantu. Tugas ini diberikan olehku":
            jump nakok_2

label nakok_2:

    menu:
        "Baik, terimakasih atas bantuannya":
            jump nakok_3
        "Tidak, aku akan tetap membantu. Tugas ini diberikan olehku":
            jump nakok_3

label nakok_3:

    menu:
        "Baik, terimakasih atas bantuannya":
            jump nakok_4
        "Tidak, aku akan tetap membantu. Tugas ini diberikan olehku":
            jump nakok_4

label nakok_4:

    menu:
        "Baik, terimakasih atas bantuannya":
            jump scene_13_01_alter
        "Tidak, aku akan tetap membantu. Tugas ini diberikan olehku":
            jump scene_13_02_alter

label scene_13_01_alter:

    b "Tak masalah kita ini temankan"

    a "Baik , terimakasih sebanyak-banyaknya"

    "Aku menunggu di sebuah lorong"

    "Sangat lama"

    "Ini sudah 1 jam lebih"

    "Aku harus memeriksanya."

    "Didepan gudang peralatan sangat sepi"

    "Aku membuka gudang itu. Tetapi aku menemukan sebuah lubang"

    "Aku memasuki sebuah lubang itu"

    "Hingga aku menemukan sebuah taman, lebih tepatnya bukan taman. Melainkan Kuburan yang dipenuhi pohon berdaun putih"

    "Aku memanggil sekencang-kencangnya"

    a "Beniiii!! Kau disini!?"

    ".........."

    "Tidak ada jawaban"

    "Sebuah muka lansung keluar didepanku"

    "Sebuah anak kecil perempuan dengan wajah hancur disebelah kanan serta penutup mata"

    gk "....."

    a "Si-Siapa kamu?"

    gk "Hayana..."

    a "Hayana?"

    gk "Lenyap"

    a "Lenyap?"

    gk "Besok"

    a "Besok...? Lenyap?"

    gk "Selamat tinggal"

    a "Tunggu"

    "Anak kecil itu menghilang"

    "Aku kembali ke lapangan"

    "Beni didepanku dan memanggilku di sebuah lorong"

    b "Kau dari mana saja"

    a "Maaf aku dari gudang mencari kalian, ternyata ada sebuah lubang"

    "Wajah beni berubah menjadi menyeramkan kemudian kembali"

    b "Kau dari mana saja"

    a "A-Apa itu tadi?"

    b "Kau tak apa? Sepertinya kau beneran capek"

    a "Mungkin aku tadi ketiduran di lorong, ayo deh kita sepakbola"

    b "Kau beneran tak apa?"

    a "Ya.."

    "Malamnya sesudah sepakbola"

    #di dapur

    a "Hitari makan malamnya sudah siap"

    h "Yatta...."

    h "Terimakasih kakak.."

    "Wajah Hitari sempat penuh darah"

    a "Kau tak apa hitari?"

    h "Heh?"

    a "Tidak, tidak apa-apa. Maaf aku sedikit pusing"

    h "Besok ijin sekolah?"

    a "Mungkin besok sudah sembuh kok"

    h "oke oke, cepat sembuh ya kak. Habis makan ini cepat istirahat"

    "Di kamar, didepan pintu kamar Hitari mematikan lampu"

    h "Selamat malam"

    #bgblack

    "........"

    "Suasana hening"

    "Sangat hening"

    "Aku mendengar suara agak aneh"

    centered "{size=+50}Mati{/size}"

    centered "{size=+40}Mati{/size}"

    centered "{size=+10}Mati{/size}"

    centered "{size=+5}Mati{/size}"

    "Pandangan semakin gelap- sangat gelap"

    "Gelap"

    $ gtext = glitchtext(12)

    "[gtext]{nw}"

    $ gtext = glitchtext(15)

    "[gtext]{nw}"

    "......"

    "Wanita itu tiba-tiba didepanku keluar"

    #jreeng

    a "Kau siapa?"

    a "Siapa yang berbicara?"

    "Siapa?"

    "Aku?"

    "Aku terbangun"

    "Suasana pagi dikamar layak biasanya"

    "Aku menuju ke kamar Hitari"

    a "Hitari...."

    a "Ayo bangun"

    a "Hitari..??"

    "Didepan kamar yang kulihat Hitari penuh darah dan melihatku"

    h "*glitch hitari*"

    "Aku lansung lari meninggalkan rumah"

    "Suasana depan rumah merah, langit memerah. Aku lari mencoba mencari pertolongan"

    "Didepan sekolah"

    "Yang kulihat kelas suasana kosong tidak ada siapa-siapa"

    "Ruang guru juga kosong"

    "Saat dilorong aku menemukan Koira"

    $ gtext = glitchtext(32)

    k "[gtext]{nw}"

    "Wajah Koira tiba-tiba patah, aku lari meninggalkanya"

    "Aku ingat masih memiliki kunci gudang olahraga, aku masuk ke gudang itu. Yang ku temukan Bu Delia"

    a "Ibu selamat?"

    d "Apa yang kau katakan?"

    a "Bu... Aku takut"

    a "Kenapa semua orang tampak sudah mati"

    d "Bukannya kamu?"

    a "Apa?"

    d "Yang sudah mati"

    "Wajah Bu Delia tersenyum mengerikan"

    jump bad_end

label scene_13_02_alter:

    b "Baiklah, kalau begitu kita selesaikan cepat-cepat"

    a "Baik!"

    "Digudang olahraga sangat cepat dibantu teman-teman"

    "Akhirnya selesai"

    a "Ya..."

    b "Hmm? Apa itu lubang?"

    a "Sepertinya, apa perlu kita mengeceknya?"

    b "Tidak, kita sudah janjian sama teman-teman. Semua sudah menunggu di lapangan"

    a "Baiklah"

    "Malamnya sesudah sepakbola"

    a "Hitari makanan sudah siap"

    h "Yata, makasih kakak"

    a "Ya sama-sama"

    h "Omong-omong kak ada yang aneh dengan perilaku Bu Delia tadi"

    a "Aneh?"

    h "Dia sepertinya mencari seseorang lari kemana-mana tetapi tak menemukannya"

    a "Ahh, kunci ruang olahraganya ada di aku"

    h "Jangan-jangan kakak yang di cari ya"

    a "Mungkin"

    h "Besok saja kembalikanya, sudah malam. Peraturan keluarga. Tehe"

    a "Iya iya, mooh dasar"

    "Di kamar aku melihat hp, dan melihat notif pesan"

    "Cepat kesekolah!!!"

    "Apa yang terjadi? Apa guru masih disekolah"

    "Cepat kesekolah!!!"

    "Cepat kesekolah!!!"

    "Cepat kesekolah!!!"

    "Cepat kesekolah!!!"

    "Cepat kesekolah!!!"

    "Aku tidak akan pergi, ini sudah peraturan bagi keluargaku. Tidak biasanya Bu Delia seperti ini"

    "Besoknya disekolah"

    "Bu Delia kearahku dengan wajah penuh emosi"

    d "KEPARAT!"

    a "A-Apa?"

    d "Kenapa kau tidak membersihkan peralatan olahraga itu!!"

    a "Sudah bu sama Beni"

    d "Beni....Sialan!!"

    a "Bu apa yang terjadi?"

    d "DIAM! Aku sudah menyuruh adikmu untuk kesana tetapi kau melarangnya. Sekarang kau juga tidak mau!"

    a "Apa yang terjadi?"

    d "Berapa kali kau me load kehidupan ini ha!?"

    a "Aku tidak tau apa yang ibu bicarakan"

    d "Mati.."

    a "Mati!?"

    d "Aku akan mati bila aku tidak mengorbankan seseorang untuk Hayana"

    a "Apa?"

    d "SEKARANG , AKU AKAN MEMBAWA MU KESANA"

    menu:
        "Lari ke Kelas":
            jump scene_13_02_01_alter
        "Lari ke gudang olahraga":
            jump scene_13_02_02_alter
        "Lari ke rumah":
            jump scene_13_02_03_alter

label scene_13_02_01_alter:

    $ delete_all_saves()

    $ raisokngesave = True

    "Aku akan pergi ke kelas"

    "Suara jeritan terdengar. Itu suara Beni"

    b "Tolong!"

    d "Sekarang apa yang kau lakukan!?"

    #layarhitam

    "Beni kehilangan kepala"

    #layarhitam

    jump bad_end

label scene_13_02_02_alter:

    $ delete_all_saves()

    $ raisokngesave = True

    "Aku lari ke gudang"

    d "Pintar sangat pintar kau menuju kesini!?"

    d "Sepertinya kamu memang ingin menyelamatkan hidupku ya"

    a "Sebelum aku masuk ke lubang itu"

    a "Siapa itu Hayana!?"

    d "Akan kuberitau kau. Dia adalah anak separuh malaikat maut"

    d "Tetapi jika kamu melihat matanya kamu akan mati besok.."

    a "Mati?"

    d "Ya, hanya aku yang tau cara menghindari kematian itu"

    d "Dengan cara memindah target."

    d "Bahkan teman-teman Hitari atau teman osismu telah lenyap."

    d "Tetapi tidak ada yang sadar..."

    a "Apa aku akan lenyap bila menyelamatkan ibu?"

    d "Tentu saja Bodoh!."

    d "Mau tidak mau kau harus mati!"

    d "Hanya kaulah yang kuincar karena kau adalah orang polos!"

    d "Mudah ditipu."

    d "Tetapi kenapa!! Kamu seperti tau semuanya!"

    a "Aku tidak akan mati"

    a "Aku tidak akan membunuh ibu"

    a "Aku tidak akan melukai siapapun!"

    a "Meski aku polos dan ditipu oleh rendah hati ibu..."

    a "Aku akan mematuhi kata ibu"

    d "Bagus!!! Itulah Muridku! Sekarang mas-"

    a "Aku akan mematuhi selama ibu masih hidup"

    d "Apa!?"

    "Koira mementung Bu Delia di belakang"

    d "AGHHH!! KEPARAT!!"

    k "Aku mendengar semuanya, kita tinggalkan dia saja"

    a "Sudah kuduga kau datang"

    k "Aku tak sengaja kesini untuk memastikan untuk menembak cinta ke kamu, justru aku menemukan sesuatu yang buruk"

    d "KEPARAT!!! Tinggal 5 menit! Tolong Aku!!"

    a "Sampai jumpa Bu Delia"

    "Mata Bu Delia menjadi putih, kepalanya rusak ditekan oleh raksasa"

    #layarhitam

    #kembali

    "Aku pun lupa soal Bu Delia itu siapa."

    "Tetapi aku menjalani kehidupan biasa dan aku berpacaran bersama Koira sekarang"

    jump good_end

label scene_13_02_03_alter:

    $ delete_all_saves()

    $ raisokngesave = True

    "Aku lari ke rumah"

    "Saat aku di meja makan, Bu Delia dan Hitari penuh babak belur memasuki rumah"

    d "Sekarang apa yang akan kau lakukan!?"

    h "TOLONG AKU KAKAK!"

    $ gtext = glitchtext(32)

    "[gtext]{nw}"

    "Hitari mati dengan kepala tidak ada"

    jump bad_end


label bad_end:

    show black
    with dissolve

    centered "{size=+100}GAME OVER{/size}"

    hide black
    with dissolve

    return

label good_end:

    show black
    with dissolve

    centered "{size=+100}AYY YU GOT REKT M8{/size}"
    centered "{size=+100}SEE YU NEXT TIME{/size}"
    centered "{size=+100}CLONE.....(lol){/size}"
    centered "{size=+100}:p{/size}"

    hide black
    with dissolve

    return
