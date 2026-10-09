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
    "hero": '''        <div class="phone" role="img" aria-label="Lotus E-3 news feed with short story cards marked as checked across sources">
          <div class="phone-screen ui">
            <div class="screen-header"><h3>Today</h3><span><span class="icon" style="font-size: 13px; vertical-align: -2px">location_on</span> Denpasar</span></div>
            <div class="news-card" style="--c: var(--accent-blue)">
              <div class="photo" style="aspect-ratio: 16 / 6; border-radius: 12px"></div>
              <div class="nc-top"><span class="pill" style="--c: var(--accent-blue)">Local</span><span class="pill" style="--c: var(--accent-green)"><span class="icon">verified</span>4 sources agree</span></div>
              <h4>New bus line connects the airport and Ubud from next month</h4>
              <div class="nc-foot"><div class="sources"><span style="--c: var(--accent-blue)">A</span><span style="--c: var(--accent-orange)">B</span><span style="--c: var(--accent-purple)">C</span><span style="--c: var(--accent-green)">D</span></div><span>12 sec read</span></div>
            </div>
            <div class="news-card">
              <div class="nc-top"><span class="pill" style="--c: var(--accent-purple)">Tech</span><span class="pill" style="--c: var(--accent-green)"><span class="icon">verified</span>3 sources</span></div>
              <h4>Phone makers agree on a longer software support standard</h4>
              <div class="nc-foot"><span>9 sec read</span><span>Tap for more</span></div>
            </div>
            <div class="tabbar" aria-hidden="true"><span class="on"><span class="icon">newspaper</span>Today</span><span><span class="icon">tag</span>Topics</span><span><span class="icon">bookmark</span>Saved</span><span><span class="icon">settings</span>Settings</span></div>
          </div>
        </div>
        <div class="float-chip chip-streak" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-green)">fact_check</span>
          <div><b class="rounded">Checked</b><small>Across 4 sources</small></div>
        </div>
        <div class="float-chip chip-done" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-red)">timer</span>
          <div><b class="rounded">12 sec</b><small>Per story</small></div>
        </div>''',
    "features_title": "Stay informed.<br>Skip the noise.",
    "features": [
        {
            "size": "two-thirds", "color": "red", "kicker": "Bite-sized cards",
            "title": "Every story in under 15 seconds",
            "text": "Each story is summarised into a few clear lines, so you can catch up on the day while your coffee brews.",
            "media": '''            <div class="card-stack">
              <div class="news-card">
                <div class="nc-top"><span class="pill" style="--c: var(--accent-orange)">World</span><span class="ui-sub">8 sec read</span></div>
                <h4>Leaders agree on a new plan to protect coral reefs</h4>
                <p>The agreement sets shared targets for reef protection and funds local monitoring programs over the next decade.</p>
                <div class="nc-foot"><div class="sources"><span style="--c: var(--accent-blue)">A</span><span style="--c: var(--accent-orange)">B</span><span style="--c: var(--accent-purple)">C</span></div><span>Tap for more</span></div>
              </div>
              <div class="news-card" aria-hidden="true"><h4>&nbsp;</h4></div>
            </div>''',
        },
        {
            "size": "third", "color": "green", "kicker": "Multi-source checks",
            "title": "Checked before you see it",
            "text": "Stories are compared across outlets, and we show you how many independent sources agree.",
            "media": '''            <div class="vstack" style="max-width: 240px">
              <div class="stat-tile" style="width: 100%; text-align: center"><div class="num" style="color: var(--accent-green)">4<small>of 4</small></div><div class="lbl">Sources agree</div></div>
              <div class="meter" style="width: 100%"><i style="--w: 100%; --c: var(--accent-green)"></i></div>
              <span class="pill" style="--c: var(--accent-orange)"><span class="icon">info</span>Still developing</span>
            </div>''',
        },
        {
            "size": "half", "color": "blue", "kicker": "Made for you",
            "title": "Your place, your interests",
            "text": "Your feed is tuned to where you live and the topics you pick. Local news included, clickbait left out.",
            "media": '''            <div class="units">
              <span class="unit-chip" style="--c: var(--accent-blue)"><span class="icon">location_on</span>Local</span>
              <span class="unit-chip" style="--c: var(--accent-purple)"><span class="icon">memory</span>Tech</span>
              <span class="unit-chip" style="--c: var(--accent-green)"><span class="icon">eco</span>Climate</span>
              <span class="unit-chip" style="--c: var(--accent-orange)"><span class="icon">sports_soccer</span>Sport</span>
              <span class="unit-chip" style="--c: var(--accent-pink)"><span class="icon">payments</span>Money</span>
              <span class="unit-chip dashed"><span class="icon">add</span>More</span>
            </div>''',
        },
        {
            "size": "half", "color": "purple", "kicker": "Tap to expand",
            "title": "Go deeper in one tap",
            "text": "Tap any story for the full article, the original sources, and how they compare.",
            "media": '''            <div class="list" style="max-width: 320px">
              <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-blue)">article</span><div class="main"><b>Source A</b><span>Full report · 4 min read</span></div><span class="trail icon">open_in_new</span></div>
              <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-orange)">article</span><div class="main"><b>Source B</b><span>Analysis · 6 min read</span></div><span class="trail icon">open_in_new</span></div>
              <div class="list-row"><span class="badge solid icon" style="--c: var(--accent-purple)">article</span><div class="main"><b>Source C</b><span>Live updates</span></div><span class="trail icon">open_in_new</span></div>
            </div>''',
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
