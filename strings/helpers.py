HELP_1 = """<b><u>YÖNETİCİ KOMUTLARI:</b></u>

Komutların başına <b>C</b> ekleyerek kanallar için kullanabilirsiniz.

/pause : Mevcut oynatılan yayını duraklatır.

/resume : Duraklatılan yayını devam ettirir.

/skip : Mevcut oynatılan yayını atlar ve sıradaki parçayı oynatmaya başlar.

/end veya /stop : Sırayı temizler ve mevcut oynatılan yayını sonlandırır.

/player : Etkileşimli bir oynatıcı paneli alır.

/queue : Sıradaki parçaları gösterir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_2 = """
<b><u>YETKİLİ KULLANICILAR:</b></u>

Yetkili kullanıcılar, sohbette yönetici haklarına sahip olmadan botta yönetici haklarını kullanabilirler.

/auth [kullanıcı adı/kullanıcı ID] : Bir kullanıcıyı botun yetkili listesine ekler.
/unauth [kullanıcı adı/kullanıcı ID] : Yetkili kullanıcıyı yetkili listesinden çıkarır.
/authusers : Grubun yetkili kullanıcılarının listesini gösterir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_3 = """
<u><b>YAYIN ÖZELLİĞİ</b></u> [Sadece Sudo kullanıcıları için]:

/broadcast [mesaj veya mesaja cevap] : Botun hizmet verdiği sohbetlerde bir mesajı yayınlar.

<u>Yayın Modları:</u>
<b>-pin</b> : Yayınlanan mesajları hizmet verilen sohbetlerde sabitler.
<b>-pinloud</b> : Yayınlanan mesajı hizmet verilen sohbetlerde sabitler ve üyelere bildirim gönderir.
<b>-user</b> : Mesajı botu başlatan kullanıcılara yayınlar.
<b>-assistant</b> : Mesajı botun yardımcı hesabından yayınlar.
<b>-nobot</b> : Botun mesajı yayınlamasını engeller.

<b>Örnek:</b> <code>/broadcast -user -assistant -pin test yayını</code>

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_4 = """<u><b>SOHBET KARALİSTESİ ÖZELLİĞİ:</b></u> [Sadece Sudo kullanıcıları için]

Botumuzu kullanmak için kötü sohbetleri kısıtlayın.

/blacklistchat [sohbet ID] : Bir sohbeti botu kullanmaktan kara listeye alır.
/whitelistchat [sohbet ID] : Kara listeden sohbeti beyaz listeye alır.
/blacklistedchat : Kara listeye alınan sohbetlerin listesini gösterir.

☆✧✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_5 = """
<u><b>KULLANICI ENGELLEME:</b></u> [Sadece Sudo kullanıcıları için]

Kara listeye alınan kullanıcıyı görmezden gelmeye başlar, böylece bot komutlarını kullanamaz.

/block [kullanıcı adı veya kullanıcıya cevap] : Kullanıcıyı botumuzdan engeller.
/unblock [kullanıcı adı veya kullanıcıya cevap] : Engellenen kullanıcıyı engellemesini kaldırır.
/blockedusers : Engellenen kullanıcıların listesini gösterir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_6 = """
<u><b>KANAL OYNATMA KOMUTLARI:</b></u>

Kanallarda ses/video akışı yapabilirsiniz.

/oynat : Kanalın video sohbetinde istenen ses parçasını oynatmaya başlar.
/cvoynat : Kanalın video sohbetinde istenen video parçasını oynatmaya başlar.
/cplayforce veya /cvplayforce : Devam eden yayını durdurur ve istenen parçayı oynatmaya başlar.

/channelplay [sohbet kullanıcı adı veya ID] veya [devre dışı bırak] : Bir gruba kanal bağlar ve grup komutlarıyla parça yayını başlatır.
/bass ➠ Ses dosyasına bas eklemek için bir ses dosyasına cevap verin...
/dj ➠ Ses dosyasına DJ efekti eklemek için bir ses dosyasına cevap verin...

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_7 = """
<u><b>GENEL YASAKLAMA ÖZELLİĞİ</b></u> [Sadece Sudo kullanıcıları için]:

/gban [kullanıcı adı veya kullanıcıya cevap] : Kullanıcıyı tüm hizmet verilen sohbetlerde genel olarak yasaklar ve botu kullanmasını engeller.
/ungban [kullanıcı adı veya kullanıcıya cevap] : Genel olarak yasaklanan kullanıcının yasaklamasını kaldırır.
/gbannedusers : Genel olarak yasaklanan kullanıcıların listesini gösterir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_8 = """
<b><u>LOOP STREAM:</b></u>

<b>Devam eden yayını döngüde oynatır</b>

/loop [etkinleştir/devre dışı bırak] : Devam eden yayın için döngüyü etkinleştirir/devre dışı bırakır
/loop [1, 2, 3, ...] : Belirtilen değer için döngüyü etkinleştirir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_9 = """
<u><b>BAKIM MODU</b></u> [Sadece Sudo kullanıcıları için]:

/logs : Botun günlüklerini alır.

/logger [etkinleştir/devre dışı bırak] : Botun etkinlikleri günlüğe kaydetmeye başlamasını sağlar.

/maintenance [etkinleştir/devre dışı bırak] : Botun bakım modunu etkinleştirir veya devre dışı bırakır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_10 = """
<b><u>Ping & Stats:</b></u>

/start : Müzik botunu başlatır.
/help : Komutların açıklamalarıyla birlikte yardım menüsünü alır.

/toe : Botun ping ve sistem istatistiklerini gösterir.

/stats : Botun genel istatistiklerini gösterir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_11 = """
<u><b>OYUN KOMUTLARI:</b></u>

<b>v :</b> Video oynatma anlamına gelir.
<b>force :</b> Zorla oynatma anlamına gelir.

/oynat veya /voynat : İstenen parçayı video sohbette oynatmaya başlar.

/playforce veya /vplayforce : Devam eden yayını durdurur ve istenen parçayı oynatmaya başlar.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_12 = """
<b><u>ŞARKI KARMA:</b></u>

/shuffle : Sıradaki parçaları karıştırır.
/queue : Karışık sıradaki parçaları gösterir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_13 = """
<b><u>AKIŞTA İLERLEME:</b></u>

/seek [saniye cinsinden süre] : Yayını belirtilen süreye getirir.
/seekback [saniye cinsinden süre] : Yayını belirtilen süreye geri alır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_14 = """
<b><u>İNDİRME BÖLÜMÜ</b></u>

/song [şarkı adı/YT URL] : YouTube'dan herhangi bir parçayı MP3 veya MP4 formatında indirir.
/video veya /yt  ➠ Bağlantı veya video adını komuttan sonra girerek videoyu indir.
/insta ➠ Instagram reeli indir
Tabii, çeviriye devam ediyorum:
/movie ➠ O filmin bilgilerini almak için kullanılır.
/remove ➠ [video veya ses] Bir video dosyasına yanıt olarak, ses veya video dosyasını kaldırmak için kullanılır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_15 = """
<b><u>HIZ KOMUTLARI:</b></u>

Devam eden yayının oynatma hızını kontrol edebilirsiniz. [Yalnızca yöneticiler]

/speed veya /playback : Grup içinde ses oynatma hızını ayarlamak için kullanılır.
/cspeed veya /cplayback : Kanal içinde ses oynatma hızını ayarlamak için kullanılır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_16 = """
<b><u>ChatGPT:</b></u>

Jarvis - Bu komutla Jarvis'e erişebilirsiniz.
Assis - Yapay zeka sesli yanıt verir.
 /gpt - GPT işlevselliğine erişmek için kullanılır.
 /bard - Bard özelliğini çağırır.
 /llama - Llama modunu etkinleştirir.
 /gemini - Gemini modunu keşfeder.
 /mistral - Mistral kodunu etkinleştirir.
 /tts - Metni sese dönüştürmek için kullanılır.
 /bingsearch - Bing platformunda arama yapmak için kullanılır.
 /logo - Komuttan sonra metin girerek logo oluşturur.
 /animelogo - Komuttan sonra metin girerek anime logosu oluşturur.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_17 = """
<b><u>STICKERS:</b></u>

/mmf ➠ Resmi veya sticker'ı meme yapmak için kullanılır.
/tiny ➠ Küçültmek istediğiniz stickera yanıt verin.
/kang ➠ Resimleri sticker olarak almak için kullanılır.
/packkang ➠ Diğer bir paketten sticker seti oluşturur.
/stickerid ➠ Sticker'ın kimliğini alır.
/st ➠ Sticker bulmak için sticker kimliğini komuttan sonra girin.
/meme ➠ Meme oluşturmak için kullanılır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_18 = """
<b><u>Tag-All:</b></u>

 /utag veya /uall ➠ Sınırsız etiketleme için kullanılır....🫠
 /stoputag veya /offuall ➠ Sınırsız etiketlemeyi durdurmak için kullanılır.
 /mention veya /all ➠ Komuttan sonra metin girin veya metne yanıt vererek herkesi etiketleyin.
 /cancel veya /alloff ➠ Etiketlemeyi iptal etmek için kullanılır.
 /tagall ➠ Rastgele komik etiketlemeler için kullanılır 😁.
 /tagoff veya /tagstop ➠ Komik etiketlemeleri durdurmak için kullanılır.
 /gmtag ➠ Sabah dilekleri için etiketleme🥰.
 /gmstop ➠ Sabah dileklerini durdurmak için kullanılır.
 /gntag ➠ Gece dilekleri için etiketleme 😴.
 /gnstop ➠ Gece dileklerini durdurmak için kullanılır.
 /hitag ➠ Kullanıcıları Hintçe alıntılarla etiketlemek için kullanılır.
 /histop ➠ Hintçe alıntıları durdurmak için kullanılır.
 /entag ➠ İngilizce etiketlemek için kullanılır...
 /entop ➠ İngilizce etiketlemeyi durdurmak için kullanılır.
 /bntag ➠ Bengalce etiketlemek için kullanılır...
 /bnstop ➠ Bengalce etiketlemeyi durdurmak için kullanılır.
 /lifetag ➠ İngilizce alıntılarla kullanıcıları etiketlemek için kullanılır.
 /lifestop ➠ İngilizce alıntıları durdurmak için kullanılır.
 /shayari ➠ Tüm kullanıcıları Shayari ile etiketlemek için kullanılır 😜.
 /shayarioff ➠ Shayari etiketlemeyi durdurmak için kullanılır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_19 = """
<b><u>BİLGİ:</b></u>

/id : Mevcut grup kimliğini alır. Bir mesaja yanıt verilirse, o kullanıcının kimliğini alır.
/info : Bir kullanıcı hakkında bilgi alır.
/github <kullanıcı adı> : Bir GitHub kullanıcısı hakkında bilgi alır.
/sg ➠ Kimlik ve kullanıcı adına yanıt vererek o kişinin geçmişini almak için kullanılır.
/groupdata & /groupinfo ➠ Grup bilgilerini almak için kullanılır.
/whois ➠ Kullanıcı adı veya yanıt vererek o kişi hakkında detayları öğrenmek için kullanılır.
/phone ➠ Komuttan sonra telefon numaranızı girerek detayları almak için kullanılır.
/Whatsapp {telefon numarası} ➠ WhatsApp için doğrudan bağlantı oluşturmak için kullanılır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_20 = """
<b><u>GRUP:</b></u>
Bu, grup yönetimi komutlarının listesidir:

⦿ /pin ➠ Grubun içinde bir mesajı sabitler.
⦿ /pinned ➠ Grubun içinde sabitlenmiş mesajı gösterir.
⦿ /unpin ➠ Mevcut sabitlenmiş mesajı sabitlemesini kaldırır.
⦿ /staff ➠ Personel üyelerinin listesini gösterir.
⦿ /bots ➠ Grubun içinde botların listesini gösterir.
⦿ /settitle ➠ Grubun başlığını ayarlar.
⦿ /setdiscription ➠ Grubun açıklamasını ayarlar.
⦿ /wel ➠ Karşılama mesajını açar veya kapatır.
⦿ /filter ➠ Grubun içinde filtre ayarlamak için kullanılır.
⦿ /stopfilter ➠ Filtre adını komuttan sonra girerek o filtreyi durdurmak için kullanılır.
⦿ /setphoto ➠ Grubun fotoğrafını ayarlar.
⦿ /removephoto ➠ Grubun fotoğrafını kaldırır.
⦿ /zombies ➠ Grubun içindeki silinmiş üyeleri kaldırır.
⦿ /imposter aç/kapat ➠ Grubunuz için izleyiciyi açar veya kapatır, kullanıcı adını veya adını değiştiren kullanıcılar hakkında bilgilendirir.
⦿ /lang ➠ Bot dilini değiştirir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_21 = """
<b><u>EKSTRA:</b></u>

⦿ /math ➠ Matematiksel problemleri ve denklemleri çözer.
⦿ /blackpink ➠ Blackpink tarzında bir logo oluşturur.
⦿ /carbon ➠ Bir kod snippet'inden karbon kodu görüntüsü oluşturur.
⦿ /speedtest ➠ İnternet hızını ölçer.
⦿ /reverse ➠ Verilen metni tersine çevirir.
⦿ /webss ➠ Bir web sitesinin ekran görüntüsünü alır.
⦿ /webdl ➠ Komuttan sonra web sitesinin bağlantısını girerek o sitenin kaynak kodunu alır.
⦿ /paste ➠ Bir metin snippet'ini buluta yükler ve bir bağlantı verir.
⦿ /tgm ➠ (5MB altında) bir fotoğrafı buluta yükler ve bir bağlantı verir.
⦿ /tr ➠ Metni çevirir.
⦿ /google ➠ Google'da bilgi arar.
⦿ /stack ➠ Stackoverflow'da programlama ile ilgili bilgi arar.
⦿ /short ➠ Kısaltmak istediğiniz bağlantıyı komuttan sonra girin.
⦿ /pdf ➠ JPEG dosyasına yanıt vererek resmi PDF'ye dönüştürür.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_22 = """
<b><u>RESİM:</b></u>
Bunlar mevcut resim komutlarıdır:

⦿ /draw ➠ Verilen bir konuya dayalı bir çizim oluşturur.
⦿ /image ➠ Verilen bir anahtar kelimeye dayalı bir resim arar.
⦿ /upscale ➠ Bir resme yanıt vererek onu büyütür ve kalitesini artırır.
⦿ /rmbg ➠ Bir resmin arka planını kaldırmak için kullanılır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_23 = """
<b><u>EYLEM:</b></u>
» Yasaklar ve Sessizler için kullanılabilir komutlar:

 ❍ /kickme: Komutu veren kullanıcıyı gruptan çıkarır.

Yalnızca yöneticiler:
 ❍ /ban <kullanıcı adı>: Bir kullanıcıyı yasaklar. (kullanıcı adıyla veya yanıtla)
 ❍ /sban <kullanıcı adı>: Bir kullanıcıyı sessizce yasaklar. Komutu, yanıtlanan mesajı siler ve yanıt vermez. (kullanıcı adıyla veya yanıtla)
 ❍ /tban <kullanıcı adı> x(m/h/g): Bir kullanıcıyı x süreyle yasaklar. (kullanıcı adıyla veya yanıtla). m = dakika, h = saat, g = gün.
 ❍ /unban <kullanıcı adı>: Bir kullanıcıyı yasaklamaktan çıkarır. (kullanıcı adıyla veya yanıtla)
 ❍ /kick <kullanıcı adı>: Bir kullanıcıyı gruptan çıkarır. (kullanıcı adıyla veya yanıtla)
 ❍ /mute <kullanıcı adı>: Bir kullanıcıyı sessize alır. Yanıt olarak da kullanılabilir, yanıtlanan kullanıcıyı sessize alır.
 ❍ /tmute <kullanıcı adı> x(m/h/g): Bir kullanıcıyı x süreyle sessize alır. (kullanıcı adıyla veya yanıtla). m = dakika, h = saat, g = gün.
 ❍ /unmute <kullanıcı adı>: Bir kullanıcıyı sessizlikten çıkarır. Yanıt olarak da kullanılabilir, yanıtlanan kullanıcıyı sessizlikten çıkarır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_24 = """
<b><u>ARAMA:</b></u>
Mevcut komutlar:
• /google <sorgu> : Verilen sorguyu Google'da arar.
• /anime <sorgu> : Verilen sorguyu myanimelist'te arar.
• /stack <sorgu> : Verilen sorguyu stackoverflow'da arar.
• /image (/imgs) <sorgu> : Sorgunuza ilişkin resimleri alır.
• /mongochk ➠ Mongo'nun durumunu kontrol eder [bağlantıyı komuttan sonra girin].
• /ip ➠ IP adresini komuttan sonra girerek bilgi alır.
• /domain ➠ Alan adı bilgisini almak için komuttan sonra alan adını girin.
• /weather ➠ Konum bilgisini komuttan sonra girerek o konumun hava durumunu alır.
• /Time ➠ Zaman diliminizin saatini almak için kullanılır.
• /calendar ➠ Yılı girerek takvim bilgilerini alır.
• /day ➠ {yıl/ay/gün} formatında tarihi girerek o günün hangi güne denk geldiğini öğrenmek için kullanılır.
• /get_states ➠ Ülke adını komuttan sonra girerek o ülkenin eyalet bilgilerini alır.

Örnek:/google pyrogram: İlk 5 sonucu döndürür.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_25 = """
<b><u>CC:</b></u>
CC ile ilgili komutlar:
 /gen ➠ Komuttan sonra BIN girerek geçerli CC oluşturur.
 /genbin ➠ BIN oluşturur.
 /bin ➠ Komuttan sonra BIN girerek BIN'in durumunu kontrol eder.
 /fake ➠ Komuttan sonra herhangi bir rastgele ülke adını girerek sahte bilgi oluşturur.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_26 = """
<b><u>METİN DÜZENLEME:</b></u>
Metin düzenleme veya tasarım komutları:
 /font veya /fonts ➠ Komuttan sonra metin girerek font efektleri oluşturur.
 /figlet ➠ Komuttan sonra metin girerek figlet oluşturur.
 /hastag ➠ Komuttan sonra metin girerek o metnin hashtagini oluşturur.
 /code ➠ Komuttan sonra metin girerek o metni kodlar.
 /genpw ➠ Güçlü bir şifre oluşturur.
 /write ➠ Komuttan sonra metin girerek not defterine yazar.
 /qr ➠ Komuttan sonra metin girerek o metnin QR kodunu oluşturur.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_27 = """
<b><u>MASTI♡︎:</b></u>
Eğlen veya hiç...
 /couples ➠ Grubunuzda çiftler oluşturur.
 /love ➠ İki kişinin adını girerek aşk istatistiklerini kontrol eder {ilk} {ikinci} [eğlence amaçlı alın 😁].
 /day ➠ {yıl/ay/gün} formatında tarihi girerek o günün hangi güne denk geldiğini öğrenmek için kullanılır.
 /cute ➠ Sevimlilik oranınızı kontrol eder 🥰.
 /hjoke ➠ Rastgele komik şakalar alır 😁.
 /kiss ➠ Birine öpmek için kullanılır.
 /hug ➠ Birine sarılmak için kullanılır.
 /slap ➠ Birine tokat atmak için kullanılır.
 /sleep ➠ Uyku komutu 🫠.
 /run ➠ Koşma komutu 😅.
 /wish ➠ Komuttan sonra dileğinizi girerek kullanılır.
 /bored ➠ Sadece eğlence için 😁.
 /gay ➠ Eşcinsel yüzdesini kontrol eder, şaka amaçlı 😅.
 /hot ➠ Sıcaklık seviyenizi kontrol eder.
 /sexy ➠ Seksi seviyenizi kontrol eder 🤣.
 /lesbian ➠ Lezbiyen yüzdesini kontrol eder.
 /cutie ➠ Sevimlilik seviyenizi kontrol eder.
 /cock ➠ Penis boyutunuzu kontrol eder.
 /horny ➠ Ne kadar azgın olduğunuzu kontrol eder.
 /boob ➠ Meme boyutunuzu kontrol eder 😝.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_28 = """
<b><u>REPO İLGİLİ:</b></u>
Repo ile ilgili mevcut komutlar:
 /allrepo ➠ Komuttan sonra GitHub kullanıcı adını girerek o hesabın tüm repolarını alır.
 /pypi ➠ Komuttan sonra proje adını girerek o projenin istatistiklerini alır [Proje = GitHub Reposu].
 /downloadrepo ➠ Komuttan sonra repo bağlantısını girerek o repoyu indirir.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_29 = """
<b><u>NOTLAR:</b></u>
Notlarla ilgili:
 /save ➠ Komuttan sonra not adını girerek notu kaydeder.
 /get ➠ Komuttan sonra almak istediğiniz not adını girin.
 /privatenotes ➠ Özel notlar 😁😁.
 /clear ➠ Notları temizlemek için kullanılır.
 /clearall ➠ Tüm notları temizlemek için kullanılır.

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""

HELP_30 = """
<b><u>OYUNLAR:</b></u>
Emojilerle Oyun Oynayın:
/dice - Zar 🎲
/dart - Dart 🎯
/basket - Basketbol 🏀
/ball - Bowling Topu 🎳
/football - Futbol ⚽
/jackpot - Slot Makinesi 🎰

✧Bu modüller ➪ [Esila🦋](https://t.me/EsilaChatBot) tarafından sağlanmaktadır."""
