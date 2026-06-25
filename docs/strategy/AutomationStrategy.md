# Automation Strategy

## Purpose

This suite protects critical Metal Archives user journeys through reliable, maintainable, domain-driven automated tests.

## Testing Priorities

### Smoke

Critical checks that confirm the site is usable.

Examples:

- Home page loads
- Quick search works
- Band page opens
- Album page opens

### Regression

Broader coverage for stable public functionality.

Examples:

- Advanced search
- Band discography
- Album reviews
- Label browsing
- Search result navigation

### Accessibility

Basic accessibility checks focused on real user behavior.

Examples:

- Keyboard navigation
- Focusable inputs
- Visible search controls
- Meaningful page titles

## Automation Rules

- Tests must describe user behavior.
- Tests must not use Playwright selectors directly.
- Journeys represent user workflows.
- Pages represent site screens.
- Components represent reusable UI elements.
- Core owns browser, config, assertions, and framework utilities.

## Test Quality Criteria

A test is production-ready when:

- It validates a meaningful user behavior.
- It has clear assertions.
- It avoids brittle selectors when possible.
- It is isolated from other tests.
- It can run locally and in CI.
- It produces useful failure information.

## Out of Scope

- CAPTCHA bypassing
- Load testing
- Scraping
- Authenticated contribution workflows without permission
- Security testing

## Initial Journey Candidates

- Search for a band
- Open a band page
- Validate band overview
- Open discography
- Open album page
- Validate album track list
- Navigate reviews