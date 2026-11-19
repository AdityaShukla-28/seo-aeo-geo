# 50 — Local SEO

Make a local or service-area business easy to find and choose in map results, local organic results and AI answers about "best <service> in <place>".

**Inputs:** `seo-workspace/<domain>/site-profile.md`, `brand-dna.md`, `research/keywords.csv` (local terms), `research/competitors.md`, GBP/Bing/Apple listing URLs or screenshots from the owner.
**Outputs:** local section of `seo-workspace/<domain>/audits/YYYY-MM-DD-audit.md`, local items in `audits/YYYY-MM-DD-fix-list.md`, citation and review actions in `plan/roadmap.md`, geo-grid snapshots in `tracking/baselines/`.

## When to use / skip

Run for **local businesses** (core), and lightly for agencies or freelancers serving a city, e-commerce with a physical store, marketplaces with local listings, and one-page sites of local businesses (02-site-types.md §1). Skip for online-only businesses. Location-page limits come from core rules §4; doorway rules from core rules §8; LocalBusiness base template from 21-schema.md; local links and digital PR from 40-links-and-mentions.md.

---

## Procedure

### 1. Classify the business

| Model | Signals | Effect |
|---|---|---|
| Storefront | Street address shown, map, "visit us" | Full NAP, map and address checks |
| Service-area business (SAB) | No public address, "we come to you", areas listed | Hide address in GBP; skip map/address checks; service areas must be cities, postcodes or neighbourhoods, not whole states or countries *(perishable, verified 2026-02)* |
| Hybrid | Showroom plus service areas | Both sets of checks |

Then detect the vertical (restaurant, healthcare, legal, home services, real estate, automotive, other). If unclear, show the top two with evidence and ask. Healthcare and legal trigger the YMYL overlay (02-site-types.md §12).

### 2. Business listings (GBP first, then Bing and Apple)

Ask the owner for the listing URL or screenshots of the dashboard; without access, read the public listing. Score each field: **2** present and optimized, **1** present, **0** missing, **N/A** if it doesn't apply. Report `score ÷ max × 100` as the "listing completeness" sub-score.

| Field | Optimized when |
|---|---|
| Primary category | Most specific true category ("Cosmetic dentist", not "Dentist") — the strongest single local factor; a wrong one is the worst mistake |
| Additional categories | Every genuinely offered category (often 3–5) |
| Business name | The real-world name exactly, no added keywords (keyword stuffing risks suspension) |
| Address / service areas | Matches site NAP; SAB areas as cities/postcodes |
| Phone | Local number matching the site |
| Website link | Correct page (home, or the location page for multi-location) with UTM tagging for tracking |
| Hours, holiday hours | Complete and current ("open now" affects visibility) |
| Verification | Verified (video verification is now common) *(perishable)* |
| Description | 250–750 characters, plain description of services and area, no links or promotions |
| Services / products | All core services with short descriptions; prices where sensible |
| Photos and video | Real exterior, interior, team, work; added regularly; logo and cover set. Geotagging photos has no effect |
| Attributes | Relevant ones set (accessibility, payments, identity attributes) |
| Booking / menu link | Configured where it applies |
| Posts | Used for offers, events, updates (weak ranking effect; helps conversions) |
| Review replies | Most reviews answered (aim 80%+) |
| Q&A | Google discontinued the Q&A API on 2025-11-03 and public Q&A is being phased out *(perishable, verified 2026-09)*: answer common questions on the website and in the description |

Duplicate listings at the same address are a serious negative: find and merge or remove them through the platform's support flow. Never create listings for virtual offices or addresses without real staffed presence.

Then repeat the core fields on **Bing Places for Business** (feeds Bing, Copilot and other assistants that use Bing's index; can import from GBP) and **Apple Business Connect** (Apple Maps, Siri; Apple reportedly reorganized its business tools in 2026 — check the current product name and flow) *(perishable, verified 2026-03)*.

### 3. NAP consistency

1. Write the canonical NAP once: legal display name, full address in local postal format, primary phone in local and international form (`+91…`, `+1…`, `+44…`).
2. Extract NAP from: visible site footer/contact page, LocalBusiness JSON-LD, GBP, Bing, Apple, Facebook, the top 10 citations.
3. Compare each field:

| Mismatch | Priority |
|---|---|
| Different business name or old brand | Critical |
| Different street address, suite, or old address | High |
| Different or tracking phone number (use a tracking number only as the website-only number; keep the main number as the listing's primary) | Medium |
| Formatting only ("St" vs "Street") | Low (note, don't chase) |

4. Fix at the source of truth first (GBP and the site), then data aggregators, then individual directories.

### 4. Citations (region-specific)

Never assume US directories. Build the list per market:

| Market | Core listings |
|---|---|
| Everywhere | Google Business Profile, Bing Places, Apple Business Connect, Facebook page, OpenStreetMap (anyone can add a correct, verified-by-you entry) |
| India | Justdial, Sulekha, IndiaMART (B2B, manufacturers, suppliers), plus vertical sites (e.g. Practo for doctors, Zomato/Swiggy for restaurants) |
| United States | Yelp, BBB, Angi, Nextdoor, Yellow Pages, Foursquare; data aggregators Data Axle, Foursquare, Neustar Localeze feed many smaller sites |
| United Kingdom | Yell, Thomson Local, plus Checkatrade or similar for trades, Trustpilot for reviews |
| Any other country | Find them (below) |

**Find the top directories for any country or niche:** search `<category> <city>` (and `best <category> <city>`) in Google and Bing; note which directories, review sites and "best of" lists appear on page 1 and in AI answers; those are the citations that matter. Repeat for 2–3 core services. Add vertical directories (healthcare: national doctor registries and booking sites; legal: bar association and lawyer directories; restaurants: delivery and reservation apps; home services: trade platforms; real estate and automotive: the leading portals in that market).

Rules: quality and relevance beat volume; skip spammy "submit to 500 directories" services (core rules §8); one listing per location; same NAP everywhere; record logins with the owner, not in workspace files (core rules §9.4).

### 5. Reviews

| Check | Healthy |
|---|---|
| Velocity | New reviews arrive steadily every month; long gaps (weeks) correlate with drops (directional study) |
| Rating and count | Compared with the top 3 competitors in the local pack, not an absolute target |
| Recency | Recent reviews visible; buyers weigh the last few months most |
| Replies | Most reviews answered, negatives within days, calmly and without private details |
| Spread | Google plus the 1–2 review sites that rank for the category in that market |

Process: ask **every** customer after the service (QR code, receipt, SMS/email link), never only happy ones (no review gating, core rules §8); never offer rewards for positive reviews; disclosed incentives only where the platform allows them at all (core rules §8). Regulated industries: healthcare replies must not confirm the reviewer is a patient; legal replies must not reveal client details.

**Fake review signals** (flag when 2+ match, for the owner's or a competitor's profile): bursts on the same day, single-review accounts, reviewer locations far from the business, all-5-star spikes without a campaign, near-identical text. Report suspicious competitor reviews through the platform, never retaliate.

Review markup: never mark up the business's own reviews or ratings on its own LocalBusiness (core rules §6).

### 6. On-site local signals and location pages

- Title and H1 name the main service and city naturally; NAP as text (not an image) in the footer or contact page; `tel:` click-to-call link; map embed on the contact page only (lazy-loaded).
- **One strong page per core service** (dedicated service pages are a top local organic factor, directional).
- **Location pages**: one per real location, or per service area with genuinely local content. Gates: core rules §4. **Swap test:** if you can replace the city name and the page still reads true, it's a doorway page. Unique content means: local team, photos of local jobs, area-specific testimonials, local prices or regulations, directions, landmarks, local FAQs.
- Multi-location URL pattern: `/locations/<city>/` subfolders with crawlable, server-rendered store-locator links (no JavaScript-only locator).
- Internal links: home → service pages → location pages (hub and spoke, 13-strategy-and-plan.md).

### 7. Local schema specifics (beyond 21-schema.md)

Use the 21 LocalBusiness template and add:

| Item | Rule |
|---|---|
| Subtype | Most specific schema.org type: `Dentist`, `MedicalClinic`, `Physician` (doctor pages with Person), `Restaurant`/`CafeOrCoffeeShop`/`Bakery`, `Plumber`, `Electrician`, `HVACBusiness`, `RoofingContractor`, `Locksmith`, `MovingCompany`, `LegalService` (not deprecated `Attorney`), `RealEstateAgent` (agents and brokerages), `AutoDealer` / `AutoRepair` / `AutoPartsStore`, `BeautySalon`, `HealthClub`, `VeterinaryCare`, `Hotel`… Generic `LocalBusiness` only when nothing fits |
| `geo` | `latitude`/`longitude` with at least 5 decimal places (~1 m), taken from the real entrance, not a city centroid |
| Hours | `openingHoursSpecification` per day group; `specialOpeningHoursSpecification` for holidays |
| SAB | Omit `streetAddress` if the address is hidden in GBP; use `areaServed` with named `City`/`AdministrativeArea` objects, each with `sameAs` to its Wikidata or Wikipedia page |
| Multi-location | Home page: one `Organization` with `"@id": "https://example.com/#organization"`. Each location page: its own LocalBusiness subtype with a unique `"@id": "https://example.com/locations/pune/#location"`, its own NAP, `geo`, hours, and `"parentOrganization": {"@id": "https://example.com/#organization"}` (`branchOf` is the older property; schema.org marks it superseded, but existing correct use is harmless) |
| Departments | `department` for separate units with their own hours or phone (car sales vs service) |
| Vertical extras | Restaurant: `servesCuisine`, `acceptsReservations`, `hasMenu` with `Menu`/`MenuSection`/`MenuItem` (menu as HTML text too); healthcare: `medicalSpecialty`, physician `Person` with credentials; legal: `Service` per practice area; home services: `Service` pages with `provider` and `areaServed` |
| Never | Self-serving `aggregateRating`/`review`, `VehicleListing` (retired; replacement in 21-schema.md §1), placeholder values |

Values must match the visible page and GBP exactly. Validate (21-schema.md).

### 8. Local authority and AI answers

- Local links and mentions: chamber of commerce, trade associations, local news, sponsorships, local events, supplier and partner pages, and **local "best of" lists** (a leading AI-visibility factor in practitioner surveys, directional). Run them through 40-links-and-mentions.md Part B.
- AI assistants answer local prompts from map data and from third-party sources: Bing's index, review sites, directories, Reddit and local press *(perishable, verified 2026-03; directional)*. So citations, reviews and Bing Places double as GEO work.
- Test 3–5 prompts ("best <service> in <city>", "<service> near <landmark> open now", "is <brand> good?") in 2+ assistants, 2+ runs each, and log them via 60-measurement.md.

### 9. Geo-grid rank tracking (optional)

Map rankings change with the searcher's location. A grid shows where the business is visible.

**Grid:** pick a centre (the business), a size (3×3 quick, 5×5 standard, 7×7 detailed) and a radius (dense city 2–5 km, suburb 5–10 km, rural 10–25 km). For point (row i, column j): `step = 2 × radius_km ÷ (size − 1)`, `lat = lat0 + (i − c) × step ÷ 111.32`, `lng = lng0 + (j − c) × step ÷ (111.32 × cos(lat0))`, where `c = (size − 1) ÷ 2`.

**Free manual method** (fine for 9–25 points, 1–2 keywords):
1. Open a private browser window, signed out.
2. For each point, open `https://www.google.com/maps/search/<keyword>/@<lat>,<lng>,14z` and record the business's position in the result list (1–20, or "–" if absent). Use the same zoom for every point.
3. Do it by hand at a human pace. Don't script or scrape Google results (against its terms).

**Paid method:** any geo-grid rank tracker or Maps SERP API. Before running, show grid size × keywords = number of checks and the estimated cost, and get the user's OK.

**Report:** the grid of positions, **Share of Local Voice** = points in top 3 ÷ total points × 100, average rank, and the weakest direction. Save as `tracking/baselines/geo-grid-<keyword>-YYYY-MM-DD.csv` (row-major from north-west; blank = not ranked) to compare after 30/60/90 days. Expect positions far from the address to be weak: proximity is the largest factor and can't be optimized away.

### 10. Competitor radius (free, OpenStreetMap)

Optional, when the user wants a list of nearby competitors. OSM data is volunteer-made and patchy in some regions; label it `OSM`.

- Geocode the address with **Nominatim** (`https://nominatim.openstreetmap.org/search?q=<address>&format=json`) and find nearby businesses with **Overpass** (`https://overpass-api.de/api/interpreter`, query `[out:json][timeout:25];nwr["amenity"="dentist"](around:3000,LAT,LNG);out center;`). Common tags: `amenity=` restaurant/cafe/dentist/doctors/pharmacy, `office=lawyer`, `craft=plumber`/`electrician`, `shop=`…
- **Etiquette (mandatory):** send a real, identifying User-Agent (your app name plus a contact URL or email; generic library agents are refused), **at most 1 request per second**, cache results, no bulk geocoding or autocomplete, attribute "© OpenStreetMap contributors".
- Cross-platform call (if you can run Python):
  ```
  python -c "import urllib.request,urllib.parse,json,time;q=urllib.parse.quote('ADDRESS');r=urllib.request.Request('https://nominatim.openstreetmap.org/search?format=json&q='+q,headers={'User-Agent':'my-seo-audit/1.0 (contact: you@example.com)'});print(json.load(urllib.request.urlopen(r))[:1]);time.sleep(1.1)"
  ```
  On Windows PowerShell use `curl.exe` (not `curl`) if calling with curl and pass `-H "User-Agent: ..."`.
- Manual fallback: open overpass-turbo.eu or openstreetmap.org in a browser and search by hand.

---

## Output format

```
## Local SEO — <business>, <city> (YYYY-MM-DD)
Model: storefront | SAB | hybrid   Vertical: <x>   Locations: <n>
Listing completeness: GBP NN/100 (owner screenshots) · Bing <claimed/unclaimed> · Apple <claimed/unclaimed/not checked>

NAP consistency
| Source | Name | Address | Phone | Status |
|---|---|---|---|---|

Citations (market: <country>)
| Directory | Found? | NAP correct? | Action |

Reviews: <rating, count, last-90-day count, reply rate> vs top 3 competitors (source: <manual count / tool>)
Location pages: <n>, swap-test result, unique-content estimate
Local schema: <present / missing / errors> + corrected JSON-LD block
Geo-grid: SoLV NN% (<method>, <keyword>, <grid>) | not measured
AI answers: <prompt → mentioned? competitors named> | not measured

Top actions (Critical → Low), each with how to do it and how we'll know it worked
Not measured: <item → access needed>
```

## Fallbacks and "not measured"

| Missing | Do instead |
|---|---|
| No GBP access | Use the public listing or ask for dashboard screenshots; mark Insights (calls, directions) "not measured" |
| Can't fetch the site | Ask for the footer/contact page text and page source for schema |
| No web search | Ask the owner which directories and review sites they're on; give the region list above as a checklist; citations "not verified" |
| Can't run code | Manual geo-grid and manual OSM browsing; compute grid coordinates in a table |
| No location data at all | Run steps 1, 3, 6 and 7 from the website only; list the rest under "not measured" |
