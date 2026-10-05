# Continue Órbita on PC 2

Repository: https://github.com/sebastianbarreragiuffra-crypto/marketing

Public website: https://orbita-marketing.pages.dev

Verified on 2026-10-05: the stable Pages URL still serves an older version. The current Wrangler account has no accessible `orbita-marketing` project. Deployment requires signing in to the account that owns the existing project; do not create a duplicate. The temporary preview serves the current local files.

The project is a static website: HTML, CSS, JavaScript and local images. No build step is required. This handoff preserves the current pages, assets, mockups, design reviews and local preview/publishing scripts.

## First time on PC 2

1. Install Git and Python 3. Install Node.js if you will publish to Cloudflare from this computer.
2. In a terminal, from the folder where you want to keep the project, run:

   ```powershell
   git clone https://github.com/sebastianbarreragiuffra-crypto/marketing.git
   cd marketing
   ```

3. Open this cloned `marketing` folder as your project. Read `AGENTS.md` for the local design rules and this file for the current state.
4. Start the preview:

   ```powershell
   python live_preview.py --port 8767
   ```

   Open http://127.0.0.1:8767/branches/ for the main website, or http://127.0.0.1:8767/branch-list/ to choose another local branch. Saved changes reload automatically while this terminal is running.

## Moving between computers

Before starting work on either computer:

```powershell
git pull --ff-only origin main
```

When you finish work, save the edited files, then upload them:

```powershell
git add index.html css/navigation.css
git commit -m "Update Orbita website"
git push origin main
```

Replace the example filenames with only the files belonging to your task. Finish and push from one computer before pulling and editing on the other. If pulling reports local changes or conflicting history, resolve those changes before continuing; do not overwrite them. GitHub carries saved, committed project files between the computers.

## Public updates from PC 2

The stable Cloudflare Pages website remains online when PC 1 is turned off. GitHub stores the source; the existing local publisher updates Pages separately.

To publish from PC 2, sign in to the Cloudflare account with access to the existing `orbita-marketing` Pages project:

```powershell
npx --yes wrangler login
python auto_publish.py --watch
```

Leave the publisher running during edits. It watches the project's local Git worktrees and publishes each branch to its own Pages URL after four seconds without another edit. `main` remains at `https://orbita-marketing.pages.dev`; a branch such as `design/hero` appears at `https://design-hero.orbita-marketing.pages.dev`. Refresh the branch URL after Cloudflare finishes publishing. No commit or push is needed for local edits, but the editor must write the file first. To publish the current branch once, run `python auto_publish.py --once`.

Use one publishing computer per branch at a time, so PC 1 and PC 2 do not replace each other's branch version. Authentication and local runtime state are configured separately on PC 2; credentials are excluded from Git. Branches that exist only on GitHub are not watched until checked out in a local worktree.

A `trycloudflare.com` tunnel is a separate temporary link tied to the computer running it. Its URL cannot be transferred by cloning the repository. Start a new tunnel on PC 2 if you need a public preview with immediate reload; use the stable Pages URL after a verified deployment. The current temporary URL is `https://promotions-red-double-volumes.trycloudflare.com/b/main/`; verify that it still responds before reusing it.

## Current design state

### Latest conversation context — 2026-10-05

The latest discussion is in **Continue Órbita website work**. The user clarified that Órbita is the digital agency and uses GISBA software. Do not describe GISBA as software developed by Órbita. The discussion shifted toward including access to GISBA with Marketing, rather than presenting it as an optional extra that the visitor must select.

The user explicitly asked to keep analyzing **without changing the website yet**. The proposed headline is “Gestionamos tus campañas. Tú sabes cómo avanzan.” Supporting copy would explain that GISBA is software for seeing campaign progress and following up with people who contact the business. These exact texts remain candidates, not approved final copy.

The proposed structure preserves the existing hero, places the explanation of GISBA inside Marketing, keeps Diseño Web as a separate service, and ends with a meeting invitation. The later clarification leaves selling GISBA independently through Órbita unresolved; do not carry that earlier assumption forward as a confirmed commercial offer. Included functions, users, setup, extra charges and access after Marketing ends remain to be defined. Booking, authentication and inquiry delivery remain in stand by.

The bullets below describe the implemented website. They do not mean the latest copy and packaging proposals have been implemented or approved. The older local rules still describe GISBA as optional; reconcile them with the latest user decisions when implementation is requested.

- Keep the Órbita brand. Design at 1440 px; at 1920 px keep useful content centered with a maximum width of 1440 px. Verify desktop and mobile before publishing visual changes.
- Keep the existing homepage hero. Its current body is hero → Marketing and Diseño Web → contact invitation, with optional GISBA mentioned below the offers. Moving that mention inside Marketing is a recorded direction, not part of the navigation fix.
- All six pages now share Inicio, Marketing, GISBA and Hablemos, plus the same footer. `css/navigation.css` owns shared header dimensions; Software retains its approved light theme. Page bodies were preserved during this fix.
- Booking, inquiry delivery, authentication and commercial prices remain in stand by. The homepage meeting button remains disabled until a real booking channel is supplied. Pending pages remain directly accessible but outside primary navigation.
- Marketing has exactly three main sections: the hero, the dynamic Meta Ads / Google Ads / Desarrollo Web section, and Contáctanos. The revised light contact card is now installed in the actual page, not only in the separate mockup.
- Contact supports optional, combinable Meta Ads, Google Ads, Desarrollo Web and Software interests; optional business context and company; and one required email or phone field. Its button only reviews the inquiry locally. A receiving service has not been configured.
- The latest Software page includes the hero, consultation flow, reports and final contact section. Its interface, conversations and metrics are illustrative.
- Automatizaciones is hidden from the primary navigation and currently keeps the shared navigation/footer with its main content cleared for redesign. Precios keeps the example plan comparison, with the previous FAQ removed. Earlier page content is saved under `mockups/pre-content-reset-2026-10-04/` and in Git history.
- Login is a visual preview; authentication is not connected. Example prices are not confirmed commercial rates.
- Independent A/B deliberation and decisions are preserved in the Marketing review files, including `MARKETING_CONTACT_2A.md`, `MARKETING_QUALITY_2A.md` and `MARKETING_THREE_SECTIONS_2A.md`. Continue from those decisions instead of restarting the design.

The `.webmaster/` installation, `.preview-sync/`, publishing copies, caches and credentials are local and ignored by Git. Project rules and review documents are included. If you need the local Webmaster workflow on PC 2, install it there before requesting that workflow.
