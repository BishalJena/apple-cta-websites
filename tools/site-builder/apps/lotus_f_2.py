"""Lotus F-2: private flight search plus route-specific travel documents."""

APP = {
    "name": "Lotus F-2",
    "title": "Fair flight prices on your phone, plus every travel document",
    "description": "Lotus F-2 searches flights from a private connection so your phone isn't shown higher prices, and lists every document your trip needs. Join the waitlist.",
    "brand": "var(--accent-blue)",
    "brand2": "var(--accent-mint)",
    "icon": {
        "from": "#4fb3ff", "to": "#1f5fe0",
        # paper plane
        "glyph": '<path d="M26 58 92 30 76 92 58 70Z"/><path d="M58 70 92 30"/><path d="M58 70v18l10-10"/>',
    },
    "status": "Coming to iPhone",
    "h1": "Laptop prices,<br>on your phone",
    "sub": "Lotus F-2 searches flights from a private connection so you aren't quoted more for using a phone. Then it lists every document your trip needs.",
    "hero_shot": 'Flight results',
    "hero_note": "No spam. Just one email when it's ready.",
    "chips": [('savings', 'green', 'Fair fares', 'Private search'), ('fingerprint', 'blue', 'Masked', 'Device fingerprint')],
    "features_title": "Book with confidence.<br>Travel without the stress.",
    "features": [
        {
            "size": 'third', "color": 'blue', "kicker": 'Price comparison',
            "title": 'Every fare in one place',
            "text": 'Compares prices across airlines and booking sites, side by side.',
        },
        {
            "size": 'two-thirds', "color": 'green', "kicker": 'Private search',
            "title": 'The same fare, wherever you search',
            "text": "Searches hide your IP address and phone fingerprint, so prices aren't marked up for searching on a phone.",
            "shots": ['Private search', 'Price comparison'],
        },
        {
            "size": 'half', "color": 'orange', "kicker": 'Document checklist',
            "title": 'Every document, for your exact route',
            "text": "Visas, entry cards, health forms and more, tailored to where you're flying from and to.",
        },
        {
            "size": 'half', "color": 'purple', "kicker": 'Step-by-step guidance',
            "title": 'No surprises at the airport',
            "text": "Simple steps for check-in, security and immigration, so you're never left guessing.",
        },
        {
            "size": 'two-thirds', "color": 'mint', "kicker": 'Travel day',
            "title": 'Reminders at the right moment',
            "text": 'Gentle reminders for check-in, bag drop and entry forms, timed to your flight.',
            "shots": ['Trip timeline', 'Reminder'],
        },
        {
            "size": 'third', "color": 'indigo', "kicker": 'Entry rules',
            "title": 'From official sources',
            "text": 'Requirements are based on official entry rules, with links so you can double-check before you fly.',
        },
        {
            "size": 'full', "color": 'pink', "kicker": 'All in one app',
            "title": 'From search to arrival',
            "text": 'Find a fair fare, get your documents in order and know what to expect at the airport, all in one place.',
            "shots": ['Search', 'Checklist', 'Travel day'],
        },
    ],
    "faq": [
        ("Why are flights more expensive on my phone?",
         "Some booking sites change prices based on your device, location and browsing history. Lotus F-2 searches without revealing those signals, so you see the same fares as everyone else."),
        ("Is the private search legal?",
         "Yes. It works like a privacy-focused VPN for your flight searches. You still book directly with the airline or booking site."),
        ("Where do the document requirements come from?",
         "We use a database of official entry rules for each country. Rules change, so we link to official sources and recommend checking them before you fly."),
        ("Will Lotus F-2 always find a lower price?",
         "Not always. Sometimes the price you're shown is already fair. When it is, you'll know you're not overpaying."),
    ],
    "values_title": "On the traveller's side",
    "values": [
        ("visibility_off", "blue", "No tracking", "We don't build a profile of where you want to go, and we never sell your searches."),
        ("verified", "green", "Honest prices", "We show the fare you'll actually pay, with baggage and fees made clear."),
        ("self_improvement", "purple", "Less travel anxiety", "Every document and step for your route in one calm checklist."),
    ],
    "cta_title": "Stop overpaying for flights",
    "cta_sub": "Join the waitlist and be first to search with Lotus F-2.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus F-2 is in development: an iPhone app that finds fair flight prices on your phone and tells you every document you need for your trip.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>Private search that masks your IP address and device fingerprint</li>
          <li>Price comparison across airlines and booking sites</li>
          <li>Route-specific checklist of visas, entry cards and health forms</li>
          <li>Step-by-step guidance and reminders for travel day</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Private search tests", "Measuring how much masking changes the prices you're shown."),
        ("", "Flight price data", "Connecting to flight price sources and APIs."),
        ("", "Entry rules database", "Visa, entry card and health form requirements by route."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-f2.app",
    "contact_topics": ["General question", "Feature idea", "Airline and travel partnerships", "Press"],
    "privacy_intro": "Lotus F-2 is built to keep your searches private. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Flight searches (once the app launches)", '''        <p>Searches are sent through our private connection so booking sites can't see your IP address or device fingerprint. We don't store your search history on our servers longer than needed to return results, and we never sell it.</p>'''),
        ("Trip details", '''        <p>Trips and checklists you save are stored on your device. If you turn on iCloud, they sync through your private iCloud account.</p>'''),
    ],
    "terms": [
        ("Prices and bookings", '''        <p>Fares come from airlines and third-party booking sites and can change at any time. Bookings are made directly with those providers, under their terms. We're not responsible for their prices, changes or cancellations.</p>'''),
        ("Travel documents", '''        <p>Our document checklists are guidance, not legal advice. Entry rules change often. Always confirm requirements with official government sources and your airline before you travel. You're responsible for having valid documents.</p>'''),
    ],
}
