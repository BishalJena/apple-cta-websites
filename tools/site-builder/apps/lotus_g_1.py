"""Lotus G-1: speed camera alerts as an iOS Live Activity."""

APP = {
    "name": "Lotus G-1",
    "title": "Speed camera alerts on your Lock Screen",
    "description": "Lotus G-1 shows upcoming speed cameras on your Dynamic Island and Lock Screen, and tells you when to ease off. Join the waitlist.",
    "brand": "var(--accent-orange)",
    "brand2": "var(--accent-red)",
    "icon": {
        "from": "#ffb340", "to": "#ff5a36",
        # speedometer arc + needle
        "glyph": '<path d="M28 78a32 32 0 1 1 64 0"/><path d="M60 78l16-20"/><circle cx="60" cy="78" r="3" fill="#fff"/>',
    },
    "status": "Launching first in Bali",
    "h1": "Ease off before<br>the camera",
    "sub": "Lotus G-1 puts the next speed camera on your Dynamic Island and Lock Screen, with a heads-up to slow down long before you reach it.",
    "hero": '''        <div class="phone" role="img" aria-label="iPhone Lock Screen showing a Lotus G-1 Live Activity: speed camera 850 metres ahead, limit 60 km/h">
          <div class="phone-screen lock">
            <div class="island">
              <span class="la-sign sm">60</span>
              <div class="la-main"><b style="font-size: 13px">Speed camera</b><span>Jl. Bypass Ngurah Rai</span></div>
              <div class="la-dist" style="font-size: 20px">850<small>m</small></div>
            </div>
            <div class="lock-inner" style="padding-top: 92px">
              <div class="lock-date">Thursday, October 9</div>
              <div class="lock-time">9:41</div>
              <div class="lock-spacer"></div>
              <div class="live-activity">
                <div class="la-row">
                  <span class="la-sign">60</span>
                  <div class="la-main"><b>Speed camera ahead</b><span>Fixed camera · both directions</span></div>
                  <div class="la-dist">850<small>m</small></div>
                </div>
                <div class="la-bar" style="--p: 68%"><i></i></div>
                <div class="la-foot"><span>You: 72 km/h</span><span class="warn">Slow down by 12</span></div>
              </div>
            </div>
          </div>
        </div>
        <div class="float-chip chip-streak" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-red)">photo_camera</span>
          <div><b class="rounded">850 m</b><small>Next camera</small></div>
        </div>
        <div class="float-chip chip-done" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-green)">verified</span>
          <div><b class="rounded">No tickets</b><small>This month</small></div>
        </div>''',
    "features_title": "Every camera, called out<br>before you get there.",
    "features": [
        {
            "size": "two-thirds", "color": "orange", "kicker": "Live Activity",
            "title": "Always on your Lock Screen",
            "text": "The next camera, its limit and your distance stay on the Dynamic Island and Lock Screen. No switching apps mid-drive.",
            "media": '''            <div class="vstack" style="max-width: 400px">
              <div class="island compact" style="position: static; transform: none; width: 190px">
                <span class="la-sign sm">60</span>
                <span class="rounded" style="font-weight: 700; font-size: 15px">850 m</span>
              </div>
              <div class="live-activity" style="max-width: 400px">
                <div class="la-row">
                  <span class="la-sign">80</span>
                  <div class="la-main"><b>Average speed zone</b><span>Next 4.2 km</span></div>
                  <div class="la-dist">1.4<small>km</small></div>
                </div>
                <div class="la-bar" style="--p: 35%"><i></i></div>
                <div class="la-foot"><span>You: 76 km/h</span><span style="color: var(--accent-green)">Within limit</span></div>
              </div>
            </div>''',
        },
        {
            "size": "third", "color": "red", "kicker": "Proximity alerts",
            "title": "Heard and seen",
            "text": "A visual and spoken warning as you get close, with the distance and the camera's limit.",
            "media": '''            <div class="notif-stack">
              <div class="notif"><img class="n-icon" src="assets/app-icon.svg" alt=""><div class="n-body"><div class="n-head"><b>Lotus G-1</b><time>now</time></div><p>Speed camera in 500 m. Limit 60 km/h.</p></div></div>
              <div class="notif"><img class="n-icon" src="assets/app-icon.svg" alt=""><div class="n-body"><div class="n-head"><b>Lotus G-1</b><time>2 km</time></div><p>Camera ahead in 2 km.</p></div></div>
            </div>''',
        },
        {
            "size": "half", "color": "green", "kicker": "Speed advisory",
            "title": "Knows when you're too fast",
            "text": "Your speed is compared with the limit ahead, so you get a nudge to ease off, or a suggestion to take another route.",
            "media": '''            <div class="gauge" role="img" aria-label="Speed gauge: 72 km/h, limit 60">
              <svg viewBox="0 0 200 120">
                <path d="M20 110a80 80 0 0 1 160 0" fill="none" stroke="var(--color-fill-3)" stroke-width="14" stroke-linecap="round"/>
                <path d="M20 110a80 80 0 0 1 160 0" fill="none" stroke="var(--accent-green)" stroke-width="14" stroke-linecap="round" stroke-dasharray="126 252"/>
                <path d="M20 110a80 80 0 0 1 160 0" fill="none" stroke="var(--accent-orange)" stroke-width="14" stroke-linecap="round" stroke-dasharray="0 126 26 252"/>
                <circle cx="100" cy="30" r="0" />
              </svg>
              <div class="gauge-read"><b>72</b><span>km/h · limit 60</span></div>
            </div>''',
        },
        {
            "size": "half", "color": "blue", "kicker": "Community reports",
            "title": "Drivers looking out for drivers",
            "text": "Report a police check or a new camera in one tap, and help everyone on the road stay informed.",
            "media": '''            <div class="list" style="max-width: 320px">
              <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-blue)">local_police</span><div class="main"><b>Police check</b><span>Reported 4 min ago · 1.2 km</span></div><span class="pill" style="--c: var(--accent-blue)">+12</span></div>
              <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-red)">photo_camera</span><div class="main"><b>New fixed camera</b><span>Confirmed by 8 drivers</span></div><span class="pill" style="--c: var(--accent-green)"><span class="icon">check</span>Verified</span></div>
              <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-orange)">add</span><div class="main"><b>Report something</b><span>Takes one tap</span></div></div>
            </div>''',
        },
        {
            "size": "third", "color": "purple", "kicker": "Your distance",
            "title": "Warnings when you want them",
            "text": "Pick how early you'd like to hear about a camera.",
            "media": '''            <div class="vstack">
              <div class="segmented"><span>500 m</span><span>1 km</span><span class="on">2 km</span></div>
              <div class="segmented"><span class="on">Sound</span><span>Voice</span><span>Silent</span></div>
            </div>''',
        },
        {
            "size": "two-thirds", "color": "red", "kicker": "Starting in Bali",
            "title": "Built on a verified camera map",
            "text": "We're launching with a speed camera database for Bali, Indonesia, then expanding region by region.",
            "media_class": "",
            "media": '''            <div class="map" role="img" aria-label="Map with speed cameras along a route">
              <svg viewBox="0 0 400 225" preserveAspectRatio="none" aria-hidden="true">
                <path d="M-10 190 C 80 170, 110 120, 170 118 S 270 70, 410 40" fill="none" stroke="var(--brand)" stroke-width="7" stroke-linecap="round" opacity=".85"/>
                <path d="M60 -10 C 90 80, 150 140, 140 240" fill="none" stroke="var(--color-fill-3)" stroke-width="5"/>
              </svg>
              <span class="pin me" style="left: 12%; top: 80%"></span>
              <span class="pin icon" style="left: 42%; top: 52%">photo_camera</span>
              <span class="label" style="left: 42%; top: 62%">60 km/h</span>
              <span class="pin icon" style="left: 74%; top: 30%; --c: var(--accent-blue)">local_police</span>
            </div>''',
        },
    ],
    "faq": [
        ("Does this help me speed without getting caught?",
         "No. Lotus G-1 is built for careful drivers who want to stay within the limit. It reminds you of the limit ahead so you can slow down in good time."),
        ("Where will it work?",
         "We're starting with Bali, Indonesia, and will add more regions as we build out the camera database."),
        ("Do I need to keep the app open?",
         "No. Alerts run as a Live Activity on your Lock Screen and Dynamic Island, so you can keep using Maps or music."),
        ("Is using camera alerts legal?",
         "Camera alert apps are legal in many countries, but not everywhere. Please check the rules where you drive. We'll only offer the app where it's allowed."),
    ],
    "values_title": "Built for calm, careful driving",
    "values": [
        ("visibility", "orange", "Eyes on the road", "Glanceable alerts and spoken warnings mean you never need to pick up your phone."),
        ("lock", "blue", "Private by default", "Your location is used on your device to find cameras near you. We don't sell where you drive."),
        ("groups", "green", "Community powered", "Reports from fellow drivers keep the map fresh, with confirmations to cut out noise."),
    ],
    "cta_title": "Drive with fewer surprises",
    "cta_sub": "Join the waitlist and be first on the road with Lotus G-1.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus G-1 is in development. It's a Live Activity for iPhone that shows the nearest speed camera on your route and warns you to slow down before you reach it.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>Live Activity on the Lock Screen and Dynamic Island</li>
          <li>Visual and spoken alerts at a distance you choose</li>
          <li>Speed advisory comparing your speed with the limit ahead</li>
          <li>Community reports for police checks and new cameras</li>
          <li>A speed camera database for Bali, Indonesia</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Bali camera database", "Collecting and verifying camera locations and limits."),
        ("", "Driver interviews", "Riding along with car and motorbike drivers to shape the alerts."),
        ("", "Route simulation", "Testing alerts on simulated drives before real-world tests."),
        ("", "CarPlay notifications", "Showing alerts on the car's display."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-g1.app",
    "contact_topics": ["General question", "Report a camera location", "Feature idea", "Partnerships", "Press"],
    "privacy_intro": "Lotus G-1 is designed to collect as little as possible. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Location (once the app launches)", '''        <p>The app needs your location and speed to find cameras on your route and warn you in time. This is processed on your device. We don't build a history of your trips or sell location data.</p>'''),
        ("Community reports", '''        <p>When you report a camera or a police check, we store the report's location and time so other drivers can see it. Reports aren't linked to your name.</p>'''),
    ],
    "terms": [
        ("Drive safely and legally", '''        <p>Lotus G-1 is a driving aid, not a substitute for attention or for road signs. Always obey posted limits, traffic laws and police instructions. Don't interact with your phone while driving.</p>
        <p>Camera locations come from our database and community reports and may be incomplete or out of date. We can't guarantee that every camera is listed, and we're not responsible for fines or penalties.</p>
        <p>Using camera alert apps is restricted in some countries. You're responsible for making sure it's legal where you drive.</p>'''),
        ("Community reports", '''        <p>Only report what you've actually seen. We may remove reports or restrict accounts that post false or abusive information.</p>'''),
    ],
}
