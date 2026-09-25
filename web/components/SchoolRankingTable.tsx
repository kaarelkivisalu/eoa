"use client";

import Link from "next/link";
import type { SchoolRanking } from "@/lib/api";
import { PageSizeSelect, useListPageSize } from "@/components/ListPageSize";
import { Pagination, pageNumber } from "@/components/Pagination";
import { SortHeading } from "@/components/SortHeading";

const columns = [
  ["school_name", "Kool"],
  ["participations", "Osalemisi"],
  ["students", "Õpilasi"],
  ["hidden_students", "Peidetud"],
  ["first_places", "1. kohti"],
  ["second_places", "2. kohti"],
  ["third_places", "3. kohti"],
] as const;

export function SchoolRankingTable({ schools, sort, order, page, rows }: { schools: SchoolRanking[]; sort?: string; order?: string; page?: string; rows?: string }) {
  const { tableRef, pageSize, selected } = useListPageSize(rows);
  const currentPage = Math.min(pageNumber(page), Math.max(1, Math.ceil(schools.length / pageSize)));
  const visible = schools.slice((currentPage - 1) * pageSize, currentPage * pageSize);

  const showHidden = schools.some((school) => school.hidden_students > 0);
  return <>
    <PageSizeSelect path="/schools" selected={selected} sort={sort} order={order} />
    <div className="table-scroll"><table ref={tableRef}><thead><tr>{columns.filter(([key]) => showHidden || key !== "hidden_students").map(([key, label]) => <SortHeading key={key} label={label} column={key} current={sort} order={order} base="/schools" params={{ rows }} />)}</tr></thead>
      <tbody>{visible.map((school) => <tr key={school.school_id}><td><Link prefetch={false} href={`/schools/${school.school_id}`}>{school.school_name}</Link></td><td>{school.participations}</td><td>{school.students}</td>{showHidden && <td>{school.hidden_students || "—"}</td>}<td>{school.first_places}</td><td>{school.second_places}</td><td>{school.third_places}</td></tr>)}</tbody>
    </table></div>
    <Pagination page={currentPage} total={schools.length} pageSize={pageSize} path="/schools" params={{ sort, order, rows }} />
    {schools.length === 0 && <p>Koole ei leitud.</p>}
  </>;
}
