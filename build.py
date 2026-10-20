"""Builds the project cards on index.html and one subpage per project in projects/.

Edit the PROJECTS list below, then run:  python3 build.py
"""
import html
import re
from pathlib import Path

ROOT = Path(__file__).parent

PROJECTS = [
    {
        "slug": "gb-dayahead-forecast",
        "title": "GB Day-Ahead Price Forecasting",
        "year": "2026",
        "image": "dayahead-live.jpg",
        "position": "center top",
        "detail_image": "dayahead-chart.jpg",
        "detail_natural": True,
        "alt": "Live GB day-ahead forecast page with hourly prices and uncertainty band",
        "card": "Online ensemble of 13 models, retrained daily and combined with Bernstein Online Aggregation. "
                "21 % lower MAE than the LEAR benchmark over 2024–2026. In a day-ahead battery backtest it "
                "captures 93.7 % of the perfect-foresight revenue in 2026 (93.1 % in 2025), against 90.4 % for LEAR.",
        "summary": "A continually retrained forecaster for the 24 hourly prices of the GB day-ahead auction, "
                   "evaluated the way a trading desk would use it.",
        "tags": ["Forecasting", "Online Learning", "BESS", "PyTorch"],
        "links": [("Live Forecast", "https://timlouiswilken.github.io/gb-dayahead-forecast/"),
                  ("Code", "https://github.com/TimLouisWilken/gb-dayahead-research")],
        "cta": ("Open the live forecast", "https://timlouiswilken.github.io/gb-dayahead-forecast/"),
        "gallery": [("dayahead.png", "Probabilistic forecast with 50, 80 and 90 % intervals, January 2025.")],
        "body": [
            "Electricity prices drift between regimes, from the 2021–22 gas crisis to the normalisation since "
            "2024, so a model trained once slowly goes stale. Here every model keeps learning: each morning before "
            "the auction it forecasts the next day, and once the prices are known it learns from them.",
            "Thirteen models from different families run side by side (LSTM, Transformer, TCN, DNN, gradient "
            "boosting, random forests, LEAR, a merit-order model and the Chronos foundation model). Bernstein "
            "Online Aggregation combines them per hour and updates the weights every day.",
        ],
        "highlights": [
            "Out of sample from January 2024 to September 2026: MAE of 8.73 EUR/MWh, 21 % below the LEAR "
            "benchmark (11.07) and better than every single model (Diebold–Mariano p < 0.001).",
            "Continual learning is the largest single gain: an online random forest reaches 11.58 against 17.12 "
            "for the same model trained once.",
            "Probabilistic forecasts via quantile regression averaging with adaptive conformal correction; the "
            "intervals hit their nominal coverage within about one percentage point.",
            "Battery backtest (50 MW / 100 MWh, 85 % round trip, daily LP on the forecast, settled at actual "
            "prices): 93.1 % of the perfect-foresight revenue in 2025 and 93.7 % in 2026, against 90 % for LEAR "
            "and 75 % for using yesterday's prices.",
            "Runs live: every morning before gate closure a GitHub Actions job publishes the next day's forecast. "
            "The live system uses a six-member selection, which has a lower MAE than the full ensemble "
            "(8.56 vs 8.73 EUR/MWh) but captures slightly less battery revenue (93.6 % vs 93.7 % in 2026).",
        ],
    },
    {
        "slug": "bess-trading-simulator",
        "title": "BESS Trading Simulator",
        "year": "2026",
        "image": "bess-simulator-desk.jpg",
        "position": "left top",
        "alt": "Day-ahead auction screen of the BESS Trading Simulator with hourly price forecast",
        "card": "Interactive web app for learning GB battery trading across the day-ahead, intraday and imbalance "
                "markets on live Elexon BMRS data, with balancing-mechanism acceptances and a P&L dashboard. "
                "Built with a fellow student.",
        "summary": "An interactive simulator that walks through the decisions a battery trader makes: when to "
                   "charge, discharge or wait across the GB markets.",
        "tags": ["Market Design", "Trading", "React", "TypeScript"],
        "links": [("Live Demo", "https://bess-trading-simulator.com"),
                  ("Code", "https://github.com/bess-trading-simulator/bess-trading-simulator")],
        "cta": ("Open the simulator", "https://bess-trading-simulator.com"),
        "gallery": [("bess-simulator-setup.jpg", "Sandbox setup: live Elexon data or illustrative scenarios such as a storm day or a cold snap.")],
        "body": [
            "We built the simulator, a fellow student and I, to understand how GB battery trading works in "
            "practice. It is not a market replica, but the reasoning behind each trade is the same: read the "
            "price signals, manage the state of charge, schedule and review.",
        ],
        "highlights": [
            "Live Elexon BMRS data: day-ahead prices, system prices, NIV and demand, wind and solar forecasts.",
            "Day-ahead auction with a 48-period schedule builder, gate closure at 09:20 UK time.",
            "Intraday re-optimisation as forecasts update, and imbalance trading with NIV-based cash-out.",
            "Balancing-mechanism acceptances with merit-based probabilities and a P&L dashboard.",
            "Guided lessons from arbitrage to market context, and a decision coach that adapts to price, "
            "battery state and forecast.",
        ],
    },
    {
        "slug": "german-spread-analysis",
        "title": "German Day-Ahead Spread Analysis",
        "year": "2026",
        "image": "spread.png",
        "contain": True,
        "alt": "German day-ahead high-low spread versus price level, 2018 to 2026",
        "card": "Extends FlexPower's analysis \"Die große Abkopplung\" to October 2026. Since 2024 the daily "
                "high-low spread has decoupled from the price level in spring and summer, while winter is "
                "unchanged. The annual mean spread rose from 111 to 159 EUR/MWh.",
        "summary": "Is the daily price spread, the core of battery arbitrage, still tied to the price level? "
                   "A reconstruction of FlexPower's blog analysis, extended to October 2026.",
        "tags": ["Market Analysis", "Germany", "BESS Spreads", "Python"],
        "links": [("Code", "https://github.com/TimLouisWilken/de-price-decoupling")],
        "gallery": [("spread-heatmap.png", "Monthly high-low spread and spread-to-price ratio, 2018 to 2026."),
                    ("spread-hourly.png", "Average daily price profile in winter and summer: the solar midday trough drives the spread.")],
        "body": [
            "Until 2023 the German day-ahead price level and its daily high-low spread moved together, because "
            "gas set both. Since 2024 they have come apart: solar pushes midday prices down while the evening "
            "ramp is still set by gas. The analysis rebuilds the chart with Energy-Charts/SMARD data from 2018 "
            "to October 2026 and splits it by season.",
        ],
        "highlights": [
            "In winter the spread is still about 0.8 times the price level, as before 2023.",
            "In spring and summer it has been 1.6 to 1.8 times the price level since 2024.",
            "The annual mean spread rose from 111 (2024) to 124 (2025) and 159 EUR/MWh (2026 to date), while "
            "the price level rose only moderately.",
            "The drop after June 2024 was seasonal; the rise of summer spreads from year to year is structural.",
        ],
    },
    {
        "slug": "masters-thesis",
        "title": "Master's Thesis: GPU Jobs on a Non-Firm Grid Connection",
        "year": "2026",
        "image": "thesis.png",
        "contain": True,
        "alt": "ECMWF ensemble of the curtailable grid import limit over one week",
        "card": "Which jobs can an AI data centre firmly commit to when the grid may curtail its supply? A two-stage "
                "stochastic MILP with real ECMWF weather ensembles and a joint chance constraint. It meets 6–21 "
                "percentage points more deadlines than a greedy scheduler.",
        "summary": "Deadline Commitments for GPU Jobs under a Forecast-Uncertain Non-Firm Grid Connection. "
                   "M.Sc. thesis for UCL, written at the University of Oxford.",
        "tags": ["Stochastic MILP", "Chance Constraints", "Data Centres", "HiGHS / Gurobi"],
        "links": [],
        "body": [
            "Data centres in Great Britain can connect to the grid earlier if they accept a non-firm import limit. "
            "That limit can be curtailed and is known at planning time only through a weather ensemble. This "
            "creates a scheduling problem: which GPU jobs can receive a deadline commitment when supply is "
            "uncertain?",
            "The thesis develops a two-stage admission program with real ECMWF ensembles, per-job suspension, a "
            "graded lateness penalty and a joint chance constraint. It evaluates one GB grid supply point in a "
            "deep winter scarcity week with published GPU cluster traces.",
            "Supervised by Prof. Thomas Morstyn and Yihong Zhou (University of Oxford) and Akylas Stratigakos (UCL).",
        ],
        "highlights": [
            "Against a greedy, deadline-blind scheduler, the admission system computes less raw work but meets "
            "6 to 21 percentage points more deadlines as scarcity deepens.",
            "Per-job suspension raises the committed work at α = 0 by a factor of 5.7.",
            "The chance constraint adds committed work only when the import limit binds; its gain is 3.7 to "
            "9.0 % in twenty constructed instances.",
            "A certified quantile rule solves scalar-ordered cases within two minutes, where the joint program "
            "reaches its time limit.",
            "Modelled in Python with PuLP, solved with HiGHS and Gurobi.",
        ],
    },
    {
        "slug": "rolls-royce-fission-project",
        "title": "Rolls-Royce: High-Temperature Gas Reactor Design",
        "year": "2026",
        "image": "rolls-royce.jpg",
        "position": "center 75%",
        "alt": "Winning team at the USI Novel Nuclear Fission Project Finals with Rolls-Royce",
        "card": "Systems Design Engineer in a UCL team that modelled an HTGR cogeneration plant with hydrogen "
                "production and thermal storage, dispatched hourly against the UK grid. Our team won the Novel "
                "Nuclear Fission Project Finals, run by Rolls-Royce and The University Sustainability Initiative.",
        "summary": "Winning team of the Novel Nuclear Fission Project Finals, hosted by The University "
                   "Sustainability Initiative with Rolls-Royce at Imperial College London.",
        "tags": ["Systems Engineering", "Nuclear", "Hydrogen", "Dispatch Modelling", "Winning Team"],
        "links": [("LinkedIn Post", "https://www.linkedin.com/posts/the-usi-recently-hosted-its-novel-nuclear-ugcPost-7441210424911499264-hZZq/")],
        "gallery": [("rr-system.png", "System layout: the helium-cooled HTGR drives a recuperated Brayton cycle; high-grade heat feeds thermal storage and a solid-oxide electrolyser for hydrogen."),
                    ("rr-daily-pattern.png", "Average daily operating pattern: electricity goes to the grid in the evening peak, overnight surplus goes into hydrogen."),
                    ("rr-revenue-netload.png", "Daily revenue against daily mean net load, 2018 to 2024: the hockey stick of scarcity pricing."),
                    ("rr-monthly-revenue.png", "Monthly revenue split between electricity and hydrogen over seven years of NESO data."),
                    ("rr-mc-cdf.png", "Monte Carlo (n = 5,000): net CO2 avoided per year, with P10, median and P90.")],
        "body": [
            "The challenge: use nuclear fission to reduce CO2 emissions while reducing reliance on water cooling. "
            "More than 120 students from Oxford, Imperial, UCL and Cambridge competed through several stages.",
            "Our four-person UCL team designed and modelled a 200 MWth high-temperature gas-cooled reactor (HTGR) "
            "with a cogeneration secondary system: a recuperated helium Brayton cycle, solid-oxide electrolysis "
            "for hydrogen, and thermal energy storage. The plant is dispatched every half hour against real "
            "NESO demand, wind, solar and grid carbon-intensity data, switching between grid export and "
            "hydrogen production depending on the system's scarcity. I was the team's Systems Design Engineer.",
        ],
        "highlights": [
            "First place at the finals at Imperial College London, against teams from Oxford, Imperial, UCL and "
            "Cambridge.",
            "Time-resolved model of reactor, Brayton cycle (50.7 % thermal efficiency at the optimised pressure "
            "ratio), electrolyser and storage, with CO2 accounting built into the dispatch.",
            "Economic dispatch over 122,736 half-hour steps (2018 to 2024): net load from NESO data drives a "
            "scarcity price, and a hydrogen strike price decides between exporting electricity and making hydrogen.",
            "Monte Carlo analysis with 5,000 runs: median net CO2 avoidance of about 76,000 t per year (P10 "
            "57,000 t) and mean gross revenue of about 62 million GBP per year.",
        ],
    },
    {
        "slug": "bachelors-thesis",
        "title": "Bachelor's Thesis: BESS Connection Requests in Germany",
        "year": "TUM · 2025",
        "image": "bachelor-spread.png",
        "contain": True,
        "alt": "Daily average price and daily spread in the German day-ahead market, 2020 to 2025",
        "card": "What drives 340 GW of battery grid-connection requests? Analysis of 2024 day-ahead price "
                "volatility and battery cost degression, quantifying arbitrage revenues and grid implications. "
                "Graded 1.3 at TUM.",
        "summary": "Rising Connection Requests for Battery Energy Storage Systems in Germany: Drivers and "
                   "Implications. B.Sc. thesis at the Technical University of Munich, graded 1.3.",
        "tags": ["BESS", "Grid Connections", "Arbitrage"],
        "links": [],
        "gallery": [("bachelor-battery-cost.png", "Lithium-ion battery pack prices 2013 to 2024: cell price and additional pack cost (data: BloombergNEF).")],
        "body": [
            "By March 2025, battery storage projects had requested 340 GW of grid connections in Germany. The "
            "thesis examines what drives this demand and what it means for the grid.",
        ],
        "highlights": [
            "Revenue side: arbitrage trading dominates. Day-ahead prices in 2024, the year most requests were "
            "filed, show clearly higher volatility; ancillary services play a subordinate role.",
            "Cost side: strong cost degression, especially in 2024. Overall the economics of BESS improved "
            "significantly.",
            "Because of how transmission system operators allocate connections, the 340 GW figure is hard to "
            "interpret as real demand.",
            "BESS matter for the future grid, but in excessive numbers they can stress it, above all within a "
            "single bidding zone. Some simulation approaches do not reflect how batteries are actually traded.",
        ],
    },
    {
        "slug": "australian-electricity-market",
        "title": "Australian Electricity-Market Dynamics",
        "year": "2026",
        "image": "australia-intraday.png",
        "contain": True,
        "alt": "Average intraday battery dispatch and South Australian price",
        "card": "Does a growing battery fleet dampen wholesale prices? A three-regime threshold vector "
                "error-correction model of South Australian and Victorian prices, 2023–2025.",
        "summary": "Battery storage and electricity price convergence: a threshold vector error-correction "
                   "analysis of the South Australian and Victorian market, 2023–2025.",
        "tags": ["Econometrics", "Time Series", "statsmodels"],
        "links": [("Code", "https://github.com/TimLouisWilken/analysis-of-the-australian-electricity-market")],
        "gallery": [("australia.png", "South Australian wholesale price with the three TVECM regimes."),
                    ("australia-capacity.png", "South Australian battery fleet capacity, 2023 to 2025.")],
        "body": [
            "South Australia runs on about 90 % wind and solar, and its battery fleet grew 4.7-fold in three "
            "years. The question is causal: do batteries measurably dampen wholesale prices, and does the effect "
            "depend on the price regime?",
            "The hard part is simultaneity. Batteries discharge because prices are already spiking, so plain OLS "
            "even shows a positive effect on prices. Six identification strategies, from lagged regressors to "
            "2SLS with a commissioning instrument, all point the same way once this is addressed: batteries "
            "prevent spikes from forming rather than blunting them once they have started.",
        ],
        "highlights": [
            "52,608 half-hourly observations, January 2023 to December 2025.",
            "Johansen cointegration and a Hansen–Seo threshold test select a three-regime TVECM (p = 0.030).",
            "Estimated consumer welfare gain of 10.8 million AUD per year in the counterfactual.",
            "SA–VIC price correlation rose from 0.38 (2023) to 0.80 (2025); the spike regime fell from 9.4 % to "
            "5.0 % of intervals.",
        ],
    },
    {
        "slug": "uk-onshore-wind-siting",
        "title": "UK Onshore-Wind Siting",
        "year": "2026",
        "image": "wind-scotland.png",
        "contain": True,
        "alt": "Recommended onshore wind sites in Scotland and Northern Ireland",
        "card": "GIS multi-criteria (AHP) suitability and financial-viability analysis siting 20 strategic "
                "0.5 GW onshore wind clusters across the UK.",
        "summary": "Spatial and financial assessment of 10 GW of new onshore wind capacity in the UK.",
        "tags": ["GIS", "Wind", "GeoPandas", "Project Finance"],
        "links": [("Code", "https://github.com/TimLouisWilken/Spatial-Assessment-of-Onshore-Wind-Capacity-in-UK")],
        "gallery": [("wind.png", "All 20 recommended 0.5 GW sites."),
                    ("wind-sites.jpg", "Close-ups of the top sites with optimised turbine positions (red).")],
        "body": [
            "Where should 20 wind farms of 0.5 GW each go, and do they pay off? All inputs are harmonised on a "
            "66.7 m grid, infeasible areas are excluded, and every remaining pixel is scored against seven "
            "criteria with Analytic Hierarchy Process weights. A geometry-based search then places 81 turbines "
            "per site with wake spacing, and a discounted cash-flow model tests each site.",
        ],
        "highlights": [
            "20 sites for 10 GW: 17 in Scotland, 2 in Wales, 1 in Northern Ireland, none in England under the "
            "constraints.",
            "Wind speed and grid congestion dominate the AHP weights (28.7 % each); consistency ratio 0.003.",
            "Portfolio IRR of about 12–13 % against a 5.8 % hurdle rate, LCOE of 44–46 GBP/MWh.",
            "The programme depends on long-distance transmission to reach demand in the south.",
        ],
    },
    {
        "slug": "saudi-vision-2030",
        "title": "Saudi Vision 2030: Can Renewables Reach 50 %?",
        "year": "2026",
        "image": "saudi-3.png",
        "contain": True,
        "alt": "Monte Carlo paths of PV and wind capacity in Saudi Arabia to 2030",
        "card": "Econometric demand model and Monte Carlo simulation of grid and capacity expansion. Even in the "
                "best case the renewable share reaches only 31–36 % by 2030, against a target of 50 %.",
        "summary": "Is Saudi Arabia's target of a 50 % renewable share in electricity by 2030 achievable?",
        "tags": ["Monte Carlo", "Econometrics", "Energy Policy", "Python"],
        "links": [("Code", "https://github.com/TimLouisWilken/Evaluation-of-Saudi-Vision-2030")],
        "gallery": [("saudi-1.png", "Simulated 2030 electricity demand (median about 567 TWh)."),
                    ("saudi-2.png", "Grid capacity available for renewables, median path with 80 % interval.")],
        "body": [
            "The analysis projects 2030 electricity demand with an econometric model and simulates the expansion "
            "of grid integration capacity and of PV and wind capacity as stochastic paths. Combining them gives a "
            "distribution of the renewable share in 2030.",
        ],
        "highlights": [
            "Simulated 2030 demand: median about 567 TWh, 90 % range about 527 to 609 TWh.",
            "Renewable share in 2030 of only 31.0 to 35.8 %.",
            "Even with 40 % annual tender growth and wind prioritised, the 50 % target is missed because of "
            "physical lead times and grid bottlenecks.",
        ],
    },
    {
        "slug": "open-roof-measurement",
        "title": "Open Roof Measurement",
        "year": "2026",
        "image": "openroof-s1.jpg",
        "position": "center center",
        "alt": "Detected roof outline, ridge and PV panels on an aerial image",
        "card": "Roof renovation and insulation are a big lever for the energy transition in buildings, but getting "
                "a quote starts with measuring the roof. This pipeline measures it from a street address and open "
                "geodata, with a web tool for a human to check the result.",
        "summary": "Measuring a roof from an address and open geodata, so that owners and roofers can get to a "
                   "quote without a site visit.",
        "tags": ["Computer Vision", "Buildings", "Energy Efficiency", "FastAPI", "Next.js"],
        "links": [("Code", "https://github.com/TimLouisWilken/open-roof-measure")],
        "gallery": [("openroof.jpg", "Terraced house, the best case: ridge (red), eaves (green) and outline (cyan) within 7 % of the building plan."),
                    ("openroof-s3.jpg", "Detached house, the worst case: the wireframe model assumes a half-hipped roof and overestimates the ridge by 16 %.")],
        "body": [
            "Buildings cause a large share of final energy demand, and the roof is where much of a house's heat "
            "is lost. Insulating it during a renovation is one of the most effective measures, and it is also the "
            "moment to add solar. In practice the process often stalls at the first step: to get a quote, someone "
            "has to measure the roof, which means a site visit, a drone survey or an estimate from the ground.",
            "This project asks whether that first step can be automated. From a street address alone, the "
            "pipeline estimates the roof geometry using only open public data from North Rhine-Westphalia: 10 cm "
            "aerial images, a 0.5 m elevation model and the cadastre. No paid APIs. A web tool lets a person check "
            "and correct the result before it goes to a roofer.",
        ],
        "highlights": [
            "SAM segmentation for the roof mask, RANSAC plane fitting for pitch and area, and RoofMapNet for "
            "ridges, eaves and verges.",
            "SegFormer fine-tuned on the RID2 dataset (3,813 training images) to detect PV panels, dormers, "
            "skylights and chimneys.",
            "Four-tier building detection with fallbacks for shadows, trees and shared walls.",
            "Validated on three houses against their building plans. On a compact terraced house all roof-edge "
            "metrics are within 7 % of the plan.",
        ],
        "caveats": [
            "There is no real training data for German houses. RoofMapNet was pretrained on 9,576 buildings from "
            "China, New Zealand, the US and Austria; German pitched gable roofs, terraced and semi-detached houses "
            "and half-hipped variants are absent. On the detached test house this shows as a 16 % ridge "
            "overestimate and a 15 % verge underestimate, a textbook case of distribution shift.",
            "On the semi-detached house the segmentation pulls in part of the neighbour's roof, so the area is "
            "overestimated and the pitch comes out 27 % too high.",
            "Validation covers only three houses, and the superstructure model was fine-tuned for 14 epochs on a "
            "free Colab GPU. The numbers show where the approach works, not that it is production-ready.",
        ],
    },
]

ICON_GH = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 .5a11.5 11.5 0 0 0-3.64 '
           '22.41c.58.11.79-.25.79-.56v-2c-3.2.7-3.88-1.37-3.88-1.37-.53-1.33-1.28-1.69-1.28-1.69-1.05-.71.08-.7.08-.7 '
           '1.16.08 1.77 1.19 1.77 1.19 1.03 1.77 2.7 1.26 3.36.96.1-.75.4-1.26.73-1.55-2.55-.29-5.24-1.28-5.24-5.68 '
           '0-1.26.45-2.28 1.19-3.09-.12-.29-.52-1.46.11-3.05 0 0 .97-.31 3.17 1.18a10.9 10.9 0 0 1 5.77 0c2.2-1.49 '
           '3.17-1.18 3.17-1.18.63 1.59.23 2.76.11 3.05.74.81 1.19 1.83 1.19 3.09 0 4.41-2.69 5.38-5.26 5.67.41.36.78 '
           '1.06.78 2.14v3.17c0 .31.21.68.8.56A11.5 11.5 0 0 0 12 .5Z"/></svg>')
ICON_LI = ('<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33'
           '-.03-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 '
           '4.27 2.37 4.27 5.45v6.29ZM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12ZM7.12 20.45H3.56V9h3.56v11'
           '.45ZM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 '
           '23.2 0 22.22 0Z"/></svg>')

e = html.escape


def cover(p, prefix, extra_class="", show_year=False, detail=False):
    year = f'<span class="year">{e(p["year"])}</span>' if show_year else ""
    image = p.get("detail_image", p.get("image")) if detail else p.get("image")
    if detail and p.get("detail_natural"):
        extra_class += " natural"
    if "metric" in p:
        big, small = p["metric"]
        return (f'<div class="cover metric {extra_class}"><span class="big">{e(big)}</span>'
                f'<span class="small">{e(small)}</span>{year}</div>')
    cls = "" if p.get("contain") else ' class="fill"'
    style = f' style="object-position: {p["position"]};"' if p.get("position") else ""
    return (f'<div class="cover {extra_class}"><img{cls}{style} src="{prefix}images/projects/{image}" '
            f'alt="{e(p["alt"])}" loading="lazy">{year}</div>')


def tags(p):
    return '<div class="tags">' + "".join(f'<span class="tag">{e(t)}</span>' for t in p["tags"]) + "</div>"


def ext_links(p, skip=None):
    return "".join(f'<a href="{e(u)}" target="_blank" rel="noreferrer">{e(n)}</a>' for n, u in p["links"] if u != skip)


def cta(p):
    if "cta" not in p:
        return ""
    n, u = p["cta"]
    return f'<a class="btn btn-primary cta" href="{e(u)}" target="_blank" rel="noreferrer">{e(n)} →</a>'


def gallery(p):
    if not p.get("gallery"):
        return ""
    figs = "".join(f'<figure><img src="../images/projects/{f}" alt="{e(c)}" loading="lazy"><figcaption>{e(c)}</figcaption></figure>'
                   for f, c in p["gallery"])
    return f'<div class="gallery">{figs}</div>'


def card(p):
    return f'''      <article class="card project reveal" data-href="projects/{p["slug"]}.html">
        {cover(p, "")}
        <div class="project-body">
          <h3><a href="projects/{p["slug"]}.html">{e(p["title"])}</a></h3>
          <p class="desc">{e(p["card"])}</p>
          {tags(p)}
          <div class="links"><a href="projects/{p["slug"]}.html">Details</a>{ext_links(p)}</div>
        </div>
      </article>
'''


def page(p):
    body = "".join(f"<p>{e(x)}</p>" for x in p["body"])
    hl = "".join(f"<li>{e(x)}</li>" for x in p["highlights"])
    if p.get("caveats"):
        hl += "</ul><h2>Limitations</h2><ul>" + "".join(f"<li>{e(x)}</li>" for x in p["caveats"])
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{e(p["title"])} | Tim-Louis Wilken</title>
  <meta name="description" content="{e(p["summary"])}">
  <link rel="icon" href="../favicon.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../style.css">
</head>
<body>
<nav class="nav">
  <div class="container nav-inner">
    <a href="../index.html" class="brand">Tim-Louis Wilken</a>
    <div class="nav-links">
      <a href="../index.html#projects">Projects</a>
      <a href="../index.html#experience">Experience</a>
      <a href="../index.html#education">Education</a>
    </div>
    <div class="nav-actions">
      <a class="icon-link" href="https://github.com/TimLouisWilken" target="_blank" rel="noreferrer" aria-label="GitHub">{ICON_GH}</a>
      <a class="icon-link" href="https://linkedin.com/in/tim-louis-wilken" target="_blank" rel="noreferrer" aria-label="LinkedIn">{ICON_LI}</a>
      <a class="btn btn-primary btn-sm" href="../cv.pdf" download="CV_Tim-Louis_Wilken.pdf">Download CV</a>
    </div>
  </div>
</nav>
<main class="container section">
  <a class="back" href="../index.html#projects">← Back to Projects</a>
  <header class="section-head detail-head">
    <h2>{e(p["title"])}</h2>
    <p>{e(p["summary"])}</p>
  </header>
  <article class="card detail">
    {cover(p, "../", "detail-cover", show_year=True, detail=True)}
    <div class="detail-body">
      <p class="eyebrow">{e(p["year"])}</p>
      <div style="margin-top: 1rem;">{tags(p)}</div>
      <div class="detail-links">{cta(p)}{ext_links(p, skip=p.get("cta", (None, None))[1])}</div>
      <div class="prose">
        {body}
        <h2>Highlights</h2>
        <ul>{hl}</ul>
      </div>
      {gallery(p)}
    </div>
  </article>
</main>
<footer class="footer">
  <div class="container footer-inner">
    <p>© 2026 Tim-Louis Wilken</p>
    <div class="footer-links">
      <a href="https://github.com/TimLouisWilken" target="_blank" rel="noreferrer">GitHub</a>
      <a href="https://linkedin.com/in/tim-louis-wilken" target="_blank" rel="noreferrer">LinkedIn</a>
      <a href="../cv.pdf" download="CV_Tim-Louis_Wilken.pdf">Download CV</a>
    </div>
  </div>
</footer>
</body>
</html>
'''


def main():
    idx = ROOT / "index.html"
    s = idx.read_text()
    cards = "".join(card(p) for p in PROJECTS)
    s = re.sub(r"<!-- PROJECTS:START -->.*?<!-- PROJECTS:END -->",
               lambda m: "<!-- PROJECTS:START -->\n" + cards + "<!-- PROJECTS:END -->", s, flags=re.S)
    idx.write_text(s)
    out = ROOT / "projects"
    out.mkdir(exist_ok=True)
    for p in PROJECTS:
        (out / f'{p["slug"]}.html').write_text(page(p))
    print(f"{len(PROJECTS)} cards and pages written")


if __name__ == "__main__":
    main()
