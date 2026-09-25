"use client";

import { useEffect, useRef, useState } from "react";
import { useRouter } from "next/navigation";

const fixedSizes = [10, 20, 50, 100] as const;

export function useListPageSize(rows: string | undefined) {
  const tableRef = useRef<HTMLTableElement>(null);
  const [autoSize, setAutoSize] = useState(12);

  useEffect(() => {
    const update = () => {
      const table = tableRef.current;
      if (!table) return;
      const top = table.getBoundingClientRect().top + window.scrollY;
      const headingHeight = table.tHead?.getBoundingClientRect().height ?? 36;
      const rowHeight = table.tBodies[0]?.rows[0]?.getBoundingClientRect().height ?? 32;
      const space = window.innerHeight - top - headingHeight - 115;
      setAutoSize(Math.max(6, Math.min(30, Math.floor(space / Math.max(30, rowHeight)))));
    };
    update();
    window.addEventListener("resize", update);
    return () => window.removeEventListener("resize", update);
  }, []);

  const fixed = fixedSizes.find((size) => String(size) === rows);
  return { tableRef, pageSize: fixed ?? autoSize, selected: fixed ? String(fixed) : "auto" };
}

export function PageSizeSelect({ path, selected, sort, order, params = {} }: { path: string; selected: string; sort?: string; order?: string; params?: Record<string, string | undefined> }) {
  const router = useRouter();
  return <label className="page-size-control">Ridu lehel
    <select value={selected} onChange={(event) => {
      const query = new URLSearchParams();
      if (sort) query.set("sort", sort);
      if (order) query.set("order", order);
      for (const [key, value] of Object.entries(params)) if (value) query.set(key, value);
      if (event.target.value !== "auto") query.set("rows", event.target.value);
      router.push(`${path}${query.size ? `?${query}` : ""}`);
    }}>
      <option value="auto">Automaatselt</option>
      {fixedSizes.map((size) => <option value={size} key={size}>{size}</option>)}
    </select>
  </label>;
}
