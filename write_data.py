import json

# Çene
P1 = "Çene Yapısı : Kare Çene, Bu çene yapısına sahip insanlar sinirli ve arıza çıkarmayı seven inatçı kişiliktedir. Bu kişiler kendilerini iyi ifade ederler. Sıklıkla insanların kalbini kıran bencil insanlardır."
P2 = "Çene Yapısı : Kısa Ve Dar Çene, Bu insanlar entellektüel ve keskin fikirlidir. Karar verme konusunda çok başarısızdırlar"
P3 = "Çene Yapısı : Yuvarlak Çene, Bu insanlar ateşli ve umut doludur. Ayrıca çok çalışkan kişilerdir."
P4 = "Çene Yapısı : Uzun Çene, Sadık ve uysal insanlardır. Kolayca arkadaş edinip, çevresindekilerle iyi anlaşırlar. Bu tip çeneye sahip insanların kutsanmış olduğu düşünülür. Yardımsever ve neşe doludurlar."

# Kaş
P5 = "Kaş Yapısı : Doğal Düz Kaş, Bu tip eğimsiz kaşlar, mantıklı ve rasyonel düşünmeyi ifade eder. Hayata bakış açıları ''İki ölç, bir biç.'' 'dir. Yine de dobradırlar, söyleyeceklerinden çekinmezler ve duygularını ifade etmekten korkmazlar."
P6 = "Kaş Yapısı : Yüksek Kenar Kaş, Bu tip kaşlar nezaket ve dikkatin tartışılmaz bir göstergesidir. Bu tip kaşlara sahip insanlar asla başkalarının sorunlarına karşı kayıtsız kalmazlar ve her zaman yardıma ihtiyacı olanlara yardım etmeye hazırdırlar."
P7 = "Kaş Yapısı : Düz Yukarı Kaş, Bu tip dik açılı kaşlar, güçlü duygular ile tutkunun ruhun içinde kaynaştığına işarettir. Bu tip kaşa sahip olan insanlar, tanıştıkları insanlar üzerinde kalıcı bir etki yaratırlar. Tam olarak hayatta her zaman istediklerini elde ederler ve başarıya giden yolda çok hızlı ilerlerler."
P8 = "Kaş Yapısı : Kısa Kaş, Ayrıntılar için son derece özenli davranırlar ve bunu herkesin yapmasını beklerler. İnsanların hayatın zorlukları konusunda şikayet etmelerini duymak istemezler. Çünkü kendileri zorluklarla baş edebiliyorlardır. Henüz hiçbir dağın çok yüksek olmadığı kesindir!"
P9 = "Kaş Yapısı : Sivri Kaş, Bu şekilde keskin, açısal kaşlara sahip insanlar oldukça dinamiktir. Olaylara karşı karar verme mekanizmaları çok hızlı işler. Doğal karakterlere sahiplerdir ve bu doğallık bazen istenmeyen sonuçlara yol açabilir ama tabii ki avantajları da vardır. Mesela insanlar asla onlarla birlikte olmaktan sıkılmazlar. Doğal bir lider olarak insanlara ilham kaynağı olurlar ve asla sorumluluk almaktan çekinmezler."
P10 = "Kaş Yapısı : Büyük Boşluk Kaş, Drama ile uğraşmayı sevmezler. Daha az yakın arkadaşlığa sahip olma eğilimindedirler. Detaycı bir insansınızdır. Diğer insanların problemleri hakkında şikayet etmelerini duymaktan hoşlanmazsınız çünkü siz de zaman zaman hayatın zorluklarıyla mücadele etmekte güçlük çekersiniz. Ama kesin bir şey var ki o da hiçbir dağ sizin için aşılamaz değildir!"
P11 = "Kaş Yapısı : Küçük Boşluk Kaş, Çok fazla arkadaşı olan türler olma eğilimindedir. Bunun bir nedeni vardır: Ekstra güçleri vardır, bu yüzden arkadaşlarının tüm kişisel dramalarını bunalmış hissetmeden halledebilirler.Strese dayanıklıdır ve sosyal insanlardır. Bu insanlar, bitmek tükenmez bir enerjiye ve çok geniş ilgi alanlarına sahiptirler. Eğer bu tipe aitseniz, problemlerinizi tek başınıza çözmeye alışıksınızdır ve diğer insanlardan nadiren yardım istersiniz."
P12 = "Kaş Yapısı : Normal Boşluk Kaş, Kaşların ortasındaki bölge ve kaşların birbirinden uzaklığı, geleneksel değerlere önem vermenin ve dürüstlüğün bir göstergesidir. Aynı zamanda bu tip kaşa sahip olanlar, bir şeyleri dramatize etmekten hoşlanmazlar."

# Göz
P13 = "Göz Yapısı : Küçük Göz, Küçük gözler düşünce doludur ve detaycıdır. Olaylara sakin ve analitik bakmaya özen gösterirler. Düşüncelerini çabuk paylaştıkları için ya da aceleci oldukları için iyi arkadaş veya eşler olabilirler.Odak ve hassasiyet, yemin ettiğiniz kelimelerdir. Detaylar için keskin ve yapışkan olduğunuz biliniyor. Zeka ve uzak görüşlülük sizi işaretler ve aklınıza koyduğunuz hemen hemen her şeyde uzmanlık kazanıp, şeylerin derinliklerine dalmayı seviyorsunuz. Genelde yabancılara karşı dikkatli olursunuz, bu da ne yazık ki birçok insanın sizin soğuk ve kibirli olduğunu varsaydığı anlamına gelir."
P14 = "Göz Yapısı : Genis Göz, Hem bilinçli, hem de bilinçli kanallardan gelen, düşler ve aura gibi bilinçaltı kanallardan gelen duygular ve bilgilere karşı çok açık ve alıcısınız. Tutku sizi tanımlar ve genel bir sıcaklık hissi sizi çevreler ve sizi ulaşılabilir bir insan haline getirir. Ayrıca yaratıcı bir düşünce tarzınız da var. Yine de kendine iyi bak, güven verici doğanın aldatıcı bir kişinin senden faydalanmasını çok kolaylaştırabilir."
P15 = "Göz Yapısı : Badem Göz, Badem şeklindeki gözler genellikle egzotik ve mistik görünümleri için değerlidir. Bunlara sahipseniz, o zaman çok dikkatli ve dikkatli bir insansınız. Durumunuzu en fazla vergi çekerken çekincenizi koruyabilirsiniz. Hayata karşı çok dengeli bir bakış açınız var ve genelde derinlerde ılık ve şefkatli olsanız da duygularınızı göstermeyin."
P16 = "Göz Yapısı : Yuvarlak Göz, Yaratıcılık ve canlı bir hayal gücü ile kutsanmış, sık sık kendi dünyasında kaybolursun. Güçlü idealizm de bu gözlerin damgasını vurdu, karamsarlık ve pratik değil. Sık sık duygularınızdan uzaklaşırsınız ve düşüncelerinizi ve duygularınızı kendinize saklamak için zorlanırsınız. Neyse ki, keskin diliniz tekrar tekrar incinse bile, insanları kolayca çeken bir cazibeye sahipsiniz."
P17 = "Göz Yapısı : Yakın Göz, Gözleri kapalı olan insanlar genellikle eski, dünya geleneklerine derin bir saygı duyarlar. Tarih onları büyüledi ve atalarının ve ailesinin her küçük geleneğini takip etmekten hoşlanıyorlar. Ne yazık ki, bu aynı zamanda yaşamlarındaki küçük değişikliklerden dolayı çok dirençli, hatta stresli oldukları anlamına geliyor. Ayrıca, biraz odaklanmış, ama sonuçta çok başarılı olmaya eğilimli, çok odaklı, disiplinli ve ayrıntı düşünen insanlar."
P18 = "Göz Yapısı : Uzak Göz, Eğer geniş gözlere sahipseniz, keşfetmeyi ve denemeyi seviyorsunuz - modadaki en yeni trendler veya en son yaşam tarzı seçenekleri . Son derece geniş görüşlü ve esnek, sık sık bir rutine sadık kalmayı biraz zor bulursunuz. Dürtüsel ve maceracı, çok sayıda özgürlük ve seçenek sunan yerlerde, bu yenilikçi fikirlerinizle şöhrete dokunmanıza rağmen, başarılı olacaksınız."
P19 = "Göz Yapısı : Normal Göz, Gözleriniz arasındaki mesafe tam olarak bir göz genişliğindeyse, hayata karşı iyi bir bakış açısı ve insanlara karşı sağlıklı bir tavırla çok dengeli bir insan olduğunuz anlamına gelir."

# Dudak
P20 = "Dudak Yapısı : Büyük Kabarık Dudak, Bu dudak yapısına sahip olanlar konuşmayı severler. İletişim yetenekleri fazlaca gelişmiştir. Sizi sözcükleriyle etkileri altına almaları kaçınılmazdır. Bu tatlı dillerine bir de cömert ve yardımsever kişilikleri eklenince tadından yenmezler."
P21 = "Dudak Yapısı : Küçük Kabarık Dudak, Hem kısa(enine doğru), hem de dolgun dudaklara sahip olanlar; ikili ilişkilerinde ilk olarak kendilerini düşünürler. Yeteri kadar ilgi ve sevgiyi aldıklarını fark ettiklerinde, ilişkilerini inanılmaz sahiplenirler. Partnerlerini de öyle elbette... Zordurlar, ancak onların kalbini fethettiyseniz hayatlarınızı güzelleştirmek için ellerinden geleni yaparlar."
P22 = "Dudak Yapısı : Üst Kalin Alt İnce Dudak, Bunun gibi dudakları olan insanlar birer kral ve kraliçedir. Duygusal, karizmatik, sevgi dolu olurlar ve bulundukları ortamda bütün dikkatleri üstlerine çekerler. İlgi merkezi olmayı severler. En çarpıcı ifadeler, en komik espriler hep onlardan gelir. "
P23 = "Dudak Yapısı : Üst İnce Alt Kalın Dudak, Bu dudak şekline sahip olanlar çalışmayı severler. Hırslı ve disiplinlidirler. Hayallerini amaçlara dönüştürüp birer birer gerçekleştirirler. Kendi yarattıkları dünyalarına birilerini almaları biraz zordur. Hayat koşturmasından sevmeye vakit bulabilirlerse onu da hakkıyla yaparlar. İlişkilerini de sırtlarına alıp hayalleri ve hayatları peşinden gitmeye devam ederler."
P24 = "Dudak Yapısı : Üst Sivri Dudak, Kalp şeklinde dudaklara sahip olan kişiler, hayatlarında çok ama çok sosyaldirler. Ayrıca yaratıcı ve kıvrak zekalıdırlar. Bu kıvrak zeka, onların düşünmeden konuşmasına neden olsa da; iletişim konusunda aşmış bireyler olmaları en zor durumları bile toparlayabilmelerini sağlar. Sanatçı bir ruha sahip olan kalp dudaklılar, derinlerinde ise oldukça romantik kişilerdir. Onları sevmenin yeri ayrıdır, onlar tarafından sevilmekse apayrıdır!"
P25 = "Dudak Yapısı : Üst Yuvarlak Dudak, Yuvarlak dudaklara sahip olanlar fazlasıyla detaycı ve nazik insanlardır. Konu şefkate geldiğinde ise kimse onların eline su dökemez. Haliyle de insanları ve onlarla ilişkilerini çok önemserler. Onlardan da aynı nezaketi ve ilgiyi haklı olarak beklerler. Kendilerine değer verildiğini hissettiklerinde onlardan mutlusu da, mutlu edeni de yoktur."
P26 = "Dudak Yapısı : Üst Düz Dudak, Bu dudak şekline sahip olanlar oldukça arkadaş canlısı, içten ve samimidirler. Kendilerinden çok etraflarındaki insanları önemserler. Bu özellikleri kimi zaman onlara zarar verse de, onlar hallerinden hiç şikayet etmezler. Sorumluluk sahibidirler. Onlara eğlenmek de, evlenmek de çok yakışır."
P27 = "Dudak Yapısı : İnce Dudak, İnce dudaklara sahip olanlar çoğunlukla yalnızlığı severler. Birilerinin dikkatini çekmek, ortamda popüler kişi olmak gibi bir dertleri yoktur. Kendi hallerinde olmak onları en çok mutlu eden şeydir. İlişkilerinde de rahat olmayı, kendileri gibi davranabilmeyi tercih ederler. Yanlış anlamayın, bu durum onları kötü ilişki insanı yapmaz. Sadece, sınırlarına saygı duyulmasını beklerler ve bunu yapanlarla son derece sağlam ilişkiler kurabilirler."
P28 = "Dudak Yapısı : Sıradan Dudak, Nizami dudaklara sahip olanlar, ilişkilerinde dengeyi severler. Onlarla mutluluk kaçınılmaz gibi bir şeydir. Çünkü onlar gelgitli bir ilişkiden de, o ilişki içinde yaratılan dramalardan da nefret ederler. Ne ilgi aşığı tiplerdir, ne de umursamaz. Özetle tam anlamıyla her konuda harika insanlardır. Onları bulduysanız sarılın, bırakmayın. Zira öyleleri biraz değil, baya zor bulunur"

# Burun
P29 = "Burun Yapısı : Geniş Burun, Bu burna sahip kişiler sürekli çözüm ve fayda elde etmek için harcarlar vakitlerini. Çok hevesli ve meraklı olmalarının yanı sıra çok açık görüşlüdürler, vizyonları oldukça geniştir. Çekicidirler, insanları kolayca etkilemede başarılıdırlar. Sürekli bir koşturmaca halinde yaşarlar."
P30 = "Burun Yapısı : Sivri Burun, İş konusunda sağduyulu, hırslı, sağlam içgüdüye sahip, liderlik altında çalışmayı seven kişilerdir.Disiplinli,dürüst ve sadık bir insan.Anlayışlı, iyilik ve yardım sever bir insan."
P31 = "Burun Yapısı : Büyük Burun, Bu tip buruna sahip olanlar; liderlik özelliği olan, güçlü, ego sahibi kişilerdir. Emir almayı sevmez, kendi işinin patronu olmak isterler.Yöneticilik, liderlik, ego ve tek başına çalışma isteği büyük burnun getirdiği özelliklerdendir. Büyük burunlu insanlar emir almaktan nefret eder, kendi kendilerinin patronu olmak isterler."
P32 = "Burun Yapısı : Kücük Burun, Ufak buruna sahip olanlar; grup aktivitelerinde etkin, yaratıcı bir hayal gücüne sahiptir. Aynı zamanda sabırsız kişilerdir.Tez canlı ve sinirli yapıdaki bu insanlar kitleleri ateşleyecek güce sahiptirler. Buna rağmen şaşırtıcı derecede başkalarının iyiliğini düşünüp insanların yararları için çalışma istekleri vardır. Yoğun çalışma temposundan hoşlanırlar ve sisteme kolayca uyum sağlarlar"

know_me_personality = {
    "kare": P1,
    "kisavedar": P2,
    "yuvarlakcene": P3,
    "uzun": P4,

    "dogalduz": P5,
    "yuksekkenar": P6,
    "duzyukari": P7,
    "kisa": P8,
    "sivri": P9,
    "buyukbosluk": P10,
    "kucukbosluk": P11,
    "normalbosluk": P12,

    "kucuk": P13,
    "genis": P14,
    "badem": P15,
    "yuvarlakgoz": P16,
    "yakin": P17,
    "uzak": P18,
    "normal": P19,

    "buyukkabarik": P20,
    "kucukkabarik": P21,
    "ustkalinaltince": P22,
    "ustincealtkalin": P23,
    "ustsivri": P24,
    "ustyuvarlak": P25,
    "ustduz": P26,
    "ince": P27,
    "siradan": P28,

    "genisburun": P29,
    "sivriburun": P30,
    "buyukburun": P31,
    "kucukburun": P32
}

json_obj = json.dumps(know_me_personality)
f = open("know_me_personality.json", "w")
f.write(json_obj)
f.close()

C1 = "Huzursuzluk ve kavgadan hoşlanmayan. Sevdiklerine düşkün, sabırlı ve çalışkan. Kimsenin bir şeyinde gözü olmayan, kendi çalışıp kazanmaktan yana olan.Başarılı olmayı isteyen ve rahat, güvende yaşamayı arzulayan. Gayet kibar ve nazik. Doğru ve dürüst davranan. Başarısızlığa tahammülü olmayan, sevgiye önem veren.Takdir edilmekten hoşlanan, yeniliklere açık, bulunduğu alanda parlamak isteyen.Kimi zaman coşkulu bazen karamsar olabilen. Fakat asla pes etmeyen, direnen"
C2 = "Son derece mantıklı, becerikli, akıllı, sözünde duran. Eğitim hayatına önem veren. Öğrendiklerini kolay kolay unutmayan. Aklını ve yaratıcı hünerlerini kolaylıkla hayata geçirebilen.Neyin gerekli neyin gereksiz olduğunu iyi ayırt edebilen. Mantıklı.Gerektiğinde sert konuşabilen. Aynı anda birden fazla konuda bilgi sahibi olabilen. Gözlem gücü yüksek, iş hayatında başarıya mutlaka ulaşabilen."
C3 = "Açık sözlü, yenilikçi, toplum bilinci yüksek, arkadaşlık ilişkileri güçlü. Orijinal düşünebilen, tavırlarıyla ilgi uyandırabilen. Buluşçu.Gerektiğinde duygularını geri planda tutarak, mantıklı hareket edebilen. Zihinsel aktivite gücü yüksek, herkesten daha çabuk öğrenebilen.Uygulamaya dönük, analizci, çağın ötesinde üşünebilen.Zorluklar karşısında aklıyla kolayca çözüme ulaşan, sınırlamalardan hoşlanmayan."
C4 = "Hızlı düşünebilen, gayet becerikli, dürüst ve arkadaşlıklara önem veren. Tarafsız bir gözlem gücüne sahip, yapmacık insanlardan hoşlanmayan.Yabancı dil konusunda başarılı, konuşmaları sıradışı, yenilikçi. Bulunduğu ortamda kolayca ilgi uyandıran, sıradışı espri kabiliyeti olan.doğum tarihine göre kişiliğiniz Zeki, diğerlerinden çok çabuk öğrenen, kısa yoldan sonuca ulaşabilen. Bilime önem veren, tartışmalardan hoşlanan, ikna gücü yüksek."
C5 = "Sıradışı ilişkiler yaşamaya hevesli, özgürlüğüne düşkün. Yenilikçi. Yeni yerler keşfetmeye meraklı, modayı takip eden. Tasarımcı.Bulunduğu alana yenilikler getiren, orijinal ve çekici. Kaliteyi seven. Başkalarından oldukça farklı, rutinlikten hoşlanmayan. Arkadaş çevresi geniş.Seçici, iyi gözlemci, farklı kişiliği ile ilgi uyandırabilen. Çekiciliği ile karşı cins tarafından beğenilen, her giydiğini yakıştırmasını bilen."
C6 = "Hayal gücü oldukça yüksek. Sevdiklerine karşı duyarlı, çatışmalardan rahatsızlık duyan. Şifa gücü yüksek, insanlara sorunlarında yardımcı olabilen.Duyarlı bir kişilik. Acıma ve şefkat duygusu yüksek. Pozitif düşünmeye çalışan. Yaratıcı kabiliyetleri olan, yargılayıcı davranmayan, değişime açık.Karmaşa içinde yönelimini kaybetmeden ilerleyebilen, negatif insanlardan etkilenebilen. Derin tutkulara sahip, aşk ilişkilerinde verici ve cömert. Oldukça romantik, hassas."

C7 = "Duygularının farkında olan, bağımlılıklarına düşkün, kimi zaman değişken. Sosyal hayatta çekici kimliğiyle ilgi uyandıran, mütevazi ve çok sevilen.Ailesine düşkün, evini yuvasını önemseyen, aşkta tutkulu, güzel düşünen.Kötülük bilmeyen, kendine yapıldığında oldukça etkilenen.Muazzam yeteneklere sahip, sezgileri güçlü, olacakları hissedebilen. Karşı cins üzerinde duruşu, tavırları, fiziksel özellikleriyle oldukça beğenilen."
C8 = "Vizyon sahibi, her yerde başarılı olabilen. Hayallerini gerçeğe dönüştürebilen. Gücünü iyilik ve güzellikler adına yönlendirebilen. Öngörüleri doğru çıkan.Doğaüstü yetenekleri olan, yalnız kaldığında güçlenen. Başkalarını kolaylıkla etkileyebilen. Olumlu ve güçlü enerjilere sahip.Kararlılık gösterdiği zamanlarda her işin üstesinden kolayca gelebilen. Güçlü bir manyetizmaya sahip, gizlilikleri kolayca öğrenebilen. Sırdaş."
C9 = "Fiziksel yönden oldukça güçlü. Hedefini bilen ve yılmadan üzerine gidebilen. İsteklerine fazlasıyla düşkün. Dediğim dedik asla geri dönmeyen Emir almaktan hoşlanmayan. Kendi bildiği yolda ilerlemeyi seven.Cinselliği yoğun ve etkileyici."
C10 = "Çok canlı, bireylik duygusu yüksek Yaratıcı enerjiye sahip, pırıltılı bir kişilik.Yönetme gücü olan, insanları kolayca etkileyebilen. İyi bir oyuncu (sanat), kendini ifade etmesini bilen.Hayatın güzel yanlarının tadını çıkarmasını bilen. İsteklerini gerçekleştirme gücüne sahip renkli bir kişi."
C11 = "Keşfetmekten, yeniliklerde bulunmaktan hoşlanan.Para harcama meyli yüksek, hoşsohbet, açık fikirli. İyi niyetli, geleceğini şekillendirmeyi seven, yürekli İnançlı, sağduyulu, cömert ve kendine güvenen. Adaletli, yardıma hazır, takdir edilmeyi seven.Yabancı dile meyilli, seyahat etmekten hoşlanan."
C12 = "Güzelliklere aşık, gösterişli ve kaliteli olan herşeyi seven. Maddi ve manevi değerlerini önemseyen, koruyan, sahiplenen.Sosyal hayatın içinde yer almaktan zevk alan. Arkadaşlarının önemseyen. Güzel bir çevrede yaşamak isteyen. Duyarlı ve estetik bir kişi.İnce ve Nazik yapısıyla takdir edilen ve sevgi duyulan. Uzlaşmazlık, kavga ve çekişmelerden hoşlanmayan."

C13 = "Zihinsel yetenekleri yüksek, aklını önemseyen, sezgileri kuvvetli. İlgi alanları yoğun, dünyayı gözlemlemekten hoşlanan.Konuşma ve yazma yeteneği son derece güçlü. İnsanları kolayca çözebilen. Değerlendirme gücü yoğun, organizasyon becerisi muazzam.Başkalarıyla çalışmaya müsait, uyumlu. Fazla detaydan hoşlanmayan. Özgürlüğüne önem veren. Konuşmasıyla karşısındakini etkileyebilen."
C14 = "Gayet güvenilir, dürüst yaklaşımlara sahip. Güçlü ve derin duyguları olan. Aşk ilişkilerinde güvenilir, karşısındakine değer veren.Gerçekçi düşünebilen, kendine yeterli. Başarma tutkusu olan, çalışkan. Güzelliklere önem veren, kabalıktan hoşlanmayan. Keskin gözlem gücü olan.Başkalarının haksız sözlerinden etkilenebilen. Arkadaşlığa önem veren. Hedefine ulaştığında böbürlenmeyen. İyiliğin, vefanın kıymetini bilen."
C15 = "Çok yönlü ve becerikli. Yargı ve mantık gücüne sahip. Yenilikten hoşlanan, yeni insanlar tanımaktan zevk alan.Bilgiyi önemseyen, meraklı ve öğrenmeye aç. Mantıklı, eğri ile doğruyu ayır etmesini bilen.Kıvrak zeka, konuşma kabiliyeti, kendini yönlendirebilen. Düşmanlarını yenmeye başarabilecek kadar akıllı."
C16 = "Sosyal ilişkilerini önemseyen, akıllı davranabilen. Zeki, uzlaşmacı, hayatın güzel yanlarının tadını çıkarabilen.Nabza göre şerbet vermeyi bilen. Yeniliklerden hoşlanan. Değerli olanı bilen, duyarlı ve yapıcı davranabilen.Rahatına düşkün, sıradan şeylerden hoşlanmayan. Kaliteye önem veren. İnce, nazik, aşka önem veren. İyi niyetli, arkadaşlıklara önem veren."
C17 = "Modern düşünebilen, tarafsız ve objektif düşünebilen. Manyetizması güçlü, arkadaşlık olgusunu önemseyen.Özgürlüğüne düşkün, mantıklı davranabilen. Orijinal herşeyden hoşlanan. Pek çok insanla anlaşabilen.Fikirleri bir çok insan tarafından beğenilen. Kuvvetli iradesi olan. Yaratıcı, bireylik duygusu gelişmiş, haksızlığa boyun eğmeyen."
C18 = "Güvende yaşamak isteyen, empati yönü güçlü, duyarlı kişilik Ailesine, sevdiklerine önem veren. Koruyucu ve kollayıcı.Gerçeklerin peşinden koşabilen. İlişkilerde uzlaşmaktan yana olan. Duygusal değerlerine önem veren, etkileme gücü yüksek.Karşısındaki kişiyi kolaylıkla etkileyebilen, ruhunun derinliklerine inebilen. Kendini güvende hissetmediğinde tepkisel davranabilen."

C19 = "Düşünce gücü yüksek, sezgileri mükemmel derecede yoğun. Bulunduğu alanı kötülüklerden arındırabilen, yenilikçi düşünebilen.Şüphelerini aydınlığa kavuşturabilen, kendini yenileyebilen. Yüzeyde olanlarla yetinmeyen, araştırmadan güvenmeyen.Zihnini ve iradesini kendi gelişimi için odaklamasını bilen. Güçlü iyileştirme gücü olan, güçlü olmayı, güvende olmayı önemseyen."
C20 = "Artistik kabiliyeti olan, aydınlanmaktan yana. Sanata meyilli. Acıma ve şefkat duyguları yüksek. İdealist Kendini inandığı bir şeye adayabilen, vizyonu yüksek. Kendini aşmak isteyen, duyarlı yüreğe sahip, özverili.Özlemleri olan, hayal gücü yüksek. Duyu dışı algıları olan. Birçok insanla anlaşabilen, aşkta derin duygulara sahip."
C21 = "Kendinden emin, bağımsız, liderlik gücü yüksek. Soylu, gururlu, gösterişli, toplumda hemen farkedilen.Sadakat duygusu yüksek, organizasyon yeteneğine sahip. Sevdiklerine düşkün, sanatkar, kolayca yükselebilen.İçi dışı bir, kalbinin sesine kulak verebilen. Sevilmeyi önemseyen. Yaratıcılık yeteneği olan, isteklerini direkt olarak açıklayabilen."
C22 = "Hoşsohbetli, neşeli, etrafını rahatlatan, vicdanlı. Para harcamayı seven, kaliteye önem veren, gururlu.Kimseyi kırmaktan hoşlanmayan, yüce gönüllü. Gezmekten, araştırmaktan hoşlanan, inanç sahibi, maneviyatı güçlü.İyi bir sırdaş, güçlü bir dost. Başkalarının emri altına girmekten hoşlanmayan, özgürlüğü seven."
C23 = "Kendini ortaya koyabilen, savaşçı, enerjik, isteklerini elde edebilen. Bilinçli, cesur, haksızlıklara boyun eğmeyen. Yeni fikirleri önemseyen.Girişimci, zeki, nerde ne yapması gerektiğini bilen. Açık sözlü. Hayatta kalmayı başarabilen. Fiziksel gücü yüksek.Karşısındaki kişiyi çabucak çözebilen, açık sözlü. Beklemekten hoşlanmayan, yeni projelere, planlamalara istekli."
C24 = "Mantıklı, becerikli, akıllı, başkalarıyla kolaylıkla bağlantı kurabilen. Aşkı önemseyen, sorunlardan pek hoşlanmayan.Kaliteli ortamlar, elit yerlerden hoşlanan. Cahil insanlardan uzak duran. Keskin gözlem gücüne sahip, bir bakışta eksiklerini görebilen.Olayların ardındaki gerçekleri önemseyen ve öğrenmek isteyen. Çabuk kavrayan, net görmek isteyen, iletişimci."

C25 = "Ciddi bakış açısına sahip, sağlam kararlar vermeye çalışan. Beklentileri akla ve mantığa uygun, çalışkan ve planlı.Güven olgusunu önemseyen, yanlış kararlar vermekten hoşlanmayan. Disiplinli çaba, görev ve sorumluluk bilinci yüksek olan.Dayanıklı, mesleki konularda yetenekli. Dikkatli konuşan. Yaşından olgun. Sözleri tutarlı, kabul edilmekten hoşlanan."
C26 = "Yerinde konuşan, güçlü bir kişilik, sevme duygusu gayet yüksek. Uyumlu, dengeli, akıllı ve gayet çekici.Aşkta sıcak yürekli, nezaket dolu, güçlü imaj sahibi. Huzursuzluktan hoşlanmayan, böyle ortamlarda bulunmak istemeyen.Sosyallikten hoşlanan ama aşırı uçlara kaçmayı sevmeyen. Öncü, akıllı, iletişimci bir kişilik. Tarafsız düşünebilen."
C27 = "Lüks, güzellik, kaliteden hoşlanan. Sevgi dolu bir kişilik. Erkekleri yakışıklı, kadınları çok güzel olan.Sosyal yönü güçlü, yeni fikirleri seven, hassas yaradılışda Zevkleri için para harcamaktan çekinmeyen, bu yüzden zorlanan.Seyahat etmekten hoşlanan, yeni insanlarla tanışmaktan zevk alan Amaçları bir şekilde gerçekleştirebilecek şansa sahip olan."
C28 = "Başkaları tarafından her zaman ilginç, sıra dışı bulunan, çok çekici Özgürlüğüne düşkün, kurallarla çevrelenmekten hoşlanmayan Sosyal ilişkilerini önemseyen, popüler ve girdiği ortamlarda farkedilen Toplum içindeki yerini önemseyen, farklı bulunmaktan hoşlanan Kararlarını kendi vermekten zevk alan ve bunda ısrar edebilen. Günün yenilik anlamındaki tüm akımlarını takip eden, uygulayabilen."
C29 = "Fiziksel ve zihinsel anlamda hızlı ve aktif hareket edebilen. Sözleriyle ilgi uyandırabilen, zekasıyla her türlü sorunun üstesinden gelebilen Aşkta aşırı duygusallık yerine gerektiğinde mantığının sesine kulak verebilen. Hislerini kağıda dökebilen. İşbirliğini önemseyen, etrafıyla uyumlu özel bir kişilik. Yenilikleri uygulamaktan hoşlanan, cinselliğine önem veren. Cazibeli, aydınlık fikirleri olan, başarmaktan, gelişmekten, büyümekte hoşlanan."
C30 = "Kadınları oldukça çekici, Erkekleri karizmatik. Karşı cins üzerinde gayet etkililer. Mistizm, bilinmeyenler konusunda meraklı ve bu yönde yetenekleri olabilen.Dönüşüm, değişim ve her türlü yenilikten hoşlanan. Bunun için gerekirse savaşabilen. Sözleri keskin kendine güvenli. Doğruluktan hoşlanan. Disiplinli ve güçlü bir karakter.Gizliliklerine önem veren, başkalarının sırlarını kolayca öğrenebilen. Güç ve kontrol kurmaktan hoşlanan, sözlerinin dinlenmesini isteyen."

C31 = "Oldukça duyarlı, Romantik ve tutkulu. İdeallerinden ödün vermeyen. Hayal gücü yüksek fakat hayal ettiklerini hayatında uygulayabilen. Sezgileri yüksek.Aşkla büyümekten, gelişmekten hoşlanan. Aşkı için her türlü mücadeleye giren. Başkalarının sorunlarına çare bulabilen, empatisi yüksek, yönlendirme gücü yoğun.Başkalarıyla yarışabilen, yüksek noktalara er veya geç gelebilecek güçlü bir karekter. Derinlikten hoşlanan, iş olsun diye dost olmayan, dostuna gerçekten yardım edebilen."
C32 = "Oldukça etkileyici bir kişilik. Haksızlıklar karşısında her türlü mücadeleye girişebilen. Dürüst ve doğrucu bir insan. Hakikatlerin ışığı altında ilerlemekten yana olan.Toplumsal vizyonu yüksek, girdiği ortamlarda çekiciliği, duruşuyla kolayca ilgi uyandıran. Gayet şanslı. Sezgileri inanılmaz güçlü. Olacakları hissedebilen.Herhangi bir durum ve olayın ardından kolayca toparlanması bilen. Empati yeteneği güçlü. Altıncı duyusu çok yüksek. Önsezileri inanılmaz kuvvetli. Vatanına, ailesine çok düşkün biri."
C33 = "Ahlaki özellikleri son derece güçlü. İnanışı, özgüven duygusu gelişmiş, dürüst kişilerdir. Geniş görüşlü, vicdanlı, değerlerine önem veren, yüksek eğitimden hoşlanan.İyimser, öngörüşleri doğru çıkan. Gezgin bir ruh, yaşamı derinlemesine yaşamaktan hoşlanan. Aşkta bağlanma duygusu fazla yüksek olmasa da, sevdiklerine düşkün ve onları koruyan.Başka insanları bilgisiyle, zarafetiyle büyüleyen. Yol gösteren abilik ablalık yapabilen. İnsancıl, açık fikirli. Etik değerlere ve kanunlara saygılı. Fazla para harcamayı seven."
C34 = "Çok cesur. İnanmadığı hiçbir şeyi kabul etmeyen. Savaşma dürtüsü yüksek. Haksızlıklara boyun eğmeyen amaca yönelik hareket edebilen.Gayet bağımsız zincirlere tahammül etmeyen. Kimsenin lafıyla hareket etmeyen. Sadık ve oldukça fedakar. Söz verdiği zaman mutlaka yerine getiren.Aktif, hızlı ve gözüpek. Cinselliği güçlü, tutkulu, girişimci, istediği kişiye elde edebilen. Kimi zaman oldukça sabırsız, aceleci davranabilen. Rekabetçi, oldukça tutkulu."
C35 = "Kişilik sahibi, bilgisiyle, tecrübeleriyle insanları kolayca etkisi altına alabilen. Vizyonu güçlü, sezgi gücü yüksek, anlamaktan, keşfetmekten zevk alabilen.Duygularını kontrol edebilen, sevilmek ve ilgi görmekten fazlasıyla hoşlanan. Aşkta kendi isteklerine düşkün. Çekiciliğiyle karşı cins üzerinde fazlasıyla etkili olan.Yanılmaktan hiç hoşlanmayan. Sanata ve yeni gelişmelere açık. Kendini gayet iyi koruyan. Yenilgilerden yılmayan, gururlu ve kendini geliştirmesini bilen, hakimiyet kurabilen."
C36 = "Sorumluluk sahibi, ne istediğini bilen, doğru ve yerinde kararlar alabilen bir kişilik. Disiplinli bir çaba ile her türlü güçlüğün üstesinden gelebilen. Sadık ve güvenilir.İç gözlem gücüne sahip, yavaş ve emin adımlarla ilerlemekten yana olan. Koşullar ve şartlara göre kendini ayarlayabilen uçarılıktan asla hoşlanmayan.Aşkta güven, saygı ve sevgiye değer veren. Oldukça tutkulu, sevdiğine sahip çıkan. Liderlik gücü yüksek, organize, iş hayatında parlayabilen. Bazen karamsar olabilen."


zod = []

zod.append({"start_day": 1, "start_month": 1, "finish_day": 10, "finish_month": 1, "comment": C1})
zod.append({"start_day": 11, "start_month": 1, "finish_day": 19, "finish_month": 1, "comment": C2})
zod.append({"start_day": 20, "start_month": 1, "finish_day": 29, "finish_month": 1, "comment": C3})
zod.append({"start_day": 30, "start_month": 1, "finish_day": 8, "finish_month": 2, "comment": C4})
zod.append({"start_day": 9, "start_month": 2, "finish_day": 18, "finish_month": 2, "comment": C5})
zod.append({"start_day": 19, "start_month": 2, "finish_day": 29, "finish_month": 2, "comment": C6})

zod.append({"start_day": 1, "start_month": 3, "finish_day": 10, "finish_month": 3, "comment": C7})
zod.append({"start_day": 11, "start_month": 3, "finish_day": 20, "finish_month": 3, "comment": C8})
zod.append({"start_day": 21, "start_month": 3, "finish_day": 31, "finish_month": 3, "comment": C9})
zod.append({"start_day": 1, "start_month": 4, "finish_day": 9, "finish_month": 4, "comment": C10})
zod.append({"start_day": 10, "start_month": 4, "finish_day": 19, "finish_month": 4, "comment": C11})
zod.append({"start_day": 20, "start_month": 4, "finish_day": 30, "finish_month": 4, "comment": C12})

zod.append({"start_day": 1, "start_month": 5, "finish_day": 10, "finish_month": 5, "comment": C13})
zod.append({"start_day": 11, "start_month": 5, "finish_day": 20, "finish_month": 5, "comment": C14})
zod.append({"start_day": 21, "start_month": 5, "finish_day": 31, "finish_month": 5, "comment": C15})
zod.append({"start_day": 1, "start_month": 6, "finish_day": 10, "finish_month": 6, "comment": C16})
zod.append({"start_day": 11, "start_month": 6, "finish_day": 21, "finish_month": 6, "comment": C17})
zod.append({"start_day": 22, "start_month": 6, "finish_day": 30, "finish_month": 6, "comment": C18})

zod.append({"start_day": 1, "start_month": 7, "finish_day": 11, "finish_month": 7, "comment": C19})
zod.append({"start_day": 12, "start_month": 7, "finish_day": 22, "finish_month": 7, "comment": C20})
zod.append({"start_day": 23, "start_month": 7, "finish_day": 1, "finish_month": 8, "comment": C21})
zod.append({"start_day": 2, "start_month": 8, "finish_day": 12, "finish_month": 8, "comment": C22})
zod.append({"start_day": 13, "start_month": 8, "finish_day": 22, "finish_month": 8, "comment": C23})
zod.append({"start_day": 23, "start_month": 8, "finish_day": 1, "finish_month": 9, "comment": C24})

zod.append({"start_day": 2, "start_month": 9, "finish_day": 12, "finish_month": 9, "comment": C25})
zod.append({"start_day": 13, "start_month": 9, "finish_day": 22, "finish_month": 9, "comment": C26})
zod.append({"start_day": 23, "start_month": 9, "finish_day": 2, "finish_month": 10, "comment": C27})
zod.append({"start_day": 3, "start_month": 10, "finish_day": 13, "finish_month": 10, "comment": C28})
zod.append({"start_day": 14, "start_month": 10, "finish_day": 23, "finish_month": 10, "comment": C29})
zod.append({"start_day": 24, "start_month": 10, "finish_day": 1, "finish_month": 11, "comment": C30})

zod.append({"start_day": 2, "start_month": 11, "finish_day": 11, "finish_month": 11, "comment": C31})
zod.append({"start_day": 12, "start_month": 11, "finish_day": 22, "finish_month": 11, "comment": C32})
zod.append({"start_day": 23, "start_month": 11, "finish_day": 1, "finish_month": 12, "comment": C33})
zod.append({"start_day": 2, "start_month": 12, "finish_day": 11, "finish_month": 12, "comment": C34})
zod.append({"start_day": 12, "start_month": 12, "finish_day": 21, "finish_month": 12, "comment": C35})
zod.append({"start_day": 22, "start_month": 12, "finish_day": 31, "finish_month": 12, "comment": C36})


json_obj = json.dumps(zod)
f = open("know_me_zodiac.json", "w")
f.write(json_obj)
f.close()