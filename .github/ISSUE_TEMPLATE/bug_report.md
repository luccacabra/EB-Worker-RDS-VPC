name: Bug Report
description: File a bug report
title: "[Bug]: "
labels: [bug, backlog]
body:
  - type: markdown
    attributes:
      value: |
        Thanks for taking the time to fill out this bug report!
  - type: textarea
    id: summary
    attributes:
      label: Summary
      description: High level summary of the bug
    validations:
      required: true
  - type: textarea
    id: expected-behavior
    attributes:
      label: Expected Behavior
      description: What were you expecting to happen?
    validations:
      required: true
  - type: textarea
    id: observed-behavior
    attributes:
      label: Observed Behavior
      description: What actually happened?
    validations:
      required: true
  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: Steps to Reproduce
      description: Please provide a detailed set of instructions on how to reproduce the bug
    validations:
      required: true
  - type: textarea
    id: additional-context
    attributes:
      label: Additional Context
      description: Any additional information that might be useful in helping us debug this issue?
