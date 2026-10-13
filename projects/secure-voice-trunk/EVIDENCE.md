# Secure Voice Trunk — Evidence Register

**Article:** [Securing a production voice trunk on Linux](index.html)  
**Author:** Josh Escobar  
**Project window:** October 12–13, 2026  
**Status:** Publication-selected excerpts and attributed historical findings. No raw production logs or call-party records are published.

This register separates (a) observations from original October 12 diagnostic files, (b) implementation details supported by the retained engineering record and operator confirmation, and (c) October 13 follow-up findings retained from an earlier review. Every on-page terminal panel is a **typeset, sanitized excerpt**, not an untouched screenshot, live command session, or newly executed test. Technical headings and redactions are editorial.

## E01 — Plaintext baseline <a id="e01"></a>

**Origin:** October 12 read-only Linux/Asterisk discovery report, original file \`ECA_Dialer4_TLS_SRTP_Discovery_v1_results_20261012_144501_49860.txt\`. Only technical fields required for the narrative are included.

\`\`\`text
UDP Bindaddress:        0.0.0.0:5060
TCP SIP Bindaddress:    Disabled
TLS SIP Bindaddress:    Disabled
Allowed transports:     UDP

[Selected legacy peer fields; peer identity omitted]
Status       : OK (23 ms)
Encryption   : No

[Existing PJSIP transport]
Transport: transport-udp   udp   0.0.0.0:5061
\`\`\`

**Supports:** working but unencrypted legacy SIP transport; TCP/TLS listener disabled; UDP/5061 does not prove TLS. **Does not prove:** full network-wide traffic capture or unrelated server behavior.

## E02 — Gateway TLS trust preflight <a id="e02"></a>

**Origin:** October 12 focused v4 preflight, original file \`ECA_Dialer4_Secure_Trunk_Preflight_v4_results_20261012_202649_21916.txt\`. The four resolved gateway IPs and certificate fingerprint are omitted, while the verification outcome is retained.

\`\`\`text
CA-chain verification, hostname validation and SNI are mandatory; no insecure retry.
DNS IPv4 count=4 | probes capped at4

[One gateway; IP address omitted]
VERIFIED: trusted certificate chain and requested hostname matched
TLS=TLSv1.2 | cipher=ECDHE-RSA-AES128-GCM-SHA256

TLS result: verified=4 failed=0
\`\`\`

**Supports:** Linux/Python client validation of four TLS gateway paths, including verified certificate chains and hostnames. **Does not prove:** the cipher used for the later Asterisk session, SIP authentication, media encryption, or production dialplan routing.

## E03 — Loaded transport and endpoint policy <a id="e03"></a>

**Origin:** October 12 post-test Asterisk runtime output, supplied as \`Pasted text(1).txt\`. Selected fields are grouped and spacing normalized. Production hostname, certificate paths, and addressing are omitted.

\`\`\`text
[Selected TLS transport fields]
method                      : tlsv1_2
protocol                    : tls
verify_server               : Yes
allow_wildcard_certs        : Yes
bind                        : 0.0.0.0:5061

[Selected endpoint fields]
media_encryption            : sdes
media_encryption_optimistic : false
srtp_tag_32                 : false
direct_media                : false
dtmf_mode                   : rfc4733
\`\`\`

**Supports:** loaded signaling and media encryption requirements. Original generated-file comparison and follow-up operator confirmation establish persistent VICIdial ownership and the rebuild flag returning to the idle state. **Does not prove:** negotiated SRTP on any individual call, nor a negative test of plaintext rejection.

## E04 — Answered SRTP echo test <a id="e04"></a>

**Origin:** Original October 12 one-call test report, \`ECA_Dialer4_Encrypted_Echo_Test_v1_results_20261012_215411_10808.txt\`. Channel/test IDs, phone numbers, and timestamps identifying the call parties are not reproduced. The order of selected closing fields is normalized.

\`\`\`text
ONE attempt; answer timeout 30s; absolute channel timeout 120s; no automatic retries.
No configuration edits, recording, restarts, or SIP/SDP trace collection.

Owned pilot channel: [redacted] | {"srtp": "1", "state": "Up"}

Answered Up observed: True
Negotiated SRTP audio flags while Up: ["1"]
SRTP negotiation flag 1 observed: True

Callfile processing finished; no owned live pilot channel remains.
Attempt record retained; running this script again will not redial.
\`\`\`

**Supports:** one answered channel reported negotiated SRTP (the Asterisk \`CHANNEL(rtp,secure,audio)\` observation). The operator separately confirmed hearing the echo and using \`#\` to end the call. **Does not prove:** encryption of other media legs, permanent recording integrity, or broader production rollout.

## E05 — Carrier-side corroboration

**Origin:** October 12 implementation review of a matching user-exported Twilio call record (\`call-log-AC…1791860680824.csv\`; filename and identifiers abbreviated here).

| Twilio export field | Observed |
|---|---|
| Direction | Trunking Terminating |
| Call status | Completed |
| Exported duration | 45 seconds |
| Secure Trunking | true |
| Local start date | October 12, 2026 |

The export's specific trunk SID field was null. No cause for that missing field is asserted; the local configured endpoint and expected matching call details were used in correlation. The \`From\` field supported the caller ID presented to Twilio, **not** the telephone display seen by the receiving user. The original CSV has not been committed.

## E06 — Follow-up traffic review (historical, separately attributed)

**Origin:** October 13 follow-up review of user-supplied Twilio CSV and Asterisk output. The raw attachments were **not available for direct re-reading during the first publication-package assembly**. Treat these as retained review findings, **not a new re-parsing of a dataset included in this repository**.

| Status | Entries with \`Secure Trunking=true\` |
|---|---:|
| Completed | 9 |
| No answer | 6 |
| Failed | 4 |
| **Total** | **19** |

Seven calls were correlated with supplied Asterisk output in that review. Separately observed local FastAGI connection refusals remain an application/logging investigation and were not claimed fixed. Unanswered and failed attempts are **not** successful media-session evidence. This is not a measurement of all calls in the company or of long-term success rates.

## Scope and outstanding tests

**Demonstrated:** a dedicated outbound Linux-to-Twilio trunk configured with verified TLS and mandatory SRTP; answered echo test with negotiated secure audio; matching secure completed carrier record.

**Not demonstrated:** complete production migration, encryption of inbound/agent/inter-server/PSTN legs, at-rest recording protection, certificate renewal and live TLS refresh, load/CPS acceptance, comprehensive failover/transfer behavior, negative plaintext-offer rejection, or organizational HIPAA/SOC 2 certification. Other legacy paths remained available during pilot staging. This is a bounded transport-security improvement, not a broad compliance finding.

## References and interpretation

- [Twilio Elastic SIP Trunking](https://www.twilio.com/docs/sip-trunking) — secure trunk requirements and signaling/media behavior.
- [Twilio trunk troubleshooting and call logs](https://www.twilio.com/docs/sip-trunking/troubleshooting) — carrier log evidence and the Secure Trunking field.
- [Asterisk PJSIP configuration](https://docs.asterisk.org/Latest_API/API_Documentation/Module_Configuration/res_pjsip/) — current documentation for transport and media encryption settings.
- [Asterisk 18.26.4 resolver source](https://raw.githubusercontent.com/asterisk/asterisk/18.26.4/res/res_pjsip/pjsip_resolver.c) — version-specific basis for the resolver-state diagnosis, not a fresh deployed-binary trace.
- [Asterisk 18.26.4 channel functions](https://raw.githubusercontent.com/asterisk/asterisk/18.26.4/channels/pjsip/dialplan_functions.c) — negotiated SRTP channel-state interpretation.

**Publication review:** Remove or further generalize these details if the employer/client does not authorize disclosure. Verify both rendered page and repository history before a public merge. Technical excerpts are included for engineering evidence rather than as deployable operating instructions.
