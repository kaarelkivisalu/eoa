import type { Metadata } from "next";
import { getApi, type SchoolRanking } from "@/lib/api";
import { SchoolRankingTable } from "@/components/SchoolRankingTable";
import { compareValues } from "@/lib/sort";
import { publicId } from "@/lib/public-id";
import Link from "next/link";

export const metadata: Metadata = { title: "Koolid" };

export default async function SchoolsPage({ searchParams }: { searchParams: Promise<{ sort?: string; order?: string; page?: string; rows?: string }> }) {
  const { sort, order, page, rows } = await searchParams;
  const schools = await getApi<SchoolRanking[]>("/site/schools");
  const sortable = ["school_name", "participations", "students", "hidden_students", "first_places", "second_places", "third_places"] as const;
  const sorted = sort && sortable.some((key) => key === sort)
    ? [...schools].sort((a, b) => {
        const key = sort as (typeof sortable)[number];
        const comparison = compareValues(a[key], b[key]);
        return order === "desc" ? -comparison : comparison;
      })
    : schools;

  return <>
    <section className="page-intro"><h1>Koolid</h1><p>Koolide osalemised avaldatavate õpilaste tulemuste põhjal.</p></section>
    <SchoolRankingTable schools={sorted.map((school) => ({ ...school, school_id: publicId("school", Number(school.school_id)) }))} sort={sort} order={order} page={page} rows={rows} />
    {schools.some((school) => school.hidden_students > 0) && <p className="visibility-note">Peidetud õpilased ei täida nimekirja kuvamistingimusi või nende nimi pole avaldatav. <Link prefetch={false} href="/data-protection">Andmekaitse</Link></p>}
  </>;
}
