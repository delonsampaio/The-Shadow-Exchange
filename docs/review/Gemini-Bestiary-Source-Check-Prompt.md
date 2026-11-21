# Gemini Bestiary Source-Check Prompt

**Why:** Claude could not verify the 40 Wikipedia links in Gemini's bestiary (the site returned HTTP 429, a rate limit, to automated requests), and several page titles look wrong or may not exist. Gemini can browse, so it checks them. Paste the block into Gemini. The raw bestiary is saved at `docs/review/Gemini-Bestiary-Raw-2026-11-20.txt`.

````
ROLE
You are a careful fact-checker. You can browse the web. Do NOT edit any files and do NOT write new creatures.

TASK
Below are source links you cited in your bestiary (read your own list in docs/review/Gemini-Bestiary-Raw-2026-11-20.txt for the creature each belongs to). For EACH link, open it and report one line:
  creature # and name | link status (OK / redirects to <title> / dead / wrong topic) | does the page support what you claimed about the creature (YES / PARTLY / NO, with the one claim that fails) | the correct URL if this one is wrong.
Pay special attention to titles that may not exist as named: El_Naddaha (is it Al-Naddaha or another title?), Ghosts_in_Malay_culture, Gef, Polybius_(urban_legend), Bulgasari_(creature), Nixie_(folklore), Noppera-bō, Kisaragi_Station, Phantom_social_workers, and the Shui gui anchor link.
Also tell me, for every creature from a LIVING faith (Golem, Vetala, Naddaha, Shui gui, Nuno sa punso, Tokoloshe, Jiangshi, Dokkaebi, Tikbalang, others), what the community would find disrespectful about a horror-comedy treatment, in one sentence each.
Finally: for any urban legend you marked "grounded in a real example", say whether the real example exists (name, year, source). If you cannot find it, say "NOT FOUND". Never guess and never invent a quote or source.

LINKS
- https://en.wikipedia.org/wiki/Adze_(folklore)
- https://en.wikipedia.org/wiki/Akaname
- https://en.wikipedia.org/wiki/Alp_(folklore)
- https://en.wikipedia.org/wiki/Baku_(mythology)
- https://en.wikipedia.org/wiki/Banshee
- https://en.wikipedia.org/wiki/Bulgasari_(creature)
- https://en.wikipedia.org/wiki/Capitol_Hill_mystery_soda_machine
- https://en.wikipedia.org/wiki/Ciguapa
- https://en.wikipedia.org/wiki/Dokkaebi
- https://en.wikipedia.org/wiki/Domovoy
- https://en.wikipedia.org/wiki/El_Naddaha
- https://en.wikipedia.org/wiki/El_Silb%C3%B3n
- https://en.wikipedia.org/wiki/El_Sombrer%C3%B3n
- https://en.wikipedia.org/wiki/Gef
- https://en.wikipedia.org/wiki/Ghosts_in_Malay_culture
- https://en.wikipedia.org/wiki/Golem
- https://en.wikipedia.org/wiki/Hasshaku-sama
- https://en.wikipedia.org/wiki/Jiangshi
- https://en.wikipedia.org/wiki/John_Zegrus
- https://en.wikipedia.org/wiki/Kisaragi_Station
- https://en.wikipedia.org/wiki/Klabautermann
- https://en.wikipedia.org/wiki/List_of_supernatural_beings_in_Chinese_folklore#Shui_gui_(水鬼)
- https://en.wikipedia.org/wiki/Mokumokuren
- https://en.wikipedia.org/wiki/Nisse_(folklore)
- https://en.wikipedia.org/wiki/Nixie_(folklore)
- https://en.wikipedia.org/wiki/Noppera-b%C5%8D
- https://en.wikipedia.org/wiki/Nuno_sa_punso
- https://en.wikipedia.org/wiki/P%C3%BAca
- https://en.wikipedia.org/wiki/Phantom_social_workers
- https://en.wikipedia.org/wiki/Polybius_(urban_legend)
- https://en.wikipedia.org/wiki/Red_Room_Curse
- https://en.wikipedia.org/wiki/Resurrection_Mary
- https://en.wikipedia.org/wiki/Rusalka
- https://en.wikipedia.org/wiki/Selkie
- https://en.wikipedia.org/wiki/Squonk
- https://en.wikipedia.org/wiki/The_Backrooms
- https://en.wikipedia.org/wiki/Tikbalang
- https://en.wikipedia.org/wiki/Tokoloshe
- https://en.wikipedia.org/wiki/Toynbee_tiles
- https://en.wikipedia.org/wiki/Vetala
````

Claude then fixes or drops any creature whose source fails before it enters the bestiary.
