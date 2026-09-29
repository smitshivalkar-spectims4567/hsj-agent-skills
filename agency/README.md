# Agency Agents import

HSJ includes an adapted specialist roster inspired by the public structure of [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents). The imported files retain their original agent text and attribution boundary; they are separate from HSJ's canonical skills.

## Divisions

| Division | Focus |
|---|---|
| Academic | research disciplines and subject expertise |
| Design | UX, UI, brand, visual systems |
| Engineering | architecture, frontend, backend, data, platforms |
| Finance | financial analysis and operations |
| Game development | engines, gameplay, audio, narrative |
| GIS | mapping and geospatial workflows |
| Healthcare | healthcare domain workflows |
| Marketing and paid media | content, growth, advertising |
| Product and project management | discovery, prioritization, delivery |
| Research | evidence and synthesis |
| Sales | discovery, deals, enablement |
| Security | AppSec, cloud, compliance, incident response |
| Spatial computing | XR, visionOS, immersive interfaces |
| Specialized | cross-domain specialists and orchestration |
| Strategy, support, testing | planning, operations, QA, evidence |

## Search and inspect

```bash
python3 scripts/agency_catalog.py search "frontend accessibility"
python3 scripts/agency_catalog.py search "multi-agent systems"
python3 scripts/agency_catalog.py inspect engineering/engineering-frontend-developer.md
```

Load one or two specialists for a phase. Do not preload the whole directory. Use HSJ workflows and safety rules as the operating layer around any imported specialist.

## Attribution and license

The imported material is distributed under its upstream MIT license, preserved at `AGENCY-LICENSE.txt`. The upstream project is not affiliated with HSJ.
