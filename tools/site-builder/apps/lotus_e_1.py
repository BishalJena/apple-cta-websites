"""Lotus E-1: strip hidden metadata from photos and videos before posting."""

APP = {
    "name": "Lotus E-1",
    "title": "Remove hidden data from photos before you post",
    "description": "Lotus E-1 strips location, time and device details from your photos and videos before you share them online. Join the waitlist.",
    "brand": "var(--accent-mint)",
    "brand2": "var(--accent-blue)",
    "icon": {
        "from": "#3fd6c4", "to": "#0f8f9c",
        # photo frame with mountains and a sparkle
        "glyph": '<rect x="26" y="32" width="68" height="56" rx="10"/><path d="m30 80 18-20 14 14 10-9 18 15"/><circle cx="74" cy="50" r="5"/>',
    },
    "status": "Coming to iPhone",
    "h1": "Share the photo.<br>Not the details.",
    "sub": "Photos carry hidden data like where you were, when, and on what device. Lotus E-1 removes it before you post.",
    "hero": '''        <div class="phone" role="img" aria-label="Lotus E-1 showing a photo with its location, date and camera details removed">
          <div class="phone-screen ui">
            <div class="screen-header"><h3>Photo</h3><span class="pill" style="--c: var(--accent-green)"><span class="icon">check</span>Ready</span></div>
            <div class="photo sunset"><span class="tag-chip"><span class="icon">location_off</span>Location removed</span></div>
            <div class="list">
              <div class="meta-row removed"><span class="icon">location_on</span><span class="k">Location</span><span class="v">-8.6705, 115.2126</span></div>
              <div class="meta-row removed"><span class="icon">schedule</span><span class="k">Date and time</span><span class="v">Oct 4, 18:42</span></div>
              <div class="meta-row removed"><span class="icon">photo_camera</span><span class="k">Device</span><span class="v">iPhone · 24 mm</span></div>
              <div class="meta-row removed"><span class="icon">tag</span><span class="k">Hidden IDs</span><span class="v">3 fields</span></div>
            </div>
            <div class="big-button" style="--c: var(--brand); color: #04312c"><span class="icon">ios_share</span>Share clean copy</div>
            <div class="tabbar" aria-hidden="true"><span class="on"><span class="icon">auto_fix_high</span>Clean</span><span><span class="icon">photo_library</span>Library</span><span><span class="icon">settings</span>Settings</span></div>
          </div>
        </div>
        <div class="float-chip chip-streak" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-red)">location_off</span>
          <div><b class="rounded">GPS gone</b><small>Before you post</small></div>
        </div>
        <div class="float-chip chip-done" aria-hidden="true">
          <span class="chip-icon icon" style="--c: var(--accent-green)">verified_user</span>
          <div><b class="rounded">23 fields</b><small>Removed</small></div>
        </div>''',
    "features_title": "Post freely.<br>Keep the details to yourself.",
    "features": [
        {
            "size": "two-thirds", "color": "mint", "kicker": "Metadata stripping",
            "title": "Removes what you can't see",
            "text": "GPS location, timestamps, camera model, lens and software details are wiped from photos and videos, leaving just the picture.",
            "media": '''            <div class="hstack" style="align-items: stretch; gap: 14px; width: 100%; max-width: 520px">
              <div class="list" style="flex: 1; min-width: 200px">
                <div class="meta-row"><span class="ui-label" style="flex: 1">Before</span></div>
                <div class="meta-row"><span class="icon">location_on</span><span class="k">GPS</span><span class="v">-8.67, 115.21</span></div>
                <div class="meta-row"><span class="icon">schedule</span><span class="k">Taken</span><span class="v">Oct 4, 18:42</span></div>
                <div class="meta-row"><span class="icon">photo_camera</span><span class="k">Camera</span><span class="v">iPhone</span></div>
                <div class="meta-row"><span class="icon">memory</span><span class="k">Software</span><span class="v">iOS 27.1</span></div>
              </div>
              <div class="list" style="flex: 1; min-width: 200px">
                <div class="meta-row"><span class="ui-label" style="flex: 1; color: var(--accent-green)">After</span></div>
                <div class="meta-row"><span class="icon">location_on</span><span class="k">GPS</span><span class="done icon">check_circle</span></div>
                <div class="meta-row"><span class="icon">schedule</span><span class="k">Taken</span><span class="done icon">check_circle</span></div>
                <div class="meta-row"><span class="icon">photo_camera</span><span class="k">Camera</span><span class="done icon">check_circle</span></div>
                <div class="meta-row"><span class="icon">memory</span><span class="k">Software</span><span class="done icon">check_circle</span></div>
              </div>
            </div>''',
        },
        {
            "size": "third", "color": "blue", "kicker": "Photos and videos",
            "title": "Works on video too",
            "text": "Clean a single photo, a whole album, or a long video in one go.",
            "media": '''            <div class="vstack" style="max-width: 250px">
              <div class="thumbs" aria-hidden="true">
                <div class="photo sunset"><span class="ok icon">check</span></div>
                <div class="photo p2"><span class="ok icon">check</span></div>
                <div class="photo"><span class="play icon">play_arrow</span><span class="dur">0:42</span><span class="ok icon">check</span></div>
                <div class="photo p3"><span class="ok icon">check</span></div>
                <div class="photo p4"><span class="play icon">play_arrow</span><span class="dur">1:15</span><span class="ok icon">check</span></div>
                <div class="photo sunset"><span class="ok icon">check</span></div>
              </div>
              <span class="pill" style="--c: var(--accent-green)"><span class="icon">check_circle</span>48 photos · 2 videos cleaned</span>
            </div>''',
        },
        {
            "size": "half", "color": "purple", "kicker": "Share sheet",
            "title": "Clean as you share",
            "text": "Pick Lotus E-1 from the share sheet and a clean copy goes straight to your favourite app. Your original stays untouched.",
            "media": '''            <div class="panel" style="max-width: 340px; gap: 12px">
              <div class="result-head"><div class="photo sunset" style="width: 52px; aspect-ratio: 1; border-radius: 10px; flex: none"></div><div style="flex: 1"><b style="font-size: 14px">1 photo selected</b><div class="ui-sub">Original stays in your library</div></div></div>
              <div class="hstack" style="justify-content: space-between; flex-wrap: nowrap">
                <span class="eco-tile icon" style="--c: var(--accent-mint); width: 52px; height: 52px; font-size: 26px; border-radius: 14px">auto_fix_high</span>
                <span class="eco-tile icon" style="--c: var(--accent-green); width: 52px; height: 52px; font-size: 26px; border-radius: 14px">chat</span>
                <span class="eco-tile icon" style="--c: var(--accent-blue); width: 52px; height: 52px; font-size: 26px; border-radius: 14px">mail</span>
                <span class="eco-tile icon" style="--c: var(--accent-orange); width: 52px; height: 52px; font-size: 26px; border-radius: 14px">photo_library</span>
              </div>
              <div class="hstack ui-sub" style="justify-content: space-between; flex-wrap: nowrap"><span>Lotus E-1</span><span>Messages</span><span>Mail</span><span>Photos</span></div>
            </div>''',
        },
        {
            "size": "half", "color": "green", "kicker": "On-device",
            "title": "Your photos never leave your iPhone",
            "text": "Everything happens on your device. No uploads, no account, no cloud processing.",
            "media": '''            <div class="vstack" style="gap: 18px">
              <div class="no-upload" aria-hidden="true">
                <span class="tile icon" style="--c: var(--accent-mint)">smartphone</span>
                <span class="link"><span class="icon">close</span></span>
                <span class="tile off icon">cloud_off</span>
              </div>
              <div class="stat-tiles" style="max-width: 300px">
                <div class="stat-tile"><div class="num">0<small>bytes</small></div><div class="lbl">Uploaded</div></div>
                <div class="stat-tile"><div class="num">0</div><div class="lbl">Accounts needed</div></div>
              </div>
            </div>''',
        },
    ],
    "faq": [
        ("What is metadata?",
         "It's hidden information saved inside photo and video files: often the exact GPS location, the date and time, and details about your device. Anyone who downloads the file can read it."),
        ("Don't social apps remove it already?",
         "Some do, some don't, and messaging apps, email and file sharing often keep everything. Lotus E-1 makes sure it's gone before the file leaves your phone."),
        ("Will it change how my photo looks?",
         "No. The picture stays exactly the same. Only the hidden data is removed, and your original stays in your library."),
        ("Are my photos uploaded anywhere?",
         "No. All processing happens on your iPhone."),
    ],
    "values_title": "Privacy you can see",
    "values": [
        ("lock", "blue", "On-device only", "Your photos are processed on your iPhone and never uploaded."),
        ("visibility", "mint", "Show, don't hide", "See exactly what was in each file and what was removed."),
        ("bolt", "orange", "Fast", "Clean a whole album in seconds, right from the share sheet."),
    ],
    "cta_title": "Post without giving yourself away",
    "cta_sub": "Join the waitlist and be first to try Lotus E-1.",
    "release_notes": [
        {
            "tag": "Pre-launch", "date": "October 9, 2026", "title": "The waitlist is open",
            "body": '''        <p>Lotus E-1 is in development: an iPhone app that removes hidden metadata from your photos and videos before you share them.</p>
        <p>Here's what we're building first:</p>
        <ul>
          <li>Removing location, timestamps and device details (EXIF and more)</li>
          <li>Support for photos and videos, one at a time or in batches</li>
          <li>A share sheet action that cleans media as you post it</li>
          <li>Fully on-device processing</li>
        </ul>''',
        },
    ],
    "roadmap": [
        ("done", "Waitlist opens", "This website and early sign-ups."),
        ("now", "Metadata engine", "Removing every known metadata field from photos and videos."),
        ("", "Share sheet action", "Clean media without leaving the app you're posting from."),
        ("", "TestFlight beta", "Early access for people on the waitlist."),
    ],
    "contact_email": "hello@lotus-e1.app",
    "contact_topics": ["General question", "Feature idea", "Partnerships", "Press"],
    "privacy_intro": "Lotus E-1 is a privacy tool, so it's built to collect nothing it doesn't need. This policy explains what we collect through this website today and what the app is designed to do once it launches.",
    "privacy": [
        ("Your photos and videos (once the app launches)", '''        <p>Media you clean is processed entirely on your iPhone. We never upload, view or store your photos or videos, and the app doesn't need an account.</p>'''),
    ],
    "terms": [
        ("Using Lotus E-1", '''        <p>Use Lotus E-1 only with media you own or have the right to share, and in line with the laws where you live and the rules of the platforms you post to.</p>
        <p>We remove all metadata fields we know about, but file formats change and we can't guarantee that every piece of identifying information is removed in every case.</p>'''),
    ],
}
