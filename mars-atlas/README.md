# Mars Atlas

**Live:** https://jeevanxx.github.io/mars-atlas/

A 3D map of Mars for planning a **Marswalk**, built for the NASA Space Apps Challenge 2026 (*Interplanetary Survival Guide: Martian Map*).
It layers data from five NASA missions (Viking, Mars Global Surveyor, Mars Odyssey, Mars Reconnaissance Orbiter and Curiosity) so an astronaut can plan a route, its science stops and its safety margins.

## What it does
- **Marswalk planner:** drop waypoints and science stops. It works out distance, climb, slopes, suit time and when you're back, and marks a **turn-back point** when a walk is too long.
- **Safer path:** a route search over the terrain that stays under your slope limit.
- **Science stops:** suggested objectives from the data under each stop (water-formed minerals, bedrock vs dust, ice, nearby features, Perseverance's real drives).
- **Jezero close-up:** 5 m HiRISE imagery on 20 m CTX terrain, with Perseverance's real traverse.
- **Conditions:** live Mars clock (Mars Year, season, local solar time, sunrise/sunset), Curiosity's latest REMS weather, radiation dose from Curiosity's RAD.
- **Geology:** the USGS global geologic map as a layer; every science stop and place card names its rock unit and age.
- **Survival analysis:** scores the planet for a first base, a solar camp or a science mission, and compares places.
- **2-minute demo** and a full guided tour.

## Data sources
- NASA Mars Trek: Viking MDIM 2.1 colour mosaic, MGS MOLA shaded relief, MRO CTX mosaics, Mars Odyssey THEMIS day IR, MGS TES thermal inertia and dust cover index, Perseverance traverse, aqueous mineral distribution (Ehlmann & Edwards 2014)
- NASA PDS: MGS MOLA MEGDR elevation
- USGS Astrogeology: HRSC/MOLA blended 200 m terrain; Mars 2020 HiRISE mosaic and CTX 20 m terrain of Jezero
- USGS–NASA Planetary Geologic Mapping Program: global geologic map of Mars (Tanaka et al. 2014, SIM 3292), https://astrogeology-usgs.hub.arcgis.com/pages/interactive-maps-mars
- Mars Perseverance raw images gallery, linked from science stops: https://mars.nasa.gov/mars2020/multimedia/raw-images/
- Curiosity's proposed path up Mount Sharp (NASA), compared with the Gale plan: https://science.nasa.gov/resource/curiositys-proposed-path-up-mount-sharp/
- NASA Worldview: inspired the layer-switching design (Earth data, so none is used): https://worldview.earthdata.nasa.gov/
- IAU/USGS Gazetteer of Planetary Nomenclature
- SWIM project: subsurface ice consistency maps
- NASA / Centro de Astrobiología: Curiosity REMS weather (https://mars.nasa.gov/msl/mission/weather/)
- Hassler et al. 2014, *Science* 343: Curiosity RAD surface radiation (0.67 mSv/day)
- NASA Mars fact sheet: surface pressure and scale height
- Allison & McEwen 2000: Mars time algorithm (as used in NASA GISS Mars24)

## Limits
This is a concept prototype, not a mission tool. Terrain is 20 m at Jezero, 200 m in the other close-ups and about 7 km elsewhere, so boulders and small scarps don't show. Walking speed, rover speed and suit time are labelled planning guesses you can change in the app.

## Use of AI
In line with the Space Apps rule to state where and how AI tools were used:
- **My part:** I chose the challenge, decided what the app should do (Marswalk planner, turn-back point, science stops, layers, demo), reviewed every version and directed the changes.
- **AI assistance:** I used **Claude (Anthropic)** as a coding assistant to write most of the JavaScript, process the NASA datasets into map tiles, and check facts against sources.
- No AI-generated images are used. All imagery and data come from the NASA, USGS and IAU sources above.

## Tech
Plain HTML, CSS and JavaScript with [three.js](https://threejs.org) r128. No build step. Hosted on GitHub Pages.

---
Made by [Jeevan J Shine](https://jeevanxx.github.io).
