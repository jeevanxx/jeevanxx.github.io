# Martian Guide

**Live:** https://jeevanxx.github.io/martian-guide/

A 3D map of Mars for planning a **Marswalk**, built for the NASA Space Apps Challenge 2026 (*Interplanetary Survival Guide: Martian Map*).
It layers data from six NASA missions (Viking, Mars Global Surveyor, Mars Odyssey, Mars Reconnaissance Orbiter, Curiosity and Perseverance) and ESA's Mars Express (HRSC terrain blend, OMEGA minerals) so an astronaut can plan a route, its science stops and its safety margins.

## What it does
- **Marswalk planner:** drop waypoints and science stops. It works out distance, climb, slopes, suit time and when you're back, and marks a **turn-back point** when a walk is too long.
- **Safer path:** a route search over the terrain that stays under your slope limit.
- **Science stops:** suggested objectives from the data under each stop (water-formed minerals, rock unit, bedrock vs dust, ice, Perseverance's real drives).
- **Live NASA Mars Trek layers:** 7 map layers (CTX global mosaic, MOLA + HRSC relief, Viking, THEMIS day/night infrared, HiRISE Jezero, HiRISE Curiosity site) stream from Mars Trek as you zoom and drape over the 3D terrain, with credits and an automatic fallback.
- **Geology:** the USGS global geologic map as a layer (filter by age or unit); place cards show the unit and its official USGS interpretation, checked live with the USGS map service; routes show the units they cross.
- **Rover routes:** Curiosity's real drive (NASA Mars Trek) with its 14 waypoints and Trek's descriptions, a replay, and NASA's 2019 proposed Mount Sharp route shown as NASA's image. Historical, not live tracking.
- **Rover images:** Perseverance raw images loaded live from NASA's feed by sol and camera, with time, camera and credit for each image. Nothing is downloaded or stored.
- **Conditions:** Mars clock (Mars Year, season, local solar time, sunrise/sunset), Curiosity's latest REMS weather, radiation from Curiosity's RAD.
- **Survival analysis:** scores the planet for a first base, a solar camp or a science mission, and compares places.
- **About the data:** a panel listing which features show real data and which are calculations or models. NASA Worldview (Earth imagery) is kept separate from the Mars map.
- **1-minute demo** and a full guided tour.

## Real data vs models
| Real data, shown as published | Calculated or modelled |
|---|---|
| Mars Trek imagery (Viking, CTX, HiRISE, THEMIS, MOLA/HRSC), MOLA/HRSC/CTX terrain, USGS geology and interpretations, CRISM/OMEGA/THEMIS minerals, TES thermal inertia and dust, SWIM ice (60°N–60°S), Mars Odyssey neutron hydrogen beyond 60°, Perseverance and Curiosity paths, Perseverance raw images, Curiosity REMS weather and RAD dose rate, IAU names | Mars clock (Mars24 method), walking/rover speed, suit time and turn-back point, path choices (safest terrain, fastest, resource-saving), rule-based Mission Assistant answers (built only from the data and calculations listed here), simulated oxygen/water/energy use and return-to-base check (Pandolf 1977 effort model; not real suit data), radiation per walk, air pressure, survival score, science-stop suggestions. Thermal inertia and dust values are read from coloured maps, so they're relative. |

## Data sources
- NASA Mars Trek live map tiles (WMTS), plus the Esri OnMars CTX service it lists (credit: NASA/JPL/MSSS/Caltech Murray Lab/Esri)
- NASA Mars Trek: Viking MDIM 2.1 colour mosaic, MGS MOLA shaded relief, MRO CTX mosaics, Mars Odyssey THEMIS day IR, MGS TES thermal inertia and dust cover index, Perseverance traverse, aqueous mineral distribution (Ehlmann & Edwards 2014)
- NASA PDS: MGS MOLA MEGDR elevation
- USGS Astrogeology: HRSC/MOLA blended 200 m terrain (HRSC: ESA/DLR/FU Berlin, ESA Mars Express; MOLA: NASA/GSFC); Mars 2020 HiRISE mosaic and CTX 20 m terrain of Jezero
- USGS–NASA Planetary Geologic Mapping Program: global geologic map of Mars (Tanaka et al. 2014, SIM 3292), https://astrogeology-usgs.hub.arcgis.com/pages/interactive-maps-mars
- Mars Perseverance raw images gallery, linked from science stops: https://mars.nasa.gov/mars2020/multimedia/raw-images/
- Curiosity's proposed path up Mount Sharp (NASA), compared with the Gale plan: https://science.nasa.gov/resource/curiositys-proposed-path-up-mount-sharp/
- NASA Worldview: Earth imagery, kept separate from the Mars map (explained in the app's About the data panel): https://worldview.earthdata.nasa.gov/
- IAU/USGS Gazetteer of Planetary Nomenclature
- SWIM project: subsurface ice consistency maps (60°N to 60°S)
- Mars Odyssey Neutron Spectrometer, Averaged Neutron Data v2 (NASA PDS Geosciences Node, ODY-M-GRS-5-AND): epithermal neutron counts averaged over local-summer seasons of Mars Years 26–33, used for ice beyond 60°. Fewer epithermal neutrons mean more hydrogen; the app turns this into a relative index and scales it to SWIM where the two overlap (correlation r = 0.78). Coarse: 5° grid, about 300 km.
- NASA Mars Trek: Curiosity traverse path and waypoint descriptions
- NASA raw-image feed for Perseverance (images credited per image, JPL image use policy)
- USGS SIM 3292 Description of Map Units: unit interpretations
- NASA / Centro de Astrobiología: Curiosity REMS weather (https://mars.nasa.gov/msl/mission/weather/)
- Hassler et al. 2014, *Science* 343: Curiosity RAD surface radiation (0.67 mSv/day)
- NASA Mars fact sheet: surface pressure and scale height
- Allison & McEwen 2000: Mars time algorithm (as used in NASA GISS Mars24)

## Limits
This is a concept prototype, not a mission tool. Terrain is 20 m at Jezero, 200 m in the other close-ups and about 7 km elsewhere, so boulders and small scarps don't show. Walking speed, rover speed and suit time are labelled planning guesses you can change in the app.

## Mission workflow
1. Pick a place on the globe (or search 1,926 IAU names).
2. Explore layers: survival score, water ice, sunlight, steepness, ground firmness, dust, geology.
3. Plan a Marswalk: click waypoints, add science stops, choose Safest / Fastest / Resource-saving / Straight path.
4. Read the turn-back point and the simulated oxygen, cooling water and battery use.
5. Simulate an emergency (SIM switch or Emergency button) and get step-by-step guidance.
6. **Generate mission debrief**: a one-page summary (GO / NO-GO, route, resources, path comparison, hazards) that can be printed or saved as PDF.

## Scientific validation
Open **About the data → Scientific validation** in the app for every formula and assumption. In short:
- **Measured:** MOLA, CTX/HRSC terrain, TES, Odyssey neutron hydrogen, THEMIS, Curiosity REMS and RAD, USGS geology, IAU names.
- **Derived:** slope, local time and seasons (Mars24, Allison & McEwen 2000), polar ice estimate, air pressure from elevation.
- **Simulated:** walking speed (Tobler), metabolic power (Pandolf et al. 1977, load terms scaled to Mars gravity), oxygen, cooling water, battery, rover energy, survival score.
- Routes use A* search on a terrain grid; the cost function differs per path mode.
- Checked with automated browser tests (resources only increase along a route, return trip ≈ 2× one-way, heavier load → more oxygen, short suit time → turn-back warning). **Not** checked against real spacesuit data or with users.

> Martian Guide is an educational research prototype, not an operational astronaut safety system.

## Use of AI
In line with the Space Apps rule to state where and how AI tools were used:
- **My part:** I chose the challenge, decided what the app should do (Marswalk planner, turn-back point, science stops, layers, demo), reviewed every version and directed the changes.
- **AI assistance:** I used **Claude (Anthropic)** as a coding assistant to write most of the JavaScript, process the NASA datasets into map tiles, and check facts against sources.
- **Interface design:** the visual style (colours, fonts, panel layout, operations sidebar) was adapted from a design generated with **Google Stitch** (AI design tool), then applied to the app by hand with Claude's help. Sensor cards show only real data, not Stitch's placeholder numbers.
- No AI-generated images are used. All imagery and data come from the NASA, USGS and IAU sources above.

## Tech
Plain HTML, CSS and JavaScript with [three.js](https://threejs.org) r128 (self-hosted in `vendor/`). Client-side app, no server: NASA/USGS/ESA data are pre-processed into `tiles/` and `data/`; live data comes from NASA Mars Trek, the USGS geologic map service and NASA's raw-image feed. Hosted on GitHub Pages.

---
Made by [Jeevan J Shine](https://jeevanxx.github.io).
