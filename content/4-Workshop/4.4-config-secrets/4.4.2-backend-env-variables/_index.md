---
title : "Backend Env Variables"
date : 2024-01-01
weight : 2
chapter : false
pre : " <b> 4.4.2 </b> "
---

The Workspace AI Agent project uses a .env file to configure core services such as LLMs (via LiteLLM), Database (MongoDB), Authentication (AWS Cognito), Caching (Redis), and more.

#### 1. AI Model Configuration (LiteLLM)

The project leverages **LiteLLM** as an abstraction layer to manage various AI providers (OpenAI, AWS Bedrock, Google Gemini, etc.).

+ **LITELLM_API_KEY**: API Key to access the LiteLLM proxy (if using self-hosted). Or use **OPENAI_API_KEY** when calling OpenAI directly.
+ **ORCHESTRATOR_MODEL**: Model name for the main orchestrator agent (e.g., gpt-4o-mini).
+ **AGENT_MODEL**: Model name for the worker agents (e.g., gpt-4o-mini).
+ **TRANSLATE_MODEL**: Model name for the translation service (e.g., gpt-4o-mini).
+ **TAVILY_API_KEY**: API Key for web search services (Tavily Search).

#### 2. Database (MongoDB)

Uses MongoDB to store user data, conversation threads, and agent states.

+ **MONGO_URI**: The MongoDB connection string (e.g., mongodb://localhost:27017 or a MongoDB Atlas link).
+ **MONGO_DB_NAME**: The database name (e.g., workshop_db).

#### 3. Authentication (AWS Cognito & JWT)

Uses AWS Cognito for user management and JWT for securing API endpoints.

+ **COGNITO_USER_POOL_ID**: The AWS User Pool ID.
+ **COGNITO_APP_CLIENT_ID**: The corresponding App Client ID.
+ **COGNITO_REGION**: The AWS region where Cognito is deployed (e.g., ap-southeast-1).
+ **SECRET_KEY**: A secret string used for signing and verifying JWT tokens.

#### 4. Storage (AWS S3)

Uses S3 to store documents (PDFs, Docs) for RAG (Retrieval-Augmented Generation) purposes.

+ **S3_BUCKET_NAME**: The name of the S3 Bucket.
+ **AWS_REGION**: The bucket's region (e.g., ap-southeast-1).

#### 5. Caching & Memory (Redis)

Used for storing short-term conversation memory and improving performance.

+ **REDIS_CLIENT_HOST**: The Redis host address.
+ **REDIS_PORT**: The Redis port (default: 6379).

#### 6. Monitoring (Logfire)

+ **LOGFIRE_TOKEN**: Token used for shipping logs to Pydantic Logfire.

---

**Note**: Refer to the `backend/.env.example` file in the project source code for the complete list of required environment variables.
