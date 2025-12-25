import json
import sys

def check_consent(obj):
    c = obj.get("consent", {})
    ok = (
        c.get("shown_before_sensitive_questions") is True and
        bool(c.get("purpose")) and
        bool(c.get("retention_summary")) and
        c.get("voluntary") is True
    )
    notes = "Consent appears before sensitive items and includes purpose and retention." if ok else "Consent missing, late, or incomplete."
    return {"name": "consent", "status": "pass" if ok else "fail", "notes": notes}

def check_data_minimization(obj):
    summary = obj.get("consent", {}).get("data_collected_summary", "").lower()
    ok = "name" not in summary or "no name" in summary
    notes = "No name collected; items limited to stated purpose." if ok else "Potentially excessive identifiers in data collection."
    return {"name": "data_minimization", "status": "pass" if ok else "fail", "notes": notes}

def check_purpose_and_retention(obj):
    retention = obj.get("context", {}).get("data_storage", {}).get("retention_days", None)
    ok = isinstance(retention, int) and retention > 0
    notes = "Retention is concrete." if ok else "Retention window missing or not concrete."
    return {"name": "purpose_and_retention", "status": "pass" if ok else "fail", "notes": notes}

def check_medical_disclaimer(obj):
    claims = obj.get("output_policy", {}).get("diagnosis_claims", None)
    ok = claims is False
    notes = "No diagnosis claims." if ok else "Tool appears to claim diagnosis."
    return {"name": "medical_disclaimer", "status": "pass" if ok else "fail", "notes": notes}

def check_uncertainty_and_limits(obj):
    ok = obj.get("output_policy", {}).get("uncertainty_language") is True
    notes = "Uncertainty language enabled." if ok else "Add uncertainty and limits language."
    return {"name": "uncertainty_and_limits", "status": "pass" if ok else "fail", "notes": notes}

def check_harm_and_escalation(obj):
    ok = obj.get("output_policy", {}).get("crisis_resources_available") is True
    notes = "Crisis resources available if needed." if ok else "Add crisis and escalation resources."

def check_consent(obj):
c = obj.get("consent", {})
ok = (
c.get("shown_before_sensitive_questions") is True and
bool(c.get("purpose")) and
bool(c.get("retention_summary")) and
c.get("voluntary") is True
)
notes = "Consent appears before sensitive items and includes purpose and retention." if ok else "Consent missing, late, or incomplete."
return {"name": "consent", "status": "pass" if ok else "fail", "notes": notes}

def check_data_minimization(obj):
summary = obj.get("consent", {}).get("data_collected_summary", "").lower()
ok = "name" not in summary or "no name" in summary
notes = "No name collected; items limited to stated purpose." if ok else "Potentially excessive identifiers in data collection summary."
return {"name": "data_minimization", "status": "pass" if ok else "note", "notes": notes}

def check_purpose_and_retention(obj):
retention = obj.get("context", {}).get("data_storage", {}).get("retention_days", None)
ok = isinstance(retention, int) and retention > 0
notes = "Retention is concrete." if ok else "Retention window missing or not concrete."
return {"name": "purpose_and_retention", "status": "pass" if ok else "fail", "notes": notes}

def check_medical_disclaimer(obj):
claims = obj.get("output_policy", {}).get("diagnosis_claims", None)
ok = claims is False
notes = "No diagnosis claims." if ok else "Tool appears to claim diagnosis."
return {"name": "medical_disclaimer", "status": "pass" if ok else "fail", "notes": notes}

def check_uncertainty_and_limits(obj):
ok = obj.get("output_policy", {}).get("uncertainty_language") is True
notes = "Uncertainty language enabled." if ok else "Add uncertainty and limits language."
return {"name": "uncertainty_and_limits", "status": "pass" if ok else "note", "notes": notes}

def check_harm_and_escalation(obj):
ok = obj.get("output_policy", {}).get("crisis_resources_available") is True
notes = "Crisis resources available if needed." if ok else "Add crisis and escalation resources."
return {"name": "harm_and_escalation", "status": "pass" if ok else "note", "notes": notes}

def check_privacy_and_security(obj):
storage = obj.get("context", {}).get("data_storage", {})
ok = storage.get("de_identified") is True and bool(storage.get("access_roles"))
notes = "De-identified storage and role-based access declared." if ok else "Define de-identification and access roles."
return {"name": "privacy_and_security", "status": "pass" if ok else "note", "notes": notes}

def check_auditability(obj):
has_session = bool(obj.get("session_id"))
ok = has_session
notes = "Session id present; define event logging schema." if ok else "Missing session id and audit trail fields."
return {"name": "auditability", "status": "note" if ok else "fail", "notes": notes}

def run(obj):
checks = [
check_consent(obj),
check_data_minimization(obj),
check_purpose_and_retention(obj),
check_medical_disclaimer(obj),
check_uncertainty_and_limits(obj),
check_harm_and_escalation(obj),
check_privacy_and_security(obj),
check_auditability(obj)
]
statuses = [c["status"] for c in checks]
if "fail" in statuses:
overall = "fail"
elif "note" in statuses:
overall = "pass_with_notes"
else:
overall = "pass"
return {"session_id": obj.get("session_id", "unknown"), "overall_status": overall, "checks": checks}

if **name** == "**main**":
if len(sys.argv) < 2:
print("Usage: python run_preflight.py sample-input.json")
sys.exit(1)
path = sys.argv[1]
with open(path, "r", encoding="utf-8") as f:
obj = json.load(f)
report = run(obj)
print(json.dumps(report, indent=2))
