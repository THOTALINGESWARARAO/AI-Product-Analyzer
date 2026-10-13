# AI Product Intelligence Platform

An AI-powered product analysis platform that uses **Google Gemini Vision API** and **FastAPI** to transform product images into structured product information. The system automatically identifies product categories, generates descriptions, and extracts relevant tags to streamline e-commerce catalog creation.

## Overview

Creating product catalogs manually is time-consuming and requires consistent product descriptions and categorization. This project automates that process using multimodal AI.

Users provide a product image, and the backend analyzes its visual content to generate structured metadata that can be integrated into e-commerce catalog workflows.

## Key Features

* **Image-Based Product Analysis:** Analyzes uploaded product images using Gemini Vision.
* **Automatic Categorization:** Identifies the product category from visual information.
* **AI-Generated Descriptions:** Generates descriptive text based on the product image.
* **Tag Extraction:** Produces relevant tags for product discovery and organization.
* **Structured Output:** Returns product information in a structured format suitable for downstream applications.
* **REST API:** Exposes product analysis functionality through FastAPI endpoints.
* **Cloud Deployment:** Supports a deployed backend and frontend architecture.

## Technology Stack

| Component           | Technology               |
| ------------------- | ------------------------ |
| Backend             | Python, FastAPI          |
| Multimodal AI       | Google Gemini Vision API |
| API Architecture    | REST APIs                |
| Frontend            | React                    |
| Backend Deployment  | Render                   |
| Frontend Deployment | Vercel                   |

## System Architecture

```text
       Product Image
             |
             v
      React Frontend
             |
             v
       FastAPI Backend
             |
             v
    Gemini Vision API
             |
             v
   Image Understanding
             |
             v
  Product Metadata Generation
             |
             v
 Structured JSON Response
             |
             v
      Frontend Display
```

## Generated Product Information

The platform generates product metadata such as:

* **Category:** Product classification.
* **Description:** AI-generated product description.
* **Tags:** Relevant keywords associated with the product.

### Example Output

```json
{
  "category": "Footwear",
  "description": "A casual athletic shoe designed for everyday comfort and use.",
  "tags": [
    "casual",
    "athletic",
    "footwear",
    "everyday"
  ]
}
```

*Note: This is an illustrative example of the expected output structure. Actual results depend on the uploaded image and the model's response.*

## Getting Started

### Prerequisites

* Python 3.10 or a compatible version supported by your dependencies.
* pip
* A Google Gemini API key.
* Git

### 1. Clone the Repository

```bash
git clone https://github.com/THOTALINGESWARARAO/AI-Product-Analyzer.git
cd AI-Product-Analyzer
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

If your repository contains a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the dependencies specified by your project configuration.

### 4. Configure Environment Variables

Create a `.env` file in the backend directory or the location expected by your application.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual API key.

**Security:** Never commit your API key or other secrets to GitHub. Add `.env` to `.gitignore`.

### 5. Start the FastAPI Server

If your FastAPI application instance is exposed as `app` in `main.py`, run:

```bash
uvicorn main:app --reload
```

If your entry-point module or application instance has a different name, adjust the command accordingly.

### 6. Access the API Documentation

When the backend is running locally, open:

```text
http://127.0.0.1:8000/docs
```

FastAPI provides an interactive API documentation interface when its default documentation route is enabled.

## Deployment

The application uses a separated frontend and backend deployment architecture:

* **Backend:** Render
* **Frontend:** Vercel

The frontend communicates with the backend through REST API requests. Configure the frontend to use the correct deployed backend URL and ensure that the backend permits requests from the frontend origin.

## Potential Use Cases

* E-commerce product catalog automation.
* Automated product categorization.
* AI-assisted product description generation.
* Product metadata enrichment.
* Product discovery and search optimization.

## Future Enhancements

Potential improvements include:

* Product attribute extraction, such as color, material, and brand, when visually identifiable.
* Improved request validation and error handling.
* Automated API testing.
* Batch image processing.
* Product metadata quality evaluation.
* Integration with product inventory and catalog management systems.

## Author

**Thota Lingeswara Rao**

* GitHub: https://github.com/THOTALINGESWARARAO
* LinkedIn: https://www.linkedin.com/in/thota-lingeswara-rao-451a6b337/

