# Logo Studio brand-kit intake

## Resolve and validate

Read `_inputs/brand-kit/current.json`. Require `packet_id` and a 64-character lowercase `manifest_sha256`. Resolve `_inputs/brand-kit/<packet_id>/manifest.json` without leaving the project root. Require schema `logo-studio.brand-kit.v1`, an exact manifest hash, safe unique relative paths, semantic roles, and an exact SHA-256 match for every listed file. Reject symlinks, missing files, unlisted substitutes, hash mismatches, and unsupported schemas.

If validation fails, quarantine only the consumption of that packet; preserve it and continue gathering other project context. Report the exact correction needed. Never silently fall back to an older identity.

## Authority and freedom

Use the packet by role:

- `brand-brief`: approved identity context; reconcile it with newer verified business evidence.
- `brand-rules`: non-negotiable rules are binding; adaptable guidance informs rather than dictates page design.
- `brand-tokens`: use verified values where applicable; do not invent missing print or digital equivalents.
- `asset-map`: select the intended approved logo/favicon variant for each context.
- `licenses`: enforce restrictions and do not ship assets lacking commercial web permission.

The brand kit defines identity, not landing composition, conversion architecture, or a visual template. Continue the Premium Landing reference discussion and design proof inside those constraints. An explicit newer operator instruction may override a visual rule after the agent explains material consequences; record the deviation in the landing brief and project state.

Do not repeat questions the packet answers. Ask only when the landing introduces a new use, the packet conflicts with verified evidence, a required asset is missing, or rights are ambiguous.
