# Public-data redaction — 31 October 2026

Public behavioural exports retain question responses, completion status and replacement participant codes. Prolific IDs, original survey response IDs, demographics, contact/location fields, timestamps, device metadata and free text have been removed. Replacement codes are scoped to each study/language dataset and remain consistent between raw and processed matching files. The ResponseId column name and R_ prefix are retained for compatibility with the R scripts. Qualtrics question-description/import rows are retained for preprocessing.

Rendered notebooks and the saved R workspace are removed because they can embed earlier data. Source R notebooks remain available. Run `python scripts/check_public_data.py` before release; CI runs the same check. This structural check does not establish anonymity or inspect the meaning of arbitrary free text elsewhere.

All six preprocessing pipelines were run before and after redaction. Participant groupings, filtered matching responses and rating summaries agree; maximum summary difference is 2.23e-16 from floating-point summation order. Existing aggregate data and published tables are unchanged. Full statistical models were not rerun.

The existing English processed matching CSV contains unresolved Git merge markers and both conflict sections. These have been preserved during privacy redaction. Resolve this pre-existing data defect separately before treating a full analysis rerun as validated.

Historical participant-level exports and cached outputs were removed from the prepared Git history, then sanitised replacements added. Hosted history, OSF file versions, forks and downloaded copies require separate remediation; this note does not claim their removal.
