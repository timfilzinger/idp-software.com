# Chunkr

Chunkr is an open-source document processing API by Lumina AI that transforms complex documents into RAG-ready data through layout analysis and semantic chunking.

## Overview

Chunkr is developed by Lumina AI, a San Francisco-based company founded in 2023 by Mehul Chadda (CEO), Ishaan Kapoor, and Akhilesh Sharma. The company participated in Y Combinator's Winter 2024 batch. Chunkr is specifically designed for Retrieval-Augmented Generation applications, knowledge bases, and workflow automation.

The platform uses transformer-based [segmentation](../../capabilities/segmentation/index.md) models and [OCR](../../capabilities/ocr/index.md) to extract structured text with spatial layout and positional metadata. It breaks documents into bounded segments including titles, tables, formulas, and captions, supporting over 11 segment types. The system processes approximately 4 pages per second on an RTX 4090 GPU.

Chunkr offers both an open-source version using community models and a cloud API with proprietary in-house models for higher accuracy and enterprise reliability. The platform maintains SOC2 and HIPAA compliance with customizable data retention policies.

## Key Features

- **Document Layout Analysis**: Identifies and segments document structure into 11+ element types
- **Semantic Chunking**: Splits documents into context-preserving segments for RAG applications
- **Advanced OCR**: Extracts text with bounding boxes and spatial positioning
- **Vision Language Models**: Processes complex elements including tables, formulas, and charts
- **Table Extraction**: Identifies and extracts tabular data while preserving structure
- **Handwriting Recognition**: Reads handwritten text and form entries
- **Reading Order Detection**: Maintains logical flow of multi-column layouts
- **High-Resolution Cropping**: Optional image cropping for detailed element processing
- **Custom Prompts**: Configurable prompts for chart and image descriptions
- **Self-Hosting**: Docker-based deployment for on-premises use

## Use Cases

### RAG System Development

AI developers building Retrieval-Augmented Generation systems use Chunkr to prepare document collections for semantic search. The platform creates intelligent chunks through [document-understanding](../../capabilities/document-understanding/index.md) that preserve document structure and context, improving retrieval accuracy. It processes research papers, technical documentation, and knowledge bases into vector database-ready formats. The semantic chunking maintains relationships between sections while creating searchable segments.

### Scientific Literature Processing

Research institutions extract structured data from academic papers and technical documents. Chunkr handles complex layouts including multi-column formats, mathematical formulas, and scientific diagrams. It identifies section boundaries, extracts tables and figures with captions, and maintains citation context. The platform processes documents from healthcare, finance, research, and government sectors.

### Healthcare Document Digitization

Healthcare organizations convert clinical forms, medical records, and research documentation into structured data. The system reads both printed and handwritten text while maintaining HIPAA compliance. It extracts patient information, treatment data, and clinical observations from complex medical documents. The platform's vision models accurately process tables, checkboxes, and mixed-format medical forms.

## Technical Specifications

| Feature | Specification |
|---------|---------------|
| Core Technology | Transformer models, OCR, Vision-Language Models |
| Supported Formats | PDF, DOCX, PPTX, XLSX, PNG, JPEG |
| Output Formats | HTML, Markdown, JSON |
| Processing Speed | ~4 pages/second (RTX 4090) |
| Language Support | ~100 languages |
| Segment Types | 11+ including titles, tables, formulas, captions |
| Implementation | Rust (43.6%), TypeScript (34.8%) |
| Deployment | Docker Compose, self-hosted, cloud API |
| LLM Integration | OpenAI, Google AI Studio, OpenRouter, self-hosted models |
| Compliance | SOC2, HIPAA |
| License | AGPL-3.0 (open-source version) |
| Free Tier | 200 pages |

## Getting Started

1. **Choose Deployment**: Select cloud API or self-hosted Docker deployment
2. **Sign Up**: Create account at chunkr.ai and receive 200 free pages
3. **Configure Models**: Set up LLM integration via models.yaml or environment variables
4. **Process Documents**: Upload PDFs, images, or Office documents
5. **Receive Output**: Get structured data in HTML, Markdown, or JSON format
6. **Integrate with RAG**: Connect output to vector databases for semantic search

## Resources

- [Website](https://www.chunkr.ai)
- [Documentation](https://docs.chunkr.ai/introduction)
- [GitHub](https://github.com/lumina-ai-inc/chunkr)
- [Y Combinator](https://www.ycombinator.com/companies/chunkr)

## Company Information

Headquarters: San Francisco, CA, USA

Founded: 2023

Founders: Mehul Chadda (CEO), Ishaan Kapoor, Akhilesh Sharma

Accelerator: Y Combinator Winter 2024
