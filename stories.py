# News data for Sunday 22 November 2026 — every story happened, or was
# first reported, on that day. Sources verified from Reuters, AP, AFP,
# UKMTO, BBC, Guardian and Sunday round-ups on 22 Nov 2026.
# Written by hand in this session; no file was copied in.

DAY_TITLE = "Sunday 22 November 2026"
KICKER_LEFT = "THE WORLD IN ONE DAY"
KICKER_RIGHT = "50 STORIES \u00b7 8 REGIONS \u00b7 EVERY ONE DATED SUNDAY 22 NOVEMBER 2026"

SUBHEAD = [
    "COP31 draft drops fossil fuels",
    "Tanker burns at anchor off Khasab",
    "Mexico captures \u2018El Chapo Isidro\u2019",
    "M7.2 quake hits Maluku",
]

# (big number, small label)
STATS = [
    ("3", "tankers hit off Khasab in ~15 hours"),
    ("0", "mentions of \u2018fossil fuels\u2019 in COP31\u2019s final draft"),
    ("11", "killed in Mexico raid that netted \u2018El Chapo Isidro\u2019"),
    ("7.2", "magnitude of the Maluku quake, 125 km deep"),
    ("$60,200", "Bitcoin, back above $60k after $55,300 dip"),
    ("2\u20132", "Arsenal held at Newcastle; City draw 1\u20131"),
]

# (name, count, colour)
REGIONS = [
    ("EUROPE", 9, "#2456A6"),
    ("ASIA-PACIFIC", 7, "#B31B1B"),
    ("MIDDLE EAST", 5, "#B58900"),
    ("AMERICAS", 4, "#2E7D32"),
    ("AFRICA", 11, "#6A1B9A"),
    ("MARKETS", 5, "#00838F"),
    ("SPORT & CULTURE", 7, "#C75B12"),
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
        "headline": "Third tanker burns at anchor as strait attacks mount",
        "dek": "TORKEL is ablaze off Khasab after two tankers were hit in an hour "
               "on Saturday \u2014 three vessels in 15 hours, no deaths. (UKMTO, Reuters)",
        "ill": "hormuz",
    },
    {
        "n": 3,
        "tag": "BAHRAIN: ATTACK",
        "place": "MANAMA, BAHRAIN",
        "beat": "SECURITY",
        "headline": "Bahrain says Iranian attack set industrial site ablaze",
        "dek": "Air defences intercepted other incoming fire late on Saturday; "
               "Tehran says it hit US bases. No injuries reported. (Reuters)",
        "ill": "bahrain",
    },
]

# Ten illustrated grid stories.
GRID = [
    {
        "n": 4,
        "tag": "MEXICO: CARTEL",
        "place": "GUASAVE",
        "beat": "CRIME",
        "headline": "\u2018El Chapo Isidro\u2019 captured, 11 killed in raid",
        "dek": "FBI most-wanted boss Fausto Isidro Meza Flores seized. (Reuters, AP)",
        "ill": "mexico",
    },
    {
        "n": 5,
        "tag": "IRAQ: FIRE",
        "place": "BASRA",
        "beat": "DISASTER",
        "headline": "Power station fire kills 4, injures 35",
        "dek": "Blaze at the Hartha plant; PM orders a probe. (State media)",
        "ill": "iraq",
    },
    {
        "n": 6,
        "tag": "PERU: QUAKE",
        "place": "JUN\u00cdN",
        "beat": "DISASTER",
        "headline": "M6.8 quake shakes Andes, 15 injured",
        "dek": "Strong tremor hits the Jun\u00edn region; no deaths. (Reports)",
        "ill": "peru",
    },
    {
        "n": 7,
        "tag": "INDONESIA: QUAKE",
        "place": "MALUKU",
        "beat": "DISASTER",
        "headline": "M7.2 quake strikes deep under Maluku",
        "dek": "125 km deep, no tsunami threat, no damage. (Reports)",
        "ill": "maluku",
    },
    {
        "n": 8,
        "tag": "EBOLA: DRC",
        "place": "NAIROBI \u00b7 KINSHASA",
        "beat": "HEALTH",
        "headline": "Kenya clears its last Ebola patient",
        "dek": "DRC death toll passes 5,300 as Kenya discharges its final case.",
        "ill": "ebola",
    },
    {
        "n": 9,
        "tag": "INDIA: POISONING",
        "place": "MANIPUR",
        "beat": "HEALTH",
        "headline": "Toxic alcohol kills 11, 180 in hospital",
        "dek": "Chief minister confirms toll after illicit liquor poisoning.",
        "ill": "manipur",
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
        "tag": "UN: ROBOTS",
        "place": "GENEVA",
        "beat": "DIPLOMACY",
        "headline": "No treaty to ban \u2018killer robots\u2019",
        "dek": "UN talks end with no binding deal; work runs to 2028. (Reports)",
        "ill": "geneva",
    },
    {
        "n": 13,
        "tag": "TENNIS: ATP",
        "place": "TURIN",
        "beat": "SPORT",
        "headline": "Alcaraz meets Zverev in final",
        "dek": "Alcaraz fights back past Shelton; world No. 1 awaits. (Reports)",
        "ill": "atp",
    },
]

# 37 more stories, one line each: (n, place, text).
ALSO = [
    (14, "TOKYO", "Bitcoin back above $60,000 after $55,300 dip"),
    (15, "WASHINGTON", "FinCEN calls MEXC a laundering concern"),
    (16, "WASHINGTON", "Fed Dec hike now near-certain"),
    (17, "SEOUL", "SoftBank\u2019s Son weighed ~$1tn SK Hynix buyout"),
    (18, "MADRID", "Spain extends bank levy to fund \u20ac1.4bn housing"),
    (19, "OSLO", "Top court voids disputed oil licences"),
    (20, "LONDON", "Arsenal held 2-2 at Newcastle; City draw 1-1"),
    (21, "LONDON", "Leeds stun Chelsea 4-1; Bournemouth up to 4th"),
    (22, "PARIS", "France beat Argentina, reach final v South Africa"),
    (23, "CARDIFF", "Australia beat Wales in Nations Championship"),
    (24, "SYDNEY", "Smith out as Australia bowl first v South Africa"),
    (25, "KYIV", "Zelenskyy: US floated NATO-for-land deal; Russia no"),
    (26, "WARSAW", "NATO jets scramble as Russian arms land"),
    (27, "GAZA CITY", "Strike kills 3 in food vehicle; Israel: militants"),
    (28, "DOHA", "Qatar sends delegation to Tehran as tensions rise"),
    (29, "DHAKA", "90 guard platoons sent to curb arson amid clashes"),
    (30, "ABUJA", "Gunmen kill village chief and 4 in Niger State"),
    (31, "MOGADISHU", "Al-Shabaab claims mass ambush toll"),
    (32, "ADDIS ABABA", "New Tigray mayor vows vote in 6 months"),
    (33, "ACCRA", "Ghana unveils \u2018Heritage Series\u2019 banknotes"),
    (34, "NIAMEY", "Sahel states restart dialogue with West Africa"),
    (35, "S\u00c3O TOM\u00c9", "Am\u00e9rico Ramos reappointed prime minister"),
    (36, "LISBON", "Thousands march over living costs"),
    (37, "FLORIDA", "St. Johns River breaks 73-year flood record"),
    (38, "SINGAPORE", "AI-agent checks, stablecoin sandbox eyed"),
    (39, "MOUNTAIN VIEW", "Google folds Duplex into Gemini Tasks"),
    (40, "SEATTLE", "AWS launches KV-cache skill for self-hosted AI"),
    (41, "NEW YORK", "SBF gives 82-min prison interview to teen"),
    (42, "TOKYO", "Binance founder CZ talks AI in Japan interview"),
    (43, "LAGOS", "Nigeria starts building its own naval ships"),
    (44, "NAIROBI", "Kenya secures 293,600 jobs in Saudi Arabia"),
    (45, "JOHANNESBURG", "Court protest as police bar rallies"),
    (46, "LONDON", "Blair: rejoin EU only if UK innovates on tech"),
    (47, "WASHINGTON", "Hegseth memo \u2018limits\u2019 US-Canada ties"),
    (48, "LOS ANGELES", "Tyla, Tems, Kidjo lead Grammy hopes"),
    (49, "KINSHASA", "Tshisekedi enacts constitutional reform law"),
    (50, "ROME", "Malen scores four as Roma rout Parma"),
]

WHY_TITLE = "WHY THE STRAIT IS BURNING"
WHY = [
    "War at sea since late February, when the US and Israel attacked Iran",
    "A 130-day US naval blockade squeezes Iran\u2019s oil exports",
    "Iran masses 14+ tankers at Kharg Island to break the blockade",
    "Attacks at their highest since the war began: 31 in Oct, ~19 in Nov",
    "About 1 in 5 barrels of the world\u2019s oil passes through the strait",
]

DATECHECK_TITLE = "DATE CHECK \u2014 WHAT WE LEFT OUT"
DATECHECK = [
    "Russia\u2019s largest strike of the year on Ukraine \u2014 Saturday 21 Nov.",
    "Houthi missiles fired at Riyadh, three intercepted \u2014 Saturday 21 Nov.",
    "Sparta II cargo ship hit by drones in the Baltic \u2014 Saturday 21 Nov.",
    "EU and Indonesia sign trade deal in Brussels \u2014 Saturday 21 Nov.",
    "Nigeria funeral-boat toll reaches 24 \u2014 Saturday 21 Nov.",
    "Nvidia \u221214% on SEC accounting-probe report \u2014 Friday 20 Nov.",
    "S&P 500 enters correction, down 3.7% \u2014 Friday 20 Nov.",
    "Shenzhen three-leader declaration issued \u2014 Thursday 19 Nov.",
]

# Map pins: (label, longitude, latitude).
PINS = [
    ("ANTALYA", 30.7, 36.9),
    ("KHASAB", 56.2, 26.2),
    ("MANAMA", 50.6, 26.2),
    ("GUASAVE", -108.5, 25.6),
    ("BASRA", 47.8, 30.5),
    ("JUN\u00cdN", -75.2, -11.2),
    ("MALUKU", 128.2, -3.7),
    ("NAIROBI", 36.8, -1.3),
    ("MANIPUR", 93.9, 24.8),
    ("NAYPYIDAW", 96.2, 19.7),
    ("SYDNEY", 151.2, -33.9),
    ("GENEVA", 6.1, 46.2),
]

FOOTER_SOURCES = (
    "Every story here happened, or was first reported, on Sunday 22 November 2026 \u00b7 "
    "Sources named beside each story \u00b7 Drawn illustrations, not photographs"
)
FOOTER_MARKETS = "MARKETS (FRI CLOSE): BTC $60,200 \u00b7 S&P 500 6,910.39 \u00b7 OIL ~$93"
FOOTER_TRENDING = (
    "TRENDING NOW: COP31 \u00b7 HORMUZ \u00b7 EL CHAPO ISIDRO \u00b7 ATP FINALS \u00b7 "
    "BITCOIN \u00b7 MALUKU QUAKE"
)
