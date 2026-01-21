from ingestion.voice_input import transcribe
from ingestion.report_input import load_report
from ingestion.scan_input import extract_scan_features
from reasoning.symptom_extraction import extract_symptoms
from reasoning.differential_diagnosis import generate
from reasoning.evidence_matcher import match
from fusion.multimodal_fusion import fuse
from explainability.reasoning_trace import Trace
from explainability.clinician_report import generate as gen_report
from ethics.clinical_guard import enforce
from config.guardrails import DISCLAIMER

voice = transcribe("patient.wav")
report = load_report("patient_report.txt")
scan = extract_scan_features("scan.png")

symptoms = extract_symptoms(voice + " " + report)
diffs = generate(symptoms)
guides = match(diffs)

trace = Trace()
trace.add(f"Extracted symptoms: {symptoms}")
trace.add("Generated differential diagnosis")
trace.add("Matched evidence-based guidelines")

print(DISCLAIMER)
print(enforce())
print("\n")
print(gen_report(trace, diffs, guides))