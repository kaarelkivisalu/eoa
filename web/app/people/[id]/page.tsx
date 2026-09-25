import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import { getApi, type MentorEntry, type PersonEntry, type PersonLink } from "@/lib/api";
import { internalId, publicId } from "@/lib/public-id";

type Props = { params: Promise<{ id: string }> };

export async function generateMetadata({ params }: Props): Promise<Metadata> {
  const { id } = await params;
  const numericId = internalId("person", id);
  if (!numericId) return { title: "Inimest ei leitud" };
  const person = await getApi<PersonLink>(`/people/${numericId}`);
  return { title: person.person_name };
}

export default async function PersonPage({ params }: Props) {
  const { id } = await params;
  const numericId = internalId("person", id);
  if (!numericId) notFound();
  const [person, results, mentees] = await Promise.all([
    getApi<PersonLink>(`/people/${numericId}`),
    getApi<PersonEntry[]>(`/contestant/${numericId}`),
    getApi<MentorEntry[]>(`/mentor/${numericId}`),
  ]);
  return <>
    <section className="page-intro"><Link prefetch={false} className="back-link" href="/people/search">← Otsing</Link><p className="eyebrow">Inimene</p><h1>{person.person_name}</h1></section>
    <section className="section-block"><h2>Osalemised</h2>{results.length ? <div className="table-scroll"><table><thead><tr><th scope="col">Õppeaasta</th><th scope="col">Õppeaine</th><th scope="col">Võistlus</th><th scope="col">Klass</th><th scope="col">Koht</th></tr></thead><tbody>{results.map((r, i) => <tr key={`${r.subcontest_id}-${i}`}><td>{r.season}</td><td>{r.subject_name}</td><td><Link prefetch={false} href={`/results/${publicId("result", r.subcontest_id)}`}>{r.type ?? "Tulemused"}</Link></td><td>{r.age_group}</td><td>{r.placement ?? ""}</td></tr>)}</tbody></table></div> : <p>Osalemisi ei leitud.</p>}</section>
    {mentees.length > 0 && <section className="section-block"><h2>Juhendamised</h2><div className="table-scroll"><table><thead><tr><th scope="col">Õppeaasta</th><th scope="col">Õpilane</th><th scope="col">Õppeaine</th><th scope="col">Võistlus</th><th scope="col">Koht</th></tr></thead><tbody>{mentees.map((m, i) => <tr key={`${m.subcontest_id}-${i}`}><td>{m.season}</td><td>{m.student_id ? <Link prefetch={false} href={`/people/${publicId("person", m.student_id)}`}>{m.student_name}</Link> : m.student_name}</td><td>{m.subject_name}</td><td><Link prefetch={false} href={`/results/${publicId("result", m.subcontest_id)}`}>{m.type ?? "Tulemused"}</Link></td><td>{m.placement ?? ""}</td></tr>)}</tbody></table></div></section>}
  </>;
}
