import re, sys

def make_srt(txt_path, srt_path, total):
    text = open(txt_path, encoding="utf-8").read().strip()
    raw = re.split(r"(?<=[.!?])\s+", text)
    cues = []
    for s in raw:
        s = s.strip()
        if not s:
            continue
        if len(s) < 12 and cues:
            cues[-1] = cues[-1] + " " + s
        elif s in ("Dislike.", "Amusement.", "Fear.", "Helpful."):
            cues[-1] = cues[-1] + " " + s
        else:
            cues.append(s)
    weights = [len(c) for c in cues]
    t = 0.0
    def ts(x):
        h = int(x // 3600); m = int((x % 3600) // 60)
        sec = int(x % 60); ms = int(round((x - int(x)) * 1000))
        return f"{h:02}:{m:02}:{sec:02},{ms:03}"
    out = []
    for i, c in enumerate(cues, 1):
        dur = total * len(c) / sum(weights)
        start = t
        end = min(total, t + dur - 0.08) if i < len(cues) else total
        out.append(f"{i}\n{ts(start)} --> {ts(end)}\n{c}\n")
        t += dur
    open(srt_path, "w", encoding="utf-8").write("\n".join(out))
    print(f"{srt_path}: {len(cues)} cues over {total}s")

make_srt("D:/Dev/repos/on-hypermind/pilot/short06.txt",
         "D:/Dev/repos/on-hypermind/pilot/short06.srt", 35.05)
make_srt("D:/Dev/repos/on-hypermind/pilot/short11.txt",
         "D:/Dev/repos/on-hypermind/pilot/short11.srt", 30.30)
