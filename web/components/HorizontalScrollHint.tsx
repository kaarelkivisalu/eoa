"use client";

import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";

export function HorizontalScrollHint() {
  const pathname = usePathname();
  const [visible, setVisible] = useState(false);

  useEffect(() => {
    const check = () => setVisible(document.documentElement.scrollWidth > window.innerWidth + 4);
    const frame = requestAnimationFrame(check);
    window.addEventListener("resize", check);
    return () => {
      cancelAnimationFrame(frame);
      window.removeEventListener("resize", check);
    };
  }, [pathname]);

  return visible ? <div className="horizontal-scroll-hint" role="status">← Kerige lehte horisontaalselt →</div> : null;
}
