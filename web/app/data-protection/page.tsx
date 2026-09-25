import type { Metadata } from "next";

export const metadata: Metadata = { title: "Andmekaitse" };

export default function DataProtectionPage() {
  return (
    <article className="privacy-content">
      <header className="page-intro">
        <h1>Andmekaitsetingimused</h1>
        <p>
          Siin selgitame, kuidas Eesti Olümpiaadide Andmebaas (EOA) töötleb
          olümpiaaditulemuste ja veebilehe kasutamisega seotud isikuandmeid.
        </p>
        <p>
          Kui oled õpilane: EOA võib näidata sinu nime ja olümpiaaditulemust.
          Kui tulemus on vale või sa ei soovi oma nime siin näha, kirjuta meile
          aadressil{" "}
          <a href="mailto:eoakontakt@gmail.com">eoakontakt@gmail.com</a>.
          Vaatame sinu soovi läbi ja vastame sulle.
        </p>
        <p>
          <strong>
            Enne avaldamist lisatakse siia vastutava töötleja nimi ja
            kontaktandmed.
          </strong>
        </p>
      </header>

      <section aria-labelledby="data">
        <h2 id="data">Andmed ja nende päritolu</h2>
        <p>
          Töötleme õpilase ning õpetaja või juhendaja nime, kooli, klassi või
          vanuserühma, võistluse ja õppeaasta andmeid ning tulemust. Mõne
          võistluse puhul sisaldab tulemus punkte ja muid tulemuse osi. Kõik
          seni kogutud tulemused pärinevad korraldajate avalikult
          kättesaadavatelt lehtedelt. Konkreetse kirje teadaoleva algallika saab
          meilt küsida.
        </p>
        <p>
          EOA-l ei ole osalejate kontaktandmeid, mille abil neile kõigile eraldi
          teade saata. Andmekaitseteade on kättesaadav siin ja võistluste
          tulemustabelite juurest.
        </p>
        <p>
          Kui kirjutate meile, töötleme teie kirjas sisalduvaid andmeid ja
          vastamiseks vajalikku suhtlust. Kirjutamine on vabatahtlik, kuid ilma
          kontaktandmeteta ei pruugi me saada vastata. Veebilehe kasutamisel
          töötleb server päringu teenindamiseks tehnilisi andmeid, sealhulgas
          IP-aadressi ja päringu aega. EOA ei salvesta eraldi külastusloge.
        </p>
      </section>

      <section aria-labelledby="purpose">
        <h2 id="purpose">Eesmärgid ja õiguslik alus</h2>
        <p>
          Koondame, kontrollime ja säilitame tulemusi Eesti olümpiaadide ajaloo
          talletamiseks, varasemate saavutuste tõendamiseks ning õpilaste ja
          juhendajate panuse nähtavaks tegemiseks. Tulemusi saab veebis sirvida,
          otsida ja alla laadida.
        </p>
        <p>
          Tulemuste kogumise, säilitamise ja avaldamise õiguslik alus on
          isikuandmete kaitse üldmääruse artikli 6 lõike 1 punkt f. Õigustatud
          huvi on säilitada Eesti olümpiaadide ajalugu, võimaldada varasema
          saavutuse kontrollimist ning tunnustada õpilase ja juhendaja panust.
          Nimi võib selleks olla vajalik võistluse tulemustabelis; nimeotsingu,
          isikuprofiili ja edetabeli puhul piirame õpilaste nähtavust allpool
          kirjeldatud viisil. Huvide kaalumisel arvestame lapse vanust, tulemust
          osalejate arvu ja võistluse tingimuste taustal ning nii avaldamise kui
          ka nime peitmise mõju. Kui inimese nime avalik kuvamine ei ole
          põhjendatud, peidame tema nime EOA avalikest väljunditest.
        </p>
        <p>
          Andmekaitseõigustega seotud pöördumistele vastamiseks töötleme
          kirjavahetust üldmääruse artikli 6 lõike 1 punkti c alusel osas,
          milles see on vajalik õigusliku kohustuse täitmiseks. Muude päringute
          ja veebilehe tehnilise toimimise alus on punkt f: huvi vastata saadud
          küsimustele ning hoida leht toimivana.
        </p>
        <p>
          See, et tulemus oli juba avalik, ei anna iseenesest EOA-le õiguslikku
          alust. Praegu ei tugine EOA tulemuste töötlemisel osalejate
          nõusolekule.
        </p>
      </section>

      <section aria-labelledby="publication">
        <h2 id="publication">Avaldamine ja vastuvõtjad</h2>
        <p>
          Võistluse tulemustabelis võivad olla nähtavad nimed ja tulemused.
          Võistluse liik ega koht tabelis ei määra üksi, kas nime näitamine on
          põhjendatud. Nimepõhises õpilase otsingus, kooli õpilaste nimekirjas,
          koondtabelis ja isikuprofiilis kuvatakse õpilast siis, kui tal on
          vähemalt kümme osalemist või vähemalt üks koht esikolmikus.
          Juhendajate nimepõhisele otsingule ja profiilile seda piiri ei
          kohaldata. Piir ei peida õpilase nime võistluse tulemustabelist. Kui
          nime avalik kuvamine on peatatud, jääb tulemus võistluse tabelisse
          nimeta; selle juures ei näita EOA ka inimese profiililinki, kooli,
          klassi ega juhendajat.
        </p>
        <p>
          Avaldatud võistlustulemused on nähtavad veebikülastajatele ning
          kättesaadavad ka avaliku API ja üksikvõistluse CSV kaudu. Õpilaste
          koondedetabeli nimelist CSV allalaadimist ei pakuta; juhendajate
          koondtabelit saab CSVna alla laadida. Külastajad saavad avaldatust
          koopia teha; nende edasine iseseisev kasutus ei ole EOA kontrolli all.
          Veebileht ja andmebaas asuvad Hetzneri Soome serveris; varukoopiad
          asuvad Hetzneri Saksamaa ja Scaleway Prantsusmaa serverites.
          Kirjavahetuseks kasutame Google Gmaili. Google võib töödelda
          kirjavahetuse andmeid ka väljaspool Euroopa Majanduspiirkonda ning
          kirjeldab oma{" "}
          <a href="https://policies.google.com/privacy/frameworks?hl=et">
            andmeedastuse kaitsemeetmeid
          </a>
          . EOA ei kasuta teisi teenuseosutajaid.
        </p>
      </section>

      <section aria-labelledby="retention">
        <h2 id="retention">Säilitamine</h2>
        <p>
          Tulemusi säilitame tuvastataval kujul seni, kuni see on ajaloolise
          arhiivi eesmärgiks vajalik ja töötlemisel on õiguslik alus. Nimelisel
          avaldamisel ei ole automaatset aastate arvu: vähemalt kord aastas
          vaatame üle avaldamisreeglid ja kontrollime valimit, kas nime
          näitamine on endiselt vajalik saavutuse tõendamiseks või ajaloo
          talletamiseks, arvestades osaleja vanust, tulemuse laadi, algallika
          usaldusväärsust ning nii avaldamise kui ka nime peitmise mõju.
          Vaidlustatud või parandatud kirje vaatame üle viivitamata. Kui inimese
          nime avaldamine ei ole enam põhjendatud, peidame tema nime avalikest
          väljunditest; kui ka sisemise tuvastatava kirje eesmärk või alus kaob,
          kustutame või anonüümime asjaomased andmed.
        </p>
        <p>
          Tavalise kirjavahetuse kustutame 12 kuud pärast viimast sisulist
          vastust või juhtumi sulgemist. Andmekaitseõiguste taotluse kohta
          säilitame minimaalset menetlusjälge kolm aastat pärast juhtumi
          sulgemist. Isikusamasuse kontrolliks küsitud eraldi tõendi kustutame
          pärast kontrolli, hiljemalt 30 päeva jooksul, välja arvatud juhul, kui
          konkreetne vaidlus nõuab pikemat säilitamist. Varukoopiaid hoiame kuni
          90 päeva; taastamisel rakendame enne taasavalikustamist vahepealsed
          parandused ja varjamised.
        </p>
      </section>

      <section aria-labelledby="rights">
        <h2 id="rights">Teie õigused</h2>
        <p>
          Võite küsida kinnitust andmete töötlemise kohta, tutvuda oma andmetega
          ning paluda ebaõigeid andmeid parandada. Olenevalt asjaoludest võite
          taotleda kustutamist või töötlemise piiramist. Kui töötlemine põhineb
          õigustatud huvil, võite oma konkreetsest olukorrast lähtudes esitada
          vastuväite; seejärel lõpetame asjaomase töötlemise, kui me ei tõenda
          ülekaalukat mõjuvat õiguspärast põhjust või õigusnõude vajadust.
        </p>
        <p>
          Kirjutage{" "}
          <a href="mailto:eoakontakt@gmail.com">eoakontakt@gmail.com</a> ja
          märkige võimaluse korral asjaomane kirje. Kui meil on põhjendatud
          kahtlus taotleja isikusamasuses, võime küsida kontrollimiseks
          vajalikku lisateavet. Vastame üldjuhul ühe kuu jooksul. Keeruka või
          arvuka taotluse puhul võime tähtaega pikendada kuni kahe kuu võrra,
          teatades sellest esimese kuu jooksul. Taotluse lahendamine on üldjuhul
          tasuta.
        </p>
      </section>

      <section aria-labelledby="site-storage">
        <h2 id="site-storage">Veebilehe kohalik salvestus</h2>
        <p>
          Värviteema valimisel salvestab teie brauser seadmesse võtme{" "}
          <code>eoa-theme</code>, et valik järgmisel külastusel taastada. Valik
          „Süsteemi järgi” eemaldab selle võtme. EOA ei kasuta veebilehel
          analüütika- ega reklaamiküpsiseid.
        </p>
      </section>

      <section aria-labelledby="automated-decisions">
        <h2 id="automated-decisions">Automaatotsused</h2>
        <p>
          Veebileht arvutab tulemuste põhjal otsingu- ja edetabelivaateid. EOA
          ei tee nende andmete põhjal üksnes automatiseeritud otsuseid, millel
          on inimesele õiguslik või samaväärselt märkimisväärne mõju.
        </p>
      </section>

      <section aria-labelledby="complaint">
        <h2 id="complaint">Kaebus ja õigusaktid</h2>
        <p>
          Võite pöörduda{" "}
          <a href="https://www.aki.ee/meist/vota-uhendust/kaebus-isikuandmete-kaitse-asjas">
            Andmekaitse Inspektsiooni
          </a>{" "}
          poole. Andmekaitse põhireeglid tulenevad{" "}
          <a href="https://eur-lex.europa.eu/legal-content/ET/TXT/?uri=CELEX%3A32016R0679">
            isikuandmete kaitse üldmäärusest
          </a>
          ; Eesti{" "}
          <a href="https://www.riigiteataja.ee/akt/106032026010">
            isikuandmete kaitse seadus
          </a>{" "}
          sisaldab muu hulgas avalikes huvides arhiveerimise erisusi.
        </p>
      </section>
      <p>Viimati uuendatud 25.09.2026.</p>
    </article>
  );
}
