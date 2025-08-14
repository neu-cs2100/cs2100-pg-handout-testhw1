#!/bin/bash

# Set variables
COVERAGE_DIR="coverage_reports"

# Run tests with coverage
coverage run --omit=".venv/*" test_runner.py

# Generate HTML report
coverage html -d "$COVERAGE_DIR"

# Show report location
echo "HTML coverage report generated in: $COVERAGE_DIR/index.html"