#!/usr/bin/env python3
"""
Flashcard Server - Extracts flashcards from markdown and serves a study UI.
Usage: python flashcard_server.py --topic TOPIC
"""

import argparse
import http.server
import json
import os
import re
import socketserver
import webbrowser
from datetime import datetime
from pathlib import Path
from urllib.parse import unquote, urlparse, parse_qs

PORT = 8765
BASE_DIR = Path(__file__).parent.parent
FLASHCARDS_DIR = BASE_DIR / "flashcards"

TOPIC_MAP = {
    "agentic-architecture": "agentic-architecture-flashcards.md",
    "tool-design": "tool-design-flashcards.md",
    "claude-code": "claude-code-flashcards.md",
    "prompt-engineering": "prompt-engineering-flashcards.md",
    "context-management": "context-management-flashcards.md",
    "all": None,
}

TOPIC_NAMES = {
    "agentic-architecture": "Agentic Architecture & Orchestration",
    "tool-design": "Tool Design & MCP Integration",
    "claude-code": "Claude Code Configuration & Workflows",
    "prompt-engineering": "Prompt Engineering & Structured Output",
    "context-management": "Context Management & Reliability",
    "all": "All Topics",
}


def extract_flashcards(topic=None):
    """Parse markdown files for flashcard sections."""
    flashcards = []

    if topic and topic != "all":
        md_file = FLASHCARDS_DIR / TOPIC_MAP.get(topic, f"{topic}-flashcards.md")
        if md_file.exists():
            flashcards.extend(_parse_file(md_file))
    else:
        for md_file in FLASHCARDS_DIR.glob("*flashcards.md"):
            flashcards.extend(_parse_file(md_file))

    return flashcards


def _parse_file(md_file):
    """Parse a single markdown file for flashcard sections."""
    flashcards = []
    content = md_file.read_text()

    front_pattern = re.compile(r"^### Front\s*\n(.*?)$", re.MULTILINE | re.DOTALL)
    back_pattern = re.compile(r"^### Back\s*\n(.*?)$", re.MULTILINE | re.DOTALL)

    fronts = front_pattern.findall(content)
    backs = back_pattern.findall(content)

    for front, back in zip(fronts, backs):
        flashcards.append({"front": front.strip(), "back": back.strip()})

    return flashcards


def generate_html(flashcards, topic_name="Flashcards", topic="all"):
    """Generate the flashcard HTML with embedded data."""
    cards_json = json.dumps(flashcards, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{topic_name}</title>
  <style>
    :root {{
      --bg: #1a1a2e;
      --card-bg: #16213e;
      --text: #eee;
      --accent: #0f3460;
      --highlight: #e94560;
      --muted: #94a3b8;
      --needs-work: #f59e0b;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      padding: 2rem;
    }}
    h1 {{ margin-bottom: 0.5rem; }}
    .subtitle {{ color: var(--muted); margin-bottom: 1.5rem; font-size: 0.85rem; }}
    .stats {{
      display: flex;
      gap: 1.5rem;
      margin-bottom: 2rem;
      font-size: 0.9rem;
    }}
    .stat {{ color: var(--muted); }}
    .stat span {{ font-weight: bold; }}
    .stat .known-count {{ color: #22c55e; }}
    .stat .needs-work-count {{ color: var(--needs-work); }}
    .card-container {{
      width: 100%;
      max-width: 600px;
      height: 340px;
      perspective: 1000px;
    }}
    .card {{
      width: 100%;
      height: 100%;
      position: relative;
      transform-style: preserve-3d;
      transition: transform 0.5s ease;
    }}
    .card.flipped {{ transform: rotateX(180deg); }}
    .card-face {{
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      background: var(--card-bg);
      border-radius: 12px;
      padding: 2rem;
      display: flex;
      flex-direction: column;
      justify-content: center;
      cursor: pointer;
      box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    }}
    .card-front {{ transform: rotateX(0deg); }}
    .card-back {{ transform: rotateX(180deg); }}
    .card:hover .card-face {{ box-shadow: 0 8px 30px rgba(0,0,0,0.4); }}
    .card-label {{
      font-size: 0.75rem;
      text-transform: uppercase;
      letter-spacing: 0.1em;
      color: var(--muted);
      margin-bottom: 1rem;
    }}
    .card-content {{
      font-size: 1.25rem;
      line-height: 1.6;
      white-space: pre-wrap;
    }}
    .controls {{
      display: flex;
      gap: 0.5rem;
      margin-top: 1.5rem;
      justify-content: center;
      flex-wrap: wrap;
    }}
    button {{
      background: transparent;
      color: var(--text);
      border: 1px solid var(--text);
      padding: 0.6rem 1rem;
      border-radius: 8px;
      cursor: pointer;
      font-size: 0.9rem;
      transition: all 0.2s;
    }}
    button:hover {{ background: var(--highlight); border-color: var(--highlight); }}
    button.secondary {{ background: transparent; border: 1px solid var(--muted); }}
    button.secondary:hover {{ border-color: var(--highlight); background: transparent; }}
    button.flip-btn:hover {{ background: var(--highlight); border-color: var(--highlight); }}
    button.known-btn {{ border-color: #22c55e; color: #22c55e; }}
    button.known-btn:hover {{ background: #22c55e; border-color: #22c55e; color: #1a1a2e; }}
    button.needs-work-btn {{ background: transparent; border: 1px solid var(--needs-work); color: var(--needs-work); }}
    button.needs-work-btn:hover {{ background: var(--needs-work); border-color: var(--needs-work); color: #1a1a2e; }}
    .keyhint {{ font-size: 0.7rem; color: var(--muted); margin-left: 0.3rem; }}
    .progress-bar {{
      width: 100%;
      max-width: 600px;
      height: 4px;
      background: var(--accent);
      border-radius: 2px;
      margin-bottom: 2rem;
      overflow: hidden;
    }}
    .progress-fill {{
      height: 100%;
      background: var(--highlight);
      transition: width 0.3s ease;
    }}
    .timer {{
      position: fixed;
      top: 1rem;
      right: 1rem;
      font-size: 1.5rem;
      font-weight: bold;
      font-variant-numeric: tabular-nums;
    }}
    .complete-screen {{
      display: none;
      text-align: center;
    }}
    .complete-screen h2 {{ color: var(--highlight); margin-bottom: 1rem; }}
    .complete-screen .time-spent {{ font-size: 2rem; margin: 1rem 0; }}
    .complete-screen .summary {{ color: var(--muted); margin-bottom: 2rem; }}
    .complete-screen .buttons {{ display: flex; gap: 1rem; justify-content: center; margin-top: 1.5rem; }}
    .header {{
      width: 100%;
      max-width: 600px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 1rem;
    }}
    .quit-btn {{
      background: transparent;
      border: 1px solid var(--highlight);
      color: var(--highlight);
      padding: 0.4rem 0.8rem;
      border-radius: 6px;
      cursor: pointer;
      font-size: 0.85rem;
      transition: all 0.2s;
    }}
    .quit-btn:hover {{ background: var(--highlight); color: var(--text); }}
  </style>
</head>
<body>
  <div class="header">
    <button class="quit-btn" id="quitBtn">❌ Quit</button>
    <div class="timer" id="timer">00:00</div>
  </div>
  
  <h1>{topic_name}</h1>
  <p class="subtitle">Space: flip • Enter: Got It • Backspace: Needs Work • h/j/k/l or arrows: navigate</p>
  
  <div class="stats">
    <div class="stat">Card: <span id="current">1</span> / <span id="total">0</span></div>
    <div class="stat">Known: <span class="known-count" id="known">0</span></div>
    <div class="stat">Needs Work: <span class="needs-work-count" id="needsWork">0</span></div>
  </div>

  <div class="progress-bar">
    <div class="progress-fill" id="progress" style="width: 0%"></div>
  </div>

  <div class="card-container">
    <div class="card" id="card">
      <div class="card-face card-front">
        <div class="card-label" id="cardLabel">Question</div>
        <div class="card-content" id="cardContent"></div>
      </div>
      <div class="card-face card-back">
        <div class="card-label" id="cardLabelBack">Answer</div>
        <div class="card-content" id="cardContentBack"></div>
      </div>
    </div>
  </div>

  <div class="controls">
    <button class="secondary" id="prevBtn">⏮️ Prev<span class="keyhint">h/←</span></button>
    <button class="flip-btn" id="flipBtn">🔁 Flip<span class="keyhint">Space</span></button>
    <button class="known-btn" id="knownBtn">😌 Got It<span class="keyhint">Enter</span></button>
    <button class="needs-work-btn" id="needsWorkBtn">🤔 Needs Work<span class="keyhint">Backspace</span></button>
    <button class="secondary" id="nextBtn">⏭️ Next<span class="keyhint">l/→</span></button>
  </div>

  <div class="complete-screen" id="complete">
    <h2>Session Complete!</h2>
    <div class="time-spent" id="finalTime">00:00</div>
    <p class="summary">Known: <span id="knownFinal">0</span> • Needs Work: <span id="needsWorkFinal">0</span> • Reviewed: <span id="cardsReviewed">0</span></p>
    <div class="buttons">
      <button id="logBtn">📝 Log in Study Tracker</button>
      <button onclick="location.reload()">🔄 Study Again</button>
      <button class="secondary" id="exitBtn">🚪 Exit</button>
    </div>
  </div>

  <script>
    const flashcards = {cards_json};

    let currentIndex = 0;
    let isFlipped = false;
    let knownCards = new Set();
    let needsWorkCards = new Set();
    let startTime = Date.now();
    let timerInterval;
    let topic = '{topic}';

    const card = document.getElementById('card');
    const cardLabel = document.getElementById('cardLabel');
    const cardContent = document.getElementById('cardContent');
    const cardLabelBack = document.getElementById('cardLabelBack');
    const cardContentBack = document.getElementById('cardContentBack');
    const currentEl = document.getElementById('current');
    const totalEl = document.getElementById('total');
    const knownEl = document.getElementById('known');
    const needsWorkEl = document.getElementById('needsWork');
    const progressEl = document.getElementById('progress');

    function init() {{
      totalEl.textContent = flashcards.length;
      showCard();
      startTimer();
      loadProgress();
    }}

    function showCard() {{
      const c = flashcards[currentIndex];
      cardContent.textContent = c.front;
      cardContentBack.textContent = c.back;
      currentEl.textContent = currentIndex + 1;
      progressEl.style.width = ((currentIndex + 1) / flashcards.length * 100) + '%';
    }}

    function flipCard() {{
      isFlipped = !isFlipped;
      card.classList.toggle('flipped', isFlipped);
      cardLabel.textContent = isFlipped ? 'Answer' : 'Question';
    }}

    function nextCard() {{
      if (currentIndex < flashcards.length - 1) {{
        currentIndex++;
        isFlipped = false;
        card.classList.remove('flipped');
        showCard();
      }} else {{
        showComplete();
      }}
    }}

    function prevCard() {{
      if (currentIndex > 0) {{
        currentIndex--;
        isFlipped = false;
        card.classList.remove('flipped');
        showCard();
      }}
    }}

    function markKnown() {{
      knownCards.add(currentIndex);
      needsWorkCards.delete(currentIndex);
      knownEl.textContent = knownCards.size;
      needsWorkEl.textContent = needsWorkCards.size;
      saveProgress();
      nextCard();
    }}

    function markNeedsWork() {{
      needsWorkCards.add(currentIndex);
      knownCards.delete(currentIndex);
      knownEl.textContent = knownCards.size;
      needsWorkEl.textContent = needsWorkCards.size;
      saveProgress();
      nextCard();
    }}

    function showComplete() {{
      clearInterval(timerInterval);
      document.querySelector('.card-container').style.display = 'none';
      document.querySelector('.controls').style.display = 'none';
      document.querySelector('.stats').style.display = 'none';
      document.querySelector('.progress-bar').style.display = 'none';
      document.querySelector('.subtitle').style.display = 'none';
      document.querySelector('.header').style.display = 'none';
      document.getElementById('complete').style.display = 'block';
      document.getElementById('finalTime').textContent = document.getElementById('timer').textContent;
      document.getElementById('knownFinal').textContent = knownCards.size;
      document.getElementById('needsWorkFinal').textContent = needsWorkCards.size;
      document.getElementById('cardsReviewed').textContent = flashcards.length;
    }}

    async function logToTracker() {{
      const elapsed = Math.floor((Date.now() - startTime) / 1000);
      const mins = Math.floor(elapsed / 60);
      const topicTitle = topic === 'all' ? 'All Topics' : topic.replace(/-/g, ' ').replace(/\b\w/g, c => c.toUpperCase());
      
      const knownList = Array.from(knownCards).map(i => flashcards[i].front.substring(0, 50)).join(', ');
      const needsWorkList = Array.from(needsWorkCards).map(i => flashcards[i].front.substring(0, 50)).join(', ');
      
      const logData = {{
        topic: topicTitle,
        elapsed: mins,
        knownCount: knownCards.size,
        needsWorkCount: needsWorkCards.size,
        total: flashcards.length,
        known: knownList || 'None',
        needsWork: needsWorkList || 'None'
      }};

      const resp = await fetch('/api/log', {{
        method: 'POST',
        headers: {{'Content-Type': 'application/json'}},
        body: JSON.stringify(logData)
      }});
      
      if (resp.ok) {{
        alert('Logged to study tracker!');
      }} else {{
        alert('Failed to log - ' + await resp.text());
      }}
    }}

    function startTimer() {{
      timerInterval = setInterval(() => {{
        const elapsed = Math.floor((Date.now() - startTime) / 1000);
        const mins = String(Math.floor(elapsed / 60)).padStart(2, '0');
        const secs = String(elapsed % 60).padStart(2, '0');
        document.getElementById('timer').textContent = `${{mins}}:${{secs}}`;
      }}, 1000);
    }}

    function saveProgress() {{
      localStorage.setItem('flashcardProgress', JSON.stringify({{
        currentIndex,
        knownCards: Array.from(knownCards),
        needsWorkCards: Array.from(needsWorkCards),
        startTime
      }}));
    }}

    function loadProgress() {{
      const saved = localStorage.getItem('flashcardProgress');
      if (saved) {{
        const data = JSON.parse(saved);
        if (data.knownCards) {{
          knownCards = new Set(data.knownCards);
          knownEl.textContent = knownCards.size;
        }}
        if (data.needsWorkCards) {{
          needsWorkCards = new Set(data.needsWorkCards);
          needsWorkEl.textContent = needsWorkCards.size;
        }}
      }}
    }}

    card.addEventListener('click', flipCard);
    document.getElementById('flipBtn').addEventListener('click', flipCard);
    document.getElementById('nextBtn').addEventListener('click', nextCard);
    document.getElementById('prevBtn').addEventListener('click', prevCard);
    document.getElementById('knownBtn').addEventListener('click', markKnown);
    document.getElementById('needsWorkBtn').addEventListener('click', markNeedsWork);
    document.getElementById('quitBtn').addEventListener('click', showComplete);
    document.getElementById('logBtn').addEventListener('click', logToTracker);
    document.getElementById('exitBtn').addEventListener('click', () => window.close());

    document.addEventListener('keydown', (e) => {{
      if (e.code === 'Space') {{
        e.preventDefault();
        flipCard();
      }}
      else if (e.code === 'Enter') {{
        e.preventDefault();
        markKnown();
      }}
      else if (e.code === 'Backspace') {{
        e.preventDefault();
        markNeedsWork();
      }}
      else if (e.code === 'ArrowRight' || e.code === 'KeyL') {{
        e.preventDefault();
        nextCard();
      }}
      else if (e.code === 'ArrowLeft' || e.code === 'KeyH') {{
        e.preventDefault();
        prevCard();
      }}
      else if (e.code === 'ArrowUp' || e.code === 'KeyK') {{
        e.preventDefault();
        prevCard();
      }}
      else if (e.code === 'ArrowDown' || e.code === 'KeyJ') {{
        e.preventDefault();
        nextCard();
      }}
    }});

    init();
  </script>
</body>
</html>"""


class FlashcardHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler that serves dynamic flashcard content."""

    def do_GET(self):
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)

        if parsed.path == "/api/cards":
            topic = query.get("topic", ["all"])[0]
            flashcards = extract_flashcards(topic)
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(flashcards).encode())
        else:
            super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)

        if parsed.path == "/api/log":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            log_data = json.loads(body.decode())

            self._log_to_tracker(log_data)

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok"}).encode())
        else:
            super().do_GET()

    def _log_to_tracker(self, data):
        """Append flashcard session to study tracker."""
        tracker_path = BASE_DIR / "course notes" / "study tracker.md"

        now = datetime.now()
        date_str = now.strftime("%Y-%m-%d")
        time_str = now.strftime("%H:%M")

        entry = f"""
### {date_str} ({data["elapsed"]} min flashcard session)
- **Time:** {time_str}
- **Topic:** {data["topic"]}
- **Cards Reviewed:** {data["total"]}
- **Known:** {data["knownCount"]} ({data["known"]})
- **Needs Work:** {data["needsWorkCount"]} ({data["needsWork"]})
"""

        existing = tracker_path.read_text() if tracker_path.exists() else ""

        if "## Study Session Log" not in existing:
            existing = "# Study Tracker Log\n\n## Study Session Log\n"

        tracker_path.write_text(existing + entry)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()


def main():
    parser = argparse.ArgumentParser(description="Flashcard Server")
    parser.add_argument(
        "--topic",
        type=str,
        default="all",
        help=f"Topic to study: {', '.join(TOPIC_MAP.keys())}",
    )
    parser.add_argument("--port", type=int, default=PORT, help="Port to run server on")
    parser.add_argument(
        "--static", action="store_true", help="Generate static HTML and exit"
    )
    parser.add_argument(
        "--no-open", action="store_true", help="Don't open browser automatically"
    )
    args = parser.parse_args()

    topic = args.topic
    if topic not in TOPIC_MAP:
        print(f"Unknown topic: {topic}")
        print(f"Available topics: {', '.join(TOPIC_MAP.keys())}")
        return

    topic_name = TOPIC_NAMES.get(topic, topic.title()) or "Flashcards"
    flashcards = extract_flashcards(topic)

    if len(flashcards) == 0:
        print(f"No flashcards found for topic: {topic}")
        print(f"Available topics: {', '.join(TOPIC_MAP.keys())}")
        return

    print(f"Found {len(flashcards)} flashcards for: {topic_name}")

    if args.static:
        html = generate_html(flashcards, topic_name, topic)
        output_path = BASE_DIR / "flashcards.html"
        output_path.write_text(html)
        print(f"Static HTML written to: {output_path}")
        return

    os.chdir(Path(__file__).parent / "templates")

    with socketserver.TCPServer(("", args.port), FlashcardHandler) as httpd:
        url = f"http://localhost:{args.port}/flashcard.html?topic={topic}"
        print(f"Flashcard server running at {url}")
        print("Press Ctrl+C to stop")

        if not args.no_open:
            webbrowser.open(url)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped")


if __name__ == "__main__":
    main()
