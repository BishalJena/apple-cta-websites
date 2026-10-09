"""Lotus C-1: microsleep detection for long drives, with CarPlay."""

APP = {
    "name": "Lotus C-1",
    "title": "Stay awake on long drives",
    "description": "Lotus C-1 watches for early signs of microsleep and wakes you with loud music through your car speakers, right from CarPlay. Join the waitlist.",
    "brand": "var(--accent-indigo)",
    "brand2": "var(--accent-purple)",
    "icon": {
        "from": "#7a6cff", "to": "#3a2fb8",
        # open eye
        "glyph": '<path d="M24 60c10-16 22-24 36-24s26 8 36 24c-10 16-22 24-36 24S34 76 24 60Z"/><circle cx="60" cy="60" r="10"/>',
    },
    "status": "Coming to iPhone and CarPlay",
    "hero_class": "wide",
    "h1": "Stay awake<br>for every mile",
    "sub": "Lotus C-1 watches for the early signs of microsleep and wakes you up with loud music through your car speakers, right from CarPlay.",
    "hero": '''        <div class="carplay" role="img" aria-label="CarPlay screen showing Lotus C-1: alertness 92, driver attentive, break suggested in 18 km">
          <div class="carplay-screen">
            <div class="cp-dock">
              <span>9:41</span>
              <span class="app icon" style="--c: var(--accent-green)">call</span>
              <span class="app icon" style="--c: var(--accent-blue)">near_me</span>
              <span class="app icon" style="--c: var(--accent-pink)">music_note</span>
              <img class="app" src="assets/app-icon.svg" alt="">
            </div>
            <div class="cp-main">
              <div class="ring-wrap">
                <svg viewBox="0 0 120 120" aria-hidden="true">
                  <circle cx="60" cy="60" r="50" fill="none" stroke="rgb(255 255 255 / 0.1)" stroke-width="12"/>
                  <circle cx="60" cy="60" r="50" fill="none" stroke="var(--accent-green)" stroke-width="12" stroke-linecap="round" stroke-dasharray="289 314"/>
                </svg>
                <div class="ring-center"><div><b>92</b><span>Alert</span></div></div>
              </div>
              <div class="cp-info">
                <h4>You're doing great</h4>
                <div class="row"><span class="icon">schedule</span>2 h 41 min on the road</div>
                <div class="row"><span class="icon">visibility</span>Blink rate normal</div>
                <div class="cp-alert"><span class="icon" style="font-size: 18px">local_cafe</span>Rest stop in 18 km</div>
              </div>
            </div>
          </div>
        </div>
        <div class="float-chip chip-streak" aria-hidden="true" style="top: 2%">
          <span class="chip-icon icon" style="--c: var(--accent-indigo)">face</span>
          <div><b class="rounded">Watching</b><small>Head and eyes</small></div>
        </div>
        <div class="float-chip chip-done" aria-hidden="true" style="bottom: 0">
          <span class="chip-icon icon" style="--c: var(--accent-orange)">volume_up</span>
          <div><b class="rounded">Ready</b><small>Wake-up alarm</small></div>
        </div>''',
    "features_title": "A co-pilot that never<br>gets tired.",
    "features": [
        {
            "size": "two-thirds", "color": "indigo", "kicker": "Apple CarPlay",
            "title": "Right on your dashboard",
            "text": "Lotus C-1 runs in CarPlay, keeps an eye on how alert you are, and plays alerts through your car's speakers.",
            "media": '''            <div class="carplay" style="max-width: 460px" aria-hidden="true">
              <div class="carplay-screen">
                <div class="cp-main">
                  <div class="ring-wrap">
                    <svg viewBox="0 0 120 120">
                      <circle cx="60" cy="60" r="50" fill="none" stroke="rgb(255 255 255 / 0.1)" stroke-width="12"/>
                      <circle cx="60" cy="60" r="50" fill="none" stroke="var(--accent-orange)" stroke-width="12" stroke-linecap="round" stroke-dasharray="185 314"/>
                    </svg>
                    <div class="ring-center"><div><b>59</b><span>Alert</span></div></div>
                  </div>
                  <div class="cp-info">
                    <h4>Feeling tired?</h4>
                    <div class="row"><span class="icon">warning</span>Two long blinks in 5 min</div>
                    <div class="cp-alert" style="background: color-mix(in srgb, var(--accent-orange) 30%, transparent)"><span class="icon" style="font-size: 18px; color: var(--accent-orange)">local_cafe</span>Take a break soon</div>
                  </div>
                </div>
              </div>
            </div>''',
        },
        {
            "size": "third", "color": "purple", "kicker": "Face tracking",
            "title": "Spots the nod",
            "text": "Tracks head position, nods and long blinks to catch fatigue before it turns into microsleep.",
            "media": '''            <div class="face" aria-hidden="true">
              <svg viewBox="0 0 200 200" fill="none" stroke="var(--brand)" stroke-width="2.5" stroke-linecap="round">
                <path d="M100 22c-38 0-62 30-62 70 0 46 28 86 62 86s62-40 62-86c0-40-24-70-62-70Z" opacity=".5"/>
                <path d="M66 90c6-5 16-5 22 0M112 90c6-5 16-5 22 0"/>
                <path d="M88 132c8 6 16 6 24 0"/>
                <g fill="var(--brand)" stroke="none">
                  <circle cx="66" cy="90" r="3.5"/><circle cx="88" cy="90" r="3.5"/><circle cx="112" cy="90" r="3.5"/><circle cx="134" cy="90" r="3.5"/>
                  <circle cx="100" cy="112" r="3.5"/><circle cx="88" cy="132" r="3.5"/><circle cx="112" cy="132" r="3.5"/>
                  <circle cx="44" cy="100" r="3"/><circle cx="156" cy="100" r="3"/><circle cx="100" cy="176" r="3"/>
                </g>
              </svg>
              <div class="scan"></div>
            </div>''',
        },
        {
            "size": "half", "color": "blue", "kicker": "Driving patterns",
            "title": "Notices when you drift",
            "text": "Using your iPhone's motion sensors, it picks up the weaving and sudden corrections that come with drowsy driving.",
            "media": '''            <div class="panel" style="max-width: 360px">
              <div class="chart-head"><div><span class="label">Steering steadiness</span><b class="rounded" style="font-size: 22px">Irregular</b></div><span class="pill" style="--c: var(--accent-orange)"><span class="icon">warning</span>Last 3 min</span></div>
              <svg viewBox="0 0 300 90" style="width: 100%; height: auto" aria-hidden="true">
                <path d="M0 45 C 20 44, 40 46, 60 45 S 100 44, 120 45 S 150 30, 165 58 S 190 22, 205 64 S 235 30, 250 52 S 280 42, 300 45" fill="none" stroke="var(--accent-blue)" stroke-width="3.5" stroke-linecap="round"/>
                <rect x="150" y="6" width="110" height="78" rx="10" fill="var(--accent-orange)" opacity=".12"/>
              </svg>
            </div>''',
        },
        {
            "size": "half", "color": "orange", "kicker": "Wake-up alarm",
            "title": "Loud enough to work",
            "text": "When drowsiness is detected, it plays loud music or high-energy sounds through the car stereo to snap you back.",
            "media": '''            <div class="vstack" style="max-width: 300px">
              <div class="wave" aria-hidden="true">
                <i style="--h: 30px; --i: 0"></i><i style="--h: 52px; --i: 1"></i><i style="--h: 66px; --i: 2"></i><i style="--h: 40px; --i: 3"></i><i style="--h: 60px; --i: 4"></i>
                <i style="--h: 70px; --i: 5"></i><i style="--h: 46px; --i: 6"></i><i style="--h: 58px; --i: 7"></i><i style="--h: 34px; --i: 8"></i><i style="--h: 50px; --i: 9"></i>
              </div>
              <div class="big-button" style="--c: var(--accent-orange); width: 100%"><span class="icon">volume_up</span>Wake-up alarm · 100%</div>
            </div>''',
        },
        {
            "size": "full", "color": "red", "kicker": "Black spots",
            "title": "Extra care where it matters most",
            "text": "Lotus C-1 knows the stretches of road with the most accidents, and is more sensitive to signs of fatigue as you approach them.",
            "media": '''            <div class="list" style="max-width: 520px">
              <div class="list-row flag"><span class="badge solid icon" style="--c: var(--accent-red)">dangerous</span><div class="main"><b>Accident black spot in 3.2 km</b><span>Sharp bends · high night-time risk</span></div><span class="pill" style="--c: var(--accent-red)">High alert</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-orange)">nights_stay</span><div class="main"><b>Long drive at night</b><span>Fatigue checks every minute</span></div><span class="pill" style="--c: var(--accent-orange)">On</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-green)">local_cafe</span><div class="main"><b>Rest area in 18 km</b><span>Suggested break · 15 min</span></div><span class="trail" style="color: var(--accent-green)">Go</span></div>
            </div>''',
        },
    ],
    "faq": [
        ("How does it know I'm getting sleepy?",
         "It combines head and eye movement from your iPhone's front camera with how steadily you're driving. Long blinks, nodding and weaving all raise the alert."),
        ("Do I need CarPlay?",
         "CarPlay is the best experience because alerts play through your car speakers. You'll also be able to use it on iPhone alone, mounted on the dashboard."),
        ("Is the camera footage stored or uploaded?",
         "No. Lotus C-1 is designed to analyse the camera feed on your iPhone in real time. Video isn't recorded or sent anywhere."),
        ("Can it replace taking a break?",
         "No. The only real fix for tiredness is rest. Lotus C-1 is a safety net that helps you notice fatigue and pull over in time."),
    ],
    "values_title": "Safety first, always",
    "values": [
        ("local_cafe", "orange", "Rest is the real fix", "We'll always nudge you toward a break, not just louder music."),
        ("lock", "blue", "Camera stays on device", "Face tracking is designed to run on your iPhone. Nothing is recorded or uploaded."),
        ("touch_app", "green", "Hands-free", "No taps needed while driving. Alerts are audible and glanceable."),
    ],
    "cta_title": "Get home safe",
    "cta_sub": "Join the waitlist to be among the first drivers to try Lotus C-1.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus C-1 is in development: an iPhone and CarPlay app for drivers on long journeys that detects early signs of microsleep and wakes them up before it's too late.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>CarPlay app with alerts through the car speakers</li>
          <li>Head nod, long-blink and facial gesture recognition</li>
          <li>Irregular driving detection using motion sensors</li>
          <li>Loud music and high-intensity sound alerts</li>
          <li>Extra sensitivity near accident black spots</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Sound research", "Finding which sounds wake drivers most reliably."),
        ("", "Driver interviews", "Talking to people who drive long distances alone."),
        ("", "Black spot data", "Mapping accident-prone stretches of road."),
        ("", "CarPlay prototype", "On-road testing with alerts through the car speakers."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-c1.app",
    "contact_topics": ["General question", "Feature idea", "Fleet and partnerships", "Press"],
    "privacy_intro": "Lotus C-1 uses your camera and motion sensors to keep you safe, so privacy is built in from the start. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Camera (once the app launches)", '''        <p>The front camera is used only while a drive is active, to track head and eye movement. Frames are analysed on your iPhone in real time and are never recorded, stored or uploaded.</p>'''),
        ("Motion and location", '''        <p>Motion sensors and location are used during drives to detect irregular driving and nearby black spots. This data is processed on your device and isn't sold or shared.</p>'''),
    ],
    "terms": [
        ("A safety aid, not a guarantee", '''        <p>Lotus C-1 helps you notice signs of fatigue, but it can't detect every one and it's not a medical device. Never drive when you feel too tired. If you feel drowsy, pull over somewhere safe and rest.</p>
        <p>You're responsible for driving safely and obeying traffic laws. Set up the app before you start driving and don't interact with it while the car is moving.</p>'''),
        ("Audio alerts", '''        <p>Alerts can be very loud by design. Keep volume at a level that's safe for you and your passengers.</p>'''),
    ],
}
