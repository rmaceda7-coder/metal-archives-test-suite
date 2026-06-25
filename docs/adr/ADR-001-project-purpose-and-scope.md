# ADR-001: Project Purpose and Scope

## Status

Accepted

## Context

The Metal Archives Automation Suite is a production-oriented end-to-end automation framework designed specifically for Metal Archives.

Unlike a generic automation framework, this project focuses on real user journeys executed against a single domain.

The project aims to become a maintainable, scalable and extensible regression suite that can be used by contributors and potentially adopted by the website maintainers.

## Objectives

- Validate core business functionality.
- Support regression testing.
- Improve accessibility validation.
- Support UX verification.
- Produce reliable automated regression suites.
- Be easy to extend and maintain.

## Guiding Principles

- Readability over cleverness.
- Business language over technical language.
- Composition over inheritance.
- Explicit behavior over hidden magic.
- Stable architecture before large test suites.

## Out of Scope

- Performance benchmarking.
- Security testing.
- Load testing.
- Web scraping.
- CAPTCHA bypassing.

## Long-Term Vision

The project should evolve into a complete regression suite capable of validating the most important user journeys of Metal Archives while remaining simple to understand and maintain.