# API Design Guidelines

As an AI assistant, I will adhere to the following guidelines when designing and implementing APIs.

## General Principles

- **Simplicity:** The API should be simple and easy to understand and use.
- **Consistency:** The API should be consistent across all endpoints.
- **Discoverability:** The API should be self-describing and easy to explore.

## Versioning

- All APIs should be versioned.
- The version should be included in the URL path (e.g., `/api/v1`).

## Authentication

- Use standard authentication methods like HTTP Basic Authentication or OAuth 2.0.
- All endpoints that modify data should require authentication.
- Publicly accessible data can be exposed through unauthenticated endpoints.

## Endpoints

- Use nouns to represent resources (e.g., `/users`, `/devices`).
- Use plural nouns for collections (e.g., `/users`).
- Use a nested structure for related resources (e.g., `/users/{userId}/posts`).

## HTTP Methods

- **GET:** Retrieve a resource or a collection of resources.
- **POST:** Create a new resource.
- **PUT:** Update an existing resource completely.
- **PATCH:** Update an existing resource partially.
- **DELETE:** Delete a resource.

## Status Codes

- **2xx (Success):**
    - `200 OK`: The request was successful.
    - `201 Created`: A new resource was created successfully.
    - `204 No Content`: The request was successful, but there is no content to return.
- **4xx (Client Error):**
    - `400 Bad Request`: The request was invalid.
    - `401 Unauthorized`: The request requires authentication.
    - `403 Forbidden`: The client is not authorized to perform the requested action.
    - `404 Not Found`: The requested resource was not found.
- **5xx (Server Error):**
    - `500 Internal Server Error`: An unexpected error occurred on the server.

## Request and Response Bodies

- Use JSON for request and response bodies.
- Use snake_case for JSON property names.
- Provide clear and consistent error messages in the response body for 4xx and 5xx errors.
  ```json
  {
    "error": {
      "code": 400,
      "message": "Invalid request body"
    }
  }
  ```

## MQTT Interface

- If an MQTT interface is provided, follow these guidelines:
- **Topics:** Use a clear and consistent topic structure (e.g., `device-type/device-id/action`).
- **Payloads:** Use simple and clear message payloads (e.g., "ON", "OFF").
- **Authentication:** Secure the MQTT broker with username/password authentication.
