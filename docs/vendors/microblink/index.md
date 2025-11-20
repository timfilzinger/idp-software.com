# Microblink

Microblink is a Brooklyn-based identity verification and document scanning provider offering AI-powered OCR solutions for identity documents and payment cards across mobile and web platforms.

![Microblink](./assets/microblink.png)

## Overview

Microblink, founded in 2013 and headquartered in Brooklyn, New York with offices in Croatia, develops proprietary AI solutions for identity document scanning, verification, and fraud prevention. The platform processes over 65 million verifications monthly, serving financial services, payments, hospitality, healthcare, crypto, and telecommunications sectors.

The company's flagship products, BlinkID and BlinkCard, use custom-built [OCR technology](../../capabilities/ocr/index.md) optimized for identity documents and payment cards. BlinkID supports 2,500+ document types from 140 countries, while BlinkCard reduces card-not-present fraud through accurate credit card data capture. Microblink offers both cloud-based and on-device processing with SDKs 6x smaller than alternative solutions.

## Key Features

- **BlinkID**: [Identity document scanning](../../capabilities/extraction/index.md) supporting passports, driver's licenses, ID cards from 140 countries
- **BlinkCard**: Payment card OCR with PCI DSS compliant data capture
- **Biometric Verification**: Face matching and liveness detection
- **Deepfake Detection**: AI-powered fraud prevention for synthetic media
- **On-Device Processing**: Client-side machine learning with 20+ models for data privacy
- **Document Verification**: Authenticity checks including security feature analysis
- **AML Watchlist Screening**: Sanctions and PEP database checks
- **Multi-Platform SDKs**: iOS, Android, Web, Cordova, React Native, Flutter, Xamarin
- **Sub-3-Second Verification**: Complete capture-to-verification process in under 3 seconds
- **No-Code Hosted UIs**: Pre-built verification interfaces requiring zero development

## Use Cases

### Digital Account Opening

Financial institutions enable customers to open accounts remotely by capturing identity documents through mobile apps. Users photograph their driver's license or passport, and BlinkID extracts name, date of birth, address, and document numbers while verifying document authenticity through security feature analysis. Biometric face matching confirms the person presenting the ID matches the document photo, with liveness detection preventing spoofing attacks. The entire verification completes in under 3 seconds, enabling immediate account provisioning while maintaining regulatory compliance.

### Payment Card Registration

E-commerce platforms and digital wallets streamline card-on-file registration through BlinkCard scanning. Customers photograph their credit or debit card instead of manually entering 16-digit numbers, expiration dates, and CVV codes. The OCR engine extracts card details with high accuracy, reducing abandoned transactions caused by input errors and improving checkout conversion rates.

### Hospitality Check-In

Hotels and rental car agencies accelerate guest check-in by scanning government-issued IDs at the front desk or through mobile pre-arrival flows. Staff capture driver's licenses or passports, automatically populating guest profiles with verified identity information. The system validates document authenticity and performs AML screening, ensuring compliance with travel industry regulations while reducing manual data entry.

## Technical Specifications

| Feature | Specification |
|---------|---------------|
| Deployment Options | Cloud API, on-device SDKs, hybrid |
| Supported Documents | 2,500+ ID types from 140 countries |
| Processing Speed | <3 seconds capture to verification |
| Capture Success Rate | 40% higher than alternatives (claimed) |
| SDK Size | 6x smaller than competitor SDKs |
| ML Models | 20+ client-side models |
| Supported Platforms | iOS, Android, Web, React Native, Flutter, Cordova, Xamarin |
| Document Formats | Passports, driver's licenses, ID cards, visas, payment cards |
| Security | PCI DSS compliant, on-device processing option |
| Compliance | GDPR, CCPA compliant |
| API Response Time | Real-time processing |
| Monthly Verifications | 65 million+ globally |

## Getting Started

1. **Product Selection**: Choose BlinkID, BlinkCard, or comprehensive verification suite
2. **Integration Method**: Select API, SDK, or no-code hosted UI
3. **SDK Implementation**: Integrate platform-specific SDK or API endpoints
4. **Configuration**: Set verification requirements and UI customization
5. **Testing**: Validate with test documents across supported ID types

## Resources

- [Website](https://microblink.com/)
- [BlinkID Product](https://microblink.com/products/blinkid)
- [BlinkCard Product](https://microblink.com/products/blinkcard)
- [Developer Documentation](https://microblink.com/developers/)
- [Supported Documents List](https://microblink.com/full-list-of-supported-identity-documents/)

## Company Information

Headquarters: Brooklyn, New York, United States

Founded: 2013

Offices: New York (USA), Croatia

Monthly Verifications: 65 million+

Supported Countries: 140

Document Types: 2,500+

Email: support@microblink.com

Phone: +1-347-817-7654

Industries: Financial services, payments, hospitality, crypto, healthcare, telecommunications, iGaming
