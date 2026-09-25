const baseUrl = process.env.API_INTERNAL_URL ?? "http://localhost:8000";

export async function GET(request: Request) {
  const view = new URL(request.url).searchParams.get("view");
  if (view !== "students" && view !== "mentors") return new Response("Not found", { status: 404 });
  const response = await fetch(`${baseUrl}/statistics/${view}?weighted=true&format=csv`, { cache: "no-store", headers: { "X-EOA-Internal-Token": process.env.EOA_INTERNAL_API_TOKEN ?? "" } });
  if (!response.ok) return new Response("Andmeid ei õnnestunud laadida", { status: 502 });
  return new Response(response.body, {
    headers: {
      "Content-Type": "text/csv; charset=utf-8",
      "Content-Disposition": `attachment; filename="${view}.csv"`,
      "Cache-Control": "no-store",
    },
  });
}
