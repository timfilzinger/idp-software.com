# Amazon Textract

Amazon Textract is a machine learning service from AWS that automatically extracts text, handwriting, forms, and tables from scanned documents and images.

![Amazon Textract](./assets/amazon-textract.png)

## Overview

Amazon Textract, launched by Amazon Web Services, provides cloud-based document analysis using machine learning to extract printed text, handwriting, and structured data from documents. Unlike basic OCR, Textract understands document context, preserves form structures, and identifies relationships between extracted data, enabling integration into applications and workflows without manual template configuration.

The service processes identity documents, invoices, receipts, and general documents through specialized APIs. Textract integrates with AWS services including Amazon Comprehend for natural language analysis, AWS Lambda for serverless processing, Amazon S3 for document storage, and Amazon DynamoDB for structured data storage. The pay-as-you-go pricing model charges per page processed based on extraction type.

## Key Features

- **[Text and Handwriting Extraction](../../capabilities/ocr/index.md)**: Recognition of both printed text and handwritten content
- **[Forms and Tables Recognition](../../capabilities/extraction/index.md)**: Data extraction preserving document structure and relationships
- **Query-Based Extraction**: Natural language queries to extract specific information without knowing document structure
- **Identity Document Analysis**: Specialized processing for passports, driver's licenses, and ID cards
- **Expense Analysis**: Automated extraction from invoices and receipts with line-item details
- **AWS Integration**: Native connections with S3, Lambda, Comprehend, DynamoDB, CloudWatch
- **API Access**: RESTful APIs for synchronous and asynchronous document processing
- **Multi-Page Document Support**: Batch processing for multi-page PDFs and image collections
- **Confidence Scores**: Accuracy ratings for extracted data elements

## Use Cases

### Invoice Processing

Organizations automate accounts payable by uploading invoices to S3 buckets that trigger Textract via Lambda functions. The service extracts vendor details, invoice numbers, dates, line items, and amounts, returning structured JSON data that Lambda functions validate and route to ERP systems. CloudWatch monitors processing workflows while DynamoDB stores extracted invoice data for reconciliation.

### Identity Verification

Applications verify customer identities during onboarding by submitting ID document images to Textract's AnalyzeID API. The service extracts names, addresses, birth dates, and document numbers from passports and driver's licenses, returning structured data that applications compare against user-provided information for verification. Integration with Amazon Comprehend enables fraud detection through text analysis.

### Document Archiving

Organizations make scanned document repositories searchable by processing files through Textract to extract full text content. Extracted text indexes in Amazon CloudSearch or Amazon Kendra, enabling full-text searches across historical document archives. The searchable text layer overlays original documents, preserving original formatting while enabling text-based retrieval.

## Technical Specifications

| Feature | Specification |
|---------|---------------|
| Deployment | Cloud-based SaaS (AWS) |
| API Types | Synchronous and asynchronous processing |
| Document Formats | PDF, PNG, JPEG, TIFF |
| Max File Size | 10MB (synchronous), 500MB (asynchronous) |
| Languages | English, Spanish, German, Italian, French, Portuguese |
| Handwriting | English only for handwriting recognition |
| Processing Types | DetectDocumentText, AnalyzeDocument, AnalyzeExpense, AnalyzeID |
| Output Format | JSON with confidence scores |
| Integration | S3, Lambda, Comprehend, DynamoDB, CloudWatch, SageMaker |
| Pricing Model | Pay-per-page processed |
| Availability | Multiple AWS regions globally |

## Getting Started

1. **AWS Account**: Set up AWS account with appropriate IAM permissions
2. **Document Storage**: Upload documents to Amazon S3 bucket
3. **API Integration**: Call Textract APIs directly or through Lambda functions
4. **Data Processing**: Process extracted JSON data with custom logic or AWS services
5. **Monitoring**: Set up CloudWatch for logging and performance monitoring

## Resources

- [AWS Textract Homepage](https://aws.amazon.com/textract/)
- [Textract Documentation](https://docs.aws.amazon.com/textract/)
- [Textract FAQs](https://aws.amazon.com/textract/faqs/)
- [Getting Started Guide](https://docs.aws.amazon.com/textract/latest/dg/getting-started.html)
- [Textract Pricing](https://aws.amazon.com/textract/pricing/)

## Company Information

Provider: Amazon Web Services (AWS)

Parent Company: Amazon.com, Inc.

Service Type: Machine learning API service

Deployment: Cloud-based (AWS global infrastructure)

Pricing: Pay-as-you-go per page processed

Availability: Multiple AWS regions worldwide

Integration Ecosystem: AWS services (S3, Lambda, Comprehend, DynamoDB, CloudWatch, SageMaker)

Use Cases: Document digitization, invoice processing, identity verification, compliance, archiving
