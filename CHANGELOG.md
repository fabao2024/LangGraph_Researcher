# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed
- Renamed `langgraph-101.py` to `langgraph_101.py` (PEP 8 compliance)
- Fixed copyright inconsistency between LICENSE and compliance.py
- Fixed invalid Gemini model reference (`gemini-2.5-flash` -> `gemini-2.0-flash`)
- Improved schema validation with proper snake_case regex
- Improved exception handling in codegen.py with specific error types
- Added `.langgraph_api/` and checkpoint files to `.gitignore`

### Added
- `adk/__init__.py` for proper Python package recognition
- `.env.example` template for environment configuration
- `CHANGELOG.md` for tracking project changes
- Version pinning in `requirements.txt`

## [1.0.0] - 2026-01-01

### Added
- Initial release
- ADK skills: git, compliance, codegen, data
- Tavily search integration
- ReAct agent with Gemini model
- Bilingual documentation (PT-BR/EN)
