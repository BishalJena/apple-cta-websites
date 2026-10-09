# Apps

Context for the seven apps that each get a waitlist site in this repo.

| Folder        | App       | Platform                     | One-liner                                                   |
| ------------- | --------- | ---------------------------- | ----------------------------------------------------------- |
| `lotus-g-1` | Lotus G-1 | iOS Live Activity widget     | Speed camera alerts so cautious drivers avoid tickets       |
| `lotus-c-1` | Lotus C-1 | iOS app + CarPlay            | Keeps long-haul drivers awake by detecting microsleep       |
| `lotus-f-1` | Lotus F-1 | iOS app                      | Detects hidden surveillance so women travelling feel safe   |
| `lotus-f-2` | Lotus F-2 | iOS app                      | Cheapest flights on mobile, plus the travel docs you need   |
| `lotus-e-1` | Lotus E-1 | iOS app                      | Strips metadata and AI fingerprints before you post media   |
| `lotus-e-2` | Lotus E-2 | iOS app                      | Checks if someone is active on dating apps                  |
| `lotus-e-3` | Lotus E-3 | iOS app                      | Bite-sized, vetted news based on your location and interests |

---

## lotus-g-1: Lotus G-1

A Live Activity widget for cautious car drivers who want to avoid speeding tickets. It shows the nearest speed sensors or cameras along a route and, using the car's accelerometer and the distance to the sensor, sends notifications advising the driver to slow down or avoid the route entirely. It uses a speed camera database, and users can report on-duty police officers and additional speed cameras.

**Platform:** iOS Live Activity widget

**Ideal customer**
- **Persona:** Cautious car drivers
- **Intent:** Want to avoid speeding tickets
- **Outcome:** Advised to slow down or avoid the route

**User story**
- Putu wants to be told to slow down when approaching a speed camera, so they can avoid speeding accidents or tickets.
- *Acceptance:* Given a known camera is 2 km ahead on my route, when I'm within that distance, then I get a visual and audio warning showing the distance and the camera's speed limit.

**Features**
- **Live Activity iOS widget:** Real-time speed camera info on the Dynamic Island and Lock Screen, no app switching.
- **Proximity alert system:** Visual and audio warnings when approaching speed cameras or sensors, within a configurable distance.
- **Route and speed advisory engine:** Compares current speed with upcoming limits and suggests slowing down or changing route.

**Dependencies**
- Speed camera database (starting with Bali, Indonesia)
- Notifications on CarPlay
- Simulation to test the app
- User interviews with a car driver and a motorbike driver

---

## lotus-c-1: Lotus C-1

An iOS app connected to CarPlay for drivers on long journeys who want to stay alert the whole way. It watches for signs of microsleep and blasts loud music to keep them awake.

**Platform:** iOS app with CarPlay

**Ideal customer**
- **Persona:** Car drivers driving for long hours
- **Intent:** Want to stay alert throughout the drive
- **Outcome:** Microsleep signs are detected and loud music keeps them awake

**User story**
- Made needs to stay awake while driving long distances alone, so they can avoid road accidents, especially at black spots.
- *Acceptance:* Given the app is active, when my driving pattern is irregular, then an alert triggers to keep me awake.

**Features**
- **Apple CarPlay integration:** Runs in the dashboard to monitor the driver and deliver alerts through the car speakers.
- **Head nod and facial gesture recognition:** Tracks head movements and nod patterns to spot microsleep and fatigue.
- **Irregular driving pattern recognition:** Uses the accelerometer.
- **Loud music and audio alert trigger:** Plays loud music or high-intensity sounds through the car audio when drowsiness is detected.

**Dependencies**
- Research on which sounds keep people awake
- User interviews with a driver
- Black spot data

---

## lotus-f-1: Lotus F-1

A women's safety app for travellers that detects hidden private networks, micro-surveillance devices, NFC cards, Meta glasses (feasibility to be checked) and similar.

**Platform:** iOS app

**Ideal customer**
- **Persona:** Women travelling
- **Intent:** Want to feel secure in the places they go
- **Outcome:** Find out whether anything is spying on them

**User story**
- Ikwan needs to know about any surveillance in their accommodation, so they feel safe during their stay.
- *Acceptance:* Given Ikwan is staying somewhere new while travelling, when they run a security scan for hidden networks, micro-surveillance devices, NFC cards or Meta glasses, then the app alerts them to any hidden spying devices or unauthorised surveillance.

**Features**
- **Hidden network scanner:** Scans local Wi-Fi and private wireless networks for unauthorised devices or hidden streaming hardware.
- **Micro-surveillance and spy camera detection:** Identifies hidden cameras, covert surveillance packages and spy devices in the accommodation.
- **Accommodation safety alerts:** Instant notifications when potential surveillance hardware is detected nearby.
- **Wearable and smart device detection:** Scans nearby Bluetooth and wireless signals, including Meta glasses.

**Dependencies**
- Network tests
- Bluetooth device tests
- User interviews with people who book hotels and travel
- Meta glasses tests

**Feasibility notes:** Meta glasses detection needs a feasibility check.

---

## lotus-f-2: Lotus F-2

A flight aggregator for travellers. Its main selling point is masking the IP address and phone hardware fingerprint so you get the best price on your phone instead of needing a laptop. It also gives a list of the documents needed for international flights.

**Platform:** iOS app

**Ideal customer**
- **Persona:** People planning travel
- **Intent:** Want the best flight prices and help working out every document they need, so they travel with less anxiety
- **Outcome:** Best prices found, plus guidance on required documents and travel procedures

**User story**
- Rishi needs all his documents and forms ready so he can take his international flight without any issues.
- *Acceptance:* Given Rishi selects his international flight, when he opens the trip checklist for his route, then the app gives a full list of required documents and forms with step-by-step procedures.

**Features**
- **IP and hardware fingerprint masking (USP):** Routes flight searches through proxy networks to hide the device's IP and fingerprint, avoiding dynamic price hikes.
- **Flight price aggregator:** Compares fares across airlines and platforms.
- **Route-specific document checklist:** Tailored list of visas, entry cards, health forms and so on, based on origin and destination.
- **Step-by-step travel guidance:** Guidelines and reminders for travel procedures to reduce anxiety and avoid airport delays.

**Dependencies**
- Flight price database or API
- International entry regulations database
- How far IP masking can go

---

## lotus-e-1: Lotus E-1

An app that removes all metadata and AI fingerprints from images before people upload them.

**Platform:** iOS app

**Ideal customer**
- **Persona:** People using social media
- **Intent:** Want to remove sensitive information before sharing media online
- **Outcome:** All metadata and AI watermarks (such as SynthID) removed

**User story**
- Sophie wants to get rid of metadata so she feels secure about her online activity.
- *Acceptance:* Given Sophie selects a photo or video to share, when she processes it through the app before uploading, then the app strips all metadata and AI fingerprints (like SynthID) from the file.

**Features**
- **Metadata stripping (EXIF):** Removes GPS coordinates, timestamps and camera hardware details from photos and videos.
- **AI fingerprint and watermark scrubbing:** Removes embedded AI signatures and invisible watermarks such as SynthID.
- **Pre-upload media processor:** Simple export flow that cleans media before posting.

**Dependencies:** None listed.

**Feasibility notes:** Could try implementing a recently published paper on the technique.

---

## lotus-e-2: Lotus E-2

Something like Cheaterbuster.

**Platform:** iOS app

**Ideal customer**
- **Persona:** Women
- **Intent:** Want to find out if someone is currently on dating apps or cheating
- **Outcome:** Profiles found by checking popular dating apps

**User story**
- Ira wants to know if her partner is cheating, so she can feel comfortable about her relationship.
- *Acceptance:* Given Ira suspects her partner is on dating platforms, when she enters search details into the app, then it checks popular dating apps for matching active profiles.

**Features**
- **Cross-platform dating search:** Checks public profiles across popular dating apps.
- **Targeted parameter matching:** Searches by identifiers such as photo matching, phone number or account details.
- **Relationship status verification:** Clear report summaries of any active dating profiles found.

**Dependencies**
- API access to Tinder, Bumble, Hinge, Coffee Meets Bagel, Grindr, Raya and OkCupid
- Carefully written copy for App Store approval
- Interview with Rania

**Feasibility notes:** Technical approach still to be figured out.

---

## lotus-e-3: Lotus E-3

A bite-sized news platform with vetted sources, tailored to the user's location and interests.

**Platform:** iOS app

**Ideal customer**
- **Persona:** People who get their news online and are vulnerable to it
- **Intent:** Prone to being misinformed
- **Outcome:** News quality vetted across channels and sources

**User story**
- Juan needs bite-sized news at a convenient time so he stays informed about recent trends.
- *Acceptance:* Given a bite-sized news item, when I read it, then it takes under 15 seconds and I can tap for more.

**Features**
- **Bite-sized news cards:** Stories summarised to read in under 15 seconds.
- **Multi-source vetting system:** Checks news quality across channels and sources to prevent misinformation.
- **Location and interest curation:** Feed tailored to the user's location and chosen topics.
- **Tap-to-expand deep dive:** Tap any snippet for the full article and source details.

**Dependencies**
- Scraping news outlets
- A model to aggregate the news

**Feasibility notes:** Unsure about the multi-source vetting system.

---

## Unassigned notes

Notes from the source sheet that don't belong to an app yet:

- Made needs to know whether the place they want to go is wheelchair accessible.
- Timeline
- Specific news
