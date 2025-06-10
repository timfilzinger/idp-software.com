# Intelligent Document Processing

This repository contains comprehensive documentation about Intelligent Document Processing,
including vendor information, technical capabilities, and research papers in the field.

Visit [idp-software.com](https://idp-software.com)

## Overview

The documentation is built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme and is automatically deployed to GitHub Pages.

## Local Development

To work on this documentation locally:

1. Clone this repository:
   ```
   git clone https://github.com/atraining/idp-software.com.git
   cd idp-software
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Start the local development server:
   ```
   mkdocs serve
   ```
   The build takes ca. 20 seconds for the full page. When you want to preview your changes fast after the first build, use [this](https://github.com/mkdocs/mkdocs/issues/3695):
    ```
     mkdocs serve --dirtyreload
    ```

5. Open your browser and go to `http://127.0.0.1:8000/`

## Project Structure

- `docs/`: Contains all the documentation markdown files
  - `capabilities/`: Information about IDP technical capabilities
  - `vendors/`: Profiles of IDP software vendors
  - `research/`: Summaries of research papers in the field
  - `contribution/`: Guidelines for contributing to the documentation
  - `events/`: Upcoming and reports about events related to IDP-Software or document processing research
- `mkdocs.yml`: MkDocs configuration file
- `.github/workflows/`: Contains the GitHub Actions workflow for deployment

## Contributing

We welcome contributions to improve and expand this documentation! Please follow the guidelines in the [Contribution Guide](docs/contribution/index.md).

## License

This documentation is licensed under [LICENSE].

Documentation site for IDP (Intelligent Document Processing) Software, built with MkDocs and the Material theme.

### Navigation Structure

This project uses the `mkdocs-awesome-pages-plugin` to automatically include all folders with `index.md` files in the navigation. To add new content:

1. Create a folder in the appropriate section (e.g., `docs/vendors/your-vendor/`)
2. Add an `index.md` file in that folder
3. Optionally add a `.pages` file to customize the navigation order
4. Add a `assets` folder if you want to add images or other files.

## Contributing

Visit the [Contribution Guide](https://idp-software.com/contribution/)

## Thanks to

- [mhausenblas](https://github.com/marketplace/actions/deploy-mkdocs)
- [Tom Christie and all contributors of MkDocs](https://github.com/mkdocs/mkdocs/blob/master/docs/index.md)
- [Material for MkDocs](https://github.com/squidfunk/mkdocs-material)
- ... and many more developers for the great work that made this homepage possible

## List of all Intelligent Document Processing Software Vendors already included

- [a2ia](https://idp-software.com/vendors/a2ia/)
- [abbyy](https://idp-software.com/vendors/abbyy/)
- [adoc-solutions](https://idp-software.com/vendors/adoc-solutions/)
- [aiim](https://idp-software.com/vendors/aiim/)
- [altilia](https://idp-software.com/vendors/altilia/)
- [amagno](https://idp-software.com/vendors/amagno/)
- [antworks](https://idp-software.com/vendors/antworks/)
- [apache-pdfbox](https://idp-software.com/vendors/apache-pdfbox/)
- [appian](https://idp-software.com/vendors/appian/)
- [aptean](https://idp-software.com/vendors/aptean/)
- [archiv-it](https://idp-software.com/vendors/archiv-it/)
- [arco](https://idp-software.com/vendors/arco/)
- [astera](https://idp-software.com/vendors/astera/)
- [attri-ai](https://idp-software.com/vendors/attri-ai/)
- [aurexus](https://idp-software.com/vendors/aurexus/)
- [automation-hero](https://idp-software.com/vendors/automation-hero/)
- [axis-ai](https://idp-software.com/vendors/axis-ai/)
- [base64-ai](https://idp-software.com/vendors/base64-ai/)
- [blue-prism](https://idp-software.com/vendors/blue-prism/)
- [box](https://idp-software.com/vendors/box/)
- [buildsimple](https://idp-software.com/vendors/buildsimple/)
- [canon](https://idp-software.com/vendors/canon/)
- [caylent](https://idp-software.com/vendors/caylent/)
- [chartpixel](https://idp-software.com/vendors/chartpixel/)
- [checkbox](https://idp-software.com/vendors/checkbox/)
- [cloudmersive](https://idp-software.com/vendors/cloudmersive/)
- [coforge](https://idp-software.com/vendors/coforge/)
- [conduent](https://idp-software.com/vendors/conduent/)
- [copysud](https://idp-software.com/vendors/copysud/)
- [coreintegrator](https://idp-software.com/vendors/coreintegrator/)
- [databank](https://idp-software.com/vendors/databank/)
- [datakeen](https://idp-software.com/vendors/datakeen/)
- [dataleon](https://idp-software.com/vendors/dataleon/)
- [datasnipper](https://idp-software.com/vendors/datasnipper/)
- [deep-neuron-lab](https://idp-software.com/vendors/deep-neuron-lab/)
- [docaposte](https://idp-software.com/vendors/docaposte/)
- [docdigitizer](https://idp-software.com/vendors/docdigitizer/)
- [docsend](https://idp-software.com/vendors/docsend/)
- [docsumo](https://idp-software.com/vendors/docsumo/)
- [docteller](https://idp-software.com/vendors/docteller/)
- [docucharm](https://idp-software.com/vendors/docucharm/)
- [docuware](https://idp-software.com/vendors/docuware/)
- [drooms](https://idp-software.com/vendors/drooms/)
- [edissyum](https://idp-software.com/vendors/edissyum/)
- [eigen-technologies](https://idp-software.com/vendors/eigen-technologies/)
- [elo-digital](https://idp-software.com/vendors/elo-digital/)
- [ephesoft](https://idp-software.com/vendors/ephesoft/)
- [epson](https://idp-software.com/vendors/epson/)
- [evana](https://idp-software.com/vendors/evana/)
- [everial](https://idp-software.com/vendors/everial/)
- [expertai](https://idp-software.com/vendors/expertai/)
- [extrascan](https://idp-software.com/vendors/extrascan/)
- [filehold](https://idp-software.com/vendors/filehold/)
- [fino-group](https://idp-software.com/vendors/fino-group/)
- [fluxym](https://idp-software.com/vendors/fluxym/)
- [formhero](https://idp-software.com/vendors/formhero/)
- [fp-digital](https://idp-software.com/vendors/fp-digital/)
- [groupe-t2i](https://idp-software.com/vendors/groupe-t2i/)
- [handl](https://idp-software.com/vendors/handl/)
- [helic-analyzer](https://idp-software.com/vendors/helic-analyzer/)
- [hypatos](https://idp-software.com/vendors/hypatos/)
- [hyperscience](https://idp-software.com/vendors/hyperscience/)
- [i-numerics](https://idp-software.com/vendors/i-numerics/)
- [imanage](https://idp-software.com/vendors/imanage/)
- [indexware](https://idp-software.com/vendors/indexware/)
- [infrrd](https://idp-software.com/vendors/infrrd/)
- [iris](https://idp-software.com/vendors/iris/)
- [itesoft](https://idp-software.com/vendors/itesoft/)
- [julsolutions](https://idp-software.com/vendors/julsolutions/)
- [kapto](https://idp-software.com/vendors/kapto/)
- [klearstack](https://idp-software.com/vendors/klearstack/)
- [klippa](https://idp-software.com/vendors/klippa/)
- [kodak-alaris](https://idp-software.com/vendors/kodak-alaris/)
- [konfuzio](https://idp-software.com/vendors/konfuzio/)
- [kyocera](https://idp-software.com/vendors/kyocera/)
- [laserfiche](https://idp-software.com/vendors/laserfiche/)
- [lector](https://idp-software.com/vendors/lector/)
- [lexmark](https://idp-software.com/vendors/lexmark/)
- [logicaldoc](https://idp-software.com/vendors/logicaldoc/)
- [m-files](https://idp-software.com/vendors/m-files/)
- [microblink](https://idp-software.com/vendors/microblink/)
- [microsoft](https://idp-software.com/vendors/microsoft/)
- [mindee](https://idp-software.com/vendors/mindee/)
- [miteksystems](https://idp-software.com/vendors/miteksystems/)
- [mobiltron](https://idp-software.com/vendors/mobiltron/)
- [moonoia](https://idp-software.com/vendors/moonoia/)
- [mr-money](https://idp-software.com/vendors/mr-money/)
- [nanonets](https://idp-software.com/vendors/nanonets/)
- [natif](https://idp-software.com/vendors/natif/)
- [netdocuments](https://idp-software.com/vendors/netdocuments/)
- [novarchive](https://idp-software.com/vendors/novarchive/)
- [numen](https://idp-software.com/vendors/numen/)
- [nuxeo](https://idp-software.com/vendors/nuxeo/)
- [objective](https://idp-software.com/vendors/objective/)
- [onbase](https://idp-software.com/vendors/onbase/)
- [openbee](https://idp-software.com/vendors/openbee/)
- [opentext](https://idp-software.com/vendors/opentext/)
- [parascript](https://idp-software.com/vendors/parascript/)
- [parashift](https://idp-software.com/vendors/parashift/)
- [perfect-memory](https://idp-software.com/vendors/perfect-memory/)
- [planet-ai](https://idp-software.com/vendors/planet-ai/)
- [pspdfkit](https://idp-software.com/vendors/pspdfkit/)
- [qbotica](https://idp-software.com/vendors/qbotica/)
- [quadient](https://idp-software.com/vendors/quadient/)
- [readsoft](https://idp-software.com/vendors/readsoft/)
- [recital](https://idp-software.com/vendors/recital/)
- [recogniform](https://idp-software.com/vendors/recogniform/)
- [redactor](https://idp-software.com/vendors/redactor/)
- [reducto-ai](https://idp-software.com/vendors/reducto-ai/)
- [reemia](https://idp-software.com/vendors/reemia/)
- [ricoh](https://idp-software.com/vendors/ricoh/)
- [ripcord](https://idp-software.com/vendors/ripcord/)
- [rippling](https://idp-software.com/vendors/rippling/)
- [rossum](https://idp-software.com/vendors/rossum/)
- [salvia-developpement](https://idp-software.com/vendors/salvia-developpement/)
- [scriptscan](https://idp-software.com/vendors/scriptscan/)
- [ser-group](https://idp-software.com/vendors/ser-group/)
- [serimag](https://idp-software.com/vendors/serimag/)
- [silverfast](https://idp-software.com/vendors/silverfast/)
- [skilja](https://idp-software.com/vendors/skilja/)
- [skyged](https://idp-software.com/vendors/skyged/)
- [smartadvocate](https://idp-software.com/vendors/smartadvocate/)
- [softco](https://idp-software.com/vendors/softco/)
- [storiesout](https://idp-software.com/vendors/storiesout/)
- [symtrax](https://idp-software.com/vendors/symtrax/)
- [systhen](https://idp-software.com/vendors/systhen/)
- [tagtog](https://idp-software.com/vendors/tagtog/)
- [taiger](https://idp-software.com/vendors/taiger/)
- [tcg-process](https://idp-software.com/vendors/tcg-process/)
- [telekom-mms](https://idp-software.com/vendors/telekom-mms/)
- [textract](https://idp-software.com/vendors/textract/)
- [tiny-IDP](https://idp-software.com/vendors/tiny-IDP/)
- [tungstenautomation](https://idp-software.com/vendors/tungstenautomation/)
- [u2d-ai](https://idp-software.com/vendors/u2d-ai/)
- [uipath](https://idp-software.com/vendors/uipath/)
- [xelians](https://idp-software.com/vendors/xelians/)
- [xenonstack-akira-ai](https://idp-software.com/vendors/xenonstack-akira-ai/)
- [xerox](https://idp-software.com/vendors/xerox/)
- [xtracta](https://idp-software.com/vendors/xtracta/)
- [zeendoc](https://idp-software.com/vendors/zeendoc/)

## Known but not yet included

- [Acodis](https://www.acodis.io): Helps unlock AI-ready Data from Documents for RAG and Fine-tuning. Stadthausstrasse 14, 8400 Winterthur, Switzerland.
- [Affinda](https://www.affinda.com): Provides artificial intelligence technologies for the automation. Melbourne, Australia.
- [AIDA](https://www.aidacloud.com): Artificial Intelligence for Document Automation. Torino, Italy.
- [AiMunshi](https://aimunshi.ai): An Intelligent Automation Tool for processing and extracting information from documents. Hyderabad, India.
- [AlgoDocs](https://www.algodocs.com): A cutting-edge document processing tool powered by AI. Bayraklı, Turkey.
- [Alphamoon](https://alphamoon.ai): Helps companies automate their document processing and extract valuable data. bud. B, Grabarska 1, 50-079 Warsaw, Poland.
- [Altilia](https://altilia.ai/): Provides a no-code Intelligent Automation platform (AIA) for content-centric processes. Located in Rende, Italy.
- [AmyGB](https://www.amygb.ai/): Develops AI-powered products to solve real-world problems, including document processing. Located in Thane, India.
- [ancora Software](https://ancorasoftware.com): An innovative provider of Business Process Automation solutions. San Diego, United States.
- [AntWorks](https://www.ant.works): A global leader in Intelligent Document Processing (IDP). London, United Kingdom.
- [AOTM](https://aotm.ai): A cognitive intelligent document processing solution built for automation and efficiency. Bengaluru, India.
- [Ascron](https://ascron.com/): Ascron's IDP solution simplifies document management processes and minimizes repetitive tasks. Warsaw, Poland.
- [Automat](https://www.runautomat.com): Simplifies automation for mid-market and enterprise customers. San Francisco, United States.
- [Automation Anywhere](https://www.automationanywhere.com): A leader in AI-powered process automation. San Jose, United States.
- [AutomationEdge](https://automationedge.com/): Offers a hyperautomation platform with RPA, AI, and IDP capabilities for end-to-end automation. Located in Houston, United States.
- [Axis Technical Group](https://axistechnical.com): An IT solutions provider that helps clients align technology with business objectives. Anaheim, United States.
- [BIS](https://www.bisok.com/): Creator of Grooper, an intelligent data platform with 35 years of experience. Potentially no real IDP vendor. Located in Edmond, United States.
- [Botminds AI](https://www.botminds.ai): Believes 'Document Understanding is the next frontier in AI', offering an IDP solution. Bellevue, United States.
- [Cambrion](https://www.cambrion.ai): Provides context-aware document processing for business automation. Munich, Germany.
- [Captova Technologies](https://www.captova.com): Mission is to deliver the best-in-class Intelligent Document Processing. Vancouver, Canada.
- [Celaton](https://celaton.com): Applies Intelligent Process Automation (IPA) technology, inSTREAM, to deliver benefits. Keynes, United Kingdom.
- [Cinnamon AI](https://www.youtube.com/watch?v=9SsDXSRzrlk): An AI Document Reader to automate the data extraction from unstructured documents. Tokyo, Japan.
- [ClearDox](https://www.cleardox.com): Allows commodity-intensive businesses to secure a competitive advantage through document automation. Stamford, United States.
- [codemantra](https://codemantra.com): Helps businesses and organizations across industries with document processing. Boston, United States.
- [Cogent Labs](https://www.cogent.co.jp/en/): Develops and provides AI solutions, including SmartRead. Tokyo, Japan.
- [Cognaize](https://www.cognaize.com/): Offers an Intelligent Document Processing solution that automates complex financial workflows. Located in New York, United States.
- [Cogniquest](https://www.cogniquest.ai/): Specializes in developing solutions for extracting information from unstructured data. Located in Bengaluru, India.
- [Concord Technologies](https://concord.net): A provider of secure document exchange and document processing. Seattle, United States.
- [Datamatics](https://www.datamatics.com): Enables enterprises to go Deep in Digital to boost productivity. Edison, United States.
- [DB Intelab](https://www.dbintelab.com): An enterprise solution company offering an Intelligent Document Processing. Petaling Jaya, Malaysia.
- [Deep Cognition](https://deepcognition.ai): Specializes in using advanced AI to automate complex data entry. Dallas, United States.
- [DeepOpinion](https://www.deepopinion.ai): A no-code platform enabling teams to build human-level AI bots for document automation. Innsbruck, Austria.
- [DocAcquire](https://www.docacquire.com/): Helps companies unlock value from unstructured content through their platform. Located in London, United Kingdom.
- [DocBits](https://docbits.com): FELLOWPRO AG's star product, a software solution for document capture. Poing, Germany.
- [Docketry](https://docketry.ai): An intelligent document processing solution built with advanced AI/M. Cranbury, United States.
- [DOConvert](https://doconvert.co): An IDP platform specializing in the supply chain and manufacturing industries. Tel Aviv, Israel.
- [DocScience](https://www.docscience.ai): An AI platform from Nexyom, a company specializing in product development. Folsom, United States.
- [Docufai](https://www.docufai.com): Built on Generative AI, Docufai removes the barriers to finding the information. Hayward, United States.
- [Docugami](https://www.docugami.com): Provides Generative AI for business documents with patented AI designed for accuracy. Kirkland, United States.
- [Docusense](https://docusense.ai): Employs Intelligent Document Processing (IDP) for document workflows. Italy.
- [Docuworx](https://docuworx.com.au): Implements intelligent data capture with advanced optical character recognition. North Adelaide, Australia.
- [DocVu.AI](https://www.docvu.ai): Uses AI and machine learning to transform information on documents. Cranbury, United States.
- [Duco](https://du.co): Duco is an enterprise platform for data automation in financial institutions. London, United Kingdom.
- [EdgeVerve](https://www.edgeverve.com): Powered by native AI and automation capabilities, with security and scalability. Bengaluru, India.
- [Evolution AI](https://www.evolution.ai): A multiple award-winning data extraction solution using the latest advancements in AI. London, United Kingdom.
- [ExB](https://exb.de): The flexible Intelligent Document Processing (IDP) platform. Munich, Germany.
- [EXL](https://www.exlservice.com): A global analytics and digital solutions company. New York, United States.
- [Extract Systems](https://www.extractsystems.com): Makes software that gives organizations quick access to the data. Madison, United States.
- [Extractly](https://extractly.ai): Advanced AI understands and processes organizations' accounting. North Wollongong, Australia.
- [FormX.ai](https://www.formx.ai): Eliminates manual data extraction from documents using AI. Stockport, United Kingdom.
- [Haystac](https://haystac.com): Built with a state-of-the-art AI/Machine Learning (ML)/Deep Learning. Newton, United States.
- [HCLTech](https://www.hcltech.com): A global technology company, home to more than 227,000 people. Noida, India.
- [HubBroker Aps](https://hubbroker.com/): More than just about EDI, iPaaS, API integration. Horsholm, Denmark.
- [HuLoop Automation](https://huloop.ai/): Focuses on Human-in-the-Loop Intelligent Automation to transform work. Auburn, United States.
- [Hyland](https://www.hyland.com/): Puts companies' content to work, making it smarter and more accessible. Westlake, United States.
- [Hypatos](https://www.hypatos.ai): Builds autonomous finance solutions for the enterprise. Berlin, Germany.
- [ibml](https://www.ibml.com): Data drives business decisions, but it's locked away in documents. Birmingham, United States.
- [iCustoms](https://www.icustoms.ai): Customs Declaration Software that leverages artificial intelligence. London, United Kingdom.
- [Impactsure](https://www.impactsure.com): An AI/ML-powered intelligent document processing and analytics web platform. Mumbai, India.
- [Indico Data](https://indicodata.ai): Offers an intelligent intake solution without compromising speed or accuracy. Boston, United States.
- [Infinia ML](https://www.infiniaml.com): Applies machine learning to knowledge work. Note: Website down, potentially due to acquisition. Durham, United States.
- [inserve.ai](https://www.inserve.de): Companies use inserve.ai services for intelligent processing of complex documents. Hannover, Germany.
- [Insiders Technologies](https://insiders-technologies.com/en/): A team of visionaries, innovators, and tech enthusiasts focused on process automation. Kaiserslautern, Germany.
- [Instabase](https://www.instabase.com): Enables organizations to automate mission-critical processes. Menlo Park, United States.
- [ITyX Solutions AG](https://www.ityxsolutions.com): A provider of intelligent process automation. Cologne, Germany.
- [JIFFY.ai](https://jiffy.ai): Offers a no-code AI-powered platform for financial institutions and Fortune companies. Milpitas, United States.
- [Kanverse.ai](https://www.kanverse.ai/): Offers hyperautomation solutions for enterprises. San Jose, United States.
- [KAPTO AI Ltd](https://www.kapto.ai/): Aims to fully automate end-to-end business processes. London, United Kingdom.
- [Klassif.ai](https://www.klassif.ai): Helps order processing teams increase productivity. Leuven, Belgium.
- [KlearStack](https://klearstack.com): Specializes in achieving intelligent data extraction and auditing from documents. Piscataway, United States.
- [Kritical](https://www.kritical.com): Helps construction and legal professionals save time and money during their workflows. Amman, Jordan.
- [Laiye](https://laiye.com/en): The pioneer of the Work Execution System. Beijing, China.
- [Letxbe](https://www.letxbe.ai): A no-code platform from France specializing in intelligent document processing. Paris, France.
- [Mely.ai](https://www.mely.ai): Helps organizations automate their document processing operations. Montreal, Canada.
- [Mindee](https://www.mindee.com): At the forefront of transforming document processing through their AI-powered APIs. Paris, France.
- [MuleSoft](https://www.mulesoft.com): Empowers teams to use AI to automatically extract and organize data from documents. San Francisco, United States.
- [Netfira](https://netfira.com): Focused on a deep understanding of challenges in document management automation. Walldorf, Germany.
- [Nividous](https://nividous.com/): An intelligent automation company focused on enabling organizational agility. Moorestown, United States.
- [Notable Systems](https://notablesystems.com/): Decreases the cost of organizations' manual data entry. Denver, United States.
- [Ocrolus](https://www.ocrolus.com): A document AI platform that enables faster and more accurate financial decisions. New York, United States.
- [OpenBots](https://openbots.ai): Automates documents for IT systems as a full-featured business automation platform. Edison, United States.
- [Paperbox](https://www.paperbox.ai): An AI-driven software company specializing in intelligent document processing. Gent, Belgium.
- [Parble](https://parble.com/): The API-based solution for intelligent document processing. Brussels, Belgium.
- [Parseur](https://parseur.com/): Offers leading AI document processing software for email parsing and data extraction. Singapore, Singapore.
- [Pixydocs](https://pixydocs.com): Building the IDP solution of the next 5-10 years. Lehi, United States.
- [Process Fusion Inc](https://www.processfusion.com): A software company and cloud services provider. Toronto, Canada.
- [ProcessMaker](https://www.processmaker.com): An American multinational corporation specializing in process automation. Durham, United States.
- [qBotica](https://qbotica.com): Leverages AI technology to revolutionize enterprise workplaces. Phoenix, United States.
- [Quantiphi](https://quantiphi.com): An AI-first digital engineering company providing cutting-edge solutions. Marlborough, United States.
- [RaccoonDoc](https://raccoondoc.com): A global provider of intelligent document processing (IDP) solutions. Kyiv, Ukraine.
- [Reshape AI](https://reshape-ai.com): Provides an adaptive communication platform for intelligent document processing. Thatcham, United Kingdom.
- [Retarus](https://www.retarus.com): Focused on digital transformation for processes and supply chains. Munich, Germany.
- [Scale](https://scale.com): Accelerates the development of AI applications through their data platform. San Francisco, United States.
- [Send AI](https://www.send.ai): Empowers companies to work with unstructured data in innovative ways. Rotterdam, Netherlands.
- [Sensible](https://www.sensible.so): A flexible API to transform documents into structured data. San Francisco, United States.
- [Skwiz](https://www.skwiz.ai): Uses a mix of generative AI and its OCR engine for document processing. Sint-Pieters-Woluwe, Belgium.
- [4Semantics](https://4semantics.pl/en/): Provider of semantic analytics. Warsaw, Poland.
- [Smart Touch Technologies](https://www.smartouch.ro): Offers "Apollo," its Intelligent Document Processing platform. Bucharest, Romania.
- [SortSpoke](https://www.sortspoke.com): Helps companies with complex, unstructured, and varied documents. Toronto, Canada.
- [Square 9 Softworks](https://www.square-9.com): An AI-powered intelligent information management platform. New Haven, United States.
- [Staple](https://staple.io): Develops a machine learning tool for reading and extracting structured data. Singapore, Singapore.
- [Straive](https://www.straive.com): Focuses on the data-to-AI value chain but is potentially not an IDP vendor. Singapore, Singapore.
- [super.AI](https://super.ai): Leverages AI for intelligent document processing (IDP) solutions. San Francisco, United States.
- [Unstructured](https://unstructured.io/): Provides organizations with access to all of their data. Rocklin, United States.
- [UST](https://www.ust.com): A global digital transformation provider offering intelligent document processing solutions. Aliso Viejo, United States.
- [WorkFusion](https://www.workfusion.com): A provider of intelligent automation solutions for financial institutions. New York, United States.
- [Workist](https://www.workist.com/en): Provides holistic solutions for document processing. Berlin, Germany.
- [Xen.AI](https://xen.ai/): Focuses on automating document tasks through intelligent document processing. Wilmington, United States.
- [xSuite](https://www.xsuite.com/en/): A leading software manufacturer for intelligent applications. Ahrensburg, Germany.
- [semantha](https://www.semantha.de/): Specialized in AI-based intelligent document understanding. Germany.
- [Daitaku](https://www.dataiku.com/): A global platform for enterprise artificial intelligence. France.
- [Convr](https://convr.com/): Uses AI for accelerating property underwriting. United States.
- [Intellect AI](https://www.intellectai.com/): Offers AI-powered products for insurance and financial services companies. United States.
- [Paradatec](https://www.paradatec.de/): Advanced OCR and document processing solutions. Germany.
- [Cytora](https://www.cytora.com/): Enables digital transformation through document automation. United Kingdom.
- [iCertis](https://www.icertis.com/): Specializes in contract intelligence using document processing. United States.
- [Moresophy](https://www.moresophy.com/en): Focuses on turning unstructured content into actionable insights. Germany.
- [Mea Platform](https://www.meaplatform.com/): Digital transformation provider offering intelligent document processing capabilities. Italy.
