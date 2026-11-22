# News data for Sunday 22 November 2026 — every story happened, or was
# first reported, on that day. Revised in this session after a full date
# audit: v1 carried ~30 stories from 19-21 Nov (El Chapo capture, Bahrain
# strike, Maluku quake, Basra fire, Peru quake, Ebola, Manipur, Geneva
# robots, FinCEN, Fed, SoftBank, Saturday sport) — all replaced below
# with stories verified as Sunday 22 Nov 2026 (UTC) from Reuters, AP,
# BBC, Al Jazeera, NYT, Guardian, Cricbuzz, CoinGecko and UKMTO.
# Micro-fix in a later session: F1 podium corrected (Norris 2nd, Piastri
# 3rd, Antonelli 4th — RacingNews365/f1headline/OneRacing); the
# Smith/Khawaja Sydney items turned out to be January 2023, replaced
# with verified Wellington Test stories from Sunday 22 Nov 2026
# (myKhel bulletin, IANS, ANI).
# Written by hand in this session; no file was copied in.

DAY_TITLE = "Sunday 22 November 2026"
KICKER_LEFT = "THE WORLD IN ONE DAY"
KICKER_RIGHT = "50 STORIES \u00b7 8 REGIONS \u00b7 EVERY ONE DATED SUNDAY 22 NOVEMBER 2026"

SUBHEAD = [
    "COP31 draft drops fossil fuels",
    "Tanker burns off Khasab",
    "Verstappen wins Las Vegas GP",
    "India pile up record 720/9",
]

# (big number, small label)
STATS = [
    ("3", "tankers hit off Khasab in ~15 hours"),
    ("0", "mentions of \u2018fossil fuels\u2019 in COP31\u2019s Sunday draft"),
    ("720/9", "India\u2019s record Test total in New Zealand"),
    ("$58,737", "Bitcoin, up 5.3% in 24 hours"),
    ("2", "days into overtime as COP31 hunts a deal"),
    ("3rd", "Las Vegas Grand Prix win for Verstappen"),
]

# (name, count, colour)
REGIONS = [
    ("EUROPE", 7, "#2456A6"),
    ("ASIA-PACIFIC", 7, "#B31B1B"),
    ("MIDDLE EAST", 6, "#B58900"),
    ("AMERICAS", 4, "#2E7D32"),
    ("AFRICA", 4, "#6A1B9A"),
    ("MARKETS", 7, "#00838F"),
    ("SPORT & CULTURE", 13, "#C75B12"),
    ("SCIENCE & HEALTH", 2, "#455A64"),
]

# Three lead stories: n, tag, place, beat, headline, dek, illustration key.
LEADS = [
    {
        "n": 1,
        "tag": "COP31: NO FOSSIL FUELS",
        "place": "ANTALYA, T\u00dcRKIYE",
        "beat": "CLIMATE",
        "headline": "COP31 final draft drops fossil fuels entirely",
        "dek": "A text released at 3 a.m. on Sunday never names coal, oil or gas in "
               "10 pages; a 9 a.m. plenary decides its fate. (AP, AFP)",
        "ill": "cop31",
    },
    {
        "n": 2,
        "tag": "HORMUZ: TANKER WAR",
        "place": "KHASAB, OMAN",
        "beat": "SECURITY",
        "headline": "Tanker burns at anchor as strait attacks mount",
        "dek": "TORKEL burns at anchor off Khasab, a Sunday warning says; two "
               "tankers were hit on Saturday. (UKMTO)",
        "ill": "hormuz",
    },
    {
        "n": 3,
        "tag": "F1: LAS VEGAS",
        "place": "LAS VEGAS",
        "beat": "SPORT",
        "headline": "Verstappen wins Las Vegas Grand Prix",
        "dek": "Third win on the Strip from pole; Norris second, Piastri third. "
               "(Reports)",
        "ill": "vegas",
    },
]

# Ten illustrated grid stories.
GRID = [
    {
        "n": 4,
        "tag": "SOUTH AFRICA: MOURNING",
        "place": "JOHANNESBURG",
        "beat": "POLITICS",
        "headline": "South Africa mourns Mlambo-Ngcuka",
        "dek": "Flags half-mast; prayer service for the ex-deputy president, 71.",
        "ill": "mourning",
    },
    {
        "n": 5,
        "tag": "US: IRAN FEARS",
        "place": "WASHINGTON",
        "beat": "POLITICS",
        "headline": "Treasury chief still on military base",
        "dek": "Bessent still lives on a military base over Iran fears. (Al Jazeera)",
        "ill": "bessent",
    },
    {
        "n": 6,
        "tag": "SUDAN: DARFUR",
        "place": "DARFUR",
        "beat": "CRISIS",
        "headline": "Darfur families face harsh winter",
        "dek": "Winter nears as aid cuts bite; crisis set to worsen. (Al Jazeera)",
        "ill": "darfur",
    },
    {
        "n": 7,
        "tag": "GAZA: PROTEST",
        "place": "GAZA CITY",
        "beat": "CONFLICT",
        "headline": "Displaced Gazans protest as strikes go on",
        "dek": "Protest as Israeli forces keep destroying homes, a mayor says. "
               "(Al Jazeera)",
        "ill": "gaza",
    },
    {
        "n": 8,
        "tag": "NIGERIA: YOUTH",
        "place": "ABUJA",
        "beat": "POLITICS",
        "headline": "Nigeria\u2019s youth shun the ballot box",
        "dek": "Fewer young Nigerians registered to vote than in 2023. (BBC)",
        "ill": "nigeria",
    },
    {
        "n": 9,
        "tag": "TAIWAN: COMEDY",
        "place": "TAIPEI",
        "beat": "CULTURE",
        "headline": "Comic who mocks Xi draws sellout crowds",
        "dek": "Huang Yi-hao survived a car crash meant to silence him. (NYT)",
        "ill": "taiwan",
    },
    {
        "n": 10,
        "tag": "MYANMAR: ASEAN",
        "place": "NAYPYIDAW",
        "beat": "DIPLOMACY",
        "headline": "Junta calls ASEAN ruling \u2018unfair\u2019",
        "dek": "Army-backed government protests denied summit seats. (Reuters)",
        "ill": "myanmar",
    },
    {
        "n": 11,
        "tag": "AUKUS: SUBS",
        "place": "SYDNEY",
        "beat": "DEFENCE",
        "headline": "Australia hits back at US budget office",
        "dek": "Marles rejects a CBO claim the pact cuts US subs. (Reuters)",
        "ill": "aukus",
    },
    {
        "n": 12,
        "tag": "UKRAINE: NATO",
        "place": "KYIV",
        "beat": "DIPLOMACY",
        "headline": "Zelenskyy wants NATO pledges in writing",
        "dek": "President demands documented security guarantees as talks grind on. "
               "(Reports)",
        "ill": "zelenskyy",
    },
    {
        "n": 13,
        "tag": "TENNIS: ATP",
        "place": "TURIN",
        "beat": "SPORT",
        "headline": "Alcaraz meets Zverev in final",
        "dek": "Singles final 18:00 CET; doubles final at 15:00 CET. (Reports)",
        "ill": "atp",
    },
]

# 37 more stories, one line each: (n, place, text).
ALSO = [
    (14, "TOKYO", "Bitcoin $58,737, up 5.3% in 24 hours"),
    (15, "NEW YORK", "Ethereum $1,647, up 5.6% in 24 hours"),
    (16, "SINGAPORE", "BNB $537, up 4.9% in 24 hours"),
    (17, "NEW YORK", "Solana $68.72, up 5.1% in 24 hours"),
    (18, "LONDON", "XRP $0.91, up 4.6% in 24 hours"),
    (19, "NEW YORK", "Dogecoin $0.054, up 4.3% in 24 hours"),
    (20, "TOKYO", "Bitcoin opened Sunday above $60,000"),
    (21, "ANTALYA", "Kurum tables last-minute COP31 proposal"),
    (22, "ANTALYA", "COP31 enters second day of overtime"),
    (23, "KHASAB", "TORKEL ablaze at anchor, 26.39N 56.31E"),
    (24, "RIYADH", "Arab states condemn Iran\u2019s Bahrain strikes"),
    (25, "TEHRAN", "Araqchi says Iran wants diplomacy to end war"),
    (26, "WASHINGTON", "Trump calls Iran\u2019s terms intolerable"),
    (27, "GAZA CITY", "Winter weather deepens Gaza\u2019s crisis"),
    (28, "HONG KONG", "5,700 voters elect Election Committee"),
    (29, "BEIJING", "China spies targeted AI chips, NYT reports"),
    (30, "DHAKA", "Deadly protests erupt over exiled Hasina"),
    (31, "DHAKA", "90 guard platoons sent to curb arson"),
    (32, "WELLINGTON", "India declare 720/9, record total in NZ"),
    (33, "WELLINGTON", "Pant 128 completes SENA centuries set"),
    (34, "WELLINGTON", "Bumrah strikes as NZ trail by 319 at tea"),
    (35, "LAS VEGAS", "Hadjar sets fastest lap in Las Vegas"),
    (36, "LAS VEGAS", "Norris second, Piastri third in Vegas"),
    (37, "TURIN", "ATP doubles final at 15:00 CET"),
    (38, "BRIGHTON", "Brighton play on Sunday, chasing Arsenal"),
    (39, "JOHANNESBURG", "Mlambo-Ngcuka funeral on 28 Nov"),
    (40, "ONLINE", "Teen gamer helps FBI rescue kidnapped girl"),
    (41, "SEATTLE", "State suspends gun background-check system"),
    (42, "LONDON", "Real people find their work cloned by AI"),
    (43, "LONDON", "Parents urged to spot online stalking signs"),
    (44, "LONDON", "Coughlan drama will leave viewers uneasy"),
    (45, "LONDON", "BBC apologises for Strictly noise disruption"),
    (46, "NEW YORK", "Mahjong rivalry stirs cultural row"),
    (47, "LONDON", "Sunday papers hail Catherine\u2019s cancer film"),
    (48, "LONDON", "Service stations become destinations"),
    (49, "LONDON", "Employers urged to give interview feedback"),
    (50, "SOFIA", "Romanian driver set for release after pile-up"),
]

WHY_TITLE = "WHY THE STRAIT IS BURNING"
WHY = [
    "War at sea since late February, when the US and Israel attacked Iran",
    "Three tankers hit off Khasab in 15 hours",
    "Houthi strikes keep Saudi Arabia on edge",
    "Bahrain says Iranian fire hit an industrial site",
    "About 1 in 5 barrels of the world\u2019s oil passes through the strait",
]

DATECHECK_TITLE = "DATE CHECK \u2014 WHAT WE LEFT OUT"
DATECHECK = [
    "\u2018El Chapo Isidro\u2019 captured in Mexico \u2014 Saturday 21 Nov.",
    "Bahrain says Iranian attack hit industrial site \u2014 Saturday 21 Nov.",
    "M7.2 Maluku quake (later revised to 6.9) \u2014 Saturday 21 Nov.",
    "EU and Indonesia sign trade deal in Brussels \u2014 Saturday 21 Nov.",
    "Sparta II cargo ship hit by drones in the Baltic \u2014 Saturday 21 Nov.",
    "Nigeria funeral-boat toll reaches 24 \u2014 Saturday 21 Nov.",
    "S&P 500 enters correction, down 3.7% \u2014 Friday 20 Nov.",
    "Nvidia \u221214% on SEC accounting-probe report \u2014 Friday 20 Nov.",
]

# Map pins: (label, longitude, latitude).
PINS = [
    ("ANTALYA", 30.7, 36.9),
    ("KHASAB", 56.2, 26.2),
    ("LAS VEGAS", -115.1, 36.2),
    ("JOHANNESBURG", 28.0, -26.2),
    ("WASHINGTON", -77.0, 38.9),
    ("DARFUR", 25.4, 13.6),
    ("GAZA CITY", 34.5, 31.5),
    ("ABUJA", 7.5, 9.1),
    ("TAIPEI", 121.6, 25.0),
    ("NAYPYIDAW", 96.2, 19.7),
    ("SYDNEY", 151.2, -33.9),
    ("KYIV", 30.5, 50.4),
    ("TURIN", 7.7, 45.1),
    ("WELLINGTON", 174.8, -41.3),
]

FOOTER_SOURCES = (
    "Every story here happened, or was first reported, on Sunday 22 November 2026 \u00b7 "
    "Sources named beside each story \u00b7 Drawn illustrations, not photographs"
)
FOOTER_MARKETS = "MARKETS (SUN LIVE): BTC $58,737 \u00b7 ETH $1,647 \u00b7 SOL $68.72"
FOOTER_TRENDING = (
    "TRENDING NOW: COP31 \u00b7 HORMUZ \u00b7 VERSTAPPEN \u00b7 ATP FINALS \u00b7 "
    "BITCOIN \u00b7 PANT"
)
