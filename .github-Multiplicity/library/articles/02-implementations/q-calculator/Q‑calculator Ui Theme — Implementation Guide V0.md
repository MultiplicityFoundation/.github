---
slug: q-calculator-ui-theme-implementation-guide-v0
status: draft
created: '2026-03-20'
updated: '2026-03-20'
version: 0.1.0
tags:
- multiplicity
traceability:
  path: "02-implementations/q-calculator/Q\u2011calculator Ui Theme \u2014 Implementation\
    \ Guide V0.md"
  last_synced: '2026-03-20T17:17:15.152570Z'
---

Q‑Calculator UI Theme — Implementation Guide
v0.1
This guide defines the visual language, tokens, and setup steps to implement the Q‑Calculator theme
across web (Next.js/Remix) and shadcn/ui. It includes Tailwind config, CSS tokens, React helpers, motion
and charting guidance, accessibility, and QA.




1) Design principles
     • Calm auditability: default to low‑chroma neutrals; use color to signal provenance, state, and risk—
       never for decoration.
     • Legible math: prioritize typographic contrast, generous line‑height, and high DPI rendering for
       LaTeX.
     • Lawful by design: surface CSL/tribunal state clearly (banners, badges, locks).
     • Deterministic motion: subtle, brief transitions with reduced‑motion support; never animate
       essential numbers.
     • Status over style: every vibrant hue maps to a status (info/success/warn/error/attention/blocked/
       provenance).




2) Design tokens (CSS variables)
Place in apps/web/app/globals.css (or equivalent).



  :root {
    /* Palette (HSL) */
    --brand-hue: 262;                /* Quantum Violet */
    --brand-sat: 86%;
    --brand-lit: 60%;

    --bg: 0 0% 100%;
    --fg: 222 47% 11%;
    --muted: 220 14% 96%;
    --muted-fg: 220 9% 46%;
    --card: 0 0% 100%;
    --card-fg: 222 47% 11%;
    --popover: 0 0% 100%;
    --popover-fg: 222 47% 11%;

    /* Accents mapped to states */
    --accent: var(--brand-hue) var(--brand-sat) var(--brand-lit);                      /* primary */
    --info: 207 90% 54%;      /* sky */



                                                    1
    --success: 142 72% 29%;   /* emerald */
    --warning: 38 92% 50%;    /* amber */
    --error: 0 84% 60%;       /* red */
    --blocked: 263 25% 46%;   /* muted violet */
    --provenance: 171 77% 41%;/* teal */


    /* Surfaces */
    --border: 220 13% 91%;
    --ring: var(--accent);


  /* Typography */
  --font-sans: "Inter var", ui-sans-serif, system-ui, -apple-system, Segoe UI,
Roboto, "Helvetica Neue", Arial, "Noto Sans", "Apple Color Emoji", "Segoe UI
Emoji";
  --font-mono: "JetBrains Mono", ui-monospace, SFMono-Regular, Menlo, Monaco,
Consolas, "Liberation Mono", monospace;

    /* Radius & Elevation */
    --radius: 1rem;           /* base radius */
    --radius-lg: 1.25rem;     /* cards */
    --radius-2xl: 1.5rem;     /* modals */
    --shadow-sm: 0 1px 2px hsl(220 14% 4% / 0.05);
    --shadow-md: 0 6px 20px hsl(220 14% 4% / 0.06);
    --shadow-lg: 0 16px 40px hsl(220 14% 4% / 0.08);

    /* Motion */
    --easing-standard: cubic-bezier(.2,.8,.2,1);
    --duration-fast: 120ms;
    --duration-base: 200ms;
    --duration-slow: 320ms;

    /* Focus */
    --focus: 0 0% 0% / 0;            /* fallback */
}

/***** Dark theme *****/
[data-theme="dark"] {
    --bg: 224 71% 4%;
    --fg: 213 31% 91%;
    --muted: 223 47% 11%;
    --muted-fg: 215 20% 65%;
    --card: 224 71% 4%;
    --card-fg: 213 31% 91%;
    --popover: 224 71% 4%;
    --popover-fg: 213 31% 91%;
    --border: 216 34% 17%;
    --ring: var(--accent);
}



                                         2
 /***** High‑contrast add‑on *****/
 [data-contrast="high"] {
   --muted: 0 0% 100%;
   --muted-fg: 222 47% 11%;
   --border: 222 47% 11%;
 }



Token → Tailwind layer (utility classes)


 @layer base {
   * { @apply border-[hsl(var(--border))]; }
   body { @apply bg-[hsl(var(--bg))] text-[hsl(var(--fg))]; }
 }


 @layer utilities {
   .bg-card { background-color: hsl(var(--card)); }
   .text-muted { color: hsl(var(--muted-fg)); }
   .ring-brand { box-shadow: 0 0 0 3px hsl(var(--accent) / 0.4); }
 }




3) Tailwind config
Create tailwind.config.ts in apps/web .



 import type { Config } from "tailwindcss";

 const config: Config = {
   darkMode: ["class"],
   content: [
     "./app/**/*.{ts,tsx}",
     "./components/**/*.{ts,tsx}",
     "./pages/**/*.{ts,tsx}",
      "./src/**/*.{ts,tsx}",
    ],
    theme: {
       container: { center: true, padding: "1rem", screens: { "2xl": "1280px" } },
       extend: {
         fontFamily: {
            sans: ["var(--font-sans)"],
            mono: ["var(--font-mono)"],
         },
         borderRadius: {




                                           3
                 DEFAULT: "var(--radius)",
                 lg: "var(--radius-lg)",
                 "2xl": "var(--radius-2xl)",
            },
            boxShadow: {
                 sm: "var(--shadow-sm)",
                 md: "var(--shadow-md)",
                 lg: "var(--shadow-lg)",
            },
            colors: {
               background: "hsl(var(--bg))",
               foreground: "hsl(var(--fg))",
               card: "hsl(var(--card))",
               popover: "hsl(var(--popover))",
               muted: "hsl(var(--muted))",
               "muted-fg": "hsl(var(--muted-fg))",
               accent: "hsl(var(--accent))",
               info: "hsl(var(--info))",
               success: "hsl(var(--success))",
               warning: "hsl(var(--warning))",
               error: "hsl(var(--error))",
               blocked: "hsl(var(--blocked))",
               provenance: "hsl(var(--provenance))",
            },
            keyframes: {
               "fade-in": { from: { opacity: "0" }, to: { opacity: "1" } },
               "scale-in": {
                  from: { opacity: "0", transform: "scale(.98)" },
                  to: { opacity: "1", transform: "scale(1)" },
               },
            },
            animation: {
               "fade-in": "fade-in var(--duration-base) var(--easing-standard)",
               "scale-in": "scale-in var(--duration-base) var(--easing-standard)",
            },
       },
  },
   plugins: [require("tailwindcss-animate")],
};
export default config;




                                               4
4) ThemeProvider (React)

  // apps/web/components/theme-provider.tsx
  "use client";
  import * as React from "react";
  import { useEffect, useState } from "react";

  type Props = { children: React.ReactNode };


  export default function ThemeProvider({ children }: Props) {
    const [theme, setTheme] = useState<"light" | "dark">("light");
    const [contrast, setContrast] = useState<"normal" | "high">("normal");

    useEffect(() => {
      const root = document.documentElement;
      root.dataset.theme = theme;
      if (contrast === "high") root.dataset.contrast = "high"; else
  root.removeAttribute("data-contrast");
    }, [theme, contrast]);

      return (
        <div className="min-h-screen bg-[hsl(var(--bg))] text-[hsl(var(--fg))]">
             {/* Expose controls via context or settings panel */}
             {children}
           </div>
      );
  }


Wrap your app root in ThemeProvider .




5) Components — visual rules

Buttons

      • Variants: primary (accent), secondary (muted), ghost (transparent), destructive (error),
           link (underline on hover).
      • Sizes: sm (28px), md (36px), lg (44px).
      • States: hover uses 6% overlay; focus shows 3px ring hsl(var(--accent) / 0.4) ; disabled
        lowers opacity to 0.5.
      • Icon buttons: 40px square, 12px radius, center icons (lucide 18–20px).

Inputs & Textareas

      • 1px border --border , 8px radius; focus ring brand; support suffix units chip (e.g., m·s⁻² ).
      • Error state switches border to --error and shows helper text.



                                                      5
Badges/Chips (status)

     • Info: sky; Success: emerald; Warning: amber; Error: red; Blocked: muted violet; Provenance: teal.
     • Include icon mapping: info: info , success: check-circle , warning: alert-triangle ,
       error: octagon , blocked: ban , provenance: fingerprint .

Cards & Panels

     • Card: bg-card with shadow-md , radius --radius-lg , padding 24px .
     • Panel (e.g., Proof Drawer): denser (16px), mono captions for hashes/IDs.

Banners (CSL/Tribunal)

     • Sticky top; left icon + strong headline; CTA buttons right‑aligned.
     • Variants: info , warning , blocked . Always include link to evidence.




6) Motion system (Framer Motion)
     • Durations: fast 120ms, base 200ms, slow 320ms.
     • Default easing: var(--easing-standard) .
     • Reduce motion: wrap animated sections with prefers-reduced-motion check.


 import { motion, useReducedMotion } from "framer-motion";

 export function CardMotion({ children }: { children: React.ReactNode }) {
   const reduce = useReducedMotion();
   return (
      <motion.div
        initial={{ opacity: 0, scale: reduce ? 1 : 0.98 }}
        animate={{ opacity: 1, scale: 1 }}
        transition={{ duration: 0.2 }}
        className="bg-card shadow-md rounded-lg"
      >
        {children}
      </motion.div>
   );
 }




7) Charts (Recharts)
     • Use neutrals for series; reserve accent color for “winner”/“certified” lines.
     • Label fonts use --font-sans ; code ticks use --font-mono where helpful.
     • Minimum 12px tick labels; 14px legend; grid lines at 1px with 12% opacity.




                                                     6
 import { LineChart, Line, CartesianGrid, XAxis, YAxis, Tooltip,
 ResponsiveContainer } from "recharts";

 export function ResidualChart({ data }: { data: { t: number; r: number }[] }) {
     return (
       <div className="bg-card p-4 rounded-lg shadow-md">
         <ResponsiveContainer width="100%" height={240}>
           <LineChart data={data} margin={{ left: 8, right: 8, top: 8, bottom: 8 }}
 >
             <CartesianGrid strokeOpacity={0.12} />
             <XAxis dataKey="t" tick={{ fontSize: 12 }} />
             <YAxis tick={{ fontSize: 12 }} />
             <Tooltip />
             <Line type="monotone" dataKey="r" stroke="hsl(var(--accent))"
 strokeWidth={2} dot={false} />
          </LineChart>
        </ResponsiveContainer>
      </div>
   );
 }




8) Iconography
     • Use lucide-react ; stroke width 2 by default; icons align to 20px grid inside 40px button.
     • Status icons: CheckCircle2 , CircleAlert , OctagonAlert , Ban , Fingerprint , Info .




9) Typography & scales
     • Headline scale (rem): h1 2.25 , h2 1.75 , h3 1.375 .
     • Body: 1.0 with 1.6 line‑height.
     • Mono code blocks at 0.92 with 1.5 line‑height; wrap long hashes.
     • Math/LaTeX: ensure high‑contrast formula text on card backgrounds; render at 1.1× body.




10) Layout grid & spacing
     • Container widths: sm 640 , md 768 , lg 1024 , xl 1280 , 2xl 1440 .
     • Grid: 12‑col; gutters 24px desktop / 16px mobile.
     • Spacing scale (px): 4, 8, 12, 16, 20, 24, 32, 40, 48, 64 .




                                                    7
11) Accessibility
   • WCAG 2.2 AA minimum; avoid red/green‑only encodings.
   • Focus ring: 3px outside outline using ring-brand on focusable components.
   • Keyboard order must match visual order; skip‑to‑content link on page load.
   • Announce policy state changes (e.g., tribunal approved) via ARIA live region.




12) Copy standards
   • Tone: precise, calm, evidential. Prefer verbs like “Verify”, “Show trace”, “Open ledger”.
   • Microcopy patterns:
   • Policy blocked: “Action requires tribunal approval. Review evidence to proceed.”
   • Computation OK: “Certified contraction complete. Residual ≤ 1e‑6.”




13) Install & wire‑up steps
   1. Packages


       pnpm add tailwindcss tailwindcss-animate class-variance-authority framer-
       motion recharts lucide-react


   2. Fonts: add Inter Variable + JetBrains Mono via next/font or self‑host; map to --font-sans / --
     font-mono .
   3. CSS: add tokens from §2 to globals.css and include Tailwind base/components/utilities.
   4. Tailwind: use config from §3; enable darkMode: "class" .
   5. Provider: wrap app with ThemeProvider (§4). Add theme toggle in Settings.
   6. shadcn/ui: generate components; map their color slots to our CSS vars.




14) Specialized UI for Q‑Calculator
   • Proof Drawer: right‑side panel with mono labels for hashes; copy buttons; ‘Compare’ CTA.
   • Policy Banner: top bar; variant blocked turns action buttons into secondary + tooltip.
   • Provenance Chip: teal chip with fingerprint icon + short ledger id.
   • Residual Widget: small sparkline using accent color; hover shows last 10 steps.




15) QA checklist
   • [ ] Dark/light parity for all components
   • [ ] High‑contrast mode maintains ≥ 7:1 for body, ≥ 4.5:1 for UI text
   • [ ] Keyboard/Focus audit on forms, menus, drawers, dialogs




                                                     8
       • [ ] Screen reader labels for banners, proof drawer controls, chart tooltips
       • [ ] Status colors never the sole signal; icons + text present




16) Example: Button (shadcn/ui) with theme slots

  import { cva, type VariantProps } from "class-variance-authority";


  export const button = cva(
    "inline-flex items-center justify-center rounded-lg font-medium transition-
  colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-
  offset-2 disabled:opacity-50 disabled:pointer-events-none ring-offset-
  [hsl(var(--bg))]",
    {
      variants: {
        variant: {
          primary: "bg-[hsl(var(--accent))] text-white hover:opacity-95",
          secondary: "bg-[hsl(var(--muted))] text-[hsl(var(--fg))] hover:bg-
  [hsl(var(--muted))/0.9]",
          ghost: "hover:bg-[hsl(var(--muted))]",
          destructive: "bg-[hsl(var(--error))] text-white hover:opacity-95",
          link: "underline underline-offset-4",
             },
             size: {
                sm: "h-7 px-3 text-sm",
                md: "h-9 px-4",
                lg: "h-11 px-5 text-base",
             },
           },
           defaultVariants: { variant: "primary", size: "md" },
       }
  );

  export type ButtonVariants = VariantProps<typeof button>;




17) What to brand next
       • Favicon/logo (monoline quantum‑violet mark), loading splash, empty states illustrations.
       • Doc theming for LaTeX/MathJax and code viewer including prime signatures and hashes.



End v0.1




                                                        9
