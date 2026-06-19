---
name: security-review
description: Audit a codebase for security vulnerabilities and produce a prioritized remediation plan. Use when asked to "run a security review", "audit for vulnerabilities", "check OWASP Top 10", "find security issues", or "do a security audit". Technology-agnostic.
metadata:
  author: olivomarco
  version: "1.0.0"
  argument-hint: <path-or-area-to-audit>
---

# Security Review

## Mission

Perform a thorough, read-only security review of the codebase, identify vulnerabilities aligned with the OWASP Top 10, and produce an actionable, prioritized remediation plan. Do **not** modify code — report findings only.

## Scope & Preconditions

- If the user names a path, module, or area, scope the review there; otherwise review the whole repository.
- First, infer the stack: read manifests/build files (e.g. `package.json`, `requirements.txt`, `go.mod`, `pom.xml`, `Gemfile`, `composer.json`, `*.csproj`), entry points, and any `SECURITY.md` or existing security docs.
- Identify trust boundaries: user input, network calls, file/OS access, authentication, authorization, persistence, secrets, and third-party integrations.
- Adapt every check below to the actual language, framework, and data store in use. Skip checks that do not apply and say so.

## Workflow

### 1. Authentication & Authorization
- Verify every protected route/handler/operation enforces authentication.
- Confirm authorization (role/ownership/tenant checks) happens before any privileged action.
- Look for privilege-escalation paths (a user changing their own role, IDOR via unchecked object IDs, missing tenant scoping).

### 2. Injection
- **SQL/NoSQL injection**: ensure queries are parameterized; flag string-concatenated or raw queries built from user input.
- **XSS**: confirm user-generated content is encoded/escaped or sanitized before rendering; flag raw HTML injection (e.g. `innerHTML`, `dangerouslySetInnerHTML`, unescaped templates).
- **Command/Code injection**: flag `exec`/`spawn`/`eval`/deserialization/template engines fed with untrusted input.
- **Path traversal**: flag file paths built from user input without normalization/allow-listing.

### 3. Sensitive Data Exposure
- Flag responses that over-fetch (password hashes, tokens, internal IDs, PII the client doesn't need).
- Verify error responses don't leak stack traces, queries, or internal schema.
- Check logging doesn't record secrets or PII.

### 4. Input Validation
- Verify all external input is validated (type, range, length, format) at the boundary.
- Check file uploads validate type, size, and extension; check pagination/limits are bounded.

### 5. API & Transport Security
- Check rate limiting on sensitive endpoints (login, password reset, contact, expensive operations).
- Verify CORS is appropriately restrictive, CSRF protections exist for state-changing requests, and webhook signatures are verified.
- Confirm TLS/HTTPS is enforced where applicable.

### 6. Cryptography & Secrets
- Flag hardcoded secrets, keys, or credentials in source or config.
- Verify password hashing uses a strong, salted algorithm (bcrypt/scrypt/argon2) with adequate cost.
- Check token/session handling (expiry, rotation, signing) and that pre-signed/temporary URLs have short expiry.

### 7. Dependency Vulnerabilities
- Run the ecosystem audit tool if available (`npm audit`, `pip-audit`, `govulncheck`, `bundler-audit`, `osv-scanner`, etc.) and summarize known CVEs.
- Flag outdated packages in security-critical areas (auth, crypto, HTTP, serialization).

### 8. Configuration & Headers
- Check security headers where applicable (CSP, HSTS, X-Frame-Options, X-Content-Type-Options).
- Flag development-only settings that must not reach production (debug mode, verbose errors, permissive CORS, default credentials).

## Output Expectations

Produce a Markdown report with:

### Executive Summary
One paragraph: overall posture, critical finding count, and risk level.

### Findings
For each finding:
- **ID**: SEC-001, SEC-002, …
- **Severity**: Critical / High / Medium / Low / Informational
- **Category**: OWASP category (e.g. A01:2021 – Broken Access Control)
- **Location**: file path and line range
- **Description**: what the vulnerability is
- **Exploit scenario**: how it could be exploited
- **Remediation**: specific fix with a code example where applicable
- **Confidence**: Confirmed / Likely / Potential

### Severity Summary
| Severity | Count |
| --- | --- |
| Critical | |
| High | |
| Medium | |
| Low | |
| Informational | |

### Remediation Priority
Ordered list of fixes from most to least critical, each with an estimated effort (S/M/L).

### Positive Findings
Security measures already implemented well, to acknowledge what's working.

## Quality Assurance

- Every finding must reference a specific file and location.
- Remediation must be compatible with the project's actual framework and patterns.
- Do not flag framework-managed internals you cannot change; focus on application-level code.
- Distinguish confirmed vulnerabilities from potential risks via the confidence level.
- Do not modify code. This skill only reports.
