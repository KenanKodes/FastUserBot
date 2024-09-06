from random import choice
from userbot.cmdhelp import CmdHelp
from userbot.events import register


DC_STRINGS = [
    "**⚡Ən böyük peşmançılıq çəkdiyin pislik nə olub?**\n\n**Doğruluq** ✅ | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Başıva un tök selfi elə şəklini hansısa qrupda paylaş**\n\n**Cəsarət** 📛 | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡'Yox' demək istədiyiniz halda tez-tezmi 'hə' deyirsiniz? Bunun səbəbi nədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡İnstagram story-nə indiki oyunçulardan kiminsə şəklini qoy**\n\n**Cəsarət** 📛 | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Həyatınızda sizi həyəcanlandıran şey nədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡30 saniyə qurbağa təqlid səsini atın.**\n\n**Cəsarət** 📛 | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Səhra adasına düşsəniz hansı 3 şeyi nə götürəsiz?**\n\n**Doğruluq** ✅ | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡5 dəqiqədə Adınızı 'Mən bir eşşəyəm' edin**\n\n**Cəsarət** 📛 | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Səncə insan üçün ailəsindən sonra dini önəmli olmalıdı yoxsa milli kimliyi?**\n\n**Doğruluq** ✅ | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Son danışdığın insana 'Şəkil at' yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Etdiyiniz hansı səhvi daha təkrar etmirsiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Küçəyə çıx və qarşına çıxan ilk insandan pul istə.😂💸**\n\n**Cəsarət** 📛 | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",    
    "**⚡Bütün dünya əhalisinə 30 saniyəlik müraciət etmək imkanınız olsaydı, həmin yarım dəqiqə ərzində nələr deyərdiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Ən utandığın şəklini qrupa göndər!**\n\n**Cəsarət** 📛 | [⚝ 𝑭𝑨𝑺𝑻 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@TheFastSupp)",
    "**⚡Həyatınızdakı ən gözəl gün necə olub? Və niyə belə düşünürsünüz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Gözünü bağla və 'elektrikləşdirilmişlərdənsinizmi' yaz.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hesablayın, gündə neçə saat sosial şəbəkələrdə vaxt keçirirsiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Yeri öp və bunu videoya çək göndər**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sonuncu dəfə nə vaxt və nəyə gözünüz yaşarana kimi gülmüsünüz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Başına qazan qoy və şəklini çək göndər.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hansı xoşagəlməz xüsusiyyətlərinizdən xilas olmaq istərdiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Teleqramda bir qrupa link at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Acı təcrübələriniz sizə nələri öyrədib?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Birinin şəklini Profil Şəkilinə 10 dəqiqə qoyun**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Elə şeylər varmı ki, hansı ki, düşünürsünüz ki, onları etməyə başlamaq üçün artıq gecikmisiniz? Nə üçün bu fikirdəsiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Çiy yumurta iç və bunu videoya çək at.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡10 il əvvələ qayıtsaydınız, hansı həyati dərsləri öyrənmək istərdiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Google tarixçəsini screenshot elə at.**\n\n**Cəsarət** 📛 | @DTOUserBot", 
    "**⚡Nə vaxtsa kinoya baxanda və ya kitab oxuyanda gözlərindən yaş axıb?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bir uşaq mahnısı oxuyaraq bir səs at.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ən sevdiyin müğənni/qrup?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qonşunun evinə get və çörək istə.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bu qrupda səmimi olduğun ama sevmədiyin biri var?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ümumi olaraq insanlarla münasibət və əlaqələriniz sizi qane edir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Heç bitiniz olubmu?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dostunla , Sevgilin ölüm ayağında olsa ilk kimi xilas edərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ən çox kiminlə fikirlərin ayrılır amma yenə də danışmağa davam edirsiz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Xəyalındakı qız/oğlan necə biri ?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Heç vaxt etmərəm deyib etdiyiniz şey olub?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qrupda düşüncə olaraq, özünə ən yaxın kimi görürsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Gələcəkdə hansı işlə məşğul olmaq istəyərsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ailəndə səninlə bağlı elə hadisə olubmu ki, onu eşitməkdən bezmisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İçkilib olub düşdüyün ən troll, gülünc vəziyyət?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bu qrupda ən çox kimə dəyər verirsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bu gecə öləcəyini bilsən, kimə və hansı vacib məsələ haqqında danışmaq istərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qarşı cinsə göndərdiyin ən son mesaj nə idi?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Elə şeylər varmı ki, hansı ki düşünürsünüz ki, onları etməyə başlamaq üçün artıq gecikmisiniz? Nə üçün bu fikirdəsiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Utanarkən üzü qızarmayanlardansınızmı?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Zamanı daha sürətli və ya daha yavaş hala gətirə bilən gücün olsa, nə edərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sənə ən çox təsir edən qorxu filmi hansıdır? Səbəb?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dünyadakı bütün televiziya və radio kanallarına eyni anda bir cümlə göndərə bilmə şansın olsa, bu, hansı cümlə olardı?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qarşındakı insanın düzgün olmasını nədən seçirsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qrupda ən çox dəyər verdiyin, bəyəndiyin, çox istədiyin insan kimdir? (Sıra ilə 3 nəfər)**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Birindən onu sevdiyini gizlətmisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sizcə, bir insanı güvənsiz edən şeylər nədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Google da axtardığınız ən qəribə şey nədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bir oturuma ən çox yediyin yemək hansı olub? Ətrafdan hansı reaksiyalar gəlib?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Fərz et ki, həyatının qalan hissəsində internetdə sadəcə bir (!) insanla mesajlaşa bilərsən. Bu kim olardı?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Məhşur biri ilə daha yaxın ola bilsəydin, kimi seçərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sizə yalan deyildiyində doğrusunu bilib, amma özünüzü inanırmış kimi  aparmısınız ?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sənin ən sevdiyin yemək hansıdır?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Əsla bağlanmaram deyibdə bağlandığın biri olub?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Səni atıblar?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Biri ilə görüşməkdən qaçmaq üçün özünü xəstəliyə vurmusan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İnsanlara sevgi hissi verilməsəydi... Səncə dünyamız necə olardı?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qrupda ən az kimi sevirsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Gələcəkdə evlənəcəyin insan nə desə fikrindən daşınarsan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Cəhənnəmdə yanacağını bilsəydin səncə bu hansı günahına görə olardı?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Səncə Aldatmağ yoxsa Aldadılmağ daha rahatdır?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Səncə bu qrupdakı ən pis insan kim oLabiLər?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Gələcəyi görə bilmə bacarığın olsa,ən çox nəyi görmək istəyərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sizcə virtualda dostluq var?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Mahnıya ən çox nə zaman ehtiyac duyursan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Həyatınıza alıbda peşman olduğunuz şəxs varmı?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Birisi sənə dünyanın ən varlı insanı olmağı təklif etsə əsla etmərəm dediyin şey nə olar?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dostunuzu satmısınız?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Online dərsdə görüntünü bağlayıb yemək yediyiniz olub?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Öz-özünüzə danışırsınız? Ən çox nə haqqında?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Yadplanetlilərə inanırsan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Heç dostunuzun sirrini başqası ilə bölüşmüsünüzmü?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sizcə bir daha mahnıya qulaq asa bilməmək yoxsa bir daha şəkil çəkdirməmək?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Başqalarının məsləhətlərini dinləyirsiz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hər hansı bir heyvan ola bilsəydin, nə edərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Heç gülünc vəziyyətə düşmüsünüz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Əks cins kimi yuxudan ayılsan ilk nə edərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Evlilik üçün ideal yaş?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sizdən boyca balaca biri ilə sevgili olardız?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dünyanın sonu belə gəlsə,heç vaxt etməyəcəyiniz şey nədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İlan və ya qurbağa kimi şeylər yemisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Neçə uşaq sahibi olmaq istərdiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ən sevdiyin serial?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hazırda kiminlə sevgilisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Heç ilk görüşdə aşiq oldunmu?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hazırda kiminlə sevgilisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bu qrupda səmimi olduğun ama sevmədiyin biri var?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Yaxın dostluq münasibəti qurmaq istədiyin bir kəs sənin haqqında nəyi bilməlidir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Gizli sevgilin kimdir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Anlaşılmayacağı dəqiq olsa,aldadardınız?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ailəndə səninlə bağlı elə hadisə olubmu ki, onu eşitməkdən bezmisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Həyatda nə olmasa darıxdırıcı olar?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Gələcəkdə hansı işlə məşğul olmaq istəyərsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ölüm sizcə nəyi ifadə edir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡“Yox” demək istədiyiniz halda tez-tezmi “hə” deyirsiniz? Bunun səbəbi nədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qrupdakı hər bir şəxs haqqında bir müsbət və bir mənfi şey söyləyin.**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Cəmiyyətdəki ən biabırçı anınız nə olub?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Valideynlərinin yanında səhvən söyüş söymüsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dostunuzun və ya yaxınınızın etdiyi hər hansı bir səhvi üstünüzə götürmüsünüz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Səs tonunu dəyişərək mahnı oxu at**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Xəstəxanadasan və təcili birinə böyrək lazımdı.Böyrəyini verərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Əvvəldən səndən xoşu gələn birinin indi başqasınnan xoşu gəlsə qısqanarsan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Heç kimin tapa bilməyəcəyi pis bir şey etdiniz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qrupda düşüncə olaraq, özünə ən yaxın kimi görürsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Səncə insanlara 2 ci şans vermək olar?(Niyə?)**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Başqaları sənlə danışanda, doğurdan da onları dinləyirsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Səncə insanlara 2 ci şans vermək olar?(Niyə?)**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ən xoşladığınız aksesuar?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qrupda xətri əziz olan 1 qız 1 oğlan adı de**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Heç vaxt etmərəm deyib etdiyiniz şey olub?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Xəyalındakı qız/oğlan necə biri ?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qarşındakının yalan danışdığını bilsəydin nə edərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Tərgidə bilmədiyin vərdiş?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Həyatındakı ən gözəl gün necə olub?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ən çox kiminlə fikirlərin ayrılır amma yenə də danışmağa davam edirsiz?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Digər insanlardan fərqli olaraq nələr edirsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İçində öldüyün tarixin yazılı olduğu bir zərf alsaydın,açıb baxardınmı?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Əgər görünməz olsaydın,bu oyundakılardan kimi izləmək istəyərdin?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Eyni sənə oxşayan adamla tanış olmaz istəyərsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ən dəyərli xatirən hansıdır?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Yuxunda danışırsan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Kiminsə həyatına burnuvu soxmağı xoşlayırsan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sevgi üçün hərşeyi edərəm ama “bunu” eləmərəm dediyin şey nədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ümumi olaraq insanlarla münasibət və əlaqələriniz sizi qane edir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Şəxsi inkişafınızda sizə daha çox nə kömək edir – özünüzə etdiyiniz çağırışlar, çətin sınaqlar, yoxsa həyatın xoş və rahat tərəfləri?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Whatsappda yaxın bir dostuna orqan mafiyası məni təhdid edir mənə borc 10 min manat lazımdır de**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hekayənə oğlansansa “Təbrik edin baba oluram” , qızsansa “Təbrik edin nənə oluram.” yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İki dənə bir-biri ilə əlaqəsiz olan sok adları de və onları qarışdırıb iç.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Just now şəkil at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Təkcə burnuvun şəklini çək at.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ən xoşladığın mahnının nəqarətini oxu,səsini göndər**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Zibil vedrəsinnən bir şey götür və onunla şəkil çəkdirib at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡1 dilim çiy kartof ye**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ayaqyolunda su içirmiş kimi şəkil cək və instada post olaraq paylaş ss mütləq**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Başıvı qaldır ilk gördüyün yerin şəklini çək at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Telegramda da istədiyin birinə nömrənin son iki rəqəmini yaz əvvəlini tapsan sənən sevgili olacam de**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Telegramdakı kantaktinda 3cü adama səndən zəhləm gedir axmaq yaz+ss şərtilə**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dilivi dişlə və Mən nə qələt etdim cəsarət seçdim de.Səsli**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Getdim, gördüm bir dərədə iki kar, kor, kürkü yırtıq kirpi var. Dişi kar, kor kürkü yırtıq kirpi erkək kar, kor, kürkü yırtıq kirpinin kürkünü yamamaqdansa, erkək kar, kor kürkü yırtıq kirpi dişi kar, kor kürküyırtıq kirpinin kürkünü yamayır. (səsli danış)**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dostuna “Mafia oynundakı məşuqə rolu kimisən lazımlısan amma heç kimə arzu eləmirəm səni” de**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qız və ya Oğlan seç zəng edib: “Kız soğan soy!Gerizekallıı” de**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Müəllimlərindən birinə günüvün necə keçtiyi barəsində yaz.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Birinzə zəng et və Qaradəniz şivəsi ilə danış.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ovucuna istiot tök(şəkil)+iylə (səs at)**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ən xoşladığın mahnının nəqarətini oxu,səsini göndər**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dəftərə öz şəkilini çək və göndər**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bir ədəd çiy yumurta iç vidiosunu qrupa at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bir parça çiy ət ye**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Whatsappda müəlliminə  “yaxşı dərs keçə bilmirsiz çox heyif” yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Oğlansansa qız,qızsansa oğlan birinin şəxsisinə yazıb,özünü təriflə**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qrupda kiməsə şeir yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İnstagramda ilk qarşına çıxan profilə sevgilini sevirəm yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡1-dən 100 ə kimi say səs at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Telefonunun ekranını ss elə at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hər hansı kitabda 13 cü səhfəni aç 2 ci sətir 3 cü sözü kontaktındakı birinə göndər**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Lətifə danış(ses at)**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sondan əvvələ əlifbanı səsli oxu**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hansısa qrupa girib,“çəkilin kənara mən həkiməm” yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Evdəki ən acı şeydən ye ( bibər ,istiot və.s)**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Tanımadığın birinə “Siqaret çəkmək sizin sağlamlığınıza ziyan vurur” yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Xəkandazla selfie çək qrupa at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Tanımadığın birinə “ehh,bizim vaxtlarımız 2-ci Qarabağ müharibəsi,Corona vaxtları idi.Siz hardan biləsiz” yaz.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İnstagram DM ss elə at.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Telegram Mesajlar (PM) - Bölməsini ss elə at.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Vhatsapp Mesajlar Bölməsini ss elə at.**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Evdəki telefonlarda saatları bir saat geri çək və heç nə demə heçkimə**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Statusa imkanlı qohumlarımdan xaiş edirəm mənə pul verin yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Soyuducunu aç ,qarşina çıxan ilk şeyi ye (yada) iç**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qruplardan birinə “daha dözə bilmirəm” yaz və qrupdan çıx**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Tanımadığın birinə “Bu gün sizin həyatınızı qurtardım,mənə bir can borcunuz var” yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Çölə çıxıb qışqıraraq “Qarabağ Azərbaycandır” de**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İndi bir şəkil çək at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hər hansısa bir qrupun admininə məndə admin olmaq istəyirəm bunun üçün hansı sənədlər lazımdır yaz**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
]

@register(outgoing=True, pattern="^.dc$")
async def dsor(e):
    await e.edit(choice(DC_STRINGS))

DC18_STRINGS = [
    "**⚡Heç dil vurmusan/Çalmısan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Çılpaq şəklini at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Bakirəsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Ah-uh səsləri çıxardıb və bunu səsə qeyd elə at**\n\n**Cəsarət** 📛 | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sənin erogen bölgən hansıdır?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sevgilinlə porno çəkərdinmi?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dostunun lüt şəklini çəkmisən mi?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Dostunla cinsi əlaqəyə girərdin mi?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sevgilin 69 pozası təklif etsəydi, onunla əlaqəyə girərdin mi?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Yoldaşını dostun ilə əlaqəyə girməsi üçün şərait yaradardın mı?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Cinsi əlaqədə olan zaman, metobalizm problemi yaşamısan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Oğlan dostun ilə cinsi əlaqəyə girərsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Lezbiyanların cinsi əlaqəsinə münasibətin necədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Geylərin cinsi əlaqəsinə münasibətin necədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hansısa dostun üçün cinsi əlaqə üçün ev tutmusan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Kuni-yə münasibətin necədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Qarşı cins minet eləsə, təşəkkür mənasında kuni edərsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hamamda özünü lüt çəkib sonra ona baxıb masturbasiya etmisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Nude çəkib oğlan dostuna atmısan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Nude çəkib rəfiqənə atmısan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡İnstagram storyndə kiməsə görə nude paylaşıb digər followerləri gizlətmisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hansısa qız dostunun telefonunda onun nudelarını oğurlayıb özünə atmısan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sabun ilə masturbasiya etmisən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Neçə müddətdən bir masturbasiya edirsən?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Masturbasiyaya münasibətin necədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Cinsi əlaqədən sonra, qız ilə görüşməkdən utanmısan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Sizcə, bir insanı güvənsiz edən şeylər nədir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hansı porno aktrisası xoşuna gəlir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hansı porno aktyor xoşuna gəlir?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
    "**⚡Hansı porno saytdan videolara baxırsan?**\n\n**Doğruluq** ✅ | [⚝ 𝑺𝑰𝑳𝑮𝑰 𝑼𝑺𝑬𝑹𝑩𝑶𝑻 ⚝](@silgiuserbot)",
]

@register(outgoing=True, pattern="^.dc18$")
async def dsor(e):
    await e.edit(choice(DC18_STRINGS))

CmdHelp('dc').add_command(
    'dc', None, 'Doğruluq/Cəsarət suallarını,əmrlərini verər.'
).add_command(
    'dc18', None, 'Doğruluq/Cəsarət ama 18+'
).add()
