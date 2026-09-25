import type { Metadata } from "next";
import Link from "next/link";
import { getApi, type Statistics } from "@/lib/api";
import { publicId } from "@/lib/public-id";
import { HonorRollTable } from "@/components/HonorRollTable";
import { compareValues } from "@/lib/sort";

export const metadata: Metadata = { title: "Inimesed" };

export default async function PeoplePage({ searchParams }: { searchParams: Promise<{ view?: string; sort?: string; order?: string; page?: string; rows?: string }> }) {
  const { view, sort, order, page, rows } = await searchParams;
  const selected = view === "mentors" ? "mentors" : "students";
  const data = await getApi<Statistics>(`/statistics/${selected}?weighted=true`);
  const indexes: Record<string, number> = { name: 1, participations: 2, first: 3, second: 4, third: 5 };
  const sorted = sort && Object.hasOwn(indexes, sort) ? [...data.rows].sort((a, b) => {
    const comparison = compareValues(a[indexes[sort]], b[indexes[sort]]);
    return order === "desc" ? -comparison : comparison;
  }) : [...data.rows].sort((a, b) => Number(b[3]) - Number(a[3]) || Number(b[4]) - Number(a[4]) || Number(b[5]) - Number(a[5]) || Number(b[2]) - Number(a[2]));
  const publicRows = sorted.map((row) => [publicId("person", Number(row[0])), ...row.slice(1)]);
  return <>
    <section className="page-intro"><h1>Inimesed</h1><p>Vähemalt kümme osalemist või juhendamist või koht esikolmikus. Esikolmiku kohad on kaalutud vanuserühma klasside arvu järgi, kõige rohkem kolme klassiga.</p><p><Link prefetch={false} href="/data-protection">Miks kõik inimesed siin ei ole?</Link></p><div className="actions"><a href={`/people/download?view=${selected}`}>Laadi alla CSV</a></div></section>
    <nav className="school-tabs" aria-label="Inimeste vaade"><Link prefetch={false} href="/people" aria-current={selected === "students" ? "page" : undefined}>Õpilased</Link><Link prefetch={false} href="/people?view=mentors" aria-current={selected === "mentors" ? "page" : undefined}>Juhendajad</Link></nav>
    <HonorRollTable data={publicRows} sort={sort} order={order} page={page} rows={rows} view={selected} />
  </>;
}
