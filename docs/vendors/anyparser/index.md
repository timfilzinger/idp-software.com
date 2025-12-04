# AnyParser

AnyParser is an API platform by CambioML that uses vision-language models to parse unstructured documents into structured formats for AI and RAG applications.

## Overview

AnyParser is developed by CambioML, a San Francisco-based company founded in 2023 by Rachel Hu and Kimi as part of Y Combinator's Summer 2023 batch. The platform is specifically designed for AI engineers, data analysts, and developers building Retrieval-Augmented Generation systems, agentic AI workflows, and ETL pipelines.

The platform leverages state-of-the-art vision-language models to accurately parse documents including PDFs, images, presentations, and web pages. It converts unstructured content into machine-readable formats like Markdown, JSON, and HTML through [document-understanding](../../capabilities/document-understanding/index.md) capabilities. AnyParser processes documents in seconds using distributed processing architecture and supports over 100 languages.

CambioML has raised funding from investors including Hub71, Embedding VC, General Catalyst, Samsung NEXT Ventures, and Z Venture Capital. The company reached $1.5M in revenue with a 10-person team in 2024.

## Key Features

- **Vision-Language Models**: Uses VLMs to understand visual and textual context within documents
- **Multi-Format Parsing**: Processes PDFs, images, Word documents, presentations, audio, and video
- **Structured Output**: Exports data in JSON, HTML, and Markdown formats
- **Automatic Table Extraction**: Detects and extracts tables while preserving structure
- **Image Recognition**: Processes and extracts information from embedded images
- **Language Detection**: Automatically identifies and processes 100+ languages
- **Distributed Processing**: 10x faster extraction through parallel processing architecture
- **Python and Node.js SDKs**: Official SDKs with full typing and documentation
- **REST API**: Compatible with any programming language

## Use Cases

### RAG System Development

AI engineers building Retrieval-Augmented Generation systems use AnyParser to prepare document collections for semantic search. The platform converts PDFs and documents into structured formats optimized for vector databases. It preserves document structure and context, enabling more accurate retrieval and generation in LLM applications.

### ETL Pipeline Automation

Data teams integrate AnyParser into [extraction](../../capabilities/extraction/index.md) pipelines to automate data collection from diverse document sources. The API processes large document volumes in parallel, extracting structured data that flows directly into databases and analytics systems. The platform performs [OCR](../../capabilities/ocr/index.md) and handles complex layouts including multi-column documents and mixed-language content.

### Financial Document Analysis

Financial institutions process statements, reports, and regulatory documents with AnyParser's table and text extraction capabilities. The system accurately extracts financial data from complex PDF layouts, handling nested tables and multi-page documents. It maintains precision required for financial applications while processing documents at scale.

## Technical Specifications

| Feature | Specification |
|---------|---------------|
| Core Technology | Vision-Language Models (VLMs), OCR |
| Supported Formats | PDF, DOCX, PPTX, XLSX, images, audio, video, web pages |
| Output Formats | JSON, HTML, Markdown |
| Processing Speed | Most documents in seconds, distributed architecture for scale |
| Language Support | 100+ languages including RTL and Asian scripts |
| Integration | Python SDK, Node.js SDK, REST API |
| Frameworks | LangChain, LlamaIndex, CrewAI, n8n |
| Security | SOC 2 compliant, end-to-end encryption |
| Data Retention | Real-time processing without storage |
| Data Policy | Documents not used for training or shared |
| Pricing | Free for local development, per-character pricing for production |

## Getting Started

1. **Create Account**: Sign up at anyparser.com
2. **Local Development**: Use the platform free for local development
3. **Install SDK**: Choose Python or Node.js SDK, or use REST API
4. **API Integration**: Obtain API credentials and implement parsing logic
5. **Process Documents**: Upload documents and receive structured output
6. **Production Deployment**: Deploy with per-character production pricing

## Resources

- [Website](https://anyparser.com)
- [GitHub](https://github.com/CambioML/any-parser)
- [Product Hunt](https://www.producthunt.com/products/anyparser)

## Company Information

Headquarters: San Francisco, CA, USA

Founded: 2023

Founders: Rachel Hu (CEO), Kimi

Investors: Hub71, Embedding VC, General Catalyst, Samsung NEXT Ventures, Z Venture Capital

Accelerator: Y Combinator Summer 2023
