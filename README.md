# HIVE

HIVE is an automated signal aggregator designed to identify cross-platform arbitrage opportunities in decentralized prediction markets. It automates the tedious, manual search for price discrepancies across platforms like Kalshi and Polymarket.

### Business Problem:
The Alpha-Discovery Problem: Markets are inefficient because human attention is finite. While Kalshi and Polymarket reflect the same real-world events, they rarely reach consensus instantly. We're automating the tedious, high-latency search for cross-platform arbitrage opportunities, effectively building a 'Low-Latency Signal Aggregator' that turns fragmented market noise into actionable Alpha.

### The Objective
Decentralized markets are fragmented. They often trade the same events at different prices, but finding these "Alpha" opportunities manually is inefficient and high-latency. HIVE bridges these platforms by normalizing event data and identifying price spreads in real-time.

### System Architecture
HIVE uses a **Shared-Encoder Semantic Matching Pipeline**:
*   **Normalization Layer:** Maps heterogeneous event titles (e.g., "Will it rain?" vs. "Precipitation expected?") into a shared vector space using a pretrained sentence-transformer.
*   **Comparison Engine:** Uses cosine similarity to detect event parity and triggers alerts when price deltas exceed defined thresholds.

### Technical Stack
*   **Core:** Python, `sentence-transformers` for semantic event matching.
*   **Data:** REST API integration for real-time market polling.
*   **Infrastructure (Planned):** Containerized via Docker; scalable via Kubernetes for high-uptime signal aggregation.

### Getting Started
1.  **Clone the repo:** `git clone https://github.com/bhargav-chataut/HIVE`
2.  **Install requirements:** `pip install -r requirements.txt`
3.  **Run:** market discovery endpoints on Kalshi and Polymarket are public and require no API key. Authentication is only needed for placing trades, which this project does not currently do.

---
*Built as a proprietary market analysis tool.*