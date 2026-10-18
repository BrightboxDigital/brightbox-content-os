# Legacy NEURONwriter REST client

Codex does not use this client. Codex uses the connected official NeuronWriter MCP tools directly
for discovery and the interactive create-blog workflow. Do not probe this client before MCP and do
not treat a missing `~/.config/brightbox/neuronwriter.json` file as a connection failure.

This script remains only for older non-Codex environments that explicitly need the REST API.

`scripts/neuronwriter` provides the NEURONwriter operations used by the Brightbox content workflow.
It keeps the API key outside the repository and adds explicit confirmation flags to the two risky
operations: consuming an analysis credit and saving a content revision.

## One-time credential setup

NEURONwriter API access requires a Gold plan or higher. In NEURONwriter, open your profile, select
**Neuron API access**, and copy the API key. Store it locally at
`~/.config/brightbox/neuronwriter.json`:

```json
{"api_key":"YOUR_NEURON_API_KEY"}
```

Set the file mode to `600`. Never paste the key into chat or commit it.

Verify access:

```bash
./scripts/neuronwriter check
```

The check confirms whether the Brightbox project `eea0682a76fd76f0` and historical Clients project
`0bdb5139dc86fbe7` are visible without printing the key.

## Discovery: read only

```bash
./scripts/neuronwriter list-queries --project brightbox
./scripts/neuronwriter list-queries --project clients
./scripts/neuronwriter get-query --query QUERY_ID
```

The scheduled discovery routine may use only these read operations. If the connection is unavailable,
the report must say `NeuronWriter overlap not checked` and continue.

## Interactive create-blog workflow

Only after Archie approves the topic and seed keyword:

```bash
./scripts/neuronwriter new-query \
  --project brightbox \
  --keyword "approved seed keyword" \
  --engine google.com \
  --language English \
  --competitors-mode top-intent \
  --confirm-credit
```

`new-query` consumes one analysis credit. The command refuses to run without `--confirm-credit`.
Poll for the completed recommendations:

```bash
./scripts/neuronwriter wait-query --query QUERY_ID
```

Score a clean semantic HTML draft without saving it:

```bash
./scripts/neuronwriter evaluate-content \
  --query QUERY_ID \
  --html-file clients/brightbox/drafts/BBX-000-draft-v1.html
```

After the article is final, save exactly one clean semantic revision to NEURONwriter:

```bash
./scripts/neuronwriter import-content \
  --query QUERY_ID \
  --html-file clients/brightbox/approved/BBX-000-clean.html \
  --title "Approved title" \
  --description "Approved meta description" \
  --confirm-write
```

`evaluate-content` does not save. `import-content` saves a revision and refuses to run without
`--confirm-write`.
