# Use-Case Flow - UC-01 Place Order & Lock Payment in Escrow

**Student:** Samarth Mohan | **SRN:** PES1UG24CS703 | **Lab 1**
**Actors:** Buyer (primary), Inspection Agent (primary), Seller (secondary), Payment Gateway (external)

## Preconditions
1. Buyer is logged in and has a saved address.
2. Product listing is active and seller is verified.
3. Payment method is ready.
4. At least one inspection agent is available.

## Postconditions (on success)
- Money is in escrow, order = 'Under Inspection'
- Inspection task created and agent notified
- Buyer sees 'Funds Locked'

## Main Success Scenario
1. Buyer clicks 'Buy & Fund Escrow'
2. System shows summary, buyer confirms
3. System calls Payment Gateway (<<include>> Process Payment)
4. Gateway locks money (<2s)
5. System sets order to 'Under Inspection' and creates task
6. Agent gets notice; buyer sees 'Funds Locked'
7. Agent uploads report (photos + grade)
8. System shows report to buyer (Approve / Dispute within 48 hrs)
9. Buyer clicks Approve
10. System releases money to seller, order = Closed

## Alternate Flows
- **3a Payment fails:** show error, allow 2 retries, then cancel, no money locked
- **7a Inspection fails:** refund to buyer within 24 hrs if accepted
- **9a Dispute (<<extend>> UC-06):** freeze escrow in <2s, block withdrawals, create ticket, no move until resolved
- **8a No response 48 hrs:** reminder then auto-rule
