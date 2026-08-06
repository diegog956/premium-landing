# Asset sourcing

## Priority

Choose among brand-owned material, licensed free or paid assets, and bespoke generated media according to maximum project fit, fidelity, distinctiveness, and production quality. Use placeholders only as a clearly disclosed temporary fallback. Price must not affect ranking unless the operator establishes a budget constraint.

Before using a paid asset, record in `.premium-landing/assets.md` the asset, price, license, intended use, material benefit, approver, and approval date. Never purchase or make the design depend on it before explicit operator approval.

## Starting sources

- **Photos:** Unsplash or Pexels.
- **Video:** Pexels Video.
- **3D models, textures, HDRIs:** Poly Haven CC0 assets.
- **Fonts:** Google Fonts, after checking the license file for the selected family.
- **Icons:** Lucide or Phosphor, retaining required license notices in the project.

This is a starting whitelist, not permanent legal approval. Recheck the official license at download time because terms can change. Other sources require an equivalent license review before use. Do not use a source whose terms are ambiguous or contradictory.
Do not restrict research to this list or to free libraries; include reputable paid marketplaces, foundries, studios, and specialist libraries whenever they can produce a better result.

## Per-asset checks

Record in `.premium-landing/assets.md` the source URL, creator when available, download date, exact file or version, applicable license, evidence of its terms or receipt, and any attribution requirement. Also check rights that copyright licenses may not clear: recognizable people, logos, trademarks, artwork, products, private property, and implied endorsement.

Never copy assets from a reference website unless the user owns them or provides independent authorization. A public URL is design evidence, not an asset license.

Before composition, inspect every logo and likely hero or section-defining asset at its intrinsic size and with transparency visible. Classify it as `ready`, `repair`, `replace`, or `exclude` after checking resolution, compression, aspect ratio, alpha/background treatment, crop flexibility, brand accuracy, license, and suitability for the intended display size.

Do not place an unfit asset merely because the operator supplied it. Repair it when authorized and quality can be preserved; otherwise request a better source, propose a legitimate replacement, or omit it. Never stretch an asset, hide defects with an accidental container, or present a low-resolution raster logo as a premium brand treatment.

## Asset naming and placement

Maintain one managed source file per supplied asset inside the project. Once its identity or actual role is known, rename and move that file from `_inputs/` into the stack-appropriate asset directory using a lowercase semantic name:

- `brand-logo-primary.ext`, `brand-wordmark-primary.ext`, or `brand-symbol-primary.ext` for verified brand variants;
- `img-<role>-NN.ext`, such as `img-hero-01.webp`;
- `video-<role>-NN.ext`, `model-<role>-NN.ext`, and `audio-<role>-NN.ext` for other media.

Use a stable content identity instead of a section role when an asset is reused, for example `img-product-dashboard-01.webp`. Never infer that an unknown graphic is a logo or wordmark from its filename alone; inspect it and use brand guidance when available.

For a supplied asset whose role is still unknown, use an observable content identity instead of inventing a role. Resolve collisions deterministically with `-01`, `-02`, and so on.

Do not keep a second source copy merely to preserve the incoming filename. Record previous name, current path, role, transformation, source, and rights in the asset records. Build-generated derivatives and temporary conversion files are allowed but must not become user-managed source duplicates.

Before discarding unique high-quality information through lossy conversion, confirm that the operator has an external backup or explain the consequence and obtain approval. After a verified conversion, retain only the approved managed source format. If a later design change makes a semantic name misleading, rename the managed file, update every code and metadata reference, and rerun the relevant build and rendered-page checks.

## Generated media

Use generated media when it improves art direction or fills a real asset gap. Do not use synthetic people, products, facilities, results, or events where viewers could reasonably interpret them as factual evidence. Match the approved visual language and verify output at final display size.

Use [Haikei](https://haikei.app/) when the approved direction specifically calls for abstract vector backgrounds, patterns, waves, layered forms, or similar generative geometry. Never add its output automatically as decoration or use generic blobs and waves merely to make a page look designed. Export the chosen result locally as SVG, record the source URL, date, license, and reproducible settings when available, then sanitize and optimize it before use. Remove unnecessary metadata, avoid remote runtime dependencies, test responsive cropping and contrast, and verify that the asset remains lightweight and distinctive in the final composition.
