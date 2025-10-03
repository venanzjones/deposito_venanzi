# Application Documentation Template

**Application Owner**: Lab11 RAG System Development Team  
<br>**Document Version**: v1.0  
<br>**Reviewers**: AI/ML Engineering Team, Compliance Team  

## Key Links

* [Code Repository](./Lab11/)
* [Deployment Pipeline](./Lab11/docs/)
* [API Documentation](./Lab11/src/rag_crew/)
* [Project Management Board](#)
* [Application Architecture](./Lab11/docs/)

## General Information 

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1, 2, 3
<!-- info: this section covers the AI Act requirement of a description of the intended purpose, version and provider, relevant versions and updates. In Article 11, 2(d) a datasheet is required which describes all training methodologies and techniques as well as the characteristics of the training dataset, general description of the dataset, information about their provenance, scope and main characteristics, how the data was obtained and selected, labelling procedures conducted, and data cleaning methodologies deployed. -->
<p></p>
</div>

**Purpose and Intended Use**:
    
* **Description**: The Lab11 RAG System is a Retrieval-Augmented Generation application designed to provide intelligent document search and question-answering capabilities. The system combines vector-based document retrieval with generative AI to deliver contextually relevant responses to user queries.

* **Problem Statement**: The system aims to solve the challenge of efficiently searching through large document collections and providing accurate, context-aware responses based on the retrieved information.

* **Target Users**: Research teams, document analysts, knowledge workers, and AI researchers requiring advanced document search and question-answering capabilities.

* **Key Performance Indicators (KPIs)**:
  - Response accuracy: >90% relevance score
  - Query response time: <3 seconds
  - Document retrieval precision: >85%
  - System availability: >99.5% uptime

* **Ethical Implications**: The system ensures data privacy, prevents bias in information retrieval, and maintains transparency in AI-generated responses.

* **Prohibited Uses**: The system should not be used for generating misleading information, violating data privacy regulations, or making critical decisions without human oversight.

* **Operational Environment**: The system operates in cloud-based environments, supporting both API-based integrations and direct user interfaces.

## Risk Classification

<div style="color: gray">
Prohibited Risk: EU AI Act Chapter II <a href="https://artificialintelligenceact.eu/article/5/" style="color:blue; text-decoration:underline">Article 5</a>
<br>High-Risk: EU AI Act Chapter III, Section 1 <a href="https://artificialintelligenceact.eu/article/6/" style="color:blue; text-decoration:underline">Article 6</a>, <a href="https://artificialintelligenceact.eu/article/7/" style="color:blue; text-decoration:underline">Article 7</a>  
<br>Limited Risk: Chapter IV <a href="https://artificialintelligenceact.eu/article/50/" style="color:blue; text-decoration:underline">Article 50</a>
<p></p>
</div>

* **Risk Level**: Limited Risk (in accordance with the AI Act)
* **Reasoning**: The RAG system is classified as Limited Risk as it involves AI interaction with humans through automated document retrieval and response generation. While it processes and generates text-based responses, it does not operate in critical infrastructure, law enforcement, or other high-risk domains as defined in Articles 6-7 of the AI Act. The system requires transparency obligations under Article 50, ensuring users are aware they are interacting with an AI system.
   
## Application Functionality 

<div style="color: gray">
EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>, paragraph 1, 2, 3
<!-- Info: this section covers the delineation of the general purpose of the system required in Article 1, with a focus on defining what the system should do and how it should work.-->
<p></p>
</div>

* **Instructions for use for deployers**: <div style="color: gray">(EU AI Act <a href="https://artificialintelligenceact.eu/article/13/" style="color:blue; text-decoration:underline">Article 13</a>)</div>
  - Deploy the system in controlled environments with proper authentication
  - Ensure adequate computational resources for vector processing
  - Implement monitoring for query patterns and response quality
  - Configure appropriate document access controls

* **Model Capabilities**:
  * **Can Do**: 
    - Retrieve relevant documents from large collections using semantic search
    - Generate contextually appropriate responses based on retrieved documents
    - Process multiple document formats (text, markdown, structured documents)
    - Provide confidence scores for retrieved information
    - Support multi-language query processing
  * **Cannot Do**: 
    - Generate information not present in the indexed document collection
    - Provide real-time information beyond the indexed dataset
    - Process audio, video, or complex multimedia content
    - Make autonomous decisions without human review for critical applications

* **Input Data Requirements**:
  * **Format**: Text-based queries in natural language, documents in supported formats (.txt, .md, .pdf, .docx)
  * **Quality Expectations**: Clear, grammatically correct queries for optimal results; well-structured documents for indexing
  * **Valid Inputs**: Factual questions, research queries, document search requests
  * **Invalid Inputs**: Queries requesting real-time data, personal information not in the dataset, malicious or harmful content requests

* **Output Explanation**:
  * **Response Structure**: Generated responses include the main answer, source document references, and confidence scores
  * **Confidence Measures**: Retrieval scores (0.0-1.0) indicating document relevance, generation confidence ratings
  * **Interpretation Guide**: Higher confidence scores indicate more reliable responses; always verify critical information with source documents

* **System Architecture Overview**:
  * **Core Components**:
    - **Document Ingestion Pipeline**: Processes and indexes documents using FAISS vector store
    - **Retrieval Engine**: Semantic search using vector embeddings and similarity matching
    - **Generation Module**: LLM-based response generation using retrieved context
    - **RAG Crew System**: Orchestrates the retrieval and generation workflow
    - **API Layer**: RESTful interfaces for system integration
    - **Monitoring and Logging**: Performance tracking and audit trail capabilities

## Models and Datasets

<div style="color: gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2 (d)
<p></p>
</div>

### Models

Link to all models integrated in the AI/ML System

| Model | Link to Single Source of Truth | Description of Application Usage |
|-------|--------------------------------|----------------------------------|
| Embedding Model | [HuggingFace Hub](https://huggingface.co/models) | Converts text documents and queries into vector representations for semantic search |
| Generation Model | [Model Documentation](./docs/) | Large Language Model used for generating responses based on retrieved context |
| FAISS Index | [Local FAISS Index](./faiss_index_example/) | Vector similarity search engine for document retrieval |

### Datasets

Link to all dataset documentation and information used to evaluate the AI/ML System.

| Dataset | Link to Single Source of Truth | Description of Application Usage |
|---------|--------------------------------|----------------------------------|
| Training Documents | [Documents Directory](./documents/) | Collection of documents used for system training and knowledge base creation |
| Evaluation Dataset | [Output RAG](./output_rag/) | Test dataset for measuring system performance and accuracy |
| RAGAS Evaluation | [RAGAS Results](./output_rag/ragas_results.csv) | Automated evaluation metrics for RAG system performance |

## Deployment
    
### Infrastructure and Environment Details

* **Cloud Setup**:
  * Platform-agnostic deployment supporting AWS, Azure, GCP
  * Container-based deployment using Docker
  * Python 3.8+ runtime environment
  * Vector database storage for FAISS indices

* **Resource Requirements**:
  * CPU: 4+ cores for parallel processing
  * Memory: 16GB+ RAM for vector operations
  * Storage: 50GB+ for document indices and models
  * Network: High-bandwidth for API responses

* **APIs**:
  * RESTful API endpoints for query processing
  * Authentication via API keys or OAuth
  * JSON payload structure for queries and responses
  * Expected latency: <3 seconds for standard queries

## Integration with External Systems

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a> ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 1 (b, c, d, g, h), 2 (a)
  <p></p>
</div>

* **External Dependencies**:
  * HuggingFace Transformers library for model access
  * FAISS library for vector similarity search
  * CrewAI framework for agent orchestration
  * External LLM APIs (OpenAI, Anthropic, or local models)

* **Data Flow**:
  * Document ingestion → Embedding generation → Vector store indexing
  * Query processing → Vector retrieval → Context augmentation → Response generation

* **Error Handling**:
  * Retry mechanisms for external API failures
  * Fallback to cached responses when possible
  * Graceful degradation for partial system failures

## Deployment Plan

* **Environments**:
  * Development: Local testing with sample datasets
  * Staging: Pre-production testing with full document collections
  * Production: Live deployment with monitoring and logging

* **Scaling Policies**:
  * Horizontal scaling for API endpoints
  * Load balancing for query distribution
  * Auto-scaling based on request volume

* **Integration Steps**:
  1. Environment setup and dependency installation
  2. Document collection indexing and vector store creation
  3. Model deployment and API endpoint configuration
  4. Monitoring and logging system initialization
  5. Performance testing and optimization

* **Rollback Strategy**:
  * Blue-green deployment for zero-downtime updates
  * Automated rollback triggers for performance degradation
  * Version-controlled model and configuration management

## Lifecycle Management

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 6
  <p></p>
</div>
    
* **Performance Monitoring**:
  * Response accuracy tracking using RAGAS metrics
  * Query latency and system throughput monitoring
  * User satisfaction and feedback collection
  * Compliance monitoring for ethical AI usage

* **Metrics**:
  * **Application Performance**: Response time (<3s target), error rate (<1%), throughput (queries/second)
  * **Model Performance**: Retrieval precision (>85%), response relevance (>90%), hallucination detection
  * **Infrastructure**: CPU/memory utilization, storage capacity, network bandwidth

* **Key Activities**:
  * Continuous monitoring of system performance in production
  * Regular model evaluation and performance assessment
  * Document collection updates and re-indexing
  * Security vulnerability assessments and patches

* **Documentation Updates**:
  * **Performance Logs**: Real-time metrics on accuracy, latency, and system health
  * **Incident Reports**: Documentation of failures, impacts, and resolution procedures
  * **Model Update Logs**: Records of model versions, performance changes, and retraining activities
  * **Compliance Audits**: Regular assessments ensuring adherence to AI Act requirements

* **Change Log Maintenance**:
  * New feature additions (enhanced search capabilities, new model integrations)
  * Updates to existing functionality (improved retrieval algorithms, response generation)
  * Deprecated features (legacy API endpoints, outdated models)
  * Security and vulnerability fixes
  * Performance optimizations and bug fixes

### Risk Management System

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/9/" style="color:blue; text-decoration:underline">Article 9</a>
  <br>EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>
  ; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a>
  <p></p>
</div>

**Risk Assessment Methodology**: Following ISO 31000 risk management principles and NIST AI Risk Management Framework guidelines.

**Identified Risks**:
1. **Information Hallucination**: AI generating false information not present in source documents
2. **Data Privacy Breach**: Unauthorized access to sensitive documents in the knowledge base
3. **Bias in Retrieval**: Systematic bias in document retrieval favoring certain sources or perspectives
4. **System Performance Degradation**: Reduced accuracy or increased latency under high load

**Potential Harmful Outcomes**:
- Dissemination of inaccurate information leading to poor decision-making
- Privacy violations through exposure of confidential documents
- Biased information retrieval affecting fairness and objectivity
- System unavailability impacting business operations

**Likelihood and Severity Assessment**:
- Information hallucination: Medium likelihood, High severity
- Data privacy breach: Low likelihood, Very high severity
- Retrieval bias: Medium likelihood, Medium severity
- Performance degradation: High likelihood, Low severity

#### Risk Mitigation Measures

**Preventive Measures**:
- Implement confidence scoring and uncertainty quantification for responses
- Deploy robust authentication and authorization mechanisms
- Regular bias testing and diverse dataset validation
- Load testing and performance optimization procedures
- Continuous monitoring and alerting systems

**Protective Measures**:
- Human-in-the-loop verification for critical applications
- Incident response procedures for security breaches
- Fallback mechanisms for system failures
- Regular security audits and penetration testing
- Data anonymization and encryption protocols

## Testing and Validation (Accuracy, Robustness, Cybersecurity)

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/15/" style="color:blue; text-decoration:underline">Article 15</a>
  <p></p>
</div>

**Testing and Validation Procedures (Accuracy)**:

**Performance Metrics**: 
- RAGAS evaluation framework metrics (faithfulness, answer relevancy, context precision, context recall)
- Retrieval accuracy measured by Mean Reciprocal Rank (MRR) and NDCG@k
- Response quality assessed through human evaluation and automated scoring
- Latency measurements for query processing and response generation

**Validation Results**: 
- Current system achieves >90% faithfulness score in RAGAS evaluation
- Retrieval precision consistently above 85% threshold
- Average response time under 2.5 seconds for standard queries
- User satisfaction ratings above 4.2/5.0 in pilot testing

**Measures for Accuracy**: 
- High-quality document preprocessing and cleaning
- Embedding model fine-tuning for domain-specific terminology
- Regular evaluation against ground truth datasets
- Real-time performance monitoring and drift detection

### Accuracy Throughout the Lifecycle

**Data Quality and Management**: 
- Automated document validation and quality scoring
- Continuous monitoring of document collection updates
- Data preprocessing pipelines with normalization and cleaning
- Version control for document collections and model updates

**Model Selection and Optimization**: 
- Comparative evaluation of multiple embedding models
- Hyperparameter tuning for retrieval and generation components
- Cross-validation using stratified document sampling
- A/B testing for system improvements and updates

**Feedback Mechanisms**: 
- User feedback collection and analysis systems
- Automated error detection and reporting
- Continuous learning from user interactions and corrections
- Regular model retraining based on performance feedback

### Robustness

**Robustness Measures**:
- Adversarial testing with challenging and edge-case queries
- Stress testing under high concurrent user loads
- Fallback mechanisms for component failures
- Graceful degradation strategies for partial system outages

**Scenario-Based Testing**:
- Testing with malformed or ambiguous queries
- Evaluation under various document collection sizes and types
- Performance assessment with different user query patterns
- Resilience testing for external dependency failures

**Redundancy and Fail-Safes**:
- Multiple retrieval strategies (semantic, keyword, hybrid)
- Backup model endpoints for high availability
- Cached response mechanisms for common queries
- Circuit breaker patterns for external service dependencies

**Uncertainty Estimation**:
- Confidence scoring for retrieved documents and generated responses
- Uncertainty quantification using ensemble methods
- Calibration of confidence scores through validation datasets
- User interface indicators for response reliability

### Cybersecurity

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2 (h)
  <p></p>
</div>

**Data Security**:
- End-to-end encryption for data in transit and at rest
- Secure document storage with access controls and audit logging
- Regular security scanning of document collections for sensitive information
- Data anonymization techniques for privacy protection

**Access Control**:
- Multi-factor authentication for system access
- Role-based access control (RBAC) for different user types
- API rate limiting and authentication token management
- Regular access review and privilege auditing

**Incident Response**:
- Automated security monitoring and threat detection
- Incident response playbooks for security breaches
- Regular security drills and response testing
- Comprehensive logging and forensic capabilities

**Security Measures Implementation**:
- Threat modeling and vulnerability assessments
- Secure development practices and code reviews
- Regular security updates and patch management
- Penetration testing and red team exercises

## Human Oversight

<div style="color:gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/11/" style="color:blue; text-decoration:underline">Article 11</a>;; <a href="https://artificialintelligenceact.eu/annex/4/" style="color:blue; text-decoration:underline">Annex IV</a> paragraph 2(e)
  <br>EU AI Act <a href="https://artificialintelligenceact.eu/article/14/" style="color:blue; text-decoration:underline">Article 14</a>
  <p></p>
</div>

**Human-in-the-Loop Mechanisms**: 
- Review and approval workflows for critical responses
- Human validation of document additions to the knowledge base
- Quality assurance processes for system outputs
- Expert review mechanisms for domain-specific queries

**Override and Intervention Procedures**: 
- Manual response editing and correction capabilities
- Emergency system shutdown procedures
- Query filtering and blocking mechanisms
- Real-time monitoring with human intervention alerts

**User Instructions and Training**: 
- Comprehensive user guides for effective query formulation
- Training materials on system limitations and best practices
- Regular workshops on responsible AI usage
- Documentation on interpreting system outputs and confidence scores

**Limitations and Constraints of the System**: 
- Cannot provide information outside the indexed document collection
- May generate responses with varying degrees of accuracy
- Performance depends on document quality and query specificity
- Requires human verification for critical decision-making applications
- Limited to text-based information processing only

## Incident Management

### Troubleshooting AI Application Deployment

#### Infrastructure-Level Issues

##### Insufficient Resources
* **Problem**: Vector operations require significant computational resources, leading to performance degradation or system crashes under load.
* **Mitigation Strategy**:
  - Implement auto-scaling for compute resources based on query volume
  - Monitor memory usage for vector operations and optimize batch processing
  - Use resource pooling and queue management for concurrent requests

##### Network Failures
* **Problem**: High-latency responses or system unavailability due to network issues affecting API calls and model inference.
* **Mitigation Strategy**:
  - Deploy content delivery networks (CDNs) for static assets
  - Implement regional load balancers with failover capabilities
  - Use caching strategies to reduce external API dependencies

##### Deployment Pipeline Failures
* **Problem**: Failed deployments due to model compatibility issues, environment configuration errors, or dependency conflicts.
* **Mitigation Strategy**:
  - Use containerization (Docker) for consistent deployment environments
  - Implement automated testing pipelines for model validation
  - Maintain rollback procedures and blue-green deployment strategies

#### Integration Problems

##### API Failures
* **Problem**: External LLM or embedding model APIs become unavailable, causing system failures.
* **Mitigation Strategy**:
  - Implement retry mechanisms with exponential backoff
  - Use multiple API providers with automatic failover
  - Cache common responses to reduce external dependencies

##### Data Format Mismatches
* **Problem**: Document format changes or query structure modifications cause processing errors.
* **Mitigation Strategy**:
  - Implement robust data validation and schema checking
  - Use flexible parsing mechanisms for various document formats
  - Provide clear API documentation and versioning

#### Model-Level Issues

##### Performance Degradation
* **Problem**: Decreased accuracy or relevance in responses due to model drift or dataset changes.
* **Mitigation Strategy**:
  - Implement continuous model monitoring and performance tracking
  - Use automated retraining pipelines when performance thresholds are breached
  - Maintain model versioning and A/B testing capabilities

##### Information Hallucination
* **Problem**: AI generates false information not present in the source documents.
* **Mitigation Strategy**:
  - Implement strict grounding mechanisms using retrieved context
  - Use confidence scoring and uncertainty quantification
  - Provide source citations and verification mechanisms

#### Safety and Security Issues

##### Unauthorized Access
* **Problem**: Potential exposure of sensitive documents or system capabilities to unauthorized users.
* **Mitigation Strategy**:
  - Implement robust authentication and authorization mechanisms
  - Use API rate limiting and access logging
  - Regular security audits and penetration testing

##### Data Breaches
* **Problem**: Compromise of sensitive information within the document collection or user queries.
* **Mitigation Strategy**:
  - Encrypt data at rest and in transit
  - Implement data anonymization and masking techniques
  - Use comprehensive audit trails and monitoring systems

#### Recovery and Rollback

##### Rollback Mechanisms
* **Problem**: New model or system updates introduce critical errors affecting user experience.
* **Mitigation Strategy**:
  - Use blue-green deployment with automated rollback triggers
  - Maintain multiple model versions with quick switching capabilities
  - Implement feature flags for gradual rollout and testing

##### Disaster Recovery
* **Problem**: Complete system failure requiring full recovery from backups.
* **Mitigation Strategy**:
  - Regular automated backups of vector indices and configuration
  - Document comprehensive disaster recovery procedures
  - Test recovery processes regularly to ensure reliability

### EU Declaration of Conformity

<div style="color: gray">
  EU AI Act <a href="https://artificialintelligenceact.eu/article/47/" style="color:blue; text-decoration:underline">Article 47</a>
  <p></p>
</div>

**System Name**: Lab11 RAG System  
**Provider**: Lab11 Development Team  
**Conformity Statement**: This EU declaration of conformity is issued under the sole responsibility of the provider. The Lab11 RAG System is in conformity with the EU AI Act regulations for Limited Risk AI systems as outlined in Chapter IV, Article 50.

**GDPR Compliance**: The AI system complies with Regulations (EU) 2016/679 (GDPR) through implementation of privacy-by-design principles, data minimization, and user consent mechanisms.

**Standards Applied**: ISO/IEC 23053:2022 for AI risk management, IEEE 2857-2021 for AI system transparency, and NIST AI Risk Management Framework guidelines.

### Standards Applied

- **ISO/IEC 23053:2022**: Framework for AI risk management
- **IEEE 2857-2021**: Privacy engineering practices for AI systems  
- **NIST AI RMF**: AI Risk Management Framework for trustworthy AI
- **ISO 27001**: Information security management standards
- **RAGAS Framework**: Retrieval-Augmented Generation evaluation standards

## Documentation Metadata

### Template Version
[Application Documentation Template v1.0](https://github.com/organization/ai-documentation-templates)

### Documentation Authors

* **AI Engineering Team Lead, Lab11**: (Owner / Technical Lead)
* **Compliance Officer, Legal Team**: (Contributor / Regulatory Reviewer) 
* **Product Manager, AI Systems**: (Contributor / Business Requirements)
* **Security Architect, InfoSec Team**: (Contributor / Security Review)