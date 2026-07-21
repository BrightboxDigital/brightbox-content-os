# generate-image: automated featured image via OpenAI

Generates one master image with the OpenAI Images API, produces optimized derivatives,
uploads them to WordPress, sets the featured image, and writes a manifest that push-social
uses to attach the right image to each GHL social draft. Never publishes. Drafts only.

## Secrets

- `OPENAI_API_KEY` from the environment, or `~/.config/brightbox/openai.json` (`{"api_key": "..."}`).
- WordPress and GHL creds reused from their existing files. Nothing new there.
- No secret is ever logged or committed. `openai.json` is gitignored.

## The image brief

Authored per article (part of the create-blog package) at
`clients/brightbox/drafts/<id>-image-brief.json`:

```json
{
  "title": "...", "summary": "...", "keyword": "...",
  "concept": "...", "prompt": "...", "focal_point": "center",
  "headline": "...", "category": "...", "filename": "<slug>",
  "alt_text": "...", "image_title": "...", "caption": ""
}
```

The `prompt` describes the article's real subject. It must not depict text, logos, fake
dashboards, floating icons, or make unsupported factual claims.

## Run the image stage

```
./scripts/generate-image --brief clients/brightbox/drafts/BBX-002-image-brief.json --post-id 5599
```

Produces: master PNG (1536x1024), then derivatives:
- wp_featured 1200x675 webp  (WordPress featured)
- facebook / linkedin 1200x630 webp
- instagram 1080x1350 jpg
- square 1080x1080 jpg

Then uploads to WordPress, sets featured_media on the draft, verifies it, and writes
`manifest.json` next to the images.

## Attach to social

```
./scripts/push-social --from <dist>/posts.json \
  --media-manifest clients/brightbox/drafts/<slug>-images/manifest.json
```

Each platform draft gets its own derivative: Facebook/LinkedIn the 1200x630, Instagram the
1080x1350, GBP and Pinterest the wide/square. GHL fetches the public WordPress URL, so no
separate GHL media upload is needed.

## Rerun just the image stage

`generate-image` is idempotent: if a complete manifest exists it does nothing. Force a fresh
image with `--rerun`. WordPress uploads are deduplicated by filename, so a rerun reuses
existing media rather than piling up copies. If a run fails partway, the article stays a draft,
the manifest records the failed stage, and rerunning resumes without recreating the article.

## Model and quality

gpt-image-2, quality medium, 1536x1024 master, opaque background, returned as base64 and saved
as PNG. Up to two retries on 429/5xx with exponential backoff. The returned file is validated as
a real image of the expected size before anything is uploaded.

## Optional branded overlay (not built yet)

Phase 2. Adds the Brightbox logo, a category label, and a short headline programmatically on top
of the AI background, using an approved transparent logo file. Not implemented until Archie
approves the base image look and supplies the logo. The AI model never renders the logo or text.
