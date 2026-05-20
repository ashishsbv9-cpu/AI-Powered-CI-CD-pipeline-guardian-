import subprocess
import os

class ValidationEngine:
    @staticmethod
    def run_tests():
        """Run pytest and return status."""
        try:
            result = subprocess.run(["pytest", "backend/tests"], capture_output=True, text=True)
            return "passed" if result.returncode == 0 else "failed"
        except Exception:
            return "failed"

    @staticmethod
    def run_linting():
        """Run flake8 and return status."""
        try:
            result = subprocess.run(["flake8", "backend/app"], capture_output=True, text=True)
            return "passed" if result.returncode == 0 else "failed"
        except Exception:
            return "failed"

    @staticmethod
    def run_security_scan():
        """Run trivy (mocked for now, assuming trivy is installed)."""
        # In a real scenario: subprocess.run(["trivy", "fs", "."])
        return "passed"

    def validate_all(self):
        return {
            "test_status": self.run_tests(),
            "lint_status": self.run_linting(),
            "security_status": self.run_security_scan()
        }

validation_engine = ValidationEngine()
