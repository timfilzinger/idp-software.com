# Unstructured

Unstructured is an ETL platform provider for transforming unstructured data into LLM-ready formats through open-source libraries and enterprise APIs supporting 25+ file types with 50+ source and destination connectors.

## Overview

Unstructured provides an automated ETL solution for [document processing](../../capabilities/document-understanding/index.md) that extracts and transforms data from PDFs, images, HTML, Word documents, emails, scanned documents, and handwritten notes. The platform offers three transformation tiers: Basic for text-only documents, Advanced for PDFs and complex files, and Platinum with VLM API integration for scanned and handwritten content. Unstructured includes a no-code drag-and-drop Workflow Builder alongside API access for engineers. Founded in 2022 by Brian Raymond, Matt Robinson, and Crag Wolfe after working together at Primer AI, the company raised $65M from Bain Capital Ventures, Menlo Ventures, Madrona Venture Group, M12, and MongoDB Ventures.

## Key Features

- **25+ File Type Support**: Processes PDFs, images, HTML, Word, emails, scanned documents, handwritten notes
- **Three Transformation Tiers**: Basic (text-only), Advanced (complex PDFs/images), Platinum (VLM API for scanned/handwritten)
- **50+ Connectors**: Source and destination connectors with automatic new data detection
- **Workflow Builder**: No-code drag-and-drop ETL orchestration for chunking, embeddings, and vector store mapping
- **Partitioning**: Extracts structured content from raw unstructured documents
- **Cleaning and Chunking**: Data preparation and [segmentation](../../capabilities/segmentation/index.md) for LLM consumption
- **API and UI**: Both user interface for teams and API for engineering control
- **Auto-Scaling**: Horizontal scaling with 300x concurrency per organization
- **Weekly Model Updates**: Regular addition of image-to-text, text-to-text, text-to-embedding models

## Use Cases

### GenAI Data Preparation

Organizations preparing data for large language models use Unstructured to transform documents from multiple sources into LLM-ready formats. The platform automatically detects new files from 50+ connectors, applies appropriate transformation tiers based on document complexity, and delivers structured outputs to vector databases for RAG workflows.

### Enterprise Document ETL

Enterprises deploy Unstructured for continuous [extraction](../../capabilities/extraction/index.md) from diverse document repositories. The Workflow Builder orchestrates multi-step transformations including partitioning, cleaning, chunking, and embedding generation without code, with RBAC controls and in-VPC deployment for sensitive data.

### Scanned Document Processing

Organizations with scanned and handwritten documents use the Platinum tier with VLM API integration. The platform processes challenging document types including low-quality scans and handwritten notes, applies appropriate cleaning and chunking, and delivers structured data to downstream AI systems.

## Technical Specifications

| Feature | Specification |
|---------|---------------|
| Platform Types | Open-source library, Enterprise UI, Enterprise API |
| File Types | 25+ including PDFs, images, HTML, Word, emails, scanned/handwritten |
| Transformation Tiers | Basic (text-only), Advanced (complex), Platinum (VLM API) |
| Connectors | 50+ source and destination |
| Processing | Partitioning, cleaning, extraction, chunking, embeddings |
| Workflow | Drag-and-drop no-code builder |
| Concurrency | 300x per organization |
| Scaling | Horizontal auto-scaling |
| Deployment | Cloud, in-VPC |
| Compliance | SOC 2 Type 2, HIPAA, GDPR |
| Access Control | RBAC, granular admin controls |
| Model Updates | Weekly additions (image-to-text, text-to-text, text-to-embedding) |

## Resources

- [Website](https://unstructured.io)
- [Platform Overview](https://unstructured.io/platform)
- [Documentation](https://docs.unstructured.io/open-source/introduction/overview)
- [GitHub: Open-Source Library](https://github.com/Unstructured-IO/unstructured)
- [Serverless API](https://unstructured.io/api-key-hosted)
- [LinkedIn](https://www.linkedin.com/company/unstructuredio)

## Company Information

Headquarters: Rocklin, California, United States

Founded: 2022

Founders: Brian Raymond (CEO), Matt Robinson, Crag Wolfe

Employees: ~40

Funding: $65M ($40M Series B March 2024, from Bain Capital Ventures, Menlo Ventures, Madrona Venture Group, M12 - Microsoft's Venture Fund, Mango Capital, MongoDB Ventures, Shield Capital)

Previous Experience: Founders worked together at Primer AI and CIA 