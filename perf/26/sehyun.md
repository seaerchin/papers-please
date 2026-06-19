---
id: sehyun
aliases: []
tags: []
---

s_5e21acd0-e819-426b-8ac1-093c13b40e02

# What did you work with this individual on? What did they do? What was their contribution and impact on public good / product / team?

- i worked with sehyun on Isomer.
- sehyun operates independently, identifies gaps in the team and proactively plugs them. she has highlighted the weekly ritual for proactive support, but i think it is worth noting that this gap was identified and addressed by her independently. i've seen the migrators benefitting greatly from these sessions - they better understand the design principles underpinning Isomer and are better equipped to handle agencies on this front (or to suggest alternatives if Isomer is unable to accept their use case). This went beyond the scope of her design work and influenced the wider team (the migrators) and by extension, the agency.
- i would also like to highlight sehyun's initiative in learning and applying said learnings. she has taken steps to understand tailwind styling, work on said styling in code and eventually moved to shipping feature PRs. this helped to increase engineering bandwidth by reducing context switching required for smaller design fixes and to date, she has shipped >30 PRs in the past year. she has moved beyond designing in Figma to actively contributing to component styling in the codebase and taking up design fixes, which is highly commendable.
- additionally, i would also like to point out her thought leadership and attention to detail to every single decision she makes. 1 clear example is on index pages - she took steps to close the gap in editing between index pages and the card block to ensure that agency users have clear signposting to understand this feature. she also

# Any non-verbatim feedback you would like to share with their manager?

# Scaled Isomer Studio into a self-serviceable platform

**Context**

- Isomer continued to scale with even bigger, complex sites.
- Needed to reduce dependency on manual ops/eng support.

**Contribution**

- Translated recurring ops/eng support into productised workflows ([user management](https://support.isomer.gov.sg/en/articles/10425945-user-access-and-permissions), [tagging pages,](https://www.notion.so/Multi-tag-editing-10b77dbba78880bab059ef571349df82?pvs=21) editing [navigation](https://support.isomer.gov.sg/en/articles/11330742-navigation-bar)/[footer](https://support.isomer.gov.sg/en/articles/11330754-footer)/[settings](https://support.isomer.gov.sg/en/articles/12605759-product-update-oct-25)).
- Defined modular, reusable primitives ([collection widget](https://support.isomer.gov.sg/en/articles/11835511-product-update-july-25), collections, [DGS-powered tables](https://support.isomer.gov.sg/en/articles/12605759-product-update-oct-25)) so agencies can manage “dynamic” content without manual linking or eng support.
- Pitched “[Index page](https://www.figma.com/board/dO0VALjqIIqbevLtIS9s8g/Mini-crit--Editing-index-pages?t=l6Qmd4uooLqxsiwc-6)” abstraction to address the systemic constraint of folders and permalinks being coupled. Benchmarked government websites and designed a system-level solution that enables large, complex sites to present topics without compromising URL structures.
- Introduced quality-of-life capabilities like [Scheduled Publishing](https://www.notion.so/Scheduled-publishing-21777dbba788800ebafcfee34f35fff2?pvs=21). Tested designs to understand sensitivity on scheduling accuracy.
- Established guardrails to balance flexibility with quality (e.g., auto-generated colour palettes). Iterated on constraints through feedback.

**Impact**

- As Isomer’s only designer, led the evolution of Studio from an MVP into a platform agencies can operate independently, freeing up hours of ops/eng support:
  - User management: eliminated ~22 requests or 6 hours of support per month.
  - Tagging a page: used by 32 sites (21,624 pages), previously required ~5 minutes of support per page.
  - Navigation/footer/settings: 132hrs saved in Q3 alone, previously required ops support.
  - Ability to edit ‘index’ pages: 18hrs saved per site for creation and maintenance.
  - Ability to pull articles from a Collection (”Collection widget”): used by 85 sites, 53% drop in on-call requests, previously required ~30 min per change
  - Scheduled publishing: 140 pages scheduled since December.
- Sustained positive NPS (0→2). Supports 2,000+ users.

---

# Identified systemic pain in team processes; built rituals for proactive support

**Context**

- Migrators were struggling to design page layouts and content.
- Migrators had insufficient updates on features or why things were built/designed a certain way.
- Background context from pre-migration agency engagement was sometimes scattered.

**Contributions**

- Ran focus groups with migrators and engineers to [map migration process](https://www.figma.com/board/jIqr6BBBe08HRTsdKGrTm0/-Crit--Migration-journey?node-id=0-1) and identify bottlenecks.
  - Shared findings with the team and [led ideation](https://www.figma.com/board/jIqr6BBBe08HRTsdKGrTm0/-Crit--Migration-journey?node-id=136-457).
- Initiated and managed [weekly migrator support sessions](https://www.notion.so/23a77dbba78880f3b987e06ad5e8adec?pvs=21) consisting of:
  - running through design queries and discussing ideas,
  - teaching ways of thinking (e.g., crash course on IA with MHA migrators),
  - coaching how to explain product rationale,
  - giving transparent updates on upcoming features,
  - providing emotional support
- Initiated [mid-migration check-ins](https://www.notion.so/24577dbba78880c7b8e8dddf7fd4a484?pvs=21).
- Co-led [some migration kickoffs](https://www.notion.so/22a77dbba78880599f4bec7f34be2332?pvs=21) to align work required.

**Impact**

- Shifted team culture from reactive to proactive support.
  - Unblocked and guided [average 5-6 sites per month](https://www.notion.so/23a77dbba7888053af11c825bec5ccc1?pvs=21) through weekly support sessions.
- Sites launched with less accessibility issues and better content presentation.
  - Led [mid-migration check-ins](https://www.notion.so/24577dbba78880c7b8e8dddf7fd4a484?pvs=21) for ~20 sites.
- Improved transparency; shortened feedback loop between migrators and product team.

---

# Enabled platform growth

**Context**

- To capture long-tail of ministries, needed to support branding requirements while not compromising accessibility and trust.
- Needed discipline to not over-build many features.

**Contributions**

- From research, abstracted that “bolder” components that support branding requirements need: striking imagery, strong typography, or imbalanced layout.
  - [Experimented](https://www.figma.com/design/edYULtpmtzwp31MjMLnJa6/Bold-components-playground?m=auto&t=l6Qmd4uooLqxsiwc-6) with 10+ variations and solicited feedback.
  - Prioritised 5+ variations ([New hero banners](https://support.isomer.gov.sg/en/articles/11835511-product-update-july-25), New Card variants, [Block quotes](https://support.isomer.gov.sg/en/articles/11721162-product-update-june-25)) and shipped them.
  - After beta test, pruned variations that didn’t work (they relied heavily on users’ design judgement).
- Designed features that add variety: [Image gallery](https://support.isomer.gov.sg/en/articles/11721162-product-update-june-25), Contact information, Form embeds, Utility navigation.
- Led pre-migration analyses to identify/prioritise feature gaps for sites in pipeline.

**Impact**

- Launched 207 sites, amounting to 68.3m traffic, [site traffic at 20%](https://docs.google.com/spreadsheets/d/1fAQ7cmZgKAL6QRvhypoXuLGDnxOCFWrDO77XLwmdxTA/edit?usp=sharing) (+57%pt. from 12.75%), including flagship sites (MCCY, MINDEF, MOT, Istana, MOF, MFA…).
- Won Ministry families (MCCY, MINDEF) with components that showcase brand identity.
  - Components were well-received; used by 45 sites across 427 pages.
- Despite the template becoming more diverse and robust, quality wasn’t compromised.
  - Median Isomer site accessibility scores: 97/100.
  - All Isomer Next websites qualified for Best Accessibility award (Digital Services Awards 2025) by hitting full marks in WOGAA’s accessibility checks, including [3 sites winning](https://www.digitalservicesawards.gov.sg/winners/2025/).

---

# Increased stakeholders’ design sensitivity and capability

**Context**

- As Isomer scaled, impact risked plateauing at feature delivery.
- Shipping improvements does not automatically produce user-centric websites.
- Without shaping agency mindsets/capability directly, transformation would stall.

**Contributions**

- Conducted [workshop with MFA](https://www.figma.com/board/4WuV4Xn62DKUejRLbqy5FP/MFA-workshop-main-doc?t=0sgL6do4rLu3b8S5-6), streamlining site structure across 5+ directorates and 80+ OMs that lacked ownership of content.
- [Consulted BiblioAsia](https://www.notion.so/29477dbba788809694a9dc5009bdad18?pvs=21), identifying 1 high-impact/low-effort feature (podcast embeds) from the list of [6 initial feature requests](https://www.notion.so/29477dbba788809694a9dc5009bdad18?pvs=21).
- Consulted ITE, URA, HSA, advising on IA. Analysed traffic data, reviewed similar websites, mocked up sitemaps.
- Engaged Wai Keong to write [reusable content guidelines](https://docs.google.com/document/d/1PuwKzPOfeOP-vf45bAn_W2uZ8U2ahdlrMHAN00XGHrQ/edit?disco=AAABnvk_s2Y).

**Impact**

- Improved agencies’ design sensitivity:
  - MFA continues to engage Isomer for continuous improvement.
  - ITE found late-stage recommendations highly useful; commented that earlier design involvement would have strengthened their decisions.
- Reduced potential scope creep and increased stakeholder acceptance of platform constraints:
  - BiblioAsia initially asked for 6+ features. After consultation, reduced scope to 1 (podcast embeds).
- Stakeholders know how to look up site traffic data and think in user-centric ways.

---

# Shaped guidelines for user-facing content

**Context**

- No clear standards for user-facing content (e.g., inconsistent feature naming).
- Needed to prepare for mass migrations from Isomer Classic to Next, where support would be tested at scale.

**Contributions/Impact**

- Established and led [weekly content workstream](https://www.notion.so/Isomer-user-help-guidance-27c77dbba788802e9817cedd18ebd05d?pvs=21). Improved clarity on user-facing content ([Guide](https://www.notion.so/2ae77dbba788808a9273dfc22bcf3635?pvs=21), Sample Site, [Streamline FAQs](https://www.notion.so/2bc77dbba78880e486e1eb9748ffb52e?pvs=21)) by feedback/coaching.
- Defined and socialised Isomer’s [user-facing voice and tone](https://www.notion.so/Junora-voice-guide-2ae77dbba788803b8166f302a689b210?pvs=21) (“Junora”), emphasising kindness, humility, and transparency.
- [Standardised 20+ terms](https://github.com/opengovsg/isomer/pull/1757) across product interface.
- [Published 4 blog articles](https://sample.isomer.gov.sg/by-design/) on crafting summaries, alt texts, and homepages, enabling scalable thought leadership.

---

# Expanded technical capacity and depth

**Contributions**

- Expanded dev scope to be able to ship Studio features with eng mentorship.
- Up-skilled in AI tools.
- Continued levelling up in visual design.

**Impact**

- Reduced design’s dependency on engineering:
  - [Enabled LogoCloud](https://github.com/opengovsg/isomer/pull/1758) on Studio.
  - [Merged 20+ PRs](https://github.com/opengovsg/isomer/pulls?q=is%3Apr+author%3Asehyunidaaa+is%3Aclosed) with component/accessibility fixes.
  - Experimented with features that require logic (e.g., [Pager](https://opengovproducts.slack.com/archives/C06R4DX966P/p1760327032929459)).
  - Created [realistic prototypes](https://opengovproducts.slack.com/archives/C06R4DX966P/p1759810196965149?thread_ts=1759453203.707399&cid=C06R4DX966P) for critiques.
- Crafted a unique brand for [SpeakEasy](https://go.gov.sg/speakeasy); resourced as limited-release.

---

# Citizenship

- Facilitated design thinking and prototyping workshop for 12 ASEAN delegates, preparing them for HFPG. [Received 4.91/5 rating](https://opengovproducts.slack.com/archives/C06GYCHKAKZ/p1767670880585469?thread_ts=1767670675.290479&cid=C06GYCHKAKZ) and positive feedback.
- [Represented OGP](https://www.figma.com/slides/hIV9G1CvJHZFINJTPtGbUr/Mar-27--ADPList-sharing?t=0sgL6do4rLu3b8S5-6) in a BFGxADPList meetup to tech community. [Improved awareness about OGP/Isomer](https://www.linkedin.com/posts/adplist-singapore-chapter_product-design-uxdesign-activity-7311293141293092865-Jwwe?utm_source=share&utm_medium=member_desktop&rcm=ACoAAB9urpYBAhygljNz2jo26ctOKwK-h-etZGY).
- Mentored 2 designers externally, with sustained engagement.
- Supported designers through Kakis and ad-hoc (Germaine’s conversion, Constance).
- Hiring squad, buddy for Zoey.
