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
    "h1": "Stay awake<br>for every mile",
    "sub": "Lotus C-1 watches for the early signs of microsleep and wakes you up with loud music through your car speakers, right from CarPlay.",
    "hero_shot": 'Driving screen',
    "hero_note": "No spam. Just one email when it's ready.",
    "chips": [('face', 'indigo', 'Watching', 'Head and eyes'), ('volume_up', 'orange', 'Ready', 'Wake-up alarm')],
    "features_title": "A co-pilot that never<br>gets tired.",
    "features": [
        {
            "size": 'third', "color": 'purple', "kicker": 'Face tracking',
            "title": 'Spots the nod',
            "text": 'Tracks head position, nods and long blinks to catch fatigue before it turns into microsleep.',
        },
        {
            "size": 'two-thirds', "color": 'indigo', "kicker": 'Apple CarPlay',
            "title": 'Right on your dashboard',
            "text": "Lotus C-1 runs in CarPlay, keeps an eye on how alert you are, and plays alerts through your car's speakers.",
            "shots": ['CarPlay dashboard', 'Alertness score'],
        },
        {
            "size": 'half', "color": 'blue', "kicker": 'Driving patterns',
            "title": 'Notices when you drift',
            "text": "Your iPhone's motion sensors pick up the weaving and sudden corrections that come with drowsy driving.",
        },
        {
            "size": 'half', "color": 'orange', "kicker": 'Wake-up alarm',
            "title": 'Loud enough to work',
            "text": 'When drowsiness is detected, it plays loud music or high-energy sounds through the car stereo.',
        },
        {
            "size": 'two-thirds', "color": 'red', "kicker": 'Black spots',
            "title": 'Extra care where it matters most',
            "text": 'Lotus C-1 knows the stretches of road with the most accidents, and is more sensitive to fatigue as you approach them.',
            "shots": ['Black spot warning', 'Route risk'],
        },
        {
            "size": 'third', "color": 'green', "kicker": 'Rest stops',
            "title": 'Time for a break?',
            "text": 'Suggests nearby places to stop when your alertness starts to drop.',
        },
        {
            "size": 'full', "color": 'mint', "kicker": 'On-device',
            "title": 'Your camera stays private',
            "text": 'Face tracking is designed to run on your iPhone. Video is never recorded or uploaded.',
            "shots": ['Camera setup', 'Privacy', 'Drive summary'],
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
