
# DocDigitizer

DocDigitizer is an intelligent document processing platform offering API-based extraction with near 100% accuracy backed by SLA, combining machine learning with human-in-the-loop validation.

![DocDigitizer](./assets/docdigitizer.png)

## Overview

DocDigitizer provides cloud-based IDP with asynchronous API processing for automated data extraction from documents. The platform handles structured, semi-structured, and unstructured documents without requiring templates or configuration, extracting data from any layout. DocDigitizer supports all Latin alphabet languages and integrates with RPA platforms including UiPath, Automation Anywhere, Blue Prism, and Zapier. The service combines machine learning extraction with optional human validation to guarantee near 100% accuracy with SLA-backed performance.

## Key Features

- **Handwriting Recognition**: Extracts cursive handwriting from paper and electronic documents with claimed 99% accuracy, processing both filled forms and free-text content
- **Table Detection**: Identifies and extracts tables using pattern recognition algorithms, including borderless tables and complex layouts
- **Signature Extraction**: Crops signatures from documents while removing background patterns, stains, and noise
- **API-First Architecture**: Asynchronous REST API at api.docdigitizer.com/api/v1/documents/annotate with callback push or query-based result retrieval
- **Human-in-the-Loop**: Optional human validation ensures SLA-backed near 100% accuracy with money-back guarantee
- **Template-Free Processing**: No training or template configuration required, handles documents of any layout

## Use Cases

### Handwritten Form Automation
Healthcare providers and insurance companies deploy DocDigitizer to process handwritten claim forms and patient intake documents. The system extracts cursive handwriting with claimed 99% accuracy, including checkbox selections, written dates, and signature fields. Human validators review uncertain characters to maintain accuracy guarantees before posting data to downstream systems.

### Invoice Processing with SLA Guarantee
Accounts payable departments use DocDigitizer's API for invoice automation with contractual accuracy commitments. The platform extracts vendor information, line items, and totals from invoices in any format, pushing results to callback URLs or making them available via query API. Processing times range from under 1 minute to 16 business hours depending on complexity and validation requirements.

### Multi-Language Document Extraction
International organizations process documents across European languages using DocDigitizer's Latin alphabet support. The platform automatically handles French invoices, German contracts, and Italian receipts without language-specific configuration. Integration with UiPath and other RPA tools enables automated routing to appropriate business systems based on extracted content.

## Technical Specifications

| Feature | Specification |
|---------|---------------|
| Core Technology | Machine learning, OCR, human-in-the-loop validation |
| Accuracy | Near 100% with SLA and money-back guarantee |
| Handwriting Accuracy | Claimed 99% for cursive text |
| API Type | Asynchronous REST API |
| API Endpoint | api.docdigitizer.com/api/v1/documents/annotate |
| Processing Time | Under 1 minute to 16 business hours |
| Language Support | All Latin alphabet languages |
| Deployment | Cloud-based |
| Integration | UiPath, Automation Anywhere, Blue Prism, Zapier, custom API |
| Supported Formats | PDF, scanned documents, images |
| Configuration | Template-free, no training required |
| Result Delivery | Callback push or API query |
| Community Edition | Available for free with each license |

## Getting Started

1. **Sign Up**: Register for account and API access at [docdigitizer.com](https://www.docdigitizer.com/)
2. **API Credentials**: Obtain API key from dashboard for authentication
3. **Integration**: Implement asynchronous API calls to extraction endpoint
4. **Callback Configuration**: Set up callback URL for result delivery or use query-based retrieval
5. **Testing**: Process sample documents to validate accuracy and processing times
6. **Production**: Deploy with SLA guarantee and optional human validation

## Resources

- [Website](https://www.docdigitizer.com/)
- [API Documentation](https://developers.docdigitizer.com/docs)
