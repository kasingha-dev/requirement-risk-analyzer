from io import BytesIO

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


class PDFGenerator:

    @classmethod
    def generate(cls, report):

        buffer = BytesIO()

        doc = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        content = []

        content.append(
            Paragraph(
                "Requirement Analysis Report",
                styles["Title"]
            )
    )

        content.append(Spacer(1, 20))

        summary = report["summary"]

        content.append(
            Paragraph(
                "Executive Summary",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                f"Features: {summary['feature_count']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Actors: {summary['actor_count']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Integrations: {summary['integration_count']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"Missing Requirements: {summary['missing_requirement_count']}",
                styles["Normal"]
            )
        )

        content.append(
            Paragraph(
                f"High Risks: {summary['high_risk_count']}",
                styles["Normal"]
            )
        )

        content.append(Spacer(1, 20))

        # Requirements

        content.append(
            Paragraph(
                "Requirements",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                "Features",
                styles["Heading2"]
            )
        )

        for item in report["requirements"]["features"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(
            Paragraph(
                "Actors",
                styles["Heading2"]
            )
        )

        for item in report["requirements"]["actors"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(
            Paragraph(
                "Integrations",
                styles["Heading2"]
            )
        )

        for item in report["requirements"]["integrations"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(Spacer(1, 20))

        # Missing Requirements

        content.append(
            Paragraph(
                "Missing Requirements",
                styles["Heading1"]
            )
        )

        for item in report["missing_requirements"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(Spacer(1, 20))

        # Risks

        content.append(
            Paragraph(
                "Risks",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                "High Risk",
                styles["Heading2"]
            )
        )

        for item in report["risks"]["high"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(
            Paragraph(
                "Medium Risk",
                styles["Heading2"]
            )
        )

        for item in report["risks"]["medium"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(
            Paragraph(
                "Low Risk",
                styles["Heading2"]
            )
        )

        for item in report["risks"]["low"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(Spacer(1, 20))

        # Questions

        content.append(
            Paragraph(
                "Questions To Ask Client",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                "Critical Questions",
                styles["Heading2"]
            )
        )

        for item in report["questions"]["critical"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(
            Paragraph(
                "Important Questions",
                styles["Heading2"]
            )
        )

        for item in report["questions"]["important"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(Spacer(1, 20))

        # Architecture

        content.append(
            Paragraph(
                "Architecture Concerns",
                styles["Heading1"]
            )
        )

        content.append(
            Paragraph(
                "High Priority",
                styles["Heading2"]
            )
        )

        for item in report["architecture_concerns"]["high_priority"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        content.append(
            Paragraph(
                "Medium Priority",
                styles["Heading2"]
            )
        )

        for item in report["architecture_concerns"]["medium_priority"]:
            content.append(
                Paragraph(
                    f"• {item}",
                    styles["Normal"]
                )
            )

        doc.build(content)

        pdf = buffer.getvalue()

        buffer.close()

        return pdf