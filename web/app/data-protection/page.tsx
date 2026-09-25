import type { Metadata } from "next";

export const metadata: Metadata = { title: "Andmekaitse" };

export default function DataProtectionPage() {
  return (
    <article className="privacy-content">
      <header className="page-intro">
        <h1>Andmekaitsetingimused</h1>
        <p>Siin selgitame, kuidas Eesti Olümpiaadide Andmebaas (EOA) töötleb olümpiaaditulemuste ja veebilehe kasutamisega seotud isikuandmeid.</p>
        <p><strong>Dokumendi kavand: enne avaldamist tuleb täita nurksulgudes väljad ning kinnitada õiguslik alus ja avaldamisviisid.</strong></p>
      </header>

      <section aria-labelledby="controller">
        <h2 id="controller">Vastutav töötleja</h2>
        <p>Vastutav töötleja: <strong>[füüsilise isiku täisnimi / mittetulundusühingu registrijärgne nimi ja registrikood]</strong>. Aadress: <strong>[postiaadress]</strong>. Andmekaitseküsimused ja taotlused: <a href="mailto:eoakontakt@gmail.com">eoakontakt@gmail.com</a>.</p>
        <p>Kui eesmärgid ja põhilised töötlemisviisid määravad koos mitu isikut, lisame siia kõigi kaasvastutavate töötlejate nimed, kontaktid ning vastutusjaotuse põhisisu.</p>
      </section>

      <section aria-labelledby="data">
        <h2 id="data">Andmed ja nende päritolu</h2>
        <p>Töötleme õpilase ning õpetaja või juhendaja nime, kooli, klassi või vanuserühma, võistluse ja õppeaasta andmeid ning tulemust. Mõne võistluse puhul sisaldab tulemus punkte ja muid tulemuse osi. Andmed pärinevad korraldajate avaldatud tulemustest või EOA-le edastatud materjalidest. Vanemate kirjete täpne algallikas ei pruugi olla säilinud; konkreetse kirje teadaoleva allika saab meilt küsida.</p>
        <p>Kui kirjutate meile, töötleme teie kirjas sisalduvaid andmeid ja vastamiseks vajalikku suhtlust. Kirjutamine on vabatahtlik, kuid ilma kontaktandmeteta ei pruugi me saada vastata. Veebilehe kasutamisel võib server töödelda päringu tehnilisi andmeid, sealhulgas IP-aadressi, päringu aega ja brauseri teavet. <strong>[Kinnitada logimise tegelik ulatus.]</strong></p>
      </section>

      <section aria-labelledby="purpose">
        <h2 id="purpose">Eesmärgid ja õiguslik alus</h2>
        <p>Koondame, kontrollime ja säilitame tulemusi Eesti olümpiaadide ajaloo talletamiseks, varasemate saavutuste tõendamiseks ning õpilaste ja juhendajate panuse nähtavaks tegemiseks. Avaldame tulemusi veebis ainult ulatuses, mille vajalikkust ja mõju oleme hinnanud.</p>
        <p><strong>Kavandatav alus:</strong> isikuandmete kaitse üldmääruse artikli 6 lõike 1 punkt f — vastutava töötleja ja avalikkuse õigustatud huvi säilitada ning leida olümpiaaditulemusi. See alus kehtib ainult siis, kui iga töötlemisviisi vajalikkus ja huvide tasakaal, eriti laste puhul, on dokumenteeritud ning andmesubjektide õigused ei kaalu huvi üles. <strong>[Kinnitada hinnangu tulemus ja vajaduse korral eristada alused töötlemisviiside kaupa.]</strong></p>
        <p>Andmekaitseõigustega seotud pöördumistele vastamiseks töötleme kirjavahetust üldmääruse artikli 6 lõike 1 punkti c alusel osas, milles see on vajalik õigusliku kohustuse täitmiseks. Muude päringute ja veebilehe tehnilise toimimise kavandatav alus on punkt f. <strong>[Kinnitada tegelikud eesmärgid, logid ja teenuseosutajad.]</strong></p>
        <p>See, et tulemus oli juba avalik või et korraldaja saatis selle EOA-le, ei anna iseenesest EOA-le õiguslikku alust. Kui kasutame mõne kirje jaoks nõusolekut, teavitame sellest eraldi ning nõusoleku saab tagasi võtta.</p>
      </section>

      <section aria-labelledby="publication">
        <h2 id="publication">Avaldamine ja vastuvõtjad</h2>
        <p>Võistluse tulemustabelis võivad olla nähtavad avaldamiseks sobivaks hinnatud nimed ja tulemused. Nimepõhises õpilase otsingus, kooli õpilaste nimekirjas ja koondtabelis kuvatakse õpilast siis, kui tal on vähemalt kümme osalemist või vähemalt üks koht esikolmikus. Juhendajate nimepõhisele otsingule seda piiri ei kohaldata. Piir ei peida õpilase nime võistluse tulemustabelist ega välista kirje leidmist muul viisil. Kui nimi ei ole avaldamiseks lubatud, seda nimena ei kuvata.</p>
        <p>Avaldatud tulemused on nähtavad veebikülastajatele ning kättesaadavad ka avaliku API ja CSV allalaadimise kaudu. Külastajad saavad avaldatust koopia teha; nende edasine iseseisev kasutus ei ole EOA kontrolli all. Majutus- ja tehnilised teenuseosutajad võivad andmeid töödelda EOA nimel: <strong>[teenuseosutajad või kategooriad ja asukohariigid]</strong>. Väljapoole Euroopa Majanduspiirkonda edastamise olemasolu ja kaitsemeetmed: <strong>[täpsustada; kui ei toimu, märkida seda]</strong>.</p>
      </section>

      <section aria-labelledby="retention">
        <h2 id="retention">Säilitamine</h2>
        <p>Tulemusi säilitame ajaloolise arhiivi eesmärgil seni, kuni andmete tuvastataval kujul säilitamine on selle eesmärgi jaoks vajalik. <strong>[Kinnitada läbivaatamise sagedus ja kustutamise või anonüümimise kriteeriumid.]</strong> Kui eesmärk kaob ja muud alust ei ole, kustutame või anonüümime andmed. Õiguste taotluste kirjavahetuse ja tehniliste logide säilitustähtajad: <strong>[täpsustada eri andmeliikide kaupa]</strong>.</p>
      </section>

      <section aria-labelledby="rights">
        <h2 id="rights">Teie õigused</h2>
        <p>Võite küsida kinnitust andmete töötlemise kohta, tutvuda oma andmetega ning paluda ebaõigeid andmeid parandada. Olenevalt asjaoludest võite taotleda kustutamist või töötlemise piiramist. Kui töötlemine põhineb õigustatud huvil, võite oma konkreetsest olukorrast lähtudes esitada vastuväite; seejärel lõpetame asjaomase töötlemise, kui me ei tõenda ülekaalukat mõjuvat õiguspärast põhjust või õigusnõude vajadust.</p>
        <p>Avalikes huvides arhiveerimise korral võib seadus lubada mõnd õigust piirata ainult siis, kui selle kasutamine tõenäoliselt muudaks arhiveerimise võimatuks või takistaks seda oluliselt ning piirang on vajalik. Hindame iga taotlust eraldi; arhiveerimise eesmärk ei anna üldist õigust taotlusi tagasi lükata.</p>
        <p>Kirjutage <a href="mailto:eoakontakt@gmail.com">eoakontakt@gmail.com</a> ja märkige võimaluse korral asjaomane kirje. Kui meil on põhjendatud kahtlus taotleja isikusamasuses, võime küsida kontrollimiseks vajalikku lisateavet. Vastame üldjuhul ühe kuu jooksul. Keeruka või arvuka taotluse puhul võime tähtaega pikendada kuni kahe kuu võrra, teatades sellest esimese kuu jooksul. Taotluse lahendamine on üldjuhul tasuta.</p>
      </section>

      <section aria-labelledby="site-storage">
        <h2 id="site-storage">Veebilehe kohalik salvestus</h2>
        <p>Värviteema valimisel salvestab teie brauser seadmesse võtme <code>eoa-theme</code>, et valik järgmisel külastusel taastada. Valik „Süsteemi järgi” eemaldab selle võtme. <strong>[Kinnitada, kas majutus või lisateenused kasutavad küpsiseid või muud seadmesalvestust; vajaduse korral täiendada teavet ja nõusoleku lahendust.]</strong></p>
      </section>

      <section aria-labelledby="automated-decisions">
        <h2 id="automated-decisions">Automaatotsused</h2>
        <p>Veebileht arvutab tulemuste põhjal otsingu- ja edetabelivaateid. <strong>[Kinnitada, et EOA ei tee üksnes automatiseeritud töötlusel põhinevaid otsuseid, millel on isikule õiguslik või samaväärselt märkimisväärne mõju; vastasel juhul lisada nõutav selgitus.]</strong></p>
      </section>

      <section aria-labelledby="complaint">
        <h2 id="complaint">Kaebus ja õigusaktid</h2>
        <p>Võite pöörduda <a href="https://www.aki.ee/meist/vota-uhendust/kaebus-isikuandmete-kaitse-asjas">Andmekaitse Inspektsiooni</a> poole. Andmekaitse põhireeglid tulenevad <a href="https://eur-lex.europa.eu/legal-content/ET/TXT/?uri=CELEX%3A32016R0679">isikuandmete kaitse üldmäärusest</a>; Eesti <a href="https://www.riigiteataja.ee/akt/106032026010">isikuandmete kaitse seadus</a> sisaldab muu hulgas avalikes huvides arhiveerimise erisusi.</p>
      </section>
    </article>
  );
}
