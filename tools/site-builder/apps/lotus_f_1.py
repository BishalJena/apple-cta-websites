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
    "hero_shot": 'Room scan',
    "hero_note": "No spam. Just one email when it's ready.",
    "chips": [('radar', 'pink', 'Scanning', 'Wi-Fi and Bluetooth'), ('verified_user', 'green', '58 sec', 'Full room check')],
    "features_title": "Know who else<br>might be watching.",
    "features": [
        {
            "size": 'third', "color": 'red', "kicker": 'Spy camera detection',
            "title": 'Spots the lens',
            "text": 'Looks for camera-like devices and covert surveillance hardware around the room.',
        },
        {
            "size": 'two-thirds', "color": 'pink', "kicker": 'Hidden network scanner',
            "title": "Finds what's hiding on the Wi-Fi",
            "text": 'Scans local Wi-Fi and private wireless networks for unknown devices and hidden streaming hardware.',
            "shots": ['Network scan', 'Hidden network details'],
        },
        {
            "size": 'half', "color": 'orange', "kicker": 'Safety alerts',
            "title": 'Tells you straight away',
            "text": 'An instant notification when possible surveillance hardware is detected nearby, with clear next steps.',
        },
        {
            "size": 'half', "color": 'purple', "kicker": 'Wearables and smart devices',
            "title": 'Notices recording wearables',
            "text": 'Scans nearby Bluetooth signals for smart devices that can record. Smart glasses detection is in research.',
        },
        {
            "size": 'two-thirds', "color": 'green', "kicker": 'Guided check',
            "title": 'A calm, step-by-step room check',
            "text": 'Lotus F-1 walks you through the spots worth checking, like smoke detectors, chargers and mirrors.',
            "shots": ['Room check steps', 'Spots to check'],
        },
        {
            "size": 'third', "color": 'blue', "kicker": 'Works anywhere',
            "title": 'No signal needed',
            "text": 'Scans run on your iPhone, so they work without Wi-Fi or a data plan.',
        },
        {
            "size": 'full', "color": 'mint', "kicker": 'Safety summary',
            "title": 'Share it with someone you trust',
            "text": 'Save a summary of every scan, or send it to a friend or family member while you travel.',
            "shots": ['Scan history', 'Safety summary', 'Share'],
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
