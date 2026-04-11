# OWASP review, April 2026

Repository: `gndx/gndx.dev`
Date: 2026-04-11
Scope: static review of source, dependency audit, and quick OWASP-oriented hardening pass.

## Executive summary

- Overall posture is decent for a mostly static Astro site.
- Positive controls already present:
  - CSP configured in `src/middleware.ts`
  - `X-Frame-Options`, `HSTS`, `nosniff`, `Referrer-Policy`, `Permissions-Policy`
  - `security.txt` published under `public/.well-known/security.txt`
- Main actionable app-layer issue found:
  - Potential DOM XSS in client-side search rendering due to `innerHTML` with content-derived fields.
- Main platform risk found:
  - Several outdated packages with published advisories, especially around Astro, Cloudflare adapter, Wrangler, Vite, Rollup, Undici.

## Findings mapped to OWASP Top 10

### A03:2021 Injection

#### Finding 1, Potential DOM XSS in search UI
- Severity: Medium
- File: `src/components/Header.astro`
- Issue:
  - Search results were rendered using `li.innerHTML = ...`.
  - `item.title`, `item.description`, and `item.url` flowed into HTML construction.
  - If content or config data becomes attacker-controlled, this can become a DOM XSS sink.
- Remediation applied:
  - Replaced `innerHTML` rendering with safe DOM node creation and `textContent` assignment.

### A06:2021 Vulnerable and Outdated Components

#### Finding 2, Dependencies with known advisories
- Severity: High
- Source: `npm audit --omit=dev --json`
- Notable vulnerable packages reported:
  - `astro` < 5.18.1, allowlist bypass advisory
  - `@astrojs/cloudflare` transitively pulling vulnerable `wrangler`
  - `wrangler` < 4.59.1, command injection advisory
  - `vite` <= 6.4.1, file read/path traversal advisories
  - `rollup` < 4.59.0, arbitrary file write advisory
  - `undici` < 7.24.0, multiple resource exhaustion and parser issues
- Notes:
  - Some of these are build-time or dev-time risks, but they still matter in CI and local maintenance workflows.
- Recommended remediation:
  - Upgrade the dependency chain in a controlled pass, starting with:
    - `astro` to `5.18.1` or newer compatible release
    - `@astrojs/cloudflare` to `12.6.13` or newer
    - refresh lockfile with a full install
  - Re-run `npm audit` after upgrades.

### A05:2021 Security Misconfiguration

#### Finding 3, CSP currently relies on `unsafe-inline` for scripts
- Severity: Low to Medium
- File: `src/middleware.ts`
- Issue:
  - CSP uses `script-src 'self' 'unsafe-inline'`.
  - This weakens protection against injected inline script execution.
- Context:
  - Current templates include inline scripts for SW handling and UI logic, which explains the policy.
- Recommendation:
  - Migrate inline scripts to external assets or nonce-based scripts.
  - Then tighten CSP by removing `'unsafe-inline'` from `script-src`.

### A01:2021 Broken Access Control

#### Finding 4, No obvious access-control surface in app layer
- Severity: Informational
- The site is primarily static and no sensitive authenticated route handling was found in scope.
- No direct broken access control issue identified during this pass.

### A02:2021 Cryptographic Failures

#### Finding 5, No obvious crypto misuse found in scoped review
- Severity: Informational
- No custom crypto usage found in the reviewed files.

### A04:2021 Insecure Design

#### Finding 6, Third-party scripts have broad trust
- Severity: Medium
- File: `src/layouts/Base.astro`
- Issue:
  - Third-party scripts from Umami and Google Ads are loaded globally.
  - CSP currently allows `'unsafe-inline'` and broad `connect-src https:`.
- Risk:
  - If a third-party script is compromised, it inherits full origin trust in the browser.
- Recommendation:
  - Limit `connect-src`, `script-src`, and related directives to explicit origins where feasible.
  - Consider only loading ad/analytics scripts on routes that actually need them.

## Positive controls observed

- Security headers set in middleware:
  - `Content-Security-Policy`
  - `Referrer-Policy: strict-origin-when-cross-origin`
  - `X-Content-Type-Options: nosniff`
  - `X-Frame-Options: DENY`
  - `Permissions-Policy`
  - `Strict-Transport-Security`
- `security.txt` present
- `rel='noopener noreferrer'` used on external links in reviewed component

## Validation commands used

```bash
grep -R "set:html\|innerHTML\|dangerouslySetInnerHTML\|new Function\|eval(" -n src public || true
npm audit --omit=dev --json
npm outdated --json || true
```

## Suggested next steps

1. Merge the DOM XSS fix from this PR.
2. Create a follow-up dependency upgrade PR focused on Astro, Cloudflare adapter, and lockfile refresh.
3. Tighten CSP to remove `'unsafe-inline'` from scripts.
4. Restrict CSP source lists to exact domains instead of broad `https:` where possible.
5. Add a lightweight security checklist to PR review for client-side rendering sinks and third-party scripts.
