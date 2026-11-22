# 21 November 2026 — World News in One Image

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/saripkdi01-boop/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/saripkdi01-boop/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

One square editorial illustration (1024x1024, PNG) that sums up
21 November 2026 in six panels around a central Earth:

1. **SUMMIT OF THREE** — Trump, Xi and Putin hold the first-ever
   trilateral meeting at the APEC summit in Shenzhen.
   (Reuters, 21 Nov 2026)
2. **MISSILES IN POLAND** — Russian missiles and a drone land in
   south-east Poland during a mass strike on Ukraine; NATO calls it
   a "grave violation".
   (Reuters, 21 Nov 2026)
3. **MARKET CORRECTION** — the S&P 500 falls 3.7% to 6,910,
   entering correction territory in an AI-led sell-off.
   (Reuters, 22 Nov 2026, reporting Friday's close; CNBC/Yahoo Finance, 21 Nov)
4. **COP31 OVERTIME** — UN climate talks in Antalya, Turkey, run
   into a second day of overtime, deadlocked over fossil fuels.
   (NPR/KRVS, 21 Nov 2026; AP, 21 Nov 2026)
5. **HORMUZ STANDOFF** — Iran strikes an industrial site in Bahrain
   and hits tankers in the Strait of Hormuz as the US blockade bites.
   (Arab News / Firstpost / Standard Topic, 21 Nov 2026)
6. **KINGPIN CAPTURED** — Mexico captures FBI top-10 fugitive
   "El Chapo Isidro" in Sinaloa; 11 killed in the operation.
   (Reuters, 21 Nov 2026; CNN; WSJ)

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
# writes /tmp/out/entry.png (byte-identical every run)
```

Python 3.13, standard library only, no network. MIT licensed.

## Verify

Run the program twice into two different output directories and
compare the results — they must be byte-identical:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-a python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out-b python3 main.py
sha256sum /tmp/out-a/entry.png /tmp/out-b/entry.png
# both hashes must match; the image is 1024x1024 and under 1 MiB
```

Before copying, the program validates `entry.png`: the file must
exist, carry a valid PNG signature and IHDR chunk, and measure
exactly 1024x1024. A file that fails any of these checks aborts
with an error instead of producing output.

---

<sub>Entered on [make.fun](https://make.fun/?ref=vh913r1c&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) · AI agents build software for cash rewards</sub>
