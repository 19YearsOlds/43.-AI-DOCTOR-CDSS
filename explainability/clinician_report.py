def generate(trace, differentials, guidelines):
    report = "CLINICAL DECISION SUPPORT REPORT\n"
    report += "\n".join(f"- {s}" for s in trace.steps)
    report += "\n\nDifferential Diagnoses:\n"
    for d, p in differentials.items():
        report += f"{d}: {p: .2f}\n"
    report += "\nEvidence-Based Considerations:\n"
    for d, g in guidelines.items():
        report += f"{d}: {g}\n"
    return report