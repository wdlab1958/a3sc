# One Cycle Dev. Framework 페이지 (ISMA3SC003M5)

기존 사이트(www.a3sc.co.kr)의 디자인 시스템 `b.css` 위에 얹는 신규 화면입니다.
기준 화면: `/a3sc/ISMA3SC003M4.do` (AI 플랫폼).

## 운영 서버에 올릴 파일 (신규 4개)

| 파일 | 올릴 위치 | 내용 |
|---|---|---|
| `fragment/ISMA3SC003M5_main.html` | 새 화면 JSP의 `<main>` 안 | 본문 전체 (페이지 전용 스크립트 포함) |
| `resources/css/A3/renewal/onecycle.css` | 같은 경로 | 페이지 전용 스타일. 선택자는 모두 `.oc-` 로 시작 |
| `resources/images/A3/renewal/img/onecycle_poster.jpg` | 같은 경로 | 영상 대표 이미지 |
| `resources/video/onecycle_intro.mp4` | 같은 경로 | 소개 영상 (약 87MB, 8분 40초) |

그 밖의 `resources/` 아래 파일(b.css, 글꼴, 로고 등)과 `reference/` 는 미리보기를 위해 기존 사이트에서 받아 둔 사본이므로 올리지 않습니다.

## 기존 화면에 붙이는 방법

1. 003M4 화면의 JSP를 복사해 새 화면(`ISMA3SC003M5`)을 만들고, `<main>` 안쪽을 `fragment/ISMA3SC003M5_main.html` 로 바꿉니다.
2. `<head>` 의 `b.css` 다음 줄에 추가합니다.
   `<link rel="stylesheet" href="/resources/css/A3/renewal/onecycle.css">`
3. `<title>`, description, canonical, og 값을 새 화면에 맞게 바꿉니다. (값은 `build_preview.py` 상단 참고)
4. 공통 머리글·바닥글의 「AI 플랫폼」 묶음에 메뉴 한 줄을 추가합니다. (모바일 전체 메뉴 `.mnav`, 바닥글 `.gf`)
   `<li><a href="/a3sc/ISMA3SC003M5.do">One Cycle Framework</a></li>`
5. 상단 메뉴는 「AI 플랫폼」에 `class="on"` 을 둡니다. (003M4와 같음)

주소 `ISMA3SC003M5.do` 는 제안값입니다. 다른 번호를 쓰면 4번의 링크와 `build_preview.py` 의 `PAGE` 만 바꾸면 됩니다.

## 플랫폼 상세 화면 연결 (2026-11-25)

「고리를 이루는 다섯 개의 플랫폼」 카드마다 「자세히 보기」 버튼(`.oc-more`)이 있고, 각 버튼은 플랫폼 상세 화면으로 갑니다.
상세 화면은 저장소가 따로 있으며, 같은 `b.css` 위에 공통 확장 `onecycle_product.css`(선택자 `.pd-`)를 씁니다.

| 단계 | 플랫폼 | 운영 주소(제안값) | 검토용 공개 주소 | 저장소 |
|---|---|---|---|---|
| 02 품질 진단 | WDLAB-LLMOps | `/a3sc/ISMA3SC003M6.do` | https://wdlab1958.github.io/WDLAB-LLMOps-Webpage/ | [WDLAB-LLMOps-Webpage](https://github.com/wdlab1958/WDLAB-LLMOps-Webpage) |
| 03 보안 분석·개선 이행 관리 | SSC | `/a3sc/ISMA3SC003M7.do` | https://wdlab1958.github.io/SSC-Platform-Webpage/ | [SSC-Platform-Webpage](https://github.com/wdlab1958/SSC-Platform-Webpage) |
| 04 형식 검증 | WDLAB-Proof-Skills | `/a3sc/ISMA3SC003M8.do` | https://wdlab1958.github.io/webpage_proof_skills/ | [webpage_proof_skills](https://github.com/wdlab1958/webpage_proof_skills) |
| 05 운영 감시 | ARGUS | `/a3sc/ISMA3SC003M9.do` | https://wdlab1958.github.io/ARGUS-Webpage/ | [ARGUS-Webpage](https://github.com/wdlab1958/ARGUS-Webpage) |
| 06 지식 자산화 | MYELIN | `/a3sc/ISMA3SC003M10.do` | https://wdlab1958.github.io/webpage_myelin/ | [webpage_myelin](https://github.com/wdlab1958/webpage_myelin) |

본문(`fragment/`)의 링크는 운영 주소로 적혀 있고, `build_preview.py` 가 `index.html`(GitHub Pages 용)을 만들 때만 `ROUTES` 표에 따라 공개 주소로 바꿉니다.
운영 화면 번호를 다르게 쓰면 본문의 `.oc-more` 링크 다섯 개와 `ROUTES` 를 함께 바꿉니다.

## 미리보기

    python3 build_preview.py            # 본문을 고친 뒤 ISMA3SC003M5.html 다시 만들기
    python3 -m http.server 8765         # http://127.0.0.1:8765/ISMA3SC003M5.html

경로가 `/resources/...` 로 시작하므로 파일을 직접 열지 말고 위처럼 서버로 봅니다.

## 소개 영상 다시 만들기

영상은 원본 폴더 `WDLAB-Proof-Skills/docs/video_intro` 에서 만듭니다. (대본 `script.json`, 슬라이드 `build_slides.py`, 영상 `build_video.py`)
`build_video.py` 를 실행하면 자막 입힌 영상·자막 없는 영상·SRT·ASS·timestamps 가 함께 나옵니다. edge-tts 7.3.1 이상이 필요합니다.
만든 뒤 `docs/A3Security-OneCycle-소개영상-FullHD.mp4` 를 이 프로젝트의 `resources/video/onecycle_intro.mp4` 로 복사하고,
본문 `.oc-chapters` 의 시각을 `timestamps.txt` 에 맞춥니다. 자막 사본: `video_build/onecycle_intro.srt`

## 내용 출처

`A3Security_2027_OneCycle_Business_Model.docx` (v2.0, 2026-11-21)와 소개 영상 자막.
공개 화면이므로 문서의 가격(안), 매출 시나리오, KPI, 리스크, 분기 로드맵, 즉시 실행 과제는 싣지 않았습니다.
