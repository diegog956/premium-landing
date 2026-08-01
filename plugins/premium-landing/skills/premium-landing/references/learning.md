# Controlled learning loop

## Goal

Improve the workflow from project evidence without allowing uncontrolled self-modification or overfitting to one landing.

## After each project

Create a concise project-local report under `.premium-landing/run-report.md` unless repository policy or the user disallows it. Record:

- project type and conversion model;
- questions that changed a decision;
- questions that produced no useful signal;
- information discovered too late;
- assumptions that proved wrong;
- references accepted, rejected, and why;
- major rework causes;
- visual, functional, accessibility, and performance defects found during QA;
- user corrections and unresolved external dependencies;
- proposed workflow changes with supporting evidence.

Do not include secrets or unnecessary customer data.

Keep every project's brief, evidence, visual direction, audience assumptions, conversion strategy, and client preferences local to that project. Never carry them into a new project as defaults merely because they succeeded once.

Classify observations before proposing reuse:

- **project-specific:** taste, brand, audience, offer, market, references, copy, and implementation choices that belong only to that context;
- **conditional pattern:** potentially reusable only when the new project shares the relevant conditions;
- **workflow-level lesson:** a repeated improvement to research, questioning, validation, safety, or delivery that is broadly useful without prescribing the outcome.

Only workflow-level lessons should normally change the shared skill. Conditional patterns may inform judgment but must be revalidated in each new brief.

## Evolve safely

Do not rewrite this skill automatically after a run. When asked to improve it:

1. Compare reports across multiple, meaningfully different projects when available.
2. Identify repeated failure patterns rather than isolated preferences.
3. Propose a small versioned change.
4. Test the changed rule against prior scenarios for regressions.
5. Apply the change only after user approval.

Treat conversion data as stronger evidence than taste feedback when attribution is credible, but never optimize away brand, accessibility, trust, or legal constraints for a single metric.
