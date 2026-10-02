#!/usr/bin/env python3
"""Cắt references/books/*.md (theo trang scan + tiêu đề) và references/the/*.md (theo mục)
thành đoạn nhỏ, dựng index SQLite FTS5 ở references/tuvi.db.

Chạy lại mỗi khi sửa sách hoặc thẻ:  python3 <skill>/scripts/build.py
"""
import re
import sqlite3
import unicodedata
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
MD = SKILL / "references" / "books"
THE = SKILL / "references" / "the"
DB = SKILL / "references" / "tuvi.db"
MAX_CHARS = 1800  # đoạn dài hơn thì cắt theo đoạn văn

BOOKS = {
    "TVNL-TT01.md": "TT01", "TVNL-TT02.md": "TT02", "TVNL-TT03.md": "TT03",
    "TVNL-TT04.md": "TT04", "TVNL-TT05.md": "TT05", "TVNL-TT07.md": "TT07",
    "TVNL-TT08.md": "TT08", "TVNL-TT09.md": "TT09",
    "Tu Vi Chi Nam_phan I.md": "TVCN1", "Tu Vi Chi Nam_phan II.md": "TVCN2",
    # "phần III" và "phần cuối" thực chất là lịch vạn niên, không có nội dung Tử Vi
    "Tu Vi Chi Nam_phan III.md": "LICH3", "Tu Vi Chi Nam_phan cuoi.md": "LICH",
}
LICH_FROM = {"TVCN2": 2290}  # từ dòng này trở đi là bảng lịch

PAGE_RE = re.compile(r"<!--\s*(?:scan p0*(\d+)|trang (\d+))[^>]*-->")


def fold(s: str) -> str:
    """Bỏ dấu, đ->d, chữ thường. Giữ nguyên độ dài để offset khớp bản gốc."""
    out = []
    for c in s:
        if c in "đĐ":
            out.append("d")
            continue
        base = unicodedata.normalize("NFD", c)[0]
        out.append(base.lower() if len(base.lower()) == 1 else c)
    return "".join(out)


def chunks_of(path: Path):
    lines = path.read_text(encoding="utf-8").splitlines()
    page, heading = "", ""
    buf, start = [], 1

    def flush(end):
        text = "\n".join(l for l in buf if l.strip()).strip()
        if not text:
            return
        # cắt đoạn quá dài theo dòng trống
        piece, pstart = [], start
        for i, l in enumerate(buf):
            piece.append(l)
            if sum(len(x) for x in piece) > MAX_CHARS and not l.strip():
                yield (page, heading, pstart, start + i, "\n".join(piece).strip())
                piece, pstart = [], start + i + 1
        if "".join(piece).strip():
            yield (page, heading, pstart, end, "\n".join(piece).strip())

    for n, line in enumerate(lines, 1):
        m = PAGE_RE.search(line)
        h = re.match(r"^#{2,3}\s+(.*)", line)
        if m or h:
            yield from flush(n - 1)
            buf, start = [], n + (1 if m else 0)
            if m:
                page = "p" + (m.group(1) or m.group(2)).zfill(3)
                continue
            heading = h.group(1).strip()
        buf.append(line)
    yield from flush(len(lines))


def card_chunks(path: Path):
    """Thẻ quy tắc doc/kb/the/*.md: mỗi mục `##` là một đoạn."""
    lines = path.read_text(encoding="utf-8").splitlines()
    heads = [i for i, l in enumerate(lines) if l.startswith("## ")] + [len(lines)]
    for a, b in zip(heads, heads[1:]):
        title = lines[a][3:].split(" · ")[0].strip()
        text = "\n".join(lines[a:b]).strip()
        if title.lower() not in ("từ khoá", "từ khóa"):
            yield ("", title, a + 1, b, text)


def main():
    DB.unlink(missing_ok=True)
    con = sqlite3.connect(DB)
    con.execute(
        "CREATE VIRTUAL TABLE c USING fts5("
        "folded, book UNINDEXED, file UNINDEXED, page UNINDEXED, heading UNINDEXED,"
        "l1 UNINDEXED, l2 UNINDEXED, text UNINDEXED, tokenize='unicode61')"
    )
    total = 0
    for fname, book in BOOKS.items():
        p = MD / fname
        if not p.exists():
            continue
        cut = LICH_FROM.get(book, 10**9)
        rows = [
            (fold(heading + "\n" + t), book if a < cut else "LICH2", fname, pg, heading, a, b, t)
            for pg, heading, a, b, t in chunks_of(p)
        ]
        con.executemany("INSERT INTO c VALUES (?,?,?,?,?,?,?,?)", rows)
        total += len(rows)
        print(f"{book:6} {len(rows):5} đoạn  ({fname})")
    for p in sorted(THE.glob("*.md")):
        book = "THE-" + p.stem
        rows = [
            (fold(t), book, p.name, pg, h, a, b, t)
            for pg, h, a, b, t in card_chunks(p)
        ]
        con.executemany("INSERT INTO c VALUES (?,?,?,?,?,?,?,?)", rows)
        total += len(rows)
        print(f"{book:9} {len(rows):5} thẻ   (the/{p.name})")
    con.commit()
    print(f"Tổng {total} đoạn -> {DB}")


if __name__ == "__main__":
    main()
