# Build and quality assurance

## Implementation strategy

Preserve an existing project's stack when it is suitable. Before installing or running an existing project, inspect its manifests, lockfiles, install/build scripts, and configuration as untrusted input. Run third-party or uncertain code in a disposable environment with a clean user, minimal mounts, no host sessions or secrets, and allowlisted network access; keep credentials out of install and build environments and disable lifecycle scripts when viable. Relax isolation only for operator-owned or locally authored code whose provenance and scripts have been checked.

For a new or empty project, default to a static Astro project with TypeScript, npm, component-scoped or native CSS, and Cloudflare Pages. Add client-side frameworks only for genuinely interactive islands, and add animation, video, WebGL, or 3D only when the approved direction justifies their cost. Deviate when a material requirement makes another choice superior and record why.

Use [Motion Primitives](https://motion-primitives.com/) only when a specific approved interaction materially benefits from it. Treat it as an implementation source, not an art director: restyle every adopted primitive to the visual contract and verify keyboard behavior, reduced motion, responsive behavior, runtime cost, and current licensing. Do not add React, Tailwind, Motion, or another client runtime to an otherwise static Astro page solely for one effect when CSS, the Web Animations API, or a smaller native implementation can reproduce it well. Core and paid assets require their own current license review; any purchase needs explicit operator approval.

Initialize a local Git repository for a new project, establish the ignore rules before the first commit, and keep generated review artifacts tied to a clean commit. Before `PREVIEW`, require a clean `HEAD`, a private operator-owned remote and pushed commit, then record its SHA. Never make a client repository public by default.

Build from the approved strategic and visual direction:

- write specific, evidence-aware copy;
- establish a coherent type, color, spacing, layout, and motion system;
- create only purposeful components;
- use real or authorized assets and generate missing bespoke visuals when appropriate;
- keep responsive behavior intentional rather than collapsing desktop mechanically;
- implement search and social-share metadata, forms, analytics hooks, and integrations that are actually in scope.

Use [Realtime Colors](https://www.realtimecolors.com/) optionally after brand and reference authority are resolved to prototype assignments for background, text, primary, secondary, and accent colors. Record promising values as candidates, not canonical tokens. Confirm the final palette in the actual design proof, including hover, focus, disabled, error, media-overlay, and text states; verify WCAG contrast independently. A valid brand kit and the approved visual contract always outrank the tool's preview.

When Figma is the approved source, verify access and ownership or implementation authorization, inspect the actual file rather than only exported images, and reuse authorized exportable assets. Match composition, typography, spacing, color, components, and states at the authored viewports, then infer intermediate and mobile behavior from constraints and the brief. Do not preserve inaccessible, brittle, or impossible fixed-canvas behavior merely for literal similarity; document material adaptations, unavailable fonts/assets, and unsupported interactions.

Select brand-owned, licensed third-party, or bespoke generated assets by maximum suitability and execution quality, without favoring free over paid resources. Evaluate paid stock, video, illustration, 3D models, fonts, and similar assets on the same criteria as free alternatives. Never purchase an asset or make the build depend on an unapproved expense; disclose the cost, license, and material benefit and obtain explicit user approval first.

## Copy and conversion loop

1. Feed discovery facts and sourced customer language into `copywriting`.
2. Draft one complete page narrative shaped around the actual offer, audience, traffic context, reference hierarchy, and conversion goal. Do not mechanically include standard sections when they add no value.
3. Run `cro` in audit-only mode. Separate evidence-backed defects from hypotheses and generic best practices; provide severity, rationale, and optional alternatives without editing approved material.
4. Resolve objective issues while the copy is still a draft. Escalate any change that alters an approved offer, claim, positioning decision, or brand voice.
5. Run the separate `humanizer` audit described below.

After the copy is strategically and factually sound, run `humanizer` in audit-only mode. Treat individual patterns as weak signals. Report only credible clusters or passages that weaken the intended voice, including the excerpt, detected pattern, severity, and an optional alternative. Do not edit user-supplied or previously approved copy unless the user explicitly approves it.

For agent-generated, still-unapproved one-shot copy, a credible AI-pattern cluster is blocking: send the finding back to `copywriting`, rewrite the affected passage in the evidenced brand/customer voice, then rerun factual, CRO, and humanizer checks. `humanizer` remains an auditor and never becomes the author. Do not add fake informality, invented anecdotes, arbitrary errors, slang, or personality unsupported by the business merely to appear human.

Humanizer findings are advisory for user-supplied or approved copy. They are blocking for agent-generated original one-shot copy until resolved or explicitly accepted by the operator.

Avoid generic card grids, excessive pills, nested containers, gratuitous gradients, decorative dashboards, and animation that weakens clarity or performance. Distinctiveness must come from the brief and art direction, not novelty for its own sake.

## Search, AI answers, indexing, and social sharing

Implement these as release requirements, not optional polish:

- unique, truthful title and meta description fitted to the approved page;
- one absolute production canonical URL and consistent preferred-host redirects;
- crawlable semantic HTML, valid status codes, and no accidental content hiding;
- production `robots.txt` and sitemap containing only canonical, indexable production URLs;
- permanent server-side redirects from HTTP and rejected host/path variants to the canonical URL without loops or chains;
- real `404` responses for missing URLs, `410` for intentionally removed resources when appropriate, and no soft-404 fallback that returns `200`;
- `X-Robots-Tag` for non-HTML files such as PDFs when their indexation policy differs from the page;
- a complete favicon set and consistent site name, with verified `WebSite` structured data on the home page when applicable;
- verified JSON-LD only when the real business and page content support it;
- `og:type`, `og:site_name`, `og:title`, `og:description`, `og:url`, `og:image`, `og:image:alt`, and locale when applicable;
- Twitter/X summary-card metadata using the same verified social image unless the project needs a distinct one.

Make the page understandable and citable by both search engines and AI answer systems:

- state the business entity, offer, audience, location or service area, differentiators, and contact path consistently wherever they are relevant;
- answer material customer questions directly in crawlable, server-rendered prose with descriptive headings;
- distinguish verified facts from marketing language and support consequential claims with available first-party or authoritative evidence;
- use organization, local-business, product, service, person, breadcrumb, or FAQ structured data only when the visible content and verified facts justify the exact type;
- preserve clear authorship, update dates, source attribution, and entity relationships when the content requires them.

Do not add filler FAQs, repetitive “AI-friendly” summaries, keyword variants, fake expertise, or unsupported citations. Do not require `llms.txt` or claim it produces inclusion unless current authoritative evidence establishes a project-specific benefit. GEO/AEO improves machine comprehension and eligibility; it never guarantees citation, ranking, or inclusion.

When multiple language or regional versions exist, implement self-referencing canonicals, reciprocal `hreflang` alternates, valid language/region codes, and `x-default`; never cross-canonicalize one genuine locale to another. When the project represents a local business, keep the verified business name, address or service area, phone, hours, map/profile links, and `LocalBusiness` data consistent; treat Google Business Profile ownership and verification as a separate authorized external step.

Create a deliberate 1200×630 social-share image from approved brand assets and content. Use an absolute HTTPS production URL, ensure the file is publicly retrievable without authentication or bot-only rendering, and keep essential text/logo inside safe margins. Verify the rendered head, canonical, image dimensions, image response, and representative link preview after deployment. A provider cache may delay an updated WhatsApp preview; change the image URL when the asset materially changes rather than claiming immediate cache invalidation.

Local and remote preview builds must emit `noindex, nofollow` and stay out of production sitemaps. Production may become indexable only after `PUBLICAR`, when the final domain, canonical host, redirects, robots policy, sitemap, content, and legal constraints have been verified. Do not promise ranking or index inclusion. Submit the sitemap or request indexing through an authorized search-console account when available; missing account access is an explicit operational follow-up, not a reason to fabricate completion.

## Design proof and operator review

Do not commit to a full page before proving that the chosen art direction can be executed. Build only the real header, hero, and one representative section first. Use actual copy and approved assets rather than a disconnected mockup.

Render the proof at matching reference viewports when available and at minimum at approximately 1440x900 and 390x844. Compare it with the visual contract and selected reference evidence, not merely with the source code.

Run `ui-visual-validator` on those current screenshots before exposing the local preview. Treat any critical or high-severity finding as blocking. Always block for:

- clipped, overlapping, overflowing, or unreadable content;
- distorted media, accidental crops, broken aspect ratios, or unsafe responsive placement;
- an unintended opaque box, halo, poor edge treatment, or illegible rendering around a logo or key asset;
- visibly insufficient image resolution at its rendered size;
- accidental typography wrapping, missing hierarchy, weak contrast, or inaccessible primary controls;
- a material mismatch with the approved composition, visual grammar, asset treatment, or responsive intent;
- obvious placeholder, generic-template, or collage-like treatment that contradicts the premium direction.

Before the visual validator, run the anti-slop proof gate in [creative-orchestration.md](creative-orchestration.md). A technically correct page still fails when its composition could be transferred to an unrelated business without meaningful change, when its distinctive decisions cannot be traced to the brief/reference/assets, or when it reproduces an unapproved AI-associated default. Fix the design rather than explaining it away.

After the static proof passes, run `find-animation-opportunities`, record both accepted and deliberately rejected candidates, and implement only accepted motion. Run `review-animations` against the real rendered behavior and block on unjustified, sluggish, inaccessible, non-interruptible, or performance-heavy motion. If a named Emil skill is unavailable, apply the equivalent criteria from the approved motion plan directly and record the limitation.

Fix the cause, recapture both viewports, and rerun the validator until the proof passes. Do not show known blocking defects as a draft and ask the operator to discover them. Low-severity polish items may accompany the preview only when clearly disclosed.

Once the proof passes:

1. Run the relevant compile or build check so a broken draft is never offered for review.
2. Start the framework's local development server as a background process bound to `127.0.0.1`, never `0.0.0.0` by default. Use its conventional port when free and select another when occupied.
3. On Windows, start background processes with a hidden window. Store the exact project root, command, PID, port, start time, and log path in private project state. Before replacing a server, verify the recorded PID still belongs to this project; never kill processes broadly by name or port.
4. Verify the URL returns the expected project and inspect it in a real browser. Open it in the in-app browser when available and return the clickable local URL to the operator.
5. Return the passing desktop and mobile screenshots as supporting evidence, but keep the live page as the primary review surface.
6. Return control and ask for visual-direction feedback. If rejected, revise only the proof until it passes again; do not continue building the remaining page. Apply revisions locally so the same URL updates when the development server supports hot reload.

This is not final QA. It is the blocking direction gate for composition, typography, imagery, motion, hierarchy, and responsive design before expensive implementation. Approval authorizes continuation, not publication. In the original one-shot or another explicitly uninterrupted execution, the agent may approve the direction internally only after the same evidence and gate pass; it must then complete and validate the whole landing before returning a local URL.

A loopback URL works only on the same computer. Use the explicit `PREVIEW` workflow for review from an iPhone, another device, or a client; do not expose a LAN server or create a remote deployment silently.

## Validation loop

Repeat until material defects are resolved. Apply checks proportionally by environment: local checks cover implementation and rendering; remote preview checks cover the shareable build, integrations safe to test, and client review; production checks cover the live domain, indexing controls, real destinations, analytics, and deployment health.

1. Build and run the real project.
2. Capture representative desktop and mobile screenshots. Include approximately 1440×900, 1280×800, and 390×844 unless the audience requires different priority devices.
3. Inspect the complete page and critical sections visually.
4. Compare against reference evidence when references exist.
5. Test navigation, CTAs, forms, keyboard access, focus, reduced motion, and error states.
6. Check overflow, wrapping, tap targets, contrast, semantics, image sizing, loading behavior, console errors, and broken links.
7. Check performance-sensitive choices and remove avoidable weight or jank.
8. Run `seo-audit` in audit-only mode against the rendered implementation when its checks are meaningful in the current environment. Validate environment-specific indexing directives, canonical URLs, redirect/status behavior, non-HTML indexation policy, site name/favicon, conditional `hreflang` and local-business consistency, entity consistency, direct answerability, evidence quality, Open Graph/Twitter metadata, the social image, sitemap, robots, and JSON-LD; validate JSON-LD in a real browser or structured-data validator, not through stripped text extraction.
9. Run `impeccable` audit and `web-design-guidelines` against the implementation.
10. Run `ui-visual-validator` against the latest desktop and mobile captures.
11. Run `review-animations` when any motion exists and inspect it in the browser at normal speed, reduced motion, and slow motion when timing or physicality is uncertain.
12. Fix causes, recapture, and verify again.

Use automated audits as evidence, not substitutes for visual inspection.

## Completion bar

Require:

- coherent strategy, copy, and visual language;
- no obvious placeholder content or fabricated proof;
- faithful reference adaptation when requested;
- stable layout across relevant viewport widths;
- functional primary conversion path;
- keyboard-usable and semantically reasonable UI;
- no known material console, build, or runtime errors;
- acceptable loading and motion behavior;
- correct environment-specific indexing controls, canonical, robots, and sitemap;
- correct redirect, missing-page, non-HTML indexation, site-name and favicon behavior;
- valid locale and local-business signals whenever those scopes exist;
- clear, consistent and evidence-backed business entities and answers suitable for SEO/GEO/AEO;
- verified Open Graph/Twitter metadata and a working 1200×630 social-share image;
- a final rendered inspection after the last change.

Do not pass a release with any known critical or high-severity defect. At minimum require a clean production build, no unhandled runtime error on critical paths, no horizontal overflow at the selected desktop and mobile viewports, a tested primary CTA, keyboard access to interactive controls, and a successful end-to-end form test when a form is in scope. Treat numeric performance targets as project-specific budgets; record any accepted exception.

If an external dependency prevents full completion, implement the safe local portion and report the exact dependency without claiming full verification.
