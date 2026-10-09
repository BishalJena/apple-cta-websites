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
    "hero": '''        <div class="phone" role="img" aria-label="Lotus F-2 flight results from Denpasar to Singapore with private search on">
          <div class="phone-screen ui">
            <div class="screen-header"><h3>Flights</h3><span class="pill" style="--c: var(--accent-green)"><span class="icon">shield</span>Private</span></div>
            <div class="route" style="padding: 2px 6px 8px">
              <div><div class="code">DPS</div><div class="city">Denpasar</div></div>
              <div class="line"><span class="icon">flight</span></div>
              <div style="text-align: right"><div class="code">SIN</div><div class="city">Singapore</div></div>
            </div>
            <div class="list">
              <div class="fare best"><span class="al" style="--c: var(--accent-blue)">CA</span><div class="times"><b>08:15 – 10:50</b><span>Coral Air · Direct</span></div><div class="price"><s>$214</s>$168</div></div>
              <div class="fare"><span class="al" style="--c: var(--accent-orange)">SJ</span><div class="times"><b>11:40 – 14:20</b><span>Sunda Jet · Direct</span></div><div class="price"><s>$229</s>$181</div></div>
              <div class="fare"><span class="al" style="--c: var(--accent-purple)">TA</span><div class="times"><b>17:05 – 21:30</b><span>Tern Airways · 1 stop</span></div><div class="price"><s>$198</s>$157</div></div>
            </div>
            <div class="list" style="margin-top: 2px">
              <div class="check-row"><span class="box icon">check</span><div class="main"><b>Passport valid 6+ months</b></div></div>
              <div class="check-row"><span class="box todo icon">check</span><div class="main"><b>SG Arrival Card</b><span>Due 3 days before</span></div></div>
            </div>
            <div class="tabbar" aria-hidden="true"><span class="on"><span class="icon">flight</span>Flights</span><span><span class="icon">luggage</span>Trips</span><span><span class="icon">description</span>Documents</span><span><span class="icon">settings</span>Settings</span></div>
          </div>
        </div>
        <div class="float-chip chip-streak" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-green)">savings</span>
          <div><b class="rounded">−$46</b><small>vs. regular search</small></div>
        </div>
        <div class="float-chip chip-done" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-blue)">fingerprint</span>
          <div><b class="rounded">Masked</b><small>Device fingerprint</small></div>
        </div>''',
    "features_title": "Book with confidence.<br>Travel without the stress.",
    "features": [
        {
            "size": "two-thirds", "color": "green", "kicker": "Private search",
            "title": "The same fare, wherever you search",
            "text": "Searches go through a private connection that hides your IP address and phone fingerprint, so prices aren't marked up for searching on a phone.",
            "media": '''            <div class="compare" role="img" aria-label="Illustration: regular phone search $214, Lotus F-2 private search $168">
              <div class="compare-row"><div class="top"><span>Regular phone search</span><b>$214</b></div><div class="bar"><i style="--w: 100%; --c: var(--color-fill-3)"></i></div></div>
              <div class="compare-row"><div class="top"><span>Laptop search</span><b>$176</b></div><div class="bar"><i style="--w: 82%; --c: color-mix(in srgb, var(--accent-blue) 45%, transparent)"></i></div></div>
              <div class="compare-row"><div class="top"><span style="color: var(--accent-green)">Lotus F-2 private search</span><b style="color: var(--accent-green)">$168</b></div><div class="bar"><i style="--w: 78%; --c: var(--accent-green)"></i></div></div>
              <span class="ui-sub">Example prices for illustration</span>
            </div>''',
        },
        {
            "size": "third", "color": "blue", "kicker": "Price comparison",
            "title": "Every fare in one place",
            "text": "Compares prices across airlines and booking sites, side by side.",
            "media": '''            <div class="list" style="max-width: 260px">
              <div class="fare best"><span class="al" style="--c: var(--accent-blue)">CA</span><div class="times"><b>Coral Air</b><span>Direct · 2h 35m</span></div><div class="price">$168</div></div>
              <div class="fare"><span class="al" style="--c: var(--accent-orange)">SJ</span><div class="times"><b>Sunda Jet</b><span>Direct · 2h 40m</span></div><div class="price">$181</div></div>
              <div class="fare"><span class="al" style="--c: var(--accent-purple)">TA</span><div class="times"><b>Tern Airways</b><span>1 stop · 4h 25m</span></div><div class="price">$157</div></div>
            </div>''',
        },
        {
            "size": "half", "color": "orange", "kicker": "Document checklist",
            "title": "Every document, for your exact route",
            "text": "Visas, entry cards, health forms and more, tailored to where you're flying from and to.",
            "media": '''            <div class="list" style="max-width: 340px">
              <div class="check-row done"><span class="box icon">check</span><div class="main"><b>Passport</b><span>Valid until March 2031</span></div></div>
              <div class="check-row done"><span class="box icon">check</span><div class="main"><b>Return ticket</b><span>Booked</span></div></div>
              <div class="check-row"><span class="box todo icon">check</span><div class="main"><b>Arrival card</b><span>Submit online, 3 days before</span></div><span class="pill" style="--c: var(--accent-orange)">To do</span></div>
              <div class="check-row"><span class="box todo icon">check</span><div class="main"><b>Health declaration</b><span>If required for your route</span></div></div>
            </div>''',
        },
        {
            "size": "half", "color": "purple", "kicker": "Step-by-step guidance",
            "title": "No surprises at the airport",
            "text": "Simple steps and reminders for check-in, security and immigration, so you're never left guessing.",
            "media": '''            <div class="steps">
              <div class="step done"><span class="n"><span class="icon">check</span></span><div><b>Online check-in</b><span>Opens 48 hours before</span></div></div>
              <div class="step now"><span class="n">2</span><div><b>Bag drop by 06:15</b><span>Terminal 2 · Counter D</span></div></div>
              <div class="step"><span class="n">3</span><div><b>Immigration</b><span>Have your arrival card ready</span></div></div>
            </div>''',
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
