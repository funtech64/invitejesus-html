# InviteJesus Knowledge Addressing Model (IKAM) v1

**Status:** Draft canonical specification  
**Repository:** `funtech64/invitejesus-html`  
**Purpose:** Define a small, permanent address space for rigorous debate, historical comparison, multilingual Scripture study, and cryptographically verifiable publication history.

---

## 1. Governing principle

InviteJesus uses exactly five top-level knowledge namespaces:

```text
GOD
ARG
BEL
LOG
OBJ
```

The identifier names a durable subject. Typed connections describe its history, interpretation, association, agreement, disagreement, and use.

The model is intentionally restrained:

- identifiers remain stable;
- names and descriptions may improve;
- relationships may be added or disputed;
- published versions receive cryptographic hashes;
- no conventional database is the canonical source of truth;
- Markdown files remain the human-readable source documents.

---

## 2. The five namespaces

### 2.1 `GOD` — Canonical Scripture locations

Format:

```text
GOD-[book]-[chapter]-[verse]
```

Example:

```text
GOD-43-001-001
```

This identifies Book 43, chapter 1, verse 1. Book, chapter, and verse use fixed-width numeric fields so the reference is language-neutral and sorts predictably.

The base `GOD` address identifies the canonical location, not a particular translation, manuscript, or printed edition.

### 2.2 `ARG` — Apologetic and debate arguments

Format:

```text
ARG-[01-12]-[0001-9999]
```

Examples:

```text
ARG-01-0001
ARG-04-0021
ARG-12-0047
```

The first number identifies one of the twelve established argument divisions. The final number identifies a particular argument within that division.

### 2.3 `BEL` — Belief systems

`BEL` is the umbrella for religions and worldviews.

```text
BEL-REL-[canonical-key]
BEL-WOR-[canonical-key]
```

Examples:

```text
BEL-REL-CHRISTIANITY
BEL-REL-LDS
BEL-REL-JW
BEL-REL-RUSSELLITES
BEL-REL-ROMAN-CATHOLIC
BEL-WOR-ATHEISM
BEL-WOR-NATURALISM
BEL-WOR-STOICISM
```

`BEL-REL` includes religions, denominations, sects, movements, traditions, and historical religious branches.

`BEL-WOR` includes nonreligious worldviews, philosophies, and structured belief frameworks.

A new movement receives its own identifier when it is a concrete historical or present identity. It is not hidden inside another movement's identifier.

For example:

```text
BEL-REL-JW
BEL-REL-RUSSELLITES
OBJ-WATCHTOWER
OBJ-CHARLES-TAZE-RUSSELL
```

These are separate durable subjects. Their meaning comes from connections such as `developed-from`, `associated-with`, or `governed-by`.

### 2.4 `LOG` — Logical fallacies and reasoning forms

The initial canonical organization uses three primary categories:

```text
LOG-REL  Relevance
LOG-AMB  Ambiguity
LOG-PRS  Presumption
```

Individual fallacies use stable mnemonic keys beneath those categories:

```text
LOG-REL-ADH  Ad Hominem
LOG-REL-RDH  Red Herring
LOG-REL-BAN  Bandwagon
LOG-AMB-EQV  Equivocation
LOG-AMB-ACC  Accent
LOG-AMB-AMP  Amphiboly
LOG-PRS-BEG  Begging the Question
LOG-PRS-CIR  Circular Reasoning
LOG-PRS-NTS  No True Scotsman
```

The canonical key does not change when the preferred display name changes. Alternate names, Greek terms, Latin terms, and modern descriptions attach as metadata.

### 2.5 `OBJ` — Concrete identifiable subjects

`OBJ` covers addressable persons, places, organizations, documents, councils, translations, manuscripts, artifacts, events, institutions, and other concrete things.

Examples:

```text
OBJ-WATCHTOWER
OBJ-CHARLES-TAZE-RUSSELL
OBJ-COUNCIL-NICAEA
OBJ-CODEX-SINAITICUS
OBJ-NASB44
OBJ-SBLGNT
```

`OBJ` does not mean that all objects are physical. It means they are concrete identifiable subjects rather than one of the four specialized namespaces.

---

## 3. Religious documents are subordinate to `BEL-REL`

A religious document belongs beneath the movement or tradition whose document corpus is being represented.

Format:

```text
BEL-REL-[canonical-key]-DOC-[book]-[chapter]-[verse]
```

Examples:

```text
BEL-REL-LDS-DOC-001-001-001
BEL-REL-JW-DOC-001-001-001
BEL-REL-ISLAM-DOC-001-001-001
```

`DOC` is not a sixth namespace. It is a subordinate address inside `BEL-REL`.

Different movements may share, inherit, reject, restore, revise, or declare documents apocryphal. Those changes are represented through typed connections rather than by rewriting the document's identity.

Examples:

```text
BEL-REL-JW --retains-document--> BEL-REL-RUSSELLITES-DOC-001-001-001
BEL-REL-JW --rejects-document--> BEL-REL-RUSSELLITES-DOC-004-001-001
BEL-REL-MOVEMENT-X --restores-document--> OBJ-GOSPEL-OF-THOMAS
```

---

## 4. Typed connections

The system is a flat collection of addressable documents connected by explicit relationships.

A connection has this minimum form:

```yaml
- relation: developed-from
  target: BEL-REL-RUSSELLITES
```

Example belief record:

```yaml
---
id: BEL-REL-JW
title: Jehovah's Witnesses
kind: religion
aliases:
  - JW
connections:
  - relation: developed-from
    target: BEL-REL-RUSSELLITES
  - relation: governed-by
    target: OBJ-WATCHTOWER
  - relation: associated-person
    target: OBJ-CHARLES-TAZE-RUSSELL
  - relation: interprets
    target: GOD-43-001-001
  - relation: addresses
    target: ARG-04-0021
  - relation: reasoning-reference
    target: LOG-AMB-EQV
---
```

Connections may include historical qualification:

```yaml
- relation: recognized-document
  target: OBJ-DOCUMENT-X
  validFrom: "1879"
  validUntil: "1931"
```

A disputed connection may carry attribution and status:

```yaml
- relation: claims-continuity-with
  target: BEL-REL-EARLY-CHRISTIANITY
  assertedBy: BEL-REL-MOVEMENT-X
  status: disputed
```

The identifier never decides which theological or historical claim is correct. The connection records who claims what and how the claim is supported.

---

## 5. Multilingual Scripture addressing

InviteJesus uses the canonical `GOD` address as the stable center and attaches language and edition identifiers with `@`.

Format:

```text
GOD-[book]-[chapter]-[verse]@[language]-[edition]
```

Examples:

```text
GOD-43-001-001@eng-nasb44
GOD-43-001-001@eng-kjv
GOD-43-001-001@grc-sblgnt
GOD-01-001-001@hbo-bhs
GOD-27-002-004@arc-bhs
```

Initial language keys:

```text
eng  English
grc  Ancient Greek
hbo  Biblical or Ancient Hebrew
arc  Biblical or Imperial Aramaic
```

The edition key identifies the translation, critical edition, manuscript tradition, or textual witness.

### 5.1 Word and phrase selections

Word selections attach to the exact language and edition rendering:

```text
GOD-43-001-001@grc-sblgnt-W003
GOD-01-001-001@hbo-bhs-W001
GOD-27-002-004@arc-bhs-W005
GOD-43-001-001@eng-nasb44-W001..W005
```

A word record may include:

```yaml
canonical: GOD-43-001-001
rendering: GOD-43-001-001@grc-sblgnt
position: W003
surface: λόγος
lemma: λόγος
transliteration: logos
language: grc
edition: sblgnt
strong: G3056
```

### 5.2 Bible text format

USFM is the selected working format for imported Bible texts because it supports translation workflows, chapters, verses, notes, and word-level attributes.

USFM is an implementation format, not a sixth namespace and not the canonical identity system. IKAM addresses remain the public references.

---

## 6. Markdown as the canonical authoring format

Each knowledge subject is stored as a Markdown file with YAML frontmatter.

Suggested source layout:

```text
src/content/
  beliefs/
    religions/
    worldviews/
  logic/
  arguments/
  objects/
  scripture/
```

Existing encyclopedia files may be migrated gradually. The addressing model does not require all files to move at once.

A canonical record should include:

```yaml
---
id: BEL-REL-LDS
title: Latter Day Saint movement
version: 1
previousHash: null
connections: []
---
```

The Markdown body contains the human-readable article and evidence.

---

## 7. Versioning and hashes

The stable identifier refers to the durable subject. Each published revision receives a new content hash.

Required version fields:

```yaml
version: 3
previousHash: "sha256-of-version-2"
```

The hash itself is calculated from a deterministic publication representation rather than being embedded inside the bytes it hashes.

Each release manifest records:

```json
{
  "id": "BEL-REL-JW",
  "version": 3,
  "path": "src/content/beliefs/religions/jehovahs-witnesses.md",
  "sha256": "...",
  "previousHash": "..."
}
```

Hash algorithm:

```text
SHA-256
```

The publication representation must use:

- UTF-8 encoding;
- Unix line endings;
- deterministic key ordering;
- deterministic object ordering;
- no volatile timestamp inside hashed content.

Retractions and corrections create new versions. Published history is not silently overwritten.

---

## 8. Distributed publication: IPFS/IPLD and Arweave

The selected middle-ground publication system has two complementary layers.

### 8.1 IPFS/IPLD — content identity and connected graph

IPFS provides a content identifier (CID) for each exact published object or release directory. A content change produces a new CID.

IPLD represents links among content-addressed objects. IKAM identifiers remain the readable public addresses, while a release registry maps each IKAM ID to its CID.

Example registry entry:

```json
{
  "id": "BEL-REL-JW",
  "sha256": "...",
  "cid": "bafy..."
}
```

IPFS/IPLD provides:

- content-addressed identity;
- distributed retrieval;
- verifiable links;
- reconstruction of the connected corpus.

### 8.2 Arweave — permanent approved publication

Arweave stores approved publication releases as permanent public records.

Arweave is not used for every draft. Only reviewed named releases are archived.

Example release names:

```text
IKAM-2026.07
IKAM-2026.08
IKAM-1.0
```

A release receipt records:

```json
{
  "schema": "IKAM-1",
  "release": "IKAM-2026.07",
  "manifestSha256": "...",
  "ipfsRootCid": "bafy...",
  "arweaveTransactionId": "...",
  "previousRelease": "IKAM-2026.06"
}
```

The two-layer decision is therefore:

```text
IPFS/IPLD = content identity and connected knowledge graph
Arweave   = permanent approved release archive
```

GitHub and Git remain authoring and review tools. They are not the sole permanent archive.

---

## 9. Validation rules

A future validator must reject:

- unknown top-level namespaces;
- malformed identifiers;
- duplicate canonical identifiers;
- missing connection targets;
- self-contradictory version chains;
- reused mnemonic keys for different subjects;
- a changed canonical identifier without an explicit migration record;
- a hash that does not match the deterministic publication bytes.

It should warn about:

- unrecognized relationship names;
- missing aliases;
- orphaned objects;
- duplicate aliases;
- disputed historical claims lacking attribution.

---

## 10. Growth model

The system is designed to grow without redesign.

New religious movement:

```text
BEL-REL-[new-key]
```

New worldview:

```text
BEL-WOR-[new-key]
```

New logical fallacy:

```text
LOG-[category]-[key]
```

New object:

```text
OBJ-[key]
```

New argument:

```text
ARG-[01-12]-[number]
```

New Scripture rendering:

```text
GOD-[book]-[chapter]-[verse]@[language]-[edition]
```

Existing subjects retain their identifiers while their relationship graph and version history grow.

---

## 11. Initial implementation sequence

1. Adopt this specification as a draft.
2. Define the canonical relationship vocabulary.
3. Build the three-category logical fallacy corpus as Markdown files.
4. Assign `BEL-REL` identifiers to religion articles.
5. Assign `BEL-WOR` identifiers to worldview articles.
6. Add deterministic manifest and SHA-256 generation.
7. Publish a test corpus to IPFS.
8. Archive the first approved release on Arweave.
9. Add USFM Bible imports and word-level selection addressing.

---

## 12. Canonical summary

```text
GOD-43-001-001
GOD-43-001-001@eng-nasb44
GOD-43-001-001@grc-sblgnt-W003

ARG-04-0021

BEL-REL-JW
BEL-REL-RUSSELLITES
BEL-REL-LDS
BEL-WOR-NATURALISM
BEL-REL-LDS-DOC-001-001-001

LOG-REL-ADH
LOG-AMB-EQV
LOG-PRS-BEG

OBJ-WATCHTOWER
OBJ-CHARLES-TAZE-RUSSELL
OBJ-CODEX-SINAITICUS
```

Exactly five top-level namespaces remain:

```text
GOD
ARG
BEL
LOG
OBJ
```

Everything else is a subtype, rendering, version, or typed connection.