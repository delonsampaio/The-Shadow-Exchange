---
entity_type: Tracker
name: "Crew Inventory"
last_updated_session: "00"
---

# Crew Inventory

Coin, claims, notable loot, Relics in the vault, Biologicals in cold storage. 
*(Note: Anchor Items live in the `Anchor-Ledger.md`, not here.)*

## Coin & Stash
* **Crew Coin:** 0
* **Stash (Per PC):** *(Reference PC sheets directly)*

## Cold Storage 
*(Spoilage clocks paused while stored. Vault locked if Audit Clock triggers.)*
* **[Item: Name of Biological]**
    * **Value:** X Coin
    * **Spoilage Clock:** `[ ◌ ◌ ◌ ]` (Currently Paused)

## Lead-Lined Vault 
*(Resonance leaks neutralized.)*
* **[Item: Name of Relic]**
    * **Value:** X Coin / Tier X
    * **Function:** Brief description of what it does.

## What kept items can do
See `01-Crew/Crew-Sheet.md` → *What kept items do*: a Biological can be sold, spent on a score or gifted; a Relic can be sold, used once per score (Resonance +1) or counted toward a bribe; an Anchor is never sold or used as a tool.

## Relics in Regular Use
*(Items carried by the crew or left exposed in the Lair. High risk of Resonance leaks.)*
## Notable Items (Mundane)
* **The Hunter's Journal** *(Containment Suite, reading stand near the Post-Op Table)*
* **Trophy Wall Polaroids** *(Containment Suite)*

## AI Inventory Management Directives
* **Spoilage Tracking:** If a Biological is moved from Cold Storage, immediately prompt the GM to resume its `[Clock: Biological Spoilage]`.
* **Resonance Leaks:** When generating consequences between sessions, look at "Relics in Regular Use" and create sensory, escalating hauntings in the Lair caused by these exposed items.
