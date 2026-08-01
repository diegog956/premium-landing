# Adaptive discovery

## Purpose

Learn enough to make every consequential landing-page decision without forcing the user through a fixed form.

## Maintain a working model

Continuously track:

- user-provided facts;
- externally verified facts;
- inferences with confidence;
- unresolved contradictions;
- decisions already safe to make;
- high-impact uncertainties still requiring action.

Use offer, audience, market, conversion, proof, objections, brand, content, assets, references, legal constraints, and technical constraints as diagnostic lenses, not mandatory question categories.

## Consume a frozen discovery packet

When `.website-discovery/portable/manifest.json` exists:

1. Verify every listed portable file and SHA-256 hash before trusting it.
2. Treat approved facts, constraints, forbidden claims, and delegated decisions as canonical inputs.
3. Import unresolved unknowns as unknowns; do not convert them into facts.
4. Do not reopen answered questions unless current evidence creates a material contradiction.
5. Keep evaluator-only rubrics out of the generation context when the comparison protocol marks them blind.

If verification fails, isolate the affected claim and continue where safe. Ask for regeneration or clarification only when the failure could materially affect truthfulness, legality, conversion, or the fairness of a controlled comparison.

## Choose the next question

Prioritize a question when all are true:

1. Its answer could materially change strategy, copy, structure, visual direction, scope, or safety.
2. Current uncertainty is meaningful.
3. The user is a better source than public research or professional judgment.

Prefer concrete language and one topic at a time. Group only tightly related questions. Do not ask users to translate their needs into design jargon.

Use reference comparisons when visual preferences are hard to verbalize.

## Handle unavailable answers

When the user says they do not know or cannot provide something:

1. Research it when externally discoverable.
2. Infer it when evidence supports a reasonable conclusion.
3. Choose a conventional default when the downside is low.
4. Generate the missing material when authorized and appropriate.
5. Omit it when an unsupported claim would be riskier than its absence.

State only important assumptions. Never stall over a low-impact unknown.

Require user input only for facts or authority that cannot safely be invented, such as regulated claims, confidential business facts, ownership or licensing, irreversible external actions, or credentials needed for a required integration.

## Recommend references during discovery

Once audience, offer, desired perception, conversion model, and content density are reasonably understood, search for references. Present three strong candidates and at most one deliberate wildcard.

Put them in a standalone `Opciones visuales para elegir` block. Do not blend this block into the business synthesis or silently elect competitor and official-business sites as design authorities.

For each candidate state:

- direct preview URL and source platform;
- why it fits;
- what role it could play;
- what should not be copied;
- distinctive typography and composition signals;
- likely implementation cost or risk;
- whether it is a live site, archived reference, free template, or paid template;
- licensing or purchase requirement when applicable.

Name the recommended option while preserving the operator's choice. Reject candidates whose main appeal is a generic AI pattern, fashionable effect, or default font rather than a coherent fit with this business. If no candidate clears the quality bar, say so and propose original art directions instead.

Keep this block open across turns. When the operator asks for better or different options, infer the dissatisfaction from their comments, ask one short calibration question only if the direction is genuinely ambiguous, and otherwise return a materially stronger or different set. Do not advance, recycle rejected candidates, or treat silence as approval.

Allow composite selection: one base may govern the visual grammar while specific candidates contribute named roles such as hero, navigation, motion, cards, or footer. Close only through explicit selection, delegated judgment, an explicit no-reference decision, or an uninterrupted one-shot instruction.

## End discovery

Stop asking when no unresolved, user-exclusive uncertainty could materially improve the result enough to justify another interruption. This is not a minimum-information rule: research and professional inference must have resolved the rest.

Produce a compact synthesis of facts, decisions, material assumptions, exclusions, reference hierarchy, and missing assets that will be created or omitted.

“One-shot” means producing a complete first delivery after sufficient adaptive discovery, not inventing an unknown business or forcing a minimum questionnaire. If the operator explicitly requests immediate execution, ask no preference questions and proceed with researched or safe assumptions; ask only for a user-exclusive fact or authority without which a truthful, lawful, or operational result cannot be produced.

If a new empty project has no discoverable business identity, offer, or conversion destination, ask once for the business/offer and primary CTA destination in one compact prompt. If the operator cannot provide them, continue as a clearly labeled unbranded concept using non-factual copy and a disabled or placeholder conversion destination; do not present or publish it as a truthful final client landing until those facts are resolved.
