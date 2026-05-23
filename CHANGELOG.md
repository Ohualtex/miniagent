# Değişiklik Günlüğü

Bu projedeki önemli değişiklikler burada belgelenmektedir.

Format: [Keep a Changelog](https://keepachangelog.com/)

---

## [Unreleased]

### Eklenen
- 5 yeni skill: `git-log`, `ip-location`, `json-format`, `open-ports`, `system-info`
- Repo hijyeni: `CONTRIBUTING.md`, `SECURITY.md`, `.editorconfig`, `requirements.txt`
- GitHub şablonları: issue (`bug_report`, `feature_request`) ve PR template
- README'ye lisans / Python / PRs welcome rozetleri

### Değişen
- `.gitignore` cross-platform genişletildi (Windows/Linux/macOS, IDE, virtualenv)
- `.gitignore`'a `.gemini/` ve `.claude/` eklendi (yerel agent dizinleri)

## [v2.0] — 2026-05-18

### Eklenen
- Lazy-load mimarisiyle skill loader sistemi (OpenClaw ilham)
- 3 yerleşik skill: `weather`, `find-large-files`, `mac-notification`
- Markdown tabanlı skill formatı (frontmatter + body) ile `skills/` dizini
- Sistem prompt'a enjekte edilen XML skill kataloğu
- SKILL.md okuma sonrası bash çalıştırmayı garanti eden deterministik hatırlatma
- `SKILLS_DIR`, `BASH_TIMEOUT`, `MAX_OUTPUT` yapılandırma sabitleri

### Değişen
- Hardcoded tool'lardan primitive + skill mimarisine geçildi
- Sistem prompt'a skill kullanım talimatları eklendi

## [v1.0] — 2026-05-15

### Eklenen
- Temel agent döngüsü (~117 satır)
- 3 hardcoded tool: `read_file`, `list_files`, `calculator`
- Qwen 2.5 7B ile Ollama entegrasyonu
- Türkçe sistem prompt'u
- Sıfır bağımlılık, tek dosya mimarisi
