import os
import sys
from pathlib import Path

import yaml

# --- CONFIG/ENV ---
llm_api_key = os.getenv("LLM_API_KEY")
article_path = os.getenv("ARTICLE_PATH")
mode = os.getenv("MODE", "revise").lower()  # 'revise' or 'draft'

if not llm_api_key:
    print("[INFO] No LLM_API_KEY found, skipping AI assist.")
    sys.exit(0)
if not article_path:
    print("[ERROR] ARTICLE_PATH not specified.")
    sys.exit(1)

article_file = Path(article_path)
if not article_file.exists():
    print(f"[ERROR] File not found: {article_file}")
    sys.exit(1)

# --- LOAD ARTICLE ---

with article_file.open("r", encoding="utf-8") as f:
    contents = f.read()

# Extract frontmatter block (---\n ... \n---\n)
def extract_fm(text):
    if not text.startswith("---"):
        return None, text
    import re
    m = re.match(r"^---\n(.*?)\n---\n(.*)", text, re.S)
    if m:
        fm = yaml.safe_load(m.group(1))
        body = m.group(2)
        return fm, body
    return None, text

fm, body = extract_fm(contents)

# --- AI Integration Stub ---
def mock_llm(prompt, mode):
    # IMPLEMENT: Actual LLM call here (OpenAI, Anthropic, Huggingface, etc)
    # For now, just stub. You could use requests + API for real integration.
    if mode == "draft":
        return body + "\n\n> [AI draft suggestion: expand or elaborate based on prompt]\n"
    elif mode == "revise":
        return body.replace("...", "... [AI review suggestion: polish, clarify, add examples]\n")
    else:
        return body

# You can build a prompt from frontmatter + body
prompt = f"Please {mode} the following article content:\n\n{body}"

new_body = mock_llm(prompt, mode)
if not new_body or new_body == body:
    print("[INFO] No changes produced.")
    sys.exit(0)

# --- Write New Article ---

with article_file.open("w", encoding="utf-8") as f:
    if fm:
        f.write("---\n")
        yaml.dump(fm, f, sort_keys=False)
        f.write("---\n")
    f.write(new_body)

print("[INFO] AI assist applied to", article_file)
