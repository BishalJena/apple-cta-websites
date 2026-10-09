"""Lotus E-2: check whether someone has an active public dating profile."""

APP = {
    "name": "Lotus E-2",
    "title": "Find out if they're still on dating apps",
    "description": "Lotus E-2 checks popular dating apps for active public profiles, so you can stop wondering and have the conversation with facts. Join the waitlist.",
    "brand": "var(--accent-purple)",
    "brand2": "var(--accent-pink)",
    "icon": {
        "from": "#c77dff", "to": "#7b2cbf",
        # heart with a magnifier
        "glyph": '<path d="M54 86S28 70 28 50a14 14 0 0 1 26-7 14 14 0 0 1 26 7c0 6-2 11-6 16"/><circle cx="78" cy="78" r="10"/><path d="m86 86 8 8"/>',
    },
    "status": "Coming to iPhone",
    "h1": "Stop wondering.<br>Start knowing.",
    "sub": "Lotus E-2 checks popular dating apps for active public profiles, so you can have the conversation with facts instead of fears.",
    "hero": '''        <div class="phone" role="img" aria-label="Lotus E-2 report: 7 dating apps checked, 1 possible active profile found">
          <div class="phone-screen ui">
            <div class="screen-header"><h3>Report</h3><span>Just now</span></div>
            <div class="panel" style="background: var(--color-fill-0); box-shadow: 0 0 0 1px var(--color-hairline)">
              <div class="result-head">
                <span class="avatar-blur" aria-hidden="true"></span>
                <div style="flex: 1"><b style="font-size: 15px">Alex, 31</b><div class="ui-sub">Within 10 km of Canggu</div></div>
                <span class="pill solid" style="--c: var(--accent-orange)">1 match</span>
              </div>
            </div>
            <div class="list">
              <div class="list-row flag" style="--c: var(--accent-orange)"><span class="badge solid icon" style="--c: var(--accent-orange)">favorite</span><div class="main"><b>Possible profile found</b><span>Active in the last 7 days</span></div><span class="trail icon">chevron_right</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-green)">check</span><div class="main"><b>6 apps clear</b><span>No matching public profile</span></div></div>
            </div>
            <div class="panel" style="gap: 8px; background: var(--color-fill-0); box-shadow: 0 0 0 1px var(--color-hairline)">
              <div class="chart-head" style="align-items: center"><span class="label">Match confidence</span><b class="rounded" style="font-size: 15px">Medium</b></div>
              <div class="meter"><i style="--w: 58%; --c: var(--accent-orange)"></i></div>
            </div>
            <div class="tabbar" aria-hidden="true"><span><span class="icon">search</span>Search</span><span class="on"><span class="icon">description</span>Reports</span><span><span class="icon">settings</span>Settings</span></div>
          </div>
        </div>
        <div class="float-chip chip-streak" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-purple)">travel_explore</span>
          <div><b class="rounded">7 apps</b><small>Checked</small></div>
        </div>
        <div class="float-chip chip-done" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-green)">lock</span>
          <div><b class="rounded">Private</b><small>Only you see it</small></div>
        </div>''',
    "features_title": "Clarity, without<br>the guesswork.",
    "features": [
        {
            "size": "two-thirds", "color": "purple", "kicker": "Cross-platform search",
            "title": "One search, every popular app",
            "text": "Checks public profiles across the most popular dating apps at once, so you don't have to sign up to each one.",
            "media": '''            <div class="list" style="max-width: 420px">
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-pink)">favorite</span><div class="main"><b>Dating app 1</b><span>Searched public profiles</span></div><span class="pill" style="--c: var(--accent-green)">Clear</span></div>
              <div class="list-row flag" style="--c: var(--accent-orange)"><span class="badge solid icon" style="--c: var(--accent-orange)">favorite</span><div class="main"><b>Dating app 2</b><span>Possible match · active this week</span></div><span class="pill solid" style="--c: var(--accent-orange)">Review</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-purple)">favorite</span><div class="main"><b>Dating app 3</b><span>Searched public profiles</span></div><span class="pill" style="--c: var(--accent-green)">Clear</span></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">more_horiz</span><div class="main"><b>4 more apps</b><span>All clear</span></div></div>
            </div>''',
        },
        {
            "size": "third", "color": "blue", "kicker": "Targeted matching",
            "title": "Just the right person",
            "text": "Narrow the search by name, age and area to cut out lookalikes.",
            "media": '''            <div class="list" style="max-width: 260px">
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">person</span><div class="main"><span>Name</span><b>Alex</b></div></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">cake</span><div class="main"><span>Age</span><b>29 – 33</b></div></div>
              <div class="list-row"><span class="badge icon" style="--c: var(--accent-blue)">location_on</span><div class="main"><span>Area</span><b>Canggu · 10 km</b></div></div>
            </div>''',
        },
        {
            "size": "full", "color": "orange", "kicker": "Clear reports",
            "title": "A straight answer, and what to do next",
            "text": "Get a simple summary of any active profiles, how confident the match is, and when it was last active, plus guidance for the conversation that follows.",
            "media": '''            <div class="stat-tiles" style="max-width: 520px; grid-template-columns: repeat(3, 1fr)">
              <div class="stat-tile"><div class="num">7</div><div class="lbl">Apps checked</div></div>
              <div class="stat-tile"><div class="num" style="color: var(--accent-orange)">1</div><div class="lbl">Possible match</div></div>
              <div class="stat-tile"><div class="num">7<small>days</small></div><div class="lbl">Last active</div></div>
            </div>''',
        },
    ],
    "faq": [
        ("How does Lotus E-2 search?",
         "It looks only at information dating apps make publicly visible, using the details you provide. It doesn't log in to anyone's account or access private messages."),
        ("Will the person know I searched?",
         "Your searches and reports are private to you. We don't contact or notify anyone."),
        ("Is a match proof of cheating?",
         "No. A profile might be old, fake or someone who looks similar. Treat results as a starting point for an honest conversation, not a verdict."),
        ("Is this legal?",
         "Lotus E-2 only uses publicly available information. You agree to use it responsibly and lawfully, never to harass or stalk anyone."),
    ],
    "values_title": "Answers, handled with care",
    "values": [
        ("public", "blue", "Public info only", "We only look at what dating apps already show publicly. No hacking, no account access."),
        ("lock", "purple", "Private to you", "Searches and reports are visible only to you, and you can delete them anytime."),
        ("favorite", "pink", "Built with empathy", "Clear, gentle reports and guidance, because this is hard enough already."),
    ],
    "cta_title": "Get the clarity you deserve",
    "cta_sub": "Join the waitlist and be first to try Lotus E-2.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus E-2 is in development: an iPhone app that checks popular dating apps for active public profiles, so you can get clarity about your relationship.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>One search across popular dating apps</li>
          <li>Targeted matching by name, age and area</li>
          <li>Clear reports with match confidence and last-active time</li>
        </ul>
        <p>We're working through how to do this using only public information, in a way that respects everyone's privacy.</p>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Technical approach", "Working out how to search public profiles reliably and responsibly."),
        ("", "User interviews", "Learning what people need when they're unsure about a relationship."),
        ("", "App Store review", "Making sure the app meets App Store guidelines."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-e2.app",
    "contact_topics": ["General question", "Feature idea", "Remove my information", "Press"],
    "privacy_intro": "Lotus E-2 deals with sensitive questions, so we take privacy seriously for both you and the people you search for. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Your searches (once the app launches)", '''        <p>The details you enter and the reports you receive are private to you. We use them only to run your search, and you can delete them at any time. We never notify the person you search for.</p>'''),
        ("People who are searched for", '''        <p>We only use information that dating apps make publicly visible. If you believe your information appears in Lotus E-2 and you'd like it removed, contact us and we'll act on it promptly.</p>'''),
    ],
    "terms": [
        ("Responsible use", '''        <p>Use Lotus E-2 only to look up a current partner or someone you're dating, and only for your own peace of mind. Don't use it to harass, stalk, threaten, embarrass or monitor anyone, or for any purpose that's illegal where you live. We may suspend access for misuse.</p>'''),
        ("Results", '''        <p>Results are based on public profile information and may be incomplete, outdated or mistaken. A possible match isn't proof that someone is using a dating app or being unfaithful. Lotus E-2 isn't affiliated with or endorsed by any dating app.</p>'''),
    ],
}
