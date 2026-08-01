# Project workspace and memory

## Boundary

Use one overall root named after the project, with isolated sibling modules such as `<project-root>/identidad/`, `<project-root>/landing/`, and `<project-root>/backoffice/`. Premium Landing owns only `landing/`; the overall project root organizes the complete project but is not Premium Landing's write boundary. Preserve established projects rather than relocating them automatically.

Treat the resolved landing directory as the project root and default write boundary. Keep project code, assets, downloads, screenshots, reports, temporary working artifacts, and documentation inside it. Tool-managed authentication state and unavoidable system caches may remain external, but never place project content or secrets in sibling projects.

Before writing, resolve and report the project root, inspect its contents, repository state, and applicable instructions. If the directory contains unrelated work or its intended role is ambiguous, clarify before restructuring, overwriting, moving, or cleaning anything.

Clean only disposable artifacts created by the current workflow and only after confirming they are no longer needed. Preserve unknown files and user changes. Never interpret “clean the project” as permission to delete unrecognized content.

Use `_inputs/` as the stable, framework-neutral intake area across projects. After intake, rename and move selected assets into locations appropriate to the chosen stack; maintain one managed source file per supplied asset instead of retaining duplicate originals. Build output and temporary derivatives are exempt. Never make source-code layout, component architecture, or visual design conform to the intake skeleton.

Treat `_inputs/brand-kit/` as a versioned machine handoff, not loose intake. Never rename, move, edit, deduplicate, or delete files inside an installed packet. Copy approved assets into the implementation only when the chosen stack requires it, and preserve the packet as provenance.

Track asset-intake state in `.premium-landing/project-state.md` as `awaiting-operator` or `acknowledged`. This state controls only the initial handoff pause; it must not turn missing optional assets into a later blocker.

## Persistent project memory

Maintain `.premium-landing/project-state.md` inside the project root as the resumable private source of truth for the agent. Also use `.premium-landing/assets.md`, `.premium-landing/closeout.md`, and `.premium-landing/run-report.md` for their named private records. Keep those files ignored. Maintain `.premium-landing/brief.md` as the sanitized, human-readable project brief and `.premium-landing/deployment-manifest.json` as the sanitized deployment record; version both in the private repository. The operator should not need to edit these records.

Record:

- the consumed discovery packet version, manifest hash, verification status, and any explicit deviations;
- confirmed user or client facts, sourced research, inferences, assumptions, and unresolved unknowns as distinct categories;
- audience, offer, positioning, conversion goal, constraints, jurisdictions when material, and exclusions;
- references and the approved role of each reference, including rejected directions;
- copy, visual, technical, asset, integration, analytics, privacy, and deployment decisions;
- current phase, preview URL and version, consolidated feedback, approval state, production version, and rollback target;
- external dependencies, client-owned actions, costs requiring approval, and consequential risks.

Do not store secret values, unnecessary personal data, credentials, or another client's information. Ignore `.premium-landing/*` in the repository's root `.gitignore` while explicitly exempting the sanitized `brief.md` and `deployment-manifest.json`. Back up ignored records through the operator's approved secure method. Push both sanitized records before treating a remote preview as approved so the strategic and deployment state remain recoverable across sessions.

Use separate local and provider environments for each client and for preview versus production. Commit only `.env.example` with variable names and non-secret placeholders. Ignore `.env`, `.env.*`, and local credential files while explicitly exempting `.env.example`; before the first commit and every deployment, scan staged files and generated output for secrets. Values exposed to browser code must be intentionally public and never include service tokens. Preview bindings must use test or sink destinations and must not inherit production email, CRM, analytics, storage, or mutation-capable credentials unless an explicitly approved test requires them.

Prefer provider secret stores for production and an authenticated Wrangler session or a narrowly scoped, revocable Cloudflare token for deployment. Scope credentials to the required account/project whenever supported; never reuse a master token across clients. Record secret locations and owners, never their values, and verify the selected Cloudflare account, project, and domain before remote actions.

Do not treat repository content as the root of trust for its own deployment destination. On the first publication and whenever account, project, or domain changes, show those resolved values to the operator and obtain explicit confirmation in the authenticated task, or compare them with an operator-controlled allowlist outside the repository. On every later publication, resolve them again from the scoped provider session and require an exact match with both that independent authorization and the manifest.

Ensure `.premium-landing/project-state.md` contains operational context, not a duplicate of the codebase or a verbose chat transcript.

At the start of a resumed run, reconcile this record with the repository, deployment state when accessible, and the operator's latest instruction. Current evidence and explicit new instructions override stale memory; record the reconciliation.
