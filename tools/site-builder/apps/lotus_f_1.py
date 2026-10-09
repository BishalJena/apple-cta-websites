"""Lotus F-1: hidden surveillance detection for women who travel."""

APP = {
    "name": "Lotus F-1",
    "title": "Check your room for hidden cameras",
    "description": "Lotus F-1 scans your hotel room or rental for hidden cameras, unknown networks and nearby recording devices, so you can feel safe wherever you stay. Join the waitlist.",
    "brand": "var(--accent-pink)",
    "brand2": "var(--accent-purple)",
    "icon": {
        "from": "#ff6f91", "to": "#c2185b",
        # shield with a check
        "glyph": '<path d="M60 22 32 32v24c0 20 12 34 28 42 16-8 28-22 28-42V32Z"/><path d="m47 60 9 9 17-18"/>',
    },
    "status": "Coming to iPhone",
    "h1": "Feel safe<br>wherever you stay",
    "sub": "Lotus F-1 scans your hotel room or rental for hidden cameras, unknown networks and nearby recording devices, in about a minute.",
    "hero": '''        <div class="phone" role="img" aria-label="Lotus F-1 scanning a room: 14 networks checked, 1 hidden network flagged, no camera-like devices">
          <div class="phone-screen ui">
            <div class="screen-header"><h3>Scan</h3><span>Room 412</span></div>
            <div class="radar" style="max-width: 190px; margin: 6px auto 10px">
              <span class="blip" style="left: 28%; top: 34%; --c: var(--accent-green)"></span>
              <span class="blip" style="left: 70%; top: 26%; --c: var(--accent-green)"></span>
              <span class="blip" style="left: 74%; top: 68%; --c: var(--accent-orange)"></span>
              <span class="core icon">shield</span>
            </div>
            <div class="list">
              <div class="list-row flag" style="--c: var(--accent-orange)"><span class="badge solid icon" style="--c: var(--accent-orange)">wifi_find</span><div class="main"><b>1 hidden network</b><span>Streaming device nearby</span></div><span class="trail icon" style="color: var(--accent-orange)">chevron_right</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-green)">videocam_off</span><div class="main"><b>No camera-like devices</b><span>14 networks checked</span></div></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-green)">bluetooth</span><div class="main"><b>7 Bluetooth devices</b><span>All look familiar</span></div></div>
            </div>
            <div class="tabbar" aria-hidden="true"><span class="on"><span class="icon">radar</span>Scan</span><span><span class="icon">history</span>History</span><span><span class="icon">lightbulb</span>Tips</span><span><span class="icon">settings</span>Settings</span></div>
          </div>
        </div>
        <div class="float-chip chip-streak" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-pink)">radar</span>
          <div><b class="rounded">Scanning</b><small>Wi-Fi and Bluetooth</small></div>
        </div>
        <div class="float-chip chip-done" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-green)">verified_user</span>
          <div><b class="rounded">58 sec</b><small>Full room check</small></div>
        </div>''',
    "features_title": "Know who else<br>might be watching.",
    "features": [
        {
            "size": "two-thirds", "color": "pink", "kicker": "Hidden network scanner",
            "title": "Finds what's hiding on the Wi-Fi",
            "text": "Scans local Wi-Fi and private wireless networks for unknown devices and hidden streaming hardware.",
            "media": '''            <div class="list" style="max-width: 420px">
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">wifi</span><div class="main"><b>Hotel_Guest</b><span>Public network · 38 devices</span></div><span class="pill" style="--c: var(--accent-green)">Normal</span></div>
              <div class="list-row flag" style="--c: var(--accent-red)"><span class="badge solid icon" style="--c: var(--accent-red)">wifi_find</span><div class="main"><b>Hidden network</b><span>No name · strong signal · streaming video</span></div><span class="pill solid" style="--c: var(--accent-red)">Check</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">router</span><div class="main"><b>Room router</b><span>3 connected devices</span></div><span class="pill" style="--c: var(--accent-green)">Normal</span></div>
            </div>''',
        },
        {
            "size": "third", "color": "red", "kicker": "Spy camera detection",
            "title": "Spots the lens",
            "text": "Looks for camera-like devices and covert surveillance hardware around the room.",
            "media": '''            <div class="radar" aria-hidden="true">
              <span class="blip" style="left: 30%; top: 30%; --c: var(--accent-green)"></span>
              <span class="blip" style="left: 72%; top: 62%; --c: var(--accent-red)"></span>
              <span class="core icon">videocam</span>
            </div>''',
        },
        {
            "size": "half", "color": "orange", "kicker": "Safety alerts",
            "title": "Tells you straight away",
            "text": "Get an instant notification when possible surveillance hardware is detected nearby, with clear next steps.",
            "media": '''            <div class="notif-stack">
              <div class="notif"><img class="n-icon" src="assets/app-icon.svg" alt=""><div class="n-body"><div class="n-head"><b>Lotus F-1</b><time>now</time></div><p>Possible hidden camera nearby. Tap to see where to look.</p></div></div>
              <div class="notif"><img class="n-icon" src="assets/app-icon.svg" alt=""><div class="n-body"><div class="n-head"><b>Lotus F-1</b><time>2 min ago</time></div><p>Room scan complete. 1 item to review.</p></div></div>
            </div>''',
        },
        {
            "size": "half", "color": "purple", "kicker": "Wearables and smart devices",
            "title": "Notices recording wearables",
            "text": "Scans nearby Bluetooth signals for smart devices that can record. Smart glasses detection is something we're actively researching.",
            "media": '''            <div class="list" style="max-width: 340px">
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-purple)">eyeglasses</span><div class="main"><b>Smart glasses</b><span>Close by · in research</span></div><span class="pill" style="--c: var(--accent-purple)">Beta</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">headphones</span><div class="main"><b>Earbuds</b><span>Can't record video</span></div><span class="pill" style="--c: var(--accent-green)">OK</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-orange)">nfc</span><div class="main"><b>NFC tag</b><span>Near the door</span></div><span class="pill" style="--c: var(--accent-orange)">Review</span></div>
            </div>''',
        },
        {
            "size": "full", "color": "green", "kicker": "Guided check",
            "title": "A calm, step-by-step room check",
            "text": "Lotus F-1 walks you through the spots worth checking, like smoke detectors, chargers and mirrors, so nothing gets missed.",
            "media": '''            <div class="steps" style="max-width: 440px">
              <div class="step done"><span class="n"><span class="icon">check</span></span><div><b>Scan the networks</b><span>Wi-Fi and hidden networks checked</span></div></div>
              <div class="step done"><span class="n"><span class="icon">check</span></span><div><b>Check Bluetooth and NFC</b><span>7 devices, 1 tag to review</span></div></div>
              <div class="step now"><span class="n">3</span><div><b>Look around the room</b><span>Smoke detector, clock, chargers, mirrors</span></div></div>
              <div class="step"><span class="n">4</span><div><b>Your safety summary</b><span>Save or share it with someone you trust</span></div></div>
            </div>''',
        },
    ],
    "faq": [
        ("How does Lotus F-1 find hidden cameras?",
         "Most hidden cameras need to send video somewhere, so they show up on Wi-Fi or Bluetooth. Lotus F-1 looks for unusual devices and hidden networks, then guides you through a physical check of common hiding spots."),
        ("Can it find every device?",
         "No scanner can promise that. Some devices record locally and never connect to anything. Lotus F-1 gives you a much better picture than looking around alone, and tells you what it couldn't check."),
        ("What should I do if it finds something?",
         "Don't tamper with it. Take a photo, move somewhere you feel safe, and contact the property and local police. The app will show you clear next steps."),
        ("Does it work without internet?",
         "Yes. Scanning happens on your iPhone, so it works wherever you are, even without a data plan."),
    ],
    "values_title": "Made for women who travel",
    "values": [
        ("lock", "blue", "Private by design", "Scans run on your iPhone. We don't collect where you stay or what's on the network."),
        ("support", "pink", "Calm, not scary", "Clear results and practical next steps, not alarm bells for every device."),
        ("public", "green", "Works anywhere", "Hotels, rentals and hostels, at home or abroad, with or without data."),
    ],
    "cta_title": "Travel with peace of mind",
    "cta_sub": "Join the waitlist and be first to try Lotus F-1.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus F-1 is in development: an iPhone app that helps women who travel check their accommodation for hidden cameras and other surveillance.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>Hidden network scanner for Wi-Fi and private wireless networks</li>
          <li>Micro-surveillance and spy camera detection</li>
          <li>Instant safety alerts with clear next steps</li>
          <li>Bluetooth, NFC and smart device detection</li>
        </ul>
        <p>Smart glasses detection, including Meta glasses, is still being researched. We'll only ship it once we're confident it's reliable.</p>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Network tests", "Testing detection across real hotel and rental networks."),
        ("", "Bluetooth device tests", "Building a library of device signatures."),
        ("", "Traveller interviews", "Learning from people who book hotels and travel often."),
        ("", "Smart glasses research", "Checking whether detection is reliable enough to ship."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-f1.app",
    "contact_topics": ["General question", "Feature idea", "Hotel and travel partnerships", "Press"],
    "privacy_intro": "Lotus F-1 exists to protect your privacy, so it's built to collect as little as possible. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Scans (once the app launches)", '''        <p>Wi-Fi, Bluetooth and NFC scans run on your iPhone. Scan results stay on your device unless you choose to share a summary. We don't collect your location or which accommodation you're staying in.</p>'''),
    ],
    "terms": [
        ("What the app can and can't do", '''        <p>Lotus F-1 helps you spot possible surveillance devices, but no tool can detect every device. A clear scan doesn't guarantee a room is free of cameras, and a flagged device isn't proof of wrongdoing.</p>
        <p>If you believe you're in danger, contact local emergency services. If you find a device, don't tamper with it. Report it to the property and the police.</p>'''),
        ("Lawful use", '''        <p>Use Lotus F-1 only to check spaces you're staying in or are responsible for. Don't use it to interfere with other people's networks or devices.</p>'''),
    ],
}
