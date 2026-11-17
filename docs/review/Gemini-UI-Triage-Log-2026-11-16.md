# Gemini UI/UX Review — Triage Log (2026-11-16)

**Gemini suggests; Claude decides.** Every claim was checked against the built CSS, source and screenshots before acting. Changes shipped to `The-Shadow-Exchange-Players`.

## Verified & ADOPTED
| Finding | Verified | Action |
|---|---|---|
| Nav order disagreed with the 1→2→3 onboarding (the *Start Here* tab opened Step 3; Character Creation lived under *Rules*) | read `mkdocs.yml` | Reordered: Quick Start → Build your character → Before Session 0 → Playbook Sheets; prev/next footers now match the step boxes |
| **Light mode failed contrast** (dark-mode amber/blue/line variables stayed active on cream paper) | read CSS; screenshot | Scheme-level overrides (`#9a5206`, `#1d5fa7`, …); header/tabs keep the bright amber; verified visually |
| Hero title overlapped the bright shop sign | screenshot | Radial scrim + darker lower gradient; button spacing |
| Hero CTAs ambiguous | read | Labels: **1. Quick Start (5 min)** / **Session 0 checklist** *(Gemini's "Checklist & Sheets" would have been inaccurate — sheets live on Official Resources)* |
| Header title truncated on phones | screenshot | `site_name` shortened to "The Shadow Exchange" |
| Floated portraits could overrun short sections / push FAQ content down on phones | read CSS | Float clearing; capped, cropped mobile image |
| **Broken nested italics** on What-Kind-of-Game | read file (my earlier edit) | Fixed |
| Missing next-step boxes (Before-Session-0, Official Resources, Glossary, FAQ, Known Contacts) | read | Added |
| Gemini watermark star on images; hero 616 KB | screenshot | Cropped 7%; hero re-exported 1400 px (≈370 KB) |
| No focus rings / reduced-motion | read CSS | Added |
| Tappable checklist; copy-paste template for the GM | idea | Added (`pymdownx.tasklist`, `content.code.copy`); also explicit ring/filled checkbox styles |
| 3-step progress bar; print stylesheet (Quick Start as table handout) | idea | Added |
| Google Fonts via blocking `@import` | read | Moved to `extra_css` link |

## ADAPTED
- Nested numbered list in the checklist: moved the template into its own section after a screenshot showed Markdown collapsing it; forced decimal numbering to match the template.
- Tab labels: modest bump (.68rem) instead of Gemini's .70.

## REJECTED
- **"Body text is 13 px; raise to .88rem."** *Wrong.* Material sets `html{font-size:125%}` (20 px), so `.82rem` renders ≈ 16.4 px. Left as is.
- **Collapsible playbook cards with special-ability text and friend lists.** The ability wording is not verified here and the sheet's friends are setting-specific (licensing excludes non-SRD setting content); the Official Resources page links the real sheets instead.

## Open
- Consider adding a "How a roll works" diagram on the Quick Start (Gemini's bigger idea 2 variant).
