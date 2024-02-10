# FastAPI 

## Overview

The FastAPI application is designed to provide APIs for dog recognition and counting in images. It includes endpoints for analyzing images to detect the presence of dogs, counting the number of dogs, and providing descriptions of images related to dogs.

## Files

1. **app_config.yaml**: Configuration file containing prompts for image analysis tasks.

2. **main.py**: Main FastAPI application script.

3. **routes.py**: Router file containing API endpoints and logic.

4. **requirements.txt**: File specifying required Python packages.

5. **utils.py**: Utility file containing functions used in the main application.

6. **env**: File containing API keys and sensitive information (not provided in this documentation).

## Endpoints

### 1. Health Check Endpoint

- **URL:** `/`
- **Method:** `GET`

#### Example Request:

```http
GET /
```

Returns a message indicating that the API is up and provides information on available endpoints.

### 2. Count Dogs API

- **URL:** `/count_dogs_API`
- **Method:** `POST`

#### Request Body

- `image` (ImageUrl): URL of the image to analyze.

```json
{
  "url": "https://example.com/path/to/image.jpg"
}
```

#### Parameters

- `title` (str, optional): The title of the API. Defaults to "count_dogs_API".

#### Response

If dogs are present in the image:

```json
{
  "title": "count_dogs_API",
  "description": "The image contains 3 dogs."
}
```

If no dogs are found in the image:

```json
{
  "title": "count_dogs_API",
  "description": "No dogs found in the image."
}
```

## Running the API

To run the API, execute the FastAPI application script using uvicorn:

```bash
uvicorn main:app --reload
```

Replace `main` with the name of your FastAPI application module.

## Example Test Case

### Request

```http
POST /count_dogs_API
Content-Type: application/json

{
  "url": "https://example.com/path/to/image.jpg"
}
```

### Response

```json
{
  "title": "count_dogs_API",
  "description": "The image contains 3 dogs."
}
```

This documentation provides an overview of the FastAPI application, details on the available endpoints, expected request formats, and example responses. Additionally, an example test case demonstrates how to make a request to the `/count_dogs_API` endpoint and shows a sample response.
