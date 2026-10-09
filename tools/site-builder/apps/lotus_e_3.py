"""Lotus E-3: bite-sized, cross-checked news for your location and interests."""

APP = {
    "name": "Lotus E-3",
    "title": "The news in 15 seconds, checked across sources",
    "description": "Lotus E-3 gives you short news stories you can read in under 15 seconds, cross-checked across sources and tailored to where you are and what you care about. Join the waitlist.",
    "brand": "var(--accent-red)",
    "brand2": "var(--accent-orange)",
    "icon": {
        "from": "#ff7a6b", "to": "#d6243a",
        # stacked cards
        "glyph": '<rect x="30" y="40" width="60" height="50" rx="10"/><path d="M38 30h44"/><path d="M42 58h36M42 72h24"/>',
    },
    "status": "Coming to iPhone",
    "h1": "The news,<br>in 15 seconds",
    "sub": "Short, clear stories checked across multiple sources, tuned to where you are and what you care about. Tap any story to go deeper.",
    "hero_shot": "Today's stories",
    "hero_note": "No spam. Just one email when it's ready.",
    "chips": [('fact_check', 'green', 'Checked', 'Across 4 sources'), ('timer', 'red', '12 sec', 'Per story')],
    "features_title": "Stay informed.<br>Skip the noise.",
    "features": [
        {
            "size": 'third', "color": 'green', "kicker": 'Multi-source checks',
            "title": 'Checked before you see it',
            "text": 'Stories are compared across outlets, and we show you how many independent sources agree.',
        },
        {
            "size": 'two-thirds', "color": 'red', "kicker": 'Bite-sized cards',
            "title": 'Every story in under 15 seconds',
            "text": 'Each story is summarised into a few clear lines, so you can catch up while your coffee brews.',
            "shots": ['Story card', 'Story feed'],
        },
        {
            "size": 'half', "color": 'blue', "kicker": 'Made for you',
            "title": 'Your place, your interests',
            "text": 'Your feed is tuned to where you live and the topics you pick. Local news included, clickbait left out.',
        },
        {
            "size": 'half', "color": 'purple', "kicker": 'Tap to expand',
            "title": 'Go deeper in one tap',
            "text": 'Tap any story for the full article, the original sources, and how they compare.',
        },
        {
            "size": 'two-thirds', "color": 'orange', "kicker": 'Your schedule',
            "title": 'News when it suits you',
            "text": "Pick when you'd like your briefing, with your morning coffee or on the way home.",
            "shots": ['Daily briefing', 'Briefing time'],
        },
        {
            "size": 'third', "color": 'indigo', "kicker": 'No clickbait',
            "title": 'Plain headlines',
            "text": 'Headlines that tell you what happened, not what to feel.',
        },
        {
            "size": 'full', "color": 'mint', "kicker": 'Sources first',
            "title": 'Every story shows its sources',
            "text": 'See which outlets reported a story and how they compare, then read the originals.',
            "shots": ['Sources', 'Comparison', 'Full article'],
        },
    ],
    "faq": [
        ("Where does the news come from?",
         "From established news outlets. Every story links back to its original sources, so you can always read the full reporting."),
        ("How do you check stories?",
         "We compare how different outlets report the same event, and show you how many independent sources agree. Stories that are still developing are clearly labelled."),
        ("Can I choose what I see?",
         "Yes. Pick your topics and location, and your feed adapts. You'll still see major stories everyone should know about."),
        ("Will there be ads?",
         "We're planning a calm, ad-free experience. We'll share details on pricing closer to launch."),
    ],
    "values_title": "News you can trust",
    "values": [
        ("fact_check", "green", "Sources first", "Every story shows where it came from and how many sources agree."),
        ("timer", "red", "Respect your time", "Short by design. Read the day's news in a couple of minutes."),
        ("block", "blue", "No clickbait", "Plain headlines that tell you what happened, not what to feel."),
    ],
    "cta_title": "Get the news that matters",
    "cta_sub": "Join the waitlist and be first to read with Lotus E-3.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus E-3 is in development: an iPhone app for short, trustworthy news tailored to where you are and what you care about.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>Bite-sized story cards that take under 15 seconds to read</li>
          <li>Multi-source checks that show how many outlets agree</li>
          <li>A feed tuned to your location and chosen topics</li>
          <li>Tap to expand for full articles and source details</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "News collection", "Gathering stories from a wide range of outlets."),
        ("", "Summaries", "Turning each story into a clear, accurate 15-second read."),
        ("", "Source checks", "Comparing coverage across outlets to flag what's confirmed."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-e3.app",
    "contact_topics": ["General question", "Feature idea", "Publishers and partnerships", "Report a correction", "Press"],
    "privacy_intro": "Lotus E-3 is built to inform you, not to track you. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Location and interests (once the app launches)", '''        <p>Your chosen topics and approximate location are used to tailor your feed. You can use a city instead of precise location. We don't sell your reading habits or share them with advertisers.</p>'''),
    ],
    "terms": [
        ("Summaries and sources", '''        <p>Stories are summaries of reporting by third-party news outlets, and may occasionally contain errors or miss context. Always refer to the original sources for full details. A "sources agree" label reflects how outlets reported a story, not a guarantee of accuracy.</p>
        <p>Original articles belong to their publishers. Links take you to their websites, under their terms.</p>'''),
    ],
}
