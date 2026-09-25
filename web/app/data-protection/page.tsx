import type { Metadata } from "next";

export const metadata: Metadata = { title: "Andmekaitse" };

export default function DataProtectionPage() {
  return (
    <article className="privacy-content">
      <header className="page-intro">
        <h1>Andmekaitsetingimused</h1>
        <p>Siin selgitame, kuidas Eesti Olümpiaadide Andmebaas (EOA) töötleb olümpiaaditulemuste ja veebilehe kasutamisega seotud isikuandmeid.</p>
        <p>Kui oled õpilane: EOA võib näidata sinu nime ja olümpiaaditulemust. Kui tulemus on vale või sa ei soovi oma nime siin näha, kirjuta meile aadressil <a href="mailto:eoakontakt@gmail.com">eoakontakt@gmail.com</a>. Vaatame sinu soovi läbi ja vastame sulle.</p>
        <p><strong>Dokumendi kavand:</strong> tulemuste avaldamise õigustatud huvi hinnang on lõpetamata. Vastutava töötleja andmed tuleb lisada enne teate lõplikku kasutamist.</p>
      </header>

      <section aria-labelledby="data">
        <h2 id="data">Andmed ja nende päritolu</h2>
        <p>Töötleme õpilase ning õpetaja või juhendaja nime, kooli, klassi või vanuserühma, võistluse ja õppeaasta andmeid ning tulemust. Mõne võistluse puhul sisaldab tulemus punkte ja muid tulemuse osi. Kõik seni kogutud tulemused pärinevad korraldajate avalikult kättesaadavatelt lehtedelt. Konkreetse kirje teadaoleva algallika saab meilt küsida.</p>
        <p>Kui kirjutate meile, töötleme teie kirjas sisalduvaid andmeid ja vastamiseks vajalikku suhtlust. Kirjutamine on vabatahtlik, kuid ilma kontaktandmeteta ei pruugi me saada vastata. Veebilehe kasutamisel töötleb server päringu teenindamiseks tehnilisi andmeid, sealhulgas IP-aadressi ja päringu aega. EOA ei salvesta eraldi külastusloge.</p>
      </section>

      <section aria-labelledby="purpose">
        <h2 id="purpose">Eesmärgid ja õiguslik alus</h2>
        <p>Koondame, kontrollime ja säilitame tulemusi Eesti olümpiaadide ajaloo talletamiseks, varasemate saavutuste tõendamiseks ning õpilaste ja juhendajate panuse nähtavaks tegemiseks. Tulemusi saab veebis sirvida, otsida ja alla laadida.</p>
        <p><strong>Kavandatav alus:</strong> isikuandmete kaitse üldmääruse artikli 6 lõike 1 punkt f — vastutava töötleja ja avalikkuse õigustatud huvi säilitada ning leida olümpiaaditulemusi. See alus kehtib ainult siis, kui iga töötlemisviisi vajalikkus ja huvide tasakaal, eriti laste puhul, on dokumenteeritud ning andmesubjektide õigused ei kaalu huvi üles. Nimeotsingu, isikuprofiilide, edetabelite ning API ja CSV kaudu avaldamise hindamine on veel lõpetamata.</p>
        <p>Andmekaitseõigustega seotud pöördumistele vastamiseks töötleme kirjavahetust üldmääruse artikli 6 lõike 1 punkti c alusel osas, milles see on vajalik õigusliku kohustuse täitmiseks. Muude päringute ja veebilehe tehnilise toimimise kavandatav alus on punkt f.</p>
        <p>See, et tulemus oli juba avalik, ei anna iseenesest EOA-le õiguslikku alust. Praegu ei tugine EOA tulemuste töötlemisel osalejate nõusolekule.</p>
      </section>

      <section aria-labelledby="publication">
        <h2 id="publication">Avaldamine ja vastuvõtjad</h2>
        <p>Võistluse tulemustabelis võivad olla nähtavad nimed ja tulemused. Avatud võistlustel ei avalda korraldaja tavaliselt kõige madalamaid punkte; kutsetega võistlustel võivad avalikud olla kõik tulemused. Nimepõhises õpilase otsingus, kooli õpilaste nimekirjas ja koondtabelis kuvatakse õpilast siis, kui tal on vähemalt kümme osalemist või vähemalt üks koht esikolmikus. Juhendajate nimepõhisele otsingule seda piiri ei kohaldata. Piir ei peida õpilase nime võistluse tulemustabelist ega välista kirje leidmist muul viisil. Kui nime avalik kuvamine on peatatud, jääb tulemus võistluse tabelisse nimeta; selle juures ei näita EOA ka inimese profiililinki, kooli, klassi ega juhendajat.</p>
        <p>Avaldatud tulemused on nähtavad veebikülastajatele ning kättesaadavad ka avaliku API ja CSV allalaadimise kaudu. Külastajad saavad avaldatust koopia teha; nende edasine iseseisev kasutus ei ole EOA kontrolli all. Veebileht ja andmebaas asuvad Hetzneri Soome serveris; varukoopiad asuvad Hetzneri Saksamaa ja Scaleway Prantsusmaa serverites. Kirjavahetuseks kasutame Google Gmaili. Google võib töödelda kirjavahetuse andmeid ka väljaspool Euroopa Majanduspiirkonda ning kirjeldab oma <a href="https://policies.google.com/privacy/frameworks?hl=et">andmeedastuse kaitsemeetmeid</a>. EOA ei kasuta teisi teenuseosutajaid.</p>
      </section>

      <section aria-labelledby="retention">
        <h2 id="retention">Säilitamine</h2>
        <p>Tulemusi säilitame tuvastataval kujul seni, kuni see on ajaloolise arhiivi eesmärgiks vajalik ja töötlemisel on õiguslik alus. Vaatame vähemalt kord aastas üle andmeliikide ja avaldamisviiside vajalikkuse ning osa algallikaid; vaidlustatud või parandatud kirje vaatame üle viivitamata. Kui eesmärk või alus kaob, kustutame või anonüümime asjaomased andmed EOA kontrollitavates väljundites.</p>
        <p>Tavalise kirjavahetuse kustutame 12 kuud pärast viimast sisulist vastust või juhtumi sulgemist. Andmekaitseõiguste taotluse kohta säilitame minimaalset menetlusjälge kolm aastat pärast juhtumi sulgemist. Isikusamasuse kontrolliks küsitud eraldi tõendi kustutame pärast kontrolli, hiljemalt 30 päeva jooksul, välja arvatud juhul, kui konkreetne vaidlus nõuab pikemat säilitamist. Varukoopiaid hoiame kuni 90 päeva; taastamisel rakendame enne taasavalikustamist vahepealsed parandused ja varjamised.</p>
      </section>

      <section aria-labelledby="rights">
        <h2 id="rights">Teie õigused</h2>
        <p>Võite küsida kinnitust andmete töötlemise kohta, tutvuda oma andmetega ning paluda ebaõigeid andmeid parandada. Olenevalt asjaoludest võite taotleda kustutamist või töötlemise piiramist. Kui töötlemine põhineb õigustatud huvil, võite oma konkreetsest olukorrast lähtudes esitada vastuväite; seejärel lõpetame asjaomase töötlemise, kui me ei tõenda ülekaalukat mõjuvat õiguspärast põhjust või õigusnõude vajadust.</p>
        <p>Avalikes huvides arhiveerimise korral võib seadus lubada mõnd õigust piirata ainult siis, kui selle kasutamine tõenäoliselt muudaks arhiveerimise võimatuks või takistaks seda oluliselt ning piirang on vajalik. Hindame iga taotlust eraldi; arhiveerimise eesmärk ei anna üldist õigust taotlusi tagasi lükata.</p>
        <p>Kirjutage <a href="mailto:eoakontakt@gmail.com">eoakontakt@gmail.com</a> ja märkige võimaluse korral asjaomane kirje. Kui meil on põhjendatud kahtlus taotleja isikusamasuses, võime küsida kontrollimiseks vajalikku lisateavet. Vastame üldjuhul ühe kuu jooksul. Keeruka või arvuka taotluse puhul võime tähtaega pikendada kuni kahe kuu võrra, teatades sellest esimese kuu jooksul. Taotluse lahendamine on üldjuhul tasuta.</p>
      </section>

      <section aria-labelledby="site-storage">
        <h2 id="site-storage">Veebilehe kohalik salvestus</h2>
        <p>Värviteema valimisel salvestab teie brauser seadmesse võtme <code>eoa-theme</code>, et valik järgmisel külastusel taastada. Valik „Süsteemi järgi” eemaldab selle võtme. EOA ei kasuta veebilehel analüütika- ega reklaamiküpsiseid.</p>
      </section>

      <section aria-labelledby="automated-decisions">
        <h2 id="automated-decisions">Automaatotsused</h2>
        <p>Veebileht arvutab tulemuste põhjal otsingu- ja edetabelivaateid. EOA ei tee nende andmete põhjal üksnes automatiseeritud otsuseid, millel on inimesele õiguslik või samaväärselt märkimisväärne mõju.</p>
      </section>

      <section aria-labelledby="complaint">
        <h2 id="complaint">Kaebus ja õigusaktid</h2>
        <p>Võite pöörduda <a href="https://www.aki.ee/meist/vota-uhendust/kaebus-isikuandmete-kaitse-asjas">Andmekaitse Inspektsiooni</a> poole. Andmekaitse põhireeglid tulenevad <a href="https://eur-lex.europa.eu/legal-content/ET/TXT/?uri=CELEX%3A32016R0679">isikuandmete kaitse üldmäärusest</a>; Eesti <a href="https://www.riigiteataja.ee/akt/106032026010">isikuandmete kaitse seadus</a> sisaldab muu hulgas avalikes huvides arhiveerimise erisusi.</p>
      </section>
    </article>
  );
}
