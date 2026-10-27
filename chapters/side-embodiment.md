# Side: Embodiment - Why Robotics Is Not Book Six

**Ontological note:** a robot is an embodied AI mind, or more precisely an exocortex with hands. Locomotion, manipulation, and presence add no new rung to the ladder of control loss; they only make the existing rungs visible in the hallway. A separate `on-robotics` volume would splinter evidence density below the ten-rung viability bar in SERIES.md. One embodiment thread per book instead: takeover owns the labor mechanics, hypermind owns the cognitive reading (this file), hyperwar already owns the violent half. No duplication.

## 1. The price ladder (all dated, all public)

The iPhone-price threshold has been crossed from both directions at once:

* **2025-10-22/23: Noetix Bumi presale, CNY 9,988 (~$1,400).** Beijing startup (founded 2023), child-sized education humanoid, 94 cm, ~12 kg, 21+ DoF, bipedal, voice + app control. The cheapest bipedal humanoid on record. `[construction: one German-language source reports 98 cm / 17 kg - resolve whether this is a variant or a spec revision.]`
* **2026-08-24/26: Nori A3 launch, $1,688, Y Combinator-backed, San Francisco.** Wheeled base, 19 DOF bimanual torso, trainable skills, 1.5 kg payload per arm, US-assembled, shipping fall 2026. The American answer at the same price point: not a walker but a household bimanual.
* **2026: Unitree G1 ~$16K; 1X NEO $20,000 purchase or $499/month subscription** (shipping 2026, 30 kg, the only platform built specifically for home use with consumer pre-orders); **Tesla Optimus target $20-30K**; **Figure enterprise estimates $50-150K** (company valued at $39B); **Agility Digit ~$250K**; **Unitree GD01 3.9M RMB (~$530K)** - see section 3.
* Reading: the consumer floor fell from ~$16K to ~$1.4K in under a year. The homebot is no longer a forecast. It is a presale.

Fleet note: `rust-saschirob-mcp` (SaschiRob, local-memory-first household platform) and `norirobotics-mcp` (Nori bridge) are the household-memory instances. When the robot remembers where you left the keys better than you do, inversion becomes visible - that is Ch. I, not a new book.

## 2. PRC vs. US: two strategies, same threshold

* **PRC, spectacle + mass production:** Unitree as official robot partner of the 2026 Spring Festival Gala (G1 + H2, billed as the first fully robot-performed segment); Noetix Bumi Spring Festival Gala appearance; presale-to-shipment consumer pipeline; GD01 manned mecha in mass production (May 2026).
* **US, enterprise + subscription:** Figure's enterprise go-to-market, Agility's warehouse deployments, Tesla's scale-manufacturing bet, 1X's $499/month home subscription (the carrier-contract model applied to bodies), Nori's YC-backed assembly story.
* Neither side leads on safety institutions - see section 5. The race is on shipment, not on governance.

## 3. The mecha datum: Unitree GD01 (2026-05-12)

On May 12, 2026, Unitree unveiled the GD01: ~3 m tall, 500 kg with pilot aboard, walking, transformable, manned - billed as the world's first mass-produced manned mecha, founder Wang Xingxing demoing in person, aimed at heavy-industrial customers and demonstration deployments. Price reported 3.9M RMB (~$530K); IPO preparation reported July 2026. `[construction: confirm price and IPO figures against primary filings, not trade press.]`

Why it belongs in this file: the GD01 is the exocortex inversion worn as a vehicle. The pilot does not drive the mecha the way a driver drives a car; the machine balances, steps, and stabilizes while the human supplies intent and liability. Preference closure (Threshold C) with 500 kilograms under it.

Counter-datum, same vendor: **2026-10-21, H2-X "Kung Fu Legend" demo** - stylized unveiling video, followed within days by a live demo in which the unit stumbled during a side flip and lost part of a leg (reported 2026-10-24/26). Spectacle and failure in the same week. File both; the gap between promo render and live physics is itself telemetry.

## 4. DIY: unrestricted replication is already here

* **Berkeley Humanoid Lite (Aug 2026):** fully open-source, under $5,000 to build, 3D-printed actuators, complete CAD + URDF/MJCF/USD, full pipeline from Isaac Lab training through MuJoCo validation to deployment (Hackaday 2026-08-30).
* **HOPEJr (May 2026):** DIY humanoid, 66 DoF, 3D-printed parts, dexterous hands, full LeRobot integration.
* **LeRobot Humanoid (Hugging Face):** open, low-cost, 3D-printed platform for robot learning.
* **pib.rocks:** printable humanoid for home assembly. **Roboto Origin (Roboparty):** fully open-source full-stack biped with complete BOM table - materials, drivers, electronics, procurement channels, assembly steps.

Reading for the hazard rule: capability is now downloadable. The BOM table is the proliferation vector - no foundry, no export license, no lab required. Governance that assumes robots ship from factories is governing the wrong decade.

## 5. Dangers (governance only, never mechanisms)

Dated public incidents, observable without speculation:

* **2026-09-10 (OECD.ai incident record):** Unitree test site, Shaoxing - humanoid malfunction, uncontrolled movements, spinning kick that knocked a remote from an engineer's hand and narrowly missed him, captured on security video.
* **2026-08-20:** remote-control connection failure, unit toppled and thrashed limbs on its back ("seizure" framing in trade press).
* **2026-10-21/26:** H2-X live demo failure, above.
* **Institutions responding:** ISO 25785-1 (2026 humanoid safety standard), ISO 10218 / ISO-TS 15066 / ISO 13482 compliance guides, OSHA facility requirements, and at least one 2026 analysis describing a "regulatory wall" between static ISO assumptions and dynamic bipedal risk.

Attachment points (Threshold C pattern): whoever certifies the fall zone, whoever insures the household deployment, whoever writes the procurement spec for the warehouse fleet. Name them when they appear; do not predict them.

## 6. What this sidecar is not

Not a product catalog (prices rot; the ladder does not). Not a safety manual (no mechanisms, per the hazard rule). Not the labor story - that belongs in `on-ai-takeover` as `side-embodied-labor.md`: teleop-to-autonomy dates, manipulation milestones, liability attachment points, still to be written. This file answers one question: what does it mean, for the observer of Ch. I-III, that the loop now has hands? Answer: inversion becomes undeniable the first morning the household mind finds your keys before you finish the sentence.
