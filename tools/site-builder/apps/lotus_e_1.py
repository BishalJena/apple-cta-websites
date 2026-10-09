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
    "hero_shot": 'Clean photo',
    "hero_note": "No spam. Just one email when it's ready.",
    "chips": [('location_off', 'red', 'GPS gone', 'Before you post'), ('verified_user', 'green', '23 fields', 'Removed')],
    "features_title": "Post freely.<br>Keep the details to yourself.",
    "features": [
        {
            "size": 'third', "color": 'blue', "kicker": 'Photos and videos',
            "title": 'Works on video too',
            "text": 'Clean a single photo, a whole album, or a long video in one go.',
        },
        {
            "size": 'two-thirds', "color": 'mint', "kicker": 'Metadata stripping',
            "title": "Removes what you can't see",
            "text": 'GPS location, timestamps, camera model and software details are wiped, leaving just the picture.',
            "shots": ['Before', 'After'],
        },
        {
            "size": 'half', "color": 'purple', "kicker": 'Share sheet',
            "title": 'Clean as you share',
            "text": 'Pick Lotus E-1 from the share sheet and a clean copy goes straight to your favourite app.',
        },
        {
            "size": 'half', "color": 'green', "kicker": 'On-device',
            "title": 'Your photos never leave your iPhone',
            "text": 'Everything happens on your device. No uploads, no account, no cloud processing.',
        },
        {
            "size": 'two-thirds', "color": 'orange', "kicker": "See what's hidden",
            "title": "Know exactly what you're sharing",
            "text": 'Inspect every hidden field in a photo before you post, from location to device details.',
            "shots": ['Hidden details', 'Location preview'],
        },
        {
            "size": 'third', "color": 'pink', "kicker": 'Batch cleaning',
            "title": 'A whole album at once',
            "text": 'Select dozens of photos and clean them in seconds.',
        },
        {
            "size": 'full', "color": 'indigo', "kicker": 'Simple by design',
            "title": 'Pick, clean, post',
            "text": 'A few taps from your library to a clean copy, ready for any app.',
            "shots": ['Pick', 'Clean', 'Post'],
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
