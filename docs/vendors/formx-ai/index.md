# FormX.ai

FormX.ai is a Hong Kong-based document extraction API provider specializing in automated data capture from identity documents, receipts, and forms using OCR and machine learning.

![FormX.ai](assets\formx-ai.png)


## Overview

FormX.ai delivers cloud-based document extraction APIs that integrate into business systems to import structured JSON data from scanned documents and images. The platform uses OCR, NLP, and machine learning to automatically extract information from diverse document types including Hong Kong, Macau, Singapore, Taiwan ID cards, passports, work permits, driver's licenses, invoices, and receipts. FormX.ai maintains ISO 27001 and SOC 2 Type II compliance certifications. The company offers pre-trained AI models for common documents while supporting custom extraction needs. Their Extraction API v2 introduced key-value objects for streamlined data access and native multi-page PDF support.

## Key Features

- **Identity Document Extraction**: Automated [data extraction](../../capabilities/extraction/index.md) from ID cards, passports, driver's licenses, and work permits for Hong Kong, Macau, Singapore, and Taiwan
- **Receipt and Invoice Processing**: Pre-trained models for receipts and invoices with field extraction returned in JSON format
- **API v2 Architecture**: Key-value object structure with seamless multi-page PDF handling by default
- **Document Detection**: Automatic identification of document types with bounding box coordinates from uploaded images
- **Custom Model Training**: Ability to train models for organization-specific document types beyond pre-built templates
- **High-Resolution Support**: Recommended minimum 1000x750 pixels or 100 DPI for optimal accuracy

## Use Cases

### Identity Verification Onboarding

Financial services firms and sharing economy platforms automate customer identity verification by integrating FormX.ai's ID extraction API into mobile apps and web portals. Users photograph government-issued IDs, the API extracts names, ID numbers, addresses, and expiration dates, and returns structured JSON for validation against customer-provided information. This accelerates KYC processes for banking, insurance, and rental applications across Hong Kong and Southeast Asian markets.

### Expense Management Automation

Corporate finance teams process employee expense receipts by submitting images through FormX.ai's receipt API. The system extracts merchant names, transaction dates, amounts, and line items, returning JSON data that populates expense management software fields. Automated extraction eliminates manual receipt transcription for accounting departments reviewing travel and business expenses.

### Cross-Border Invoice Processing

Companies operating across Hong Kong, Singapore, and Taiwan markets process vendor invoices in multiple languages and formats. FormX.ai's invoice extraction captures invoice numbers, dates, vendor details, line items, and totals from varied layouts. Extracted data feeds into ERP and accounts payable systems, supporting multi-currency and multi-language invoice workflows for regional operations.

## Technical Specifications

| Feature | Specification |
|---------|---------------|
| Core Technology | OCR, NLP, machine learning |
| API Version | Extraction API v2 with key-value objects |
| Supported Formats | JPEG, PNG, PDF (multi-page supported) |
| Image Requirements | Minimum 1000x750 pixels or 100 DPI recommended |
| Output Format | Structured JSON |
| Document Types | ID cards, passports, licenses, receipts, invoices |
| Geographic Coverage | Hong Kong, Macau, Singapore, Taiwan identity documents |
| Deployment | Cloud-based API |
| Compliance | ISO 27001, SOC 2 Type II |
| Pre-Trained Models | ID documents, receipts, invoices |

## Resources

- [Website](https://www.formx.ai)
- [API Documentation](https://help.formx.ai/reference/document-extraction)
- [Product Updates](https://www.formx.ai/whats-new/2023-08-01)

## Company Information

Headquarters: Hong Kong

Compliance Certifications: ISO 27001, SOC 2 Type II

Target Markets: Hong Kong, Macau, Singapore, Taiwan

Deployment: Cloud API integration
