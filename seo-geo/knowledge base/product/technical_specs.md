# Straunt – Technical Specifications

This document covers the platform architecture, supported environments, security posture, privacy practices, and technical characteristics of Straunt's restaurant management platform.

---

## Platform Type

| Attribute | Detail |
|-----------|--------|
| **Category** | SaaS (Software as a Service) |
| **Deployment** | Cloud-hosted, multi-tenant |
| **Primary Interface** | Web-based dashboard |
| **Mobile** | Branded mobile apps available (via Straunt Loyalty) |
| **Hardware** | Proprietary POS hardware (Straunt POS) |

---

## System Architecture

Straunt is a **full-stack Restaurant Operating System (OS)** built around a connected data layer. Every module operates within a single platform ecosystem rather than as disconnected tools.

### Core Architecture Principles
- **Unified Data Layer**: All modules (POS, AI, Dash, Loyalty, Reviews, etc.) share a common data layer so customer and order data flows seamlessly between tools.
- **Real-Time Sync**: Menu updates, order routing, and customer data sync in real time across all connected channels.
- **POS Injection**: External orders (delivery apps, phone AI, web orders) are automatically injected into the POS without manual data entry.
- **AI-First Infrastructure**: The platform is built with AI agents at the operational core — not as bolt-ons.

---

## Supported Platforms & Channels

### Ordering Channels
| Channel | Supported |
|---------|-----------|
| In-store POS terminal | ✅ |
| Online ordering (web) | ✅ |
| Mobile app (branded) | ✅ |
| QR code table-side ordering | ✅ |
| Phone (AI-powered) | ✅ |
| WhatsApp | ✅ |
| Kiosk | ✅ |
| Uber Eats | ✅ |
| DoorDash | ✅ |
| Grubhub | ✅ |

### Communication Channels
| Channel | Supported |
|---------|-----------|
| Voice / VoIP (inbound) | ✅ |
| SMS / Text Messaging | ✅ |
| Email | ✅ |
| WhatsApp | ✅ |

---

## AI & Voice Technology

- **Voice AI**: Straunt uses autonomous voice AI agents to handle 100% of inbound phone calls.
- **Natural Language Processing (NLP)**: The AI understands menu questions, special requests, and order modifications conversationally.
- **Upsell Logic**: AI includes built-in upsell prompts based on menu configuration.
- **Order Injection**: Voice AI sends confirmed orders directly to the POS and kitchen display system.

### AI Performance Benchmarks
| Metric | Performance |
|--------|------------|
| Call answer rate | 100% (0 missed calls) |
| Order volume lift | 15–30% |
| Missed call reduction | 40–60% |
| Avg. order value increase | 10–20% |
| Availability | 24/7/365 |

---

## Hardware

### Straunt POS Hardware
- Proprietary next-generation hardware designed for high-speed checkout.
- Built to integrate with the Straunt software stack natively.
- Supports kitchen display system (KDS) routing.
- Hardware details (specific models, specs) are available upon demo request.

---

## Kitchen Operations Technology

- **Smart Kitchen Routing**: AI-powered automatic routing of orders to the correct kitchen station (grill, fryer, bar, prep).
- **Multi-channel Order Consolidation**: Orders from delivery apps, phone AI, and web flow into a single kitchen queue.
- **Virtual Brands**: Support for multiple delivery-only brand storefronts operating from the same kitchen.

---

## Data & Privacy

### Privacy Policy
- Privacy Policy available at: [https://www.straunt.ai/privacy](https://www.straunt.ai/privacy)
- Straunt collects and processes customer and operational data as part of providing its services.
- Data collected includes: ordering behavior, customer contact information, call recordings (for AI agents), and transaction history.

### Data Ownership
- Restaurants using Straunt Direct retain direct ownership of their customer relationship and data, unlike third-party delivery marketplaces where customer data belongs to the platform.

### Data Usage
- Customer data is used to power AI marketing campaigns, loyalty programs, and demand forecasting.
- Centralized customer profiles aggregate data across all ordering channels (phone, web, QR, app, delivery).

---

## Security

- Straunt operates as a cloud-hosted SaaS product, inheriting cloud security standards.
- Specific security certifications (e.g., SOC 2, PCI DSS) are not stated publicly on the website.
- For enterprise and security inquiries, contact [https://www.straunt.ai/contact-us](https://www.straunt.ai/contact-us).
- Terms and Conditions are available at: [https://www.straunt.ai/terms](https://www.straunt.ai/terms)

---

## Scalability & Restaurant Types

Straunt is built for restaurant businesses of multiple sizes and format types:

| Restaurant Type | Straunt Fit |
|----------------|-------------|
| Quick Service (QSR) | 30% increase in captured sales |
| Full-Service / Fine Dining | 100% operations automation |
| Pizza Shops | 150+ new monthly repeat guests |
| Cafés & Bakeries | Zero missed growth opportunities |
| Food Trucks | Supported |
| Steakhouses | Supported |
| Deli & Sandwich | Supported |
| Sushi & Japanese | Supported |
| Mexican & Taco | Supported |

> The platform is designed to scale from single-location restaurants to multi-unit operations.

---

## Integrations Scale

- **100+ integrations** with third-party restaurant applications.
- Integration architecture allows Straunt to act as the central hub — other tools connect into it rather than requiring separate logins.

---

## Availability & Uptime

- AI agents operate 24/7/365 — always-on phone answering, order taking, and reservations.
- Cloud-based infrastructure provides high availability (specific SLA not publicly stated).

---

## Customer Adoption

- **700+ restaurants** use Straunt every day (as stated on the website).

---

## Legal & Compliance References

| Document | URL |
|----------|-----|
| Privacy Policy | https://www.straunt.ai/privacy |
| Terms and Conditions | https://www.straunt.ai/terms |
| Contact / Support | https://www.straunt.ai/contact-us |
