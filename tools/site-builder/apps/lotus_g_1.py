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
    "hero_shot": 'Lock Screen with Live Activity',
    "hero_note": "No spam. Just one email when it's ready.",
    "chips": [('photo_camera', 'red', '850 m', 'Next camera'), ('verified', 'green', 'Slow down', 'Before the camera')],
    "features_title": "Every camera, called out<br>before you get there.",
    "features": [
        {
            "size": 'third', "color": 'orange', "kicker": 'Live Activity',
            "title": 'Always on your Lock Screen',
            "text": 'The next camera, its limit and your distance, right on the Dynamic Island and Lock Screen.',
        },
        {
            "size": 'two-thirds', "color": 'red', "kicker": 'Proximity alerts',
            "title": 'Heard and seen',
            "text": "A visual and spoken warning as you get close, with the distance and the camera's speed limit.",
            "shots": ['Proximity alert', 'Alert details'],
        },
        {
            "size": 'half', "color": 'green', "kicker": 'Speed advisory',
            "title": "Knows when you're too fast",
            "text": 'Your speed is compared with the limit ahead, with a nudge to ease off or a suggestion to change route.',
        },
        {
            "size": 'half', "color": 'blue', "kicker": 'Community reports',
            "title": 'Drivers looking out for drivers',
            "text": 'Report a police check or a new camera in one tap and help everyone on the road stay informed.',
        },
        {
            "size": 'two-thirds', "color": 'pink', "kicker": 'Starting in Bali',
            "title": 'Built on a verified camera map',
            "text": "We're launching with a speed camera database for Bali, Indonesia, then expanding region by region.",
            "shots": ['Camera map', 'Camera details'],
        },
        {
            "size": 'third', "color": 'purple', "kicker": 'Your distance',
            "title": 'Warnings when you want them',
            "text": "Choose how early you hear about a camera, and how you're told.",
        },
        {
            "size": 'full', "color": 'indigo', "kicker": 'Made for the drive',
            "title": 'Glanceable and hands-free',
            "text": 'Big, simple alerts you can take in at a glance, with spoken warnings so your eyes stay on the road.',
            "shots": ['Driving view', 'Spoken alerts', 'Trip summary'],
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
