# Module handoffs

## Backoffice input

Search the sibling `backoffice/deliverables/integration-kit/portable/manifest.json` before asking for login routes or public integration contracts. Accept schema `backoffice-builder.integration-kit.v1` only. Install it immutably under `_inputs/integration-kit/<packet-id>/`, update `current.json`, and verify safe paths, symlinks, unique entries, every file hash, and the manifest hash before use.

Use only consumer-safe material: public routes, login entry points, public API/event contracts, environment-variable names without values, shared terminology, permitted assets, licenses, and limitations. Never use a service-role key, private endpoint, production record, internal note, or implicit authorization from a packet.

## Design output

After the visual direction and implementation are approved, a sibling module may consume a sanitized design kit. Package `deliverables/design-kit/portable/` with schema `premium-landing.design-kit.v1` and include only applicable:

- approved design tokens and typography stacks;
- reusable licensed brand/graphic assets not already canonical in the brand kit;
- visual grammar, density, hierarchy, border/radius/shadow, and motion rules;
- responsive principles and accessibility constraints;
- source/rights notes and material deviations from the brand kit.

Do not export page composition as a mandatory Backoffice layout, framework-specific components, private notes, rejected references, copied proprietary assets, credentials, or customer data.

The manifest needs `schema`, `packet_id`, `created_at`, `source_release`, and a non-empty `files` array. Each file entry requires a unique safe POSIX `path`, lowercase SHA-256, and semantic `role`.
