#!/usr/bin/env python3
"""미리보기용 전체 페이지(ISMA3SC003M5.html)를 만든다.

기존 화면(ISMA3SC003M4.do)의 머리글·바닥글을 그대로 가져와 본문만 fragment/ISMA3SC003M5_main.html 로 바꾼다.
본문을 고친 뒤 다시 실행하면 미리보기가 갱신된다.  사용: python3 build_preview.py
"""
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC_URL = "https://www.a3sc.co.kr/a3sc/ISMA3SC003M4.do"
CACHE = ROOT / "reference" / "ISMA3SC003M4.html"
PAGE = "/a3sc/ISMA3SC003M5.do"
TITLE = "One Cycle Dev. Framework | 에이쓰리시큐리티"
DESC = "개발·품질 진단·보안 분석·형식 검증·24시간 감시·지식 자산화를 하나의 순환 고리로 묶은 에이쓰리시큐리티의 One Cycle Dev. Framework를 소개합니다."


def source() -> str:
    if not CACHE.exists():
        CACHE.parent.mkdir(exist_ok=True)
        req = urllib.request.Request(SRC_URL, headers={"User-Agent": "Mozilla/5.0"})
        CACHE.write_bytes(urllib.request.urlopen(req, timeout=30).read())
    return CACHE.read_text(encoding="utf-8")


def must_sub(pattern: str, repl: str, text: str, flags: int = 0) -> str:
    out, n = re.subn(pattern, lambda _m: repl, text, count=1, flags=flags)
    if n != 1:
        sys.exit(f"기존 화면 구조가 바뀌어 치환하지 못했습니다: {pattern}")
    return out


def main() -> None:
    html = source().lstrip()
    body = (ROOT / "fragment" / "ISMA3SC003M5_main.html").read_text(encoding="utf-8")

    # 본문 교체
    html = must_sub(r"<main>.*?</main>", "<main>\n" + body + "</main>", html, re.S)
    # 머리: 제목·설명·주소, 페이지 전용 스타일 추가
    html = must_sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", html)
    html = re.sub(r'(<meta (?:name="description"|property="og:description") content=")[^"]*', lambda m: m.group(1) + DESC, html)
    html = must_sub(r'(?<=<meta property="og:title" content=")[^"]*', TITLE, html)
    html = html.replace("/a3sc/ISMA3SC003M4.do\">\n<meta property=\"al", PAGE + "\">\n<meta property=\"al")
    html = html.replace('rel="canonical" href="https://www.a3sc.co.kr/a3sc/ISMA3SC003M4.do"', f'rel="canonical" href="https://www.a3sc.co.kr{PAGE}"')
    html = html.replace('global_request_uri = "/a3sc/ISMA3SC003M4.do"', f'global_request_uri = "{PAGE}"')
    html = must_sub(r'<link rel="stylesheet" href="/resources/css/A3/renewal/b\.css">',
                    '<link rel="stylesheet" href="/resources/css/A3/renewal/b.css">\n'
                    '<link rel="stylesheet" href="/resources/css/A3/renewal/onecycle.css">', html)
    # 메뉴: 모바일 전체 메뉴와 바닥글의 「AI 플랫폼」 묶음에 새 화면 추가
    item = f'<li><a href="{PAGE}">One Cycle Framework</a></li>'
    html = must_sub(r'(?<=<li><a href="/a3sc/ISMA3SC003M4\.do#lineup">플랫폼 9종</a></li>)(?=<li><a href="/a3sc/ISMA3SC003M4\.do#contact">)', item, html)
    html = must_sub(r'(?<=<li><a href="/a3sc/ISMA3SC003M4\.do#lineup">플랫폼 9종</a></li>)(?=<li class="fam-off">)', item, html)
    # 미리보기에서는 기존 화면 전용 스크립트(게시판·세션·통계)를 뺀다
    html = re.sub(r"<!-- jquery.*?</script>\n</head>", "</head>", html, flags=re.S)

    (ROOT / "ISMA3SC003M5.html").write_text(html, encoding="utf-8")
    print("written: ISMA3SC003M5.html", len(html), "bytes")

    # GitHub Pages 용 index.html: 하위 경로(/a3sc/)에서 열리므로 자원은 상대 경로로,
    # 다른 화면 링크는 실제 사이트로 보낸다. 검토용이므로 검색 노출을 막는다.
    pages = html.replace('"/resources/', '"resources/').replace("url(/resources/", "url(resources/")
    pages = pages.replace(f'href="{PAGE}"', 'href="./"')
    pages = pages.replace('href="/a3sc/', 'href="https://www.a3sc.co.kr/a3sc/')
    pages = re.sub(r'<link rel="canonical"[^>]*>\n?', "", pages)
    pages = must_sub(r'(?<=<meta name="robots" content=")[^"]*', "noindex,nofollow", pages)
    (ROOT / "index.html").write_text(pages, encoding="utf-8")
    print("written: index.html", len(pages), "bytes")


if __name__ == "__main__":
    main()
