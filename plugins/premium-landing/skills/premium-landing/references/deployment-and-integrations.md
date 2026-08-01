# Deployment and integrations

## Hosting

Use Cloudflare Pages as the default deployment target for new Astro landing pages. Keep the project portable and choose another provider only when a material project requirement makes it clearly superior. Never enable a paid service or usage-based billing without explicit approval.

For an existing project, preserve its compatible preview and production workflow. Before any remote action, verify authentication, account, project, branch, domain, billing implications, and the immutable commit to deploy. Use per-client least-privilege credentials and compare the target against `.premium-landing/project-state.md`.

Use the operator-managed model by default: source repositories, Cloudflare projects, deployment configuration, and operational integrations remain in the user's accounts because clients are generally non-technical. Isolate every client in a separate private repository, Pages project, secrets set, analytics property, and integration configuration. Never reuse credentials or expose one client's data to another.

Keep every project exportable and document the domain owner, renewal payer and date, service ownership, recurring costs, recovery contacts, and transfer procedure. If domains are also held in the operator's account, require written clarity on beneficial ownership and exit/transfer terms. Protect central accounts with strong unique credentials, MFA, recovery codes, billing alerts, and tested backups because one account failure can affect every client.

## Preview, revision, and approval

Use the project's remote preview deployment as the official client-review environment so approval covers the same immutable build bundle that will reach production. Use Cloudflare previews by default for new compatible projects. Prefer native artifact promotion; otherwise retain the exact built output and deploy it without rebuilding. Record a deterministic bundle digest and a public-build fingerprint covering the lockfile, runtime version, build command, and public build-time variables. Record preview and production binding manifests separately without secret values, plus the explicitly allowed delta between them. If the provider rebuilds, the bundle/public fingerprint changes, or a binding change falls outside the approved delta, treat it as a new artifact or configuration requiring validation and approval. Keep production unchanged throughout review.

Force local and preview environments to emit `noindex, nofollow`; exclude preview URLs from production sitemaps and never canonicalize a preview to itself as though it were production. A password or obscure URL is not an indexing control.

- Record each review round's commit SHA, bundle digest, public-build fingerprint, binding-manifest ID, deployment ID, URL, target account/project, date, and approval state; preserve enough history to compare or restore prior work.
- Accept feedback through low-friction channels such as WhatsApp or email; clients may annotate screenshots when location is ambiguous.
- Consolidate scattered or conflicting comments into one interpreted change set before editing. Flag requests that materially affect scope, conversion, accessibility, performance, cost, or the approved direction.
- After each round, provide a new preview and a concise change summary. Recheck affected desktop and mobile behavior instead of assuming the change is isolated.
- Treat client approval as approval of that exact deployment ID and commit, not permission to deploy. Any artifact change invalidates approval. Require an explicit `PUBLICAR` instruction from the operator before changing production.
- Protect previews from public access by default. Make one publicly accessible only after an operator opt-in and a review confirms it contains no secrets, personal data, confidential information, unfinished legal claims, or unauthorized assets. Prefer identity-based access for client review.

## Post-deployment

Immediately after publishing, verify the live domain, TLS, preferred-host redirects, primary journeys, forms and delivery, analytics events, desktop and mobile rendering, and performance-sensitive behavior. Verify production title and description, absolute canonical, robots policy, sitemap, structured data, Open Graph/Twitter tags, public 1200×630 social image, and a representative live link preview. Enable indexation only after those checks pass and the operator has authorized the production launch. When authorized access exists, submit the sitemap or request indexing in the relevant search console; record missing access as a follow-up and never promise ranking or inclusion. Do not assume a successful deployment means a successful launch.

Complete the search-engine handoff automatically when the scoped credentials and independently confirmed domain authority permit it:

- verify or reuse the exact production-domain property in Google Search Console and Bing Webmaster Tools without transferring ownership or exposing verification secrets;
- submit the canonical sitemap, inspect the home page and other agreed critical URLs, request indexing when the service supports it, and record the returned state;
- enable IndexNow only for sites with recurring additions, updates, or removals when the hosting integration is trustworthy and adds operational value;
- when a local business requires Google Business Profile work, create, claim, or configure only the independently confirmed profile and business after the operator authorizes that external action, then pause for any owner, postal, phone, video, or identity verification Google requires;
- never report submission, crawl, indexation, rich-result eligibility, profile verification, ranking, or AI citation as equivalent states.

After `PUBLICAR`, create bounded post-launch monitoring when a supported automation mechanism is available. Recheck the canonical home page and agreed critical URLs through the authorized consoles until they are indexed or an actionable blocker is documented; also inspect sitemap processing, selected rich-result reports, Core Web Vitals when field data becomes available, manual actions, and security issues. Stop the indexation monitor when the expected state is confirmed or operator input is required; do not create an endless monitor. If automation or credentials are unavailable, write the exact pending checks and responsible account to `.premium-landing/closeout.md` rather than claiming completion.

Fix defects introduced by the delivered implementation without treating them as a new design iteration. Treat later requests for copy, sections, behavior, integrations, or visual changes as a new revision cycle: work locally, validate internally, issue a client preview, obtain approval, and require the operator's explicit `PUBLICAR` instruction. Preserve the last known-good production version and keep rollback practical.

When a proposal, contract, or support agreement is available, use it as the authority for warranty and maintenance boundaries. Classify incoming requests as delivered-work defects, new changes, or uncertain scope, and flag uncertain cases to the operator before acting. Never invent commercial terms, warranty periods, included hours, prices, or service commitments. Treat uptime, form-delivery, domain-renewal, and periodic technical monitoring as optional recurring services unless the supplied agreement says otherwise.

## Closeout record

After launch, write `.premium-landing/closeout.md`, a concise operator-facing record that does not require reading code. Include the production and repository URLs; domain ownership and renewal details; the accounts, services, integrations, and secrets locations used without exposing secret values; verified form destinations and analytics events; Search Console/Bing property and sitemap state; indexation-monitor state; conditional Google Business Profile or IndexNow state; recurring costs and renewal dates; the deployed version and deterministic rollback deployment ID/commit; known limitations, unresolved dependencies, and any client-owned actions still pending. Keep client records isolated and update the record after material production changes.

## Conversion destinations

Choose according to the client's actual sales process. Prefer existing destinations such as WhatsApp, email, booking, checkout, or CRM. For a new contact form on Cloudflare, use a Pages Function or Worker, strict server-side schema and length validation, an origin allowlist, rate limiting, and abuse protection such as Turnstile verified server-side against the expected hostname/action. Use idempotency where duplicate submissions are possible and redact tokens and personal data from logs and error responses. Send through a transactional provider such as Resend. A professional mailbox such as Google Workspace receives and answers messages; it does not replace transactional delivery.

Do not add D1 by default. Use durable storage or a queue only when lead persistence, retries, recovery, history, a dashboard, or later CRM integration justifies the added personal-data and operational burden. Collect the minimum data, define retention, protect access, and never represent an email as delivered merely because an API accepted it. Define the success contract, test the real destination end to end, and add failure visibility appropriate to the client's reliance on the form.

## Analytics

Use the smallest measurement setup that answers the business question:

- start with Cloudflare Web Analytics when basic traffic measurement is sufficient;
- measure meaningful conversion events such as WhatsApp, email, booking and CTA clicks, and confirmed form submissions;
- add GA4 when the client needs deeper acquisition or funnel analysis;
- add advertising pixels only for active campaigns that require them;
- implement consent controls when required by the trackers, audience, or applicable law;
- when applicability is unresolved, block non-essential trackers and cookies until affirmative consent, provide revocation, and verify that no pre-consent requests occur.

Do not install trackers speculatively. Document what each tracker measures, who receives the data, and how it was verified.

## Privacy and legal boundaries

Inventory the actual personal data, cookies, trackers, processors, retention, and transfer destinations before drafting notices or consent controls. Tailor privacy and cookie text to that implementation; do not copy generic policies or invent a legal entity, address, lawful basis, retention period, user right, guarantee, or consent.

Ask about operating and audience jurisdictions only when the answer materially changes the implementation. If unavailable, choose the least invasive setup, document the uncertainty, and mark any legal text that requires client or professional review. Require qualified review for regulated or high-risk contexts such as health, finance, children, sensitive personal data, or jurisdiction-specific compliance. Treat generated legal text as an implementation draft, never legal advice.
