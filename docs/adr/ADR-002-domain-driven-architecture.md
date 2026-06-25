# ADR-002: Domain-Driven Architecture

## Status

Accepted

## Context

Metal Archives is not a generic website. It is a domain-specific database focused on heavy metal music.

The automation suite should not be designed around Playwright first. It should be designed around the domain first.

Core domain concepts include:

- Band
- Album
- Artist
- Label
- Review
- Search
- Discography

## Decision

The project will follow a domain-driven testing approach.

Tests will describe user behavior using Metal Archives business language.

Preferred:

```python
SearchBandJourney(browser_context).search_for_band("Opeth")

Avoid:
page.locator("#searchQuery").fill("Opeth")
page.keyboard.press("Enter")

Architecture Direction
Test
  ↓
Journey
  ↓
Page
  ↓
Component
  ↓
Core
  ↓
Playwright

Domain Areas

The initial domain areas will be:

Search
Band pages
Album pages
Discography
Reviews
Benefits
Tests are easier to understand.
The framework speaks the language of the website.
Future contributors can understand intent faster.
Page structure changes will have limited impact.
The suite can evolve into a maintainable regression package.
Final Decision

Design the Metal Archives Automation Suite around domain-specific user journeys instead of generic browser actions.