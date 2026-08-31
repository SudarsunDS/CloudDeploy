# CloudDeploy Architecture

## Architecture Overview

```text
                    ┌─────────────────────┐
                    │   Developer / User  │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   Flask Application │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Docker Container   │
                    └──────────┬──────────┘
                               │
                               ▼
              ┌────────────────────────────────┐
              │ IBM Cloud Container Registry   │
              └───────────────┬────────────────┘
                              │
                              ▼
              ┌────────────────────────────────┐
              │       IBM Code Engine          │
              │                                │
              │  Serverless Container Runtime  │
              │  Auto Scaling                  │
              │  Managed Infrastructure        │
              └───────────────┬────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   Public Endpoint   │
                    └─────────────────────┘
