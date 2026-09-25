import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { Breadcrumbs } from "@/components/Breadcrumbs";
import { Pagination, pageNumber } from "@/components/Pagination";
import { getApi, type SchoolPeople } from "@/lib/api";
import { internalId, publicId } from "@/lib/public-id";

type Props = { params: Promise<{ id: string }>; searchParams: Promise<{ view?: string; page?: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { id } = await params;
  const numericId = internalId("school", id);
  if (!numericId) return { title: "Kooli ei leitud" };
  const school = await getApi<SchoolPeople>(`/schools/${numericId}/students`);
  return { title: school.school_name };
}

export default async function SchoolPage({ params, searchParams }: Props) {
  const { id } = await params;
  const { view, page } = await searchParams;
  const numericId = internalId("school", id);
  if (!numericId) notFound();
  const selected = view === "mentors" ? "mentors" : "students";
  const data = await getApi<SchoolPeople>(`/schools/${numericId}/${selected}`);
  const people = (selected === "students" ? data.students ?? [] : data.mentors ?? []).map((person) => ({ ...person, person_id: publicId("person", person.person_id) }));
  const currentPage = Math.min(pageNumber(page), Math.max(1, Math.ceil(people.length / 50)));

  return <>
    <section className="page-intro"><Breadcrumbs items={[{ label: "Koolid", href: "/schools" }, { label: data.school_name, href: `/schools/${id}` }]} /></section>
    <nav className="school-tabs" aria-label="Kooli inimesed">
      <Link prefetch={false} href={`/schools/${id}`} aria-current={selected === "students" ? "page" : undefined}>Õpilased</Link>
      <Link prefetch={false} href={`/schools/${id}?view=mentors`} aria-current={selected === "mentors" ? "page" : undefined}>Juhendajad</Link>
    </nav>
    <PeopleTable people={people.slice((currentPage - 1) * 50, currentPage * 50)} countLabel={selected === "students" ? "Osalemisi" : "Õpilasi juhendatud"} />
    <Pagination page={currentPage} total={people.length} pageSize={50} path={`/schools/${id}`} params={selected === "mentors" ? { view: "mentors" } : {}} />
    {selected === "students" && <p className="visibility-note">Kokku {data.total_students ?? people.length} õpilast.{(data.hidden_students ?? 0) > 0 && <> {data.hidden_students} nime ei kuvata, sest õpilasel pole vähemalt kümmet osalemist ega kohta esikolmikus või tema nimi ei ole avaldatav. <Link prefetch={false} href="/data-protection">Andmekaitse</Link></>}</p>}
  </>;
}

function PeopleTable({ people, countLabel }: { people: { person_id: string; person_name: string; participations: number }[]; countLabel: string }) {
  if (!people.length) return <p>Andmeid ei leitud.</p>;
  return <div className="table-scroll"><table><thead><tr><th scope="col">Nimi</th><th scope="col">{countLabel}</th></tr></thead><tbody>{people.map((person) => <tr key={person.person_id}><td><Link prefetch={false} href={`/people/${person.person_id}`}>{person.person_name}</Link></td><td>{person.participations}</td></tr>)}</tbody></table></div>;
}
