# Second-Hand Product Escrow Marketplace - Lab 3

**Student:** Samarth Mohan
**SRN:** PES1UG24CS703
**Problem No:** 39
**Domain:** Retail, E-Commerce & Finance
**Topic:** Component modelling and architectural pattern selection

## What this lab does

It compares the three architectural styles, Layered, Microservices and Client-Server, against the escrow marketplace, selects one with reasons taken from the Lab 1 requirements, and models the chosen system as UML components with their interfaces.

## What was decided

Microservices with an API Gateway. Three things drive the choice: money must move correctly, the escrow lock must finish in under 2 seconds, and a dispute must freeze funds at once. Separate services let the busy browsing and photo upload paths scale on their own, keep a failure in the notification or inspection path away from the money path, and keep card data inside one service.

The model has 10 components: Buyer Web / Mobile App, Inspection Agent Console, Web API Gateway, Order Manager, Payment Service, Escrow Ledger, Inspection Service, Photo Object Store, Notification Service and Identity & Access. The External Payment Gateway is the one element outside the system boundary. Interfaces are drawn with ball and socket notation, ports group the interfaces that meet at one interaction point, and the one dependency that is not an interface, the inspection photo store, is drawn as a dashed usage dependency.

## Files in this folder

1. **UML_Component_Diagram_PES1UG24CS703.pdf** (also .png) - the component diagram deliverable, exported from LucidChart.
2. **Architecture_Justification_PES1UG24CS703.pdf** - the one page justification deliverable: architecture choice, two reasons, security advantage, performance benefit.
3. **Lab3_Report.pdf** - the full report: the style comparison, selection and justification, component table, interface table and the diagram.
4. **README.md** - this file.

Requirement IDs FR-001 to FR-005, NFR-001 and NFR-002 come from the Lab 1 requirements table for the same problem statement.
