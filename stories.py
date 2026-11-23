# News data for Sunday 22 November 2026 — every story happened, or was
# first reported, on that day. v2.1 (HEAD 7081765) was a full date audit;
# this v3 refresh (23 Nov 20:00 WIB) re-audits it against the full-day
# round-ups (Reuters/AP/BBC) and the leaderboard, and swaps in the big
# stories v2.1 missed. Corrections found in the re-audit:
# - COP31 did NOT end with a draft to vote on: the talks COLLAPSED on
#   Sunday, EU formally objecting; first no-deal summit since 2009.
# - "Hadjar fastest lap" was WRONG: fastest lap was Liam Lawson 1:35.591.
# - Bessent "still on a military base" is a 10-20 Nov story (CNBC, 20 Nov),
#   no 22 Nov development — replaced by the Democrats' House majority.
# - Trump "Iran's terms intolerable" was said Fri 20 / Sat 21 Nov — out.
# - Iran's "missile city" dual launcher was unveiled Sat 21 Nov — out.
# - Hegseth Canada memo was reported Fri 20 Nov; Canada replied Sat — out.
# - FBI NCIC hack broke Fri 20 / Sat 21 Nov — not added.
# Swapped in (all verified 22 Nov): Benghazi Merkury sinking, Dymer
# apartment strike, 186-drone barrage context, Cikande factory fire
# (24 body bags), Korea minister resigns, Democrats 258 seats, Sudan
# Khartoum drone strikes, West Bank settler arson, Liverpool 4-0 Man
# Utd, Alcaraz wins ATP Finals (+ doubles), Miley Cyrus wedding,
# Wembanyama 50, Shuri Castle, Iowa explosives, HK record turnout.
# Written by hand in this session; no file was copied in.

DAY_TITLE = "Sunday 22 November 2026"
KICKER_LEFT = "THE WORLD IN ONE DAY"
KICKER_RIGHT = "50 STORIES \u00b7 8 REGIONS \u00b7 EVERY ONE DATED SUNDAY 22 NOVEMBER 2026"

SUBHEAD = [
    "COP31 collapses with no deal",
    "Sea drones sink Russian corvette",
    "Verstappen wins Las Vegas GP",
    "India pile up record 720/9",
]

# (big number, small label)
STATS = [
    ("3", "tankers hit off Khasab in ~15 hours"),
    ("0", "mentions of \u2018fossil fuels\u2019 in COP31\u2019s Sunday draft"),
    ("720/9", "India\u2019s record Test total in New Zealand"),
    ("$58,737", "Bitcoin, up 5.3% in 24 hours"),
    ("2", "days of overtime before COP31 collapsed"),
    ("3rd", "Las Vegas Grand Prix win for Verstappen"),
]

# (name, count, colour)
REGIONS = [
    ("EUROPE", 7, "#2456A6"),
    ("ASIA-PACIFIC", 9, "#B31B1B"),
    ("MIDDLE EAST", 7, "#B58900"),
    ("AMERICAS", 6, "#2E7D32"),
    ("AFRICA", 6, "#6A1B9A"),
    ("MARKETS", 6, "#00838F"),
    ("SPORT & CULTURE", 8, "#C75B12"),
    ("SCIENCE & HEALTH", 1, "#455A64"),
]

# Three lead stories: n, tag, place, beat, headline, dek, illustration key.
LEADS = [
    {
        "n": 1,
        "tag": "COP31: COLLAPSE",
        "place": "ANTALYA, T\u00dcRKIYE",
        "beat": "CLIMATE",
        "headline": "COP31 collapses with no deal at all",
        "dek": "EU rejects a text that never names fossil fuels; the longest "
               "summit ever ends empty. (Reuters, BBC)",
        "ill": "cop31",
    },
    {
        "n": 2,
        "tag": "HORMUZ: TANKER WAR",
        "place": "KHASAB, OMAN",
        "beat": "SECURITY",
        "headline": "Tankers burn off Khasab as attacks mount",
        "dek": "TORKEL hit off Khasab, crew evacuated; Iran claims two more "
               "tankers hit mines Sunday. (UKMTO)",
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
        "tag": "US: MIDTERMS",
        "place": "WASHINGTON",
        "beat": "POLITICS",
        "headline": "Democrats clinch biggest House majority since 1992",
        "dek": "258 seats after a North Carolina recount win. (BBC)",
        "ill": "nigeria",
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
        "headline": "Alcaraz wins first ATP Finals title",
        "dek": "Beats Zverev 6-2, 7-6(7); first Spaniard since 1998. (ATP)",
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
    (20, "BENGHAZI", "Sea drones sink Russian corvette Merkury"),
    (21, "ANTALYA", "COP31 draft drops $120bn adaptation target"),
    (22, "ANTALYA", "EU objects to COP31 text; no deal adopted"),
    (23, "KHASAB", "TORKEL hit off Khasab; crew evacuated"),
    (24, "JERUSALEM", "Israel, US agree joint plans vs Iran"),
    (25, "TEHRAN", "Araqchi says Iran wants diplomacy to end war"),
    (26, "DYMER", "Drone collapses flats; 4 killed, 14 missing"),
    (27, "GAZA CITY", "Winter weather deepens Gaza\u2019s crisis"),
    (28, "HONG KONG", "5,640 vote; record 98.79% turnout"),
    (29, "BEIJING", "China spies targeted AI chips, NYT reports"),
    (30, "DHAKA", "Violence goes on in 17 districts over Hasina"),
    (31, "KHARTOUM", "Drone strikes kill 4, damage UN building"),
    (32, "WELLINGTON", "India declare 720/9, record total in NZ"),
    (33, "WELLINGTON", "Pant 128 completes SENA centuries set"),
    (34, "WELLINGTON", "Bumrah strikes as NZ trail by 319 at tea"),
    (35, "LAS VEGAS", "Lawson sets fastest lap in Las Vegas"),
    (36, "LAS VEGAS", "Norris second, Piastri third in Vegas"),
    (37, "TURIN", "Arribage, Olivetti win ATP doubles final"),
    (38, "LIVERPOOL", "Liverpool 4-0 Man Utd in Pochettino debut"),
    (39, "JOHANNESBURG", "Mlambo-Ngcuka funeral on 28 Nov"),
    (40, "ONLINE", "Teen gamer helps FBI rescue kidnapped girl"),
    (41, "IOWA", "Army to detonate tonnes of unstable explosives"),
    (42, "LONDON", "Real people find their work cloned by AI"),
    (43, "LONDON", "Parents urged to spot online stalking signs"),
    (44, "CALIFORNIA", "Miley Cyrus marries Maxx Morando"),
    (45, "LONDON", "BBC apologises for Strictly noise disruption"),
    (46, "SEOUL", "Education minister quits over AI exam chaos"),
    (47, "SAN ANTONIO", "Wembanyama scores 50 in Spurs win"),
    (48, "RAMALLAH", "Settlers torch vehicles; Eisenkot condemns"),
    (49, "CIKANDE", "24 body bags pulled from factory fire"),
    (50, "OKINAWA", "Shuri Castle hall restored, 7 years after fire"),
]

WHY_TITLE = "WHY THE STRAIT IS BURNING"
WHY = [
    "War at sea since late February, when the US and Israel attacked Iran",
    "Three tankers hit off Khasab in 15 hours",
    "Houthis claim a hit on Saudi Arabia\u2019s Rabigh refinery",
    "Iran claims two tankers hit mines on Sunday",
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
    "Trump calls Iran\u2019s terms unacceptable \u2014 Friday 20 Nov.",
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
    ("BENGHAZI", 20.1, 32.1),
]

FOOTER_SOURCES = (
    "Every story here happened, or was first reported, on Sunday 22 November 2026 \u00b7 "
    "Sources named beside each story \u00b7 Drawn illustrations, not photographs"
)
FOOTER_MARKETS = "MARKETS (SUN LIVE): BTC $58,737 \u00b7 ETH $1,647 \u00b7 SOL $68.72"
FOOTER_TRENDING = (
    "TRENDING NOW: COP31 \u00b7 BENGHAZI \u00b7 DYMER \u00b7 VERSTAPPEN \u00b7 "
    "ALCARAZ \u00b7 BITCOIN"
)
