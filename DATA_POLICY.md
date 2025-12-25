# DATA_POLICY.md

Data policy and privacy posture

**Purpose**  
This repository exists to support research design, transparency, and reproducibility without exposing participant data.

**Data we do not accept in this repository**  
- No raw participant responses.  
- No direct identifiers.  
- No indirect identifiers that can reasonably re-identify someone.  
- No audio, video, transcripts, chat logs, or screenshots that contain personal information.  
- No PHI, clinical records, or sensitive personal narratives.

**Allowed content**  
- Synthetic data that cannot be linked to real people.  
- Schemas, codebooks, and example fixtures with fabricated values.  
- Aggregated results that are not re-identifiable.  
- Study materials such as protocols, consent language drafts, measure lists, recruitment copy, analysis plans, posters, and paper drafts, as long as they contain no participant data.

**Storage and processing principles**  
- Data minimization: store only what is necessary for the stated purpose.  
- Local first when possible: prefer local-only operation and avoid server logs for prototypes.  
- No tracking by default: avoid analytics, third-party trackers, and ad pixels.  
- Clear retention: if any local storage exists in an app, document what is stored, where, and how to clear it.

**IRB alignment and boundaries**  
- If a study is covered by an IRB protocol, include the protocol identifier and status in the relevant docs.  
- Do not store anything that violates the approved protocol or consent terms.  
- If something is outside IRB scope, label it clearly as a non-research prototype or internal development artifact.

**Contributor rules**  
- Before committing, run a quick check for secrets and sensitive strings.  
- If you accidentally commit something sensitive, rotate credentials immediately and remove the content from git history, then notify the maintainer.

**Contact**  
For questions about this policy or whether something is safe to include, contact: thejenniferpattee@gmail.com
